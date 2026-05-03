"""Pack/unpack sessions/<model>/ into sessions/<model>.tar.gz, and copy a
representative session per model/reasoning combo into sessions_examples/.

Usage:
    python manage_sessions.py pack       # sessions/<model>/   -> sessions/<model>.tar.gz
    python manage_sessions.py unpack     # sessions/<model>.tar.gz -> sessions/<model>/
    python manage_sessions.py examples   # copy first session per model/reasoning -> sessions_examples/
"""
from __future__ import annotations

import argparse
import shutil
import sys
import tarfile
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SESSIONS = ROOT / "sessions"
EXAMPLES = ROOT / "sessions_examples"


def _model_dirs() -> list[Path]:
    return sorted(p for p in SESSIONS.iterdir() if p.is_dir())


def _pack_one(model_dir: Path) -> tuple[str, int]:
    out = SESSIONS / f"{model_dir.name}.tar.gz"
    tmp = out.with_suffix(out.suffix + ".tmp")
    with tarfile.open(tmp, "w:gz") as tar:
        tar.add(model_dir, arcname=model_dir.name)
    tmp.replace(out)
    return model_dir.name, out.stat().st_size


def _unpack_one(archive: Path) -> tuple[str, int]:
    with tarfile.open(archive, "r:gz") as tar:
        tar.extractall(SESSIONS)
    return archive.name, sum(1 for _ in (SESSIONS / archive.name.removesuffix(".tar.gz")).rglob("*") if _.is_file())


def pack() -> None:
    dirs = _model_dirs()
    if not dirs:
        sys.exit(f"no model directories under {SESSIONS}")
    print(f"Packing {len(dirs)} model dirs in parallel: {[d.name for d in dirs]}")
    with ProcessPoolExecutor(max_workers=min(len(dirs), 4)) as ex:
        futures = {ex.submit(_pack_one, d): d for d in dirs}
        for fut in as_completed(futures):
            name, size = fut.result()
            print(f"  {name}.tar.gz  {size / 2**20:.1f} MiB")


def unpack() -> None:
    archives = sorted(SESSIONS.glob("*.tar.gz"))
    if not archives:
        sys.exit(f"no *.tar.gz under {SESSIONS}")
    print(f"Unpacking {len(archives)} archives in parallel: {[a.name for a in archives]}")
    with ProcessPoolExecutor(max_workers=min(len(archives), 4)) as ex:
        futures = {ex.submit(_unpack_one, a): a for a in archives}
        for fut in as_completed(futures):
            name, n_files = fut.result()
            print(f"  {name}  ({n_files} files)")


def examples() -> None:
    if not SESSIONS.exists():
        sys.exit(f"{SESSIONS} not found — run unpack first")
    EXAMPLES.mkdir(exist_ok=True)
    copied = 0
    for model in _model_dirs():
        for reasoning in sorted(p for p in model.iterdir() if p.is_dir()):
            session_dirs = sorted(p for p in reasoning.iterdir() if p.is_dir())
            if not session_dirs:
                continue
            src = session_dirs[0]
            dst = EXAMPLES / model.name / reasoning.name / src.name
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(src, dst, dirs_exist_ok=True)
            print(f"  {src.relative_to(ROOT)} -> {dst.relative_to(ROOT)}")
            copied += 1
    print(f"Copied {copied} example session(s) to {EXAMPLES.relative_to(ROOT)}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("action", choices=["pack", "unpack", "examples"])
    args = parser.parse_args()
    {"pack": pack, "unpack": unpack, "examples": examples}[args.action]()


if __name__ == "__main__":
    main()
