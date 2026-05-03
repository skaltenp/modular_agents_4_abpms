#!/usr/bin/env bash
# Run test_all.sh sequentially for each (model, reasoning_effort) combo used by the paper.
#
# Standard runs (3):
#   1. gpt-5.4    + reasoning_effort=none   (gpt-5.4 doesn't accept reasoning_effort with tools)
#   2. gpt-5.1    + reasoning_effort=high
#   3. qwen3.5:35b + reasoning_effort=high  (Ollama strips it from the LLM call,
#                                            but we store sessions under reasoning-high
#                                            since Qwen's internal thinking is always "high")
#
# Ablations (2):
#   4. gpt-5.1    + reasoning_effort=none
#   5. gpt-5.4    + reasoning_effort=high
#
# Any extra args (e.g. --evaluate-only) are forwarded to test_all.sh.
# Usage:
#   ./scripts/test_all_with_all_models.sh
#   ./scripts/test_all_with_all_models.sh --evaluate-only
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# Each entry: "label|model|reasoning-effort"
COMBOS=(
    "Standard 1/3: gpt-5.4 / none|gpt-5.4|none"
    "Standard 2/3: gpt-5.1 / high|gpt-5.1|high"
    "Standard 3/3: qwen3.5:35b / high|qwen3.5:35b|high"
    "Ablation 1/2: gpt-5.1 / none|gpt-5.1|none"
    "Ablation 2/2: gpt-5.4 / high|gpt-5.4|high"
)

for combo in "${COMBOS[@]}"; do
    IFS='|' read -r label model effort <<< "$combo"
    echo ""
    echo "######################################"
    echo "  $label"
    echo "  model=$model  reasoning_effort=$effort"
    echo "######################################"
    echo ""
    bash "$SCRIPT_DIR/test_all.sh" --model "$model" --reasoning-effort "$effort" "$@"
done

echo ""
echo "######################################"
echo "  All ${#COMBOS[@]} combos tested successfully"
echo "######################################"
