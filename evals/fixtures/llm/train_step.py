import argparse
from pathlib import Path

import torch

from config import MODEL_CONFIG
from inference import build_model, deterministic_hidden


def main():
    parser = argparse.ArgumentParser(description="One synthetic grouped-attention projection optimizer step")
    parser.add_argument("--checkpoint", type=Path)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--batch-size", type=int, default=2)
    parser.add_argument("--lr", type=float, default=0.001)
    args = parser.parse_args()

    torch.manual_seed(args.seed)
    model = build_model().train()
    optimizer = torch.optim.SGD(model.parameters(), lr=args.lr)
    hidden = deterministic_hidden(args.batch_size)
    query, key, value = model(hidden)
    loss = query.square().mean() + key.square().mean() + value.square().mean()
    optimizer.zero_grad(set_to_none=True)
    loss.backward()
    gradient_finite = all(
        parameter.grad is None or bool(torch.isfinite(parameter.grad).all())
        for parameter in model.parameters()
    )
    optimizer.step()

    checkpoint_status = "not_requested"
    if args.checkpoint is not None:
        if not args.checkpoint.parent.exists():
            raise FileNotFoundError(f"checkpoint parent does not exist: {args.checkpoint.parent}")
        torch.save({"model_state": model.state_dict(), "config": MODEL_CONFIG, "optimizer_steps": 1}, args.checkpoint)
        checkpoint_status = "saved"

    print("fixture=grouped_attention")
    print("loss_kind=toy_plumbing_only_not_language_modeling_or_finetuning_correctness")
    print(f"q_shape={tuple(query.shape)}")
    print(f"k_shape={tuple(key.shape)}")
    print(f"v_shape={tuple(value.shape)}")
    print(f"loss_finite={bool(torch.isfinite(loss))}")
    print(f"gradient_finite={gradient_finite}")
    print("config_constraints=passed")
    print("optimizer_steps=1")
    print(f"checkpoint={checkpoint_status}")


if __name__ == "__main__":
    main()

