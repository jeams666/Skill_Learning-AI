import copy
import torch
from torch import nn


class Encoder(nn.Module):
    def __init__(self, image_size=64, patch_size=16, dim=64, heads=4):
        super().__init__()
        self.patch = nn.Conv2d(3, dim, patch_size, patch_size)
        self.position = nn.Parameter(torch.zeros(1, (image_size // patch_size) ** 2, dim))
        self.attention = nn.MultiheadAttention(dim, heads, batch_first=True)

    def forward(self, images):
        tokens = self.patch(images).flatten(2).transpose(1, 2) + self.position
        attended, _ = self.attention(tokens, tokens, tokens, need_weights=False)
        return (tokens + attended).mean(dim=1)


class StudentTeacher(nn.Module):
    def __init__(self, dim=64, output_dim=256):
        super().__init__()
        self.student_encoder = Encoder(dim=dim)
        self.student_head = nn.Linear(dim, output_dim)
        self.teacher_encoder = copy.deepcopy(self.student_encoder)
        self.teacher_head = copy.deepcopy(self.student_head)

    @torch.no_grad()
    def update_teacher(self, momentum):
        student = list(self.student_encoder.parameters()) + list(self.student_head.parameters())
        teacher = list(self.teacher_encoder.parameters()) + list(self.teacher_head.parameters())
        for source, target in zip(student, teacher):
            target.data.mul_(momentum).add_(source.data, alpha=1 - momentum)

    @torch.no_grad()
    def retrieval_embedding(self, images):
        return torch.nn.functional.normalize(self.teacher_encoder(images), dim=-1)

