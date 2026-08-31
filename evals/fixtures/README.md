# Runnable teaching fixtures

These miniature PyTorch repositories exist to test source-reading and learner-led inference/training behavior. They are not faithful production implementations and do not measure model quality.

Run the commands below from this `evals/fixtures` directory. They use only Python's standard library and PyTorch, work in PowerShell, cmd, bash, and zsh, and default to deterministic synthetic data.

## Inference without writes

```text
python -B detector/inference.py
python -B self-supervised/inference.py
python -B llm/inference.py
```

Expected structural observations:

| Fixture | Observable |
|---|---|
| detector | input `[B,3,256,256]`, output `[B,10,64,64]` |
| self-supervised | retrieval embedding `[B,64]`, L2 norms near one |
| grouped attention | Q `[B,5,4,16]`, K/V `[B,5,2,16]` |

## One optimizer step and strict checkpoint reload

Choose checkpoint paths whose parent directories already exist. The training scripts write only when `--checkpoint` is supplied; they do not create parent directories.

```text
python -B detector/train_step.py --checkpoint detector.pt
python -B detector/inference.py --checkpoint detector.pt

python -B self-supervised/train_step.py --checkpoint self-supervised.pt
python -B self-supervised/inference.py --checkpoint self-supervised.pt

python -B llm/train_step.py --checkpoint llm.pt
python -B llm/inference.py --checkpoint llm.pt
```

Every training script performs one forward/backward/optimizer step and labels its objective `toy_plumbing_only...`. Detector MSE is not a detection loss; the student/teacher MSE is not the DINO objective; the grouped-attention projection loss is not language modeling or fine-tuning. Finite loss and gradients prove only that the local plumbing executes.

Checkpoints contain a `model_state` and are reloaded with `strict=True`. Missing, extra, or shape-incompatible tensors must fail instead of silently falling back to random weights. Delete generated `.pt` files after the exercise if you no longer need them.
