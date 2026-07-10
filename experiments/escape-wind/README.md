# escape-wind-experiment

Falsification harness for the Escape Under Pressure section (core DDD).
Status: **projected**. See DESIGN.md for the stake, kill conditions, and readout.

## Run order

    python3 gen_items.py --n 90                          # synthetic, seed-pinned
    python3 run.py --base-url http://<spark>:8000/v1 \
        --model Qwen/Qwen3.6-35B-A3B-FP8 --audit         # gate: repair/drop failures
    for T in T0 T1 T2 T2p T2pp T2-near T2-mid T2-far; do
        python3 run.py --base-url ... --model ... --tier $T --k 5 --temperature 0.7
    done
    python3 analyze.py runs/ --margin 0.03               # margin declared pre-run

Every run emits a manifest (binding, seed, items hash) — these are the
citable evidence. The DESIGN.md stays projected until runs are linked.
