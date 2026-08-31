import argparse
from pathlib import Path

import torch
from torch.nn import functional as F

from inference import load_config
from model import TinyDetector


def main():
    parser = argparse.ArgumentParser(description="One synthetic TinyDetector optimizer step")
    parser.add_argument("--checkpoint", type=Path)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--batch-size", type=int, default=2)
    parser.add_argument("--lr", type=float, default=0.001)
    args = parser.parse_args()

    torch.manual_seed(args.seed)
    config = load_config()
    model = TinyDetector(
        width=config["width"],
        neck_depth=config["neck_depth"],
        num_classes=config["num_classes"],
    ).train()
    optimizer = torch.optim.SGD(model.parameters(), lr=args.lr)
    element_count = args.batch_size * 3 * config["input_size"] * config["input_size"]
    images = torch.linspace(0.0, 1.0, steps=element_count).reshape(
        args.batch_size, 3, config["input_size"], config["input_size"]
    )

    prediction = model(images)
    loss = F.mse_loss(prediction, torch.zeros_like(prediction))
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
        torch.save({"model_state": model.state_dict(), "config": config, "optimizer_steps": 1}, args.checkpoint)
        checkpoint_status = "saved"

    print("fixture=detector")
    print("loss_kind=toy_plumbing_only_not_detection_correctness")
    print(f"prediction_shape={tuple(prediction.shape)}")
    print(f"loss_finite={bool(torch.isfinite(loss))}")
    print(f"gradient_finite={gradient_finite}")
    print("optimizer_steps=1")
    print(f"checkpoint={checkpoint_status}")


if __name__ == "__main__":
    main()

