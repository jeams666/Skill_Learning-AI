import argparse
import sys
from pathlib import Path

import torch

from model import TinyDetector


def load_config():
    config = {}
    for line in Path(__file__).with_name("config.yaml").read_text(encoding="utf-8").splitlines():
        if line.strip():
            key, value = line.split(":", 1)
            config[key.strip()] = int(value.strip())
    return config


def main():
    parser = argparse.ArgumentParser(description="Deterministic TinyDetector inference fixture")
    parser.add_argument("--checkpoint", type=Path)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--batch-size", type=int, default=2)
    args = parser.parse_args()

    torch.manual_seed(args.seed)
    config = load_config()
    model = TinyDetector(
        width=config["width"],
        neck_depth=config["neck_depth"],
        num_classes=config["num_classes"],
    )
    checkpoint_status = "not_requested"
    if args.checkpoint is not None:
        payload = torch.load(args.checkpoint, map_location="cpu", weights_only=True)
        model.load_state_dict(payload["model_state"], strict=True)
        checkpoint_status = "loaded_strict"

    element_count = args.batch_size * 3 * config["input_size"] * config["input_size"]
    images = torch.linspace(0.0, 1.0, steps=element_count).reshape(
        args.batch_size, 3, config["input_size"], config["input_size"]
    )
    model.eval()
    with torch.inference_mode():
        output = model(images)

    print(f"python={sys.version.split()[0]}")
    print(f"torch={torch.__version__}")
    print(f"device={images.device}")
    print("fixture=detector")
    print(f"input_shape={tuple(images.shape)}")
    print(f"output_shape={tuple(output.shape)}")
    print(f"output_finite={bool(torch.isfinite(output).all())}")
    print(f"checkpoint={checkpoint_status}")


if __name__ == "__main__":
    main()
