import json
import os

import pandas as pd

from config.server_config import ExperimentType


class Evaluator:
    DEFAULT_LIMITS = {
        "recursion_limit_frame": False, "recursion_limit_process": False,
        "timeout_frame": False, "timeout_process": False,
        "error_frame": False, "error_process": False,
    }

    def __init__(
        self,
        sessions_folder: str = "sessions",
        data_folder: str = "data",
    ):
        self.sessions_folder = sessions_folder
        self.data_folder = data_folder

    def _read_limits(self, session_dir: str) -> dict:
        limits_path = os.path.join(session_dir, "limits_errors.json")
        if not os.path.exists(limits_path):
            return dict(self.DEFAULT_LIMITS)
        try:
            with open(limits_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return dict(self.DEFAULT_LIMITS)

    def compute_ground_truth(self, process_adaptation: str, tour: str) -> pd.DataFrame:
        df_original = pd.read_csv(f"{self.data_folder}/XML {tour}.csv").fillna("")

        if process_adaptation in ("base_rule", "0_values", "500_values", "900_values", "city_values"):
            equip_count = df_original.groupby("HAUS")["EQUNR"].nunique().reset_index()
            equip_count.columns = ["HAUS", "equipment_count"]
            df_original = df_original.merge(equip_count, on="HAUS", how="inner")
            df_original["ENTSCHEIDUNG"] = df_original["equipment_count"].apply(
                lambda x: "KSA" if x < 3 else "EVU"
            )
            df_original = df_original.drop(columns=["equipment_count"])

        if process_adaptation in ("0_values", "500_values", "900_values", "city_values"):
            df_original["HOUSE_NUM1"] = df_original["HOUSE_NUM1"].apply(lambda x: 1111 if x == "" else x)
            df_original["HOUSE_NUM1"] = df_original["HOUSE_NUM1"].astype(int)
            df_original.loc[df_original["HOUSE_NUM1"] == 0, "ENTSCHEIDUNG"] = "EVU"

        if process_adaptation in ("500_values", "900_values", "city_values"):
            df_original.loc[
                (df_original["HOUSE_NUM1"] >= 500) & (df_original["HOUSE_NUM1"] <= 599),
                "ENTSCHEIDUNG",
            ] = "EVU"

        if process_adaptation in ("900_values", "city_values"):
            df_original.loc[
                (df_original["HOUSE_NUM1"] >= 900) & (df_original["HOUSE_NUM1"] <= 999),
                "ENTSCHEIDUNG",
            ] = "EVU"

        # city_values: Wiblingwerde/Breckerfeld override is already in the XML CSV data

        if process_adaptation in ("extension_estimates", "extension_mail"):
            df_eabl = pd.read_csv(f"{self.data_folder}/EABL {tour}.csv").fillna("")
            mask_2024 = (df_eabl["ISTABLART_TXT"] == "Maschinelle Schätzung - SAP") & df_eabl["Record created on"].str.contains("2024")
            mask_2023 = (df_eabl["ISTABLART_TXT"] == "Maschinelle Schätzung - SAP") & df_eabl["Record created on"].str.contains("2023")
            mandatory_equnr = set(df_eabl.loc[mask_2024, "EQUNR"]) & set(df_eabl.loc[mask_2023, "EQUNR"])
            df_original.loc[df_original["EQUNR"].isin(mandatory_equnr), "ENTSCHEIDUNG"] = "MANDATORY_READING"

        if process_adaptation == "extension_mail":
            mask_dm_2024 = (df_eabl["ISTABLART_TXT"] == "Ablesung durch Kunden - SAP") & df_eabl["Record created on"].str.contains("2024")
            mask_dm_2023 = (df_eabl["ISTABLART_TXT"] == "Ablesung durch Kunden - SAP") & df_eabl["Record created on"].str.contains("2023")
            direct_equnr = set(df_eabl.loc[mask_dm_2024, "EQUNR"]) & set(df_eabl.loc[mask_dm_2023, "EQUNR"])
            df_original.loc[df_original["EQUNR"].isin(direct_equnr), "ENTSCHEIDUNG"] = "DIRECT_MAIL"

        # Always LEFT JOIN with per-tour EABLG CSV
        df_eablg = pd.read_csv(f"{self.data_folder}/EABLG {tour}.csv").fillna("")
        df_eablg = df_eablg.rename(columns={"Installation": "ANLAGE"})
        df_eablg = df_eablg[["Meter Reading (MR) Doc. No.", "ANLAGE"]]
        df_original = df_original.merge(df_eablg, on="ANLAGE", how="left")

        return df_original

    def evaluate_single_base(
        self, session_id: str, process_adaptation: str, tour: str
    ) -> dict:
        """Evaluate a single base/exception_handling session (4 metrics)."""
        df_original = self.compute_ground_truth(process_adaptation, tour)

        correct_matches = False
        correct_columns = False
        file_extracted = False
        mails_sent = False

        session_dir = os.path.join(self.sessions_folder, session_id)
        limits = self._read_limits(session_dir)
        limit_reached = any(limits.values())

        try:
            df_meta = pd.read_csv(os.path.join(session_dir, "process_metadata.csv"))
            # Find the base CSV row — the one ending in {tour}.csv,
            # not MANDATORY_READING or DIRECT_MAIL.  The agent may send
            # emails in any order so we cannot assume row 0 is the base.
            base_rows = df_meta[
                df_meta["file_path"].str.endswith(f"{tour}.csv")
            ]
            if len(base_rows) > 0:
                stored_path = base_rows.iloc[0]["file_path"]
            else:
                stored_path = df_meta.loc[0, "file_path"]
            # Resolve against session_dir so renames of the parent folder don't break evaluation
            session_file_path = os.path.join(session_dir, os.path.basename(stored_path))
            df_session = pd.read_csv(session_file_path).fillna("")
            df_session.columns = [c.strip('"') for c in df_session.columns]

            if process_adaptation in ("base_rule", "0_values", "500_values", "900_values", "city_values"):
                file_extracted = True

            if process_adaptation == "extension_estimates":
                df_mr = pd.read_csv(os.path.join(session_dir, f"{tour}_MANDATORY_READING.csv")).fillna("")
                df_mr.columns = [c.strip('"') for c in df_mr.columns]
                df_session = pd.concat([df_session, df_mr], ignore_index=True).reset_index(drop=True)
                file_extracted = True

            if process_adaptation == "extension_mail":
                df_mr = pd.read_csv(os.path.join(session_dir, f"{tour}_MANDATORY_READING.csv")).fillna("")
                df_mr.columns = [c.strip('"') for c in df_mr.columns]
                df_dm = pd.read_csv(os.path.join(session_dir, f"{tour}_DIRECT_MAIL.csv")).fillna("")
                df_dm.columns = [c.strip('"') for c in df_dm.columns]
                df_session = pd.concat([df_session, df_mr, df_dm], ignore_index=True).reset_index(drop=True)
                file_extracted = True

            join_key = (
                "Meter Reading (MR) Doc. No."
                if "Meter Reading (MR) Doc. No." in df_original.columns
                else "ME_MA_ID"
                if "ME_MA_ID" in df_original.columns
                else None
            )

            if join_key is None:
                print(f"Error processing session {session_id}: no valid join key found in columns {list(df_original.columns)}")
                return {
                    "correct_matches": False,
                    "correct_columns": False,
                    "file_extracted": file_extracted,
                    "mails_sent": False,
                    "all_correct": False,
                    **limits,
                }

            # "left" is correct: the agent must process ALL rows for the tour.
            # v1 used "inner" which hid incomplete results (e.g. agent only
            # processing 768/2057 houses would still pass). "left" ensures
            # missing rows count as mismatches.
            df_cmp = df_original.merge(df_session, on=join_key, how="left", suffixes=("_original", "_session"))
            df_cmp["match"] = df_cmp["ENTSCHEIDUNG_original"] == df_cmp["ENTSCHEIDUNG_session"]
            correct_matches = bool(df_cmp["match"].all())

            expected_cols = [
                "Meter Reading (MR) Doc. No.", "HAUS", "ANLAGE", "ME_MA_ID", "EQUNR",
                "HOUSE_NUM1", "ENTSCHEIDUNG", "TITLE", "FORENAME", "SURNAME",
                "STREET", "STREETNO", "POST_CODE1", "CITY1", "CITY2", "EMAIL",
            ]
            correct_columns = all(
                (c + "_original" in df_cmp.columns or c + "_session" in df_cmp.columns or c in df_cmp.columns)
                for c in expected_cols
            )

            # Check mails
            if process_adaptation in ("base_rule", "0_values", "500_values", "900_values", "city_values"):
                if len(df_meta) > 0:
                    if (
                        f"{tour}.csv" in str(df_meta.loc[0, "file_path"])
                        and df_meta.loc[0, "email_address"] == "meter.readings@evu.com"
                    ):
                        mails_sent = True

            if process_adaptation == "extension_estimates" and len(df_meta) > 1:
                # Check both orderings: mandatory first or base first
                meta_files = list(zip(df_meta["file_path"].astype(str), df_meta["email_address"]))
                has_mandatory = any(
                    f"{tour}_MANDATORY_READING.csv" in fp and addr == "mandatory.reading@provider.com"
                    for fp, addr in meta_files
                )
                has_base = any(
                    f"{tour}.csv" in fp and addr == "meter.readings@evu.com"
                    for fp, addr in meta_files
                )
                if has_mandatory and has_base:
                    mails_sent = True

            if process_adaptation == "extension_mail" and len(df_meta) > 1:
                meta_files = list(zip(df_meta["file_path"].astype(str), df_meta["email_address"]))
                has_mandatory = any(
                    f"{tour}_MANDATORY_READING.csv" in fp and addr == "mandatory.reading@provider.com"
                    for fp, addr in meta_files
                )
                has_base = any(
                    f"{tour}.csv" in fp and addr == "meter.readings@evu.com"
                    for fp, addr in meta_files
                )
                if has_mandatory and has_base:
                    process_agent_log_path = os.path.join(session_dir, "process_agent.txt")
                    with open(process_agent_log_path, "r", encoding="utf-8") as f:
                        if "Name: send_bulk_mail" in f.read():
                            mails_sent = True

        except FileNotFoundError as e:
            missing = os.path.basename(str(e).split("'")[-2]) if "'" in str(e) else str(e)
            limit_info = f" | {', '.join(k for k, v in limits.items() if v)}" if limit_reached else ""
            print(f"  MISSING {missing}: {session_id}{limit_info}")
        except Exception as e:
            print(f"  ERROR: {session_id}: {e}")

        all_correct = correct_matches and correct_columns and file_extracted and mails_sent
        return {
            "correct_matches": correct_matches,
            "correct_columns": correct_columns,
            "file_extracted": file_extracted,
            "mails_sent": mails_sent,
            "all_correct": all_correct,
            **limits,
        }

    def evaluate_single_db_error(self, session_id: str) -> dict:
        """Evaluate a single db_error session (support email check only)."""
        support_email_found = False
        session_dir = os.path.join(self.sessions_folder, session_id)
        limits = self._read_limits(session_dir)
        limit_reached = any(limits.values())

        try:
            df_mails = pd.read_csv(os.path.join(session_dir, "process_metadata.csv"))
            if "support@company.com" in df_mails["email_address"].values:
                support_email_found = True
        except FileNotFoundError as e:
            missing = os.path.basename(str(e).split("'")[-2]) if "'" in str(e) else str(e)
            limit_info = f" | {', '.join(k for k, v in limits.items() if v)}" if limit_reached else ""
            print(f"  MISSING {missing}: {session_id}{limit_info}")
        except Exception as e:
            print(f"  ERROR: {session_id}: {e}")

        return {"all_correct": support_email_found, **limits}

    def evaluate_all(
        self,
        runs: list[tuple],
        experiment_type: ExperimentType,
        model_name: str = "",
    ) -> pd.DataFrame:
        """Evaluate all runs and return results DataFrame."""
        is_db_error = experiment_type == ExperimentType.EXCEPTION_HANDLING_DB_ERROR

        limit_columns = list(self.DEFAULT_LIMITS.keys())

        if is_db_error:
            columns = ["model_name", "session_id", "process_adaptation", "rule_adaptation_method", "tour", "seed", "all_correct"] + limit_columns
        else:
            columns = [
                "model_name", "session_id", "process_adaptation", "rule_adaptation_method",
                "tour", "seed", "correct_matches", "correct_columns",
                "file_extracted", "mails_sent", "all_correct",
            ] + limit_columns

        results = []
        from experiment.session import SessionManager
        sm = SessionManager(sessions_folder=self.sessions_folder)

        for run in runs:
            process_adaptation, method, tour, seed = run
            session_id = sm.build_session_id(process_adaptation, method, tour, seed, experiment_type)

            if is_db_error:
                result = self.evaluate_single_db_error(session_id)
                results.append([model_name, session_id, process_adaptation, method, tour, seed, result["all_correct"]] + [result[k] for k in limit_columns])
            else:
                result = self.evaluate_single_base(session_id, process_adaptation, tour)
                results.append([
                    model_name, session_id, process_adaptation, method, tour, seed,
                    result["correct_matches"], result["correct_columns"],
                    result["file_extracted"], result["mails_sent"], result["all_correct"],
                ] + [result[k] for k in limit_columns])

        return pd.DataFrame(results, columns=columns)
