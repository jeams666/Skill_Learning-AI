import torch
from torch import nn


class GroupedAttention(nn.Module):
    def __init__(self, hidden_size, num_heads, num_key_value_heads):
        super().__init__()
        if hidden_size % num_heads or num_heads % num_key_value_heads:
            raise ValueError("attention dimensions must divide evenly")
        self.num_heads = num_heads
        self.num_key_value_heads = num_key_value_heads
        self.head_dim = hidden_size // num_heads
        self.q_proj = nn.Linear(hidden_size, num_heads * self.head_dim, bias=False)
        self.k_proj = nn.Linear(hidden_size, num_key_value_heads * self.head_dim, bias=False)
        self.v_proj = nn.Linear(hidden_size, num_key_value_heads * self.head_dim, bias=False)

    def forward(self, hidden):
        batch, sequence, _ = hidden.shape
        query = self.q_proj(hidden).view(batch, sequence, self.num_heads, self.head_dim)
        key = self.k_proj(hidden).view(batch, sequence, self.num_key_value_heads, self.head_dim)
        value = self.v_proj(hidden).view(batch, sequence, self.num_key_value_heads, self.head_dim)
        return query, key, value

