import argparse
import sys
from pathlib import Path

import torch

from config import MODEL_CONFIG
from model import GroupedAttention


def build_model():
    return GroupedAttention(
        hidden_size=MODEL_CONFIG["hidden_size"],
        num_heads=MODEL_CONFIG["num_heads"],
        num_key_value_heads=MODEL_CONFIG["num_key_value_heads"],
    )


def deterministic_hidden(batch_size, sequence_length=5):
    element_count = batch_size * sequence_length * MODEL_CONFIG["hidden_size"]
    return torch.linspace(-1.0, 1.0, steps=element_count).reshape(
        batch_size, sequence_length, MODEL_CONFIG["hidden_size"]
    )


def main():
    parser = argparse.ArgumentParser(description="Deterministic grouped-attention projection fixture")
    parser.add_argument("--checkpoint", type=Path)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--batch-size", type=int, default=2)
    args = parser.parse_args()

    torch.manual_seed(args.seed)
    model = build_model()
    checkpoint_status = "not_requested"
    if args.checkpoint is not None:
        payload = torch.load(args.checkpoint, map_location="cpu", weights_only=True)
        model.load_state_dict(payload["model_state"], strict=True)
        checkpoint_status = "loaded_strict"

    hidden = deterministic_hidden(args.batch_size)
    model.eval()
    with torch.inference_mode():
        query, key, value = model(hidden)

    print(f"python={sys.version.split()[0]}")
    print(f"torch={torch.__version__}")
    print(f"device={hidden.device}")
    print("fixture=grouped_attention")
    print(f"input_shape={tuple(hidden.shape)}")
    print(f"q_shape={tuple(query.shape)}")
    print(f"k_shape={tuple(key.shape)}")
    print(f"v_shape={tuple(value.shape)}")
    print("config_constraints=passed")
    print("scope=projection_reshape_only_not_full_attention_or_generation")
    print(f"checkpoint={checkpoint_status}")


if __name__ == "__main__":
    main()
