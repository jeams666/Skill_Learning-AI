import argparse
from pathlib import Path

import torch
from torch.nn import functional as F

from inference import build_model, deterministic_images


def main():
    parser = argparse.ArgumentParser(description="One synthetic student/teacher optimizer step")
    parser.add_argument("--checkpoint", type=Path)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--batch-size", type=int, default=2)
    parser.add_argument("--lr", type=float, default=0.001)
    parser.add_argument("--teacher-momentum", type=float, default=0.9)
    args = parser.parse_args()

    torch.manual_seed(args.seed)
    model = build_model()
    for parameter in list(model.teacher_encoder.parameters()) + list(model.teacher_head.parameters()):
        parameter.requires_grad_(False)
    optimizer = torch.optim.SGD(
        list(model.student_encoder.parameters()) + list(model.student_head.parameters()), lr=args.lr
    )
    view_a = deterministic_images(args.batch_size)
    view_b = torch.roll(view_a, shifts=1, dims=-1)

    model.train()
    student_output = model.student_head(model.student_encoder(view_a))
    with torch.no_grad():
        teacher_output = model.teacher_head(model.teacher_encoder(view_b))
    loss = F.mse_loss(student_output, teacher_output)
    optimizer.zero_grad(set_to_none=True)
    loss.backward()
    gradient_finite = all(
        parameter.grad is None or bool(torch.isfinite(parameter.grad).all())
        for parameter in model.student_encoder.parameters()
    )
    optimizer.step()
    teacher_before = next(model.teacher_encoder.parameters()).detach().clone()
    model.update_teacher(args.teacher_momentum)
    teacher_after = next(model.teacher_encoder.parameters()).detach()
    teacher_updated = bool(torch.any(teacher_before != teacher_after))

    checkpoint_status = "not_requested"
    if args.checkpoint is not None:
        if not args.checkpoint.parent.exists():
            raise FileNotFoundError(f"checkpoint parent does not exist: {args.checkpoint.parent}")
        torch.save(
            {
                "model_state": model.state_dict(),
                "teacher_momentum": args.teacher_momentum,
                "optimizer_steps": 1,
            },
            args.checkpoint,
        )
        checkpoint_status = "saved"

    print("fixture=self_supervised_retrieval")
    print("loss_kind=toy_plumbing_only_not_dino_or_retrieval_correctness")
    print(f"student_shape={tuple(student_output.shape)}")
    print(f"teacher_shape={tuple(teacher_output.shape)}")
    print(f"loss_finite={bool(torch.isfinite(loss))}")
    print(f"gradient_finite={gradient_finite}")
    print(f"teacher_updated={teacher_updated}")
    print("optimizer_steps=1")
    print(f"checkpoint={checkpoint_status}")


if __name__ == "__main__":
    main()

