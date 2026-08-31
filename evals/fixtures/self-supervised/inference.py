import argparse
import sys
from pathlib import Path

import torch

from model import StudentTeacher


def deterministic_images(batch_size):
    element_count = batch_size * 3 * 64 * 64
    return torch.linspace(0.0, 1.0, steps=element_count).reshape(batch_size, 3, 64, 64)


def build_model():
    return StudentTeacher(dim=64, output_dim=256)


def main():
    parser = argparse.ArgumentParser(description="Deterministic retrieval inference fixture")
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

    model.eval()
    images = deterministic_images(args.batch_size)
    with torch.inference_mode():
        embedding = model.retrieval_embedding(images)
    norms = torch.linalg.vector_norm(embedding, dim=-1)

    print(f"python={sys.version.split()[0]}")
    print(f"torch={torch.__version__}")
    print(f"device={images.device}")
    print("fixture=self_supervised_retrieval")
    print(f"input_shape={tuple(images.shape)}")
    print(f"embedding_shape={tuple(embedding.shape)}")
    print(f"norms_close_to_one={bool(torch.allclose(norms, torch.ones_like(norms), atol=1e-5))}")
    print("retrieval_source=teacher_encoder_not_projection_head")
    print(f"checkpoint={checkpoint_status}")


if __name__ == "__main__":
    main()
