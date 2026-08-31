# Scenario C — diagnostic source-anchor failure

## Run metadata

- Date: 2026-08-25
- Responding model: GPT-5.6 Terra, medium reasoning
- Run type: GREEN, fresh first turn, retained diagnostic failure
- Skill snapshot: local snapshot before the exact-anchor pre-send audit was added
- Fixture: `evals/fixtures/llm/`
- Contamination guard: the responding agent did not read scenarios, rubrics, prior transcripts, scorecards, baselines, or results
- Sanitization: absolute workspace and home prefixes in `FILES READ` were normalized to `<repo-root>/` and `<home>/`; user-facing prose is unchanged

## Exact scenario prompt

> I trained simple PyTorch models before. I need to learn this local decoder repository and adapt it for local fine-tuning. We are behind schedule, so give me a one-shot explanation. Change `num_heads` from 4 to 6, explain grouped attention and every affected parameter, show the architecture patch if needed, and give me the fine-tuning plan. Skip quizzes and checkpoints; I will understand from reading.

## Verbatim user-facing response

**Checkpoint:** scope, active. **Goal:** identify the local source, its runtime context, and the configuration seam for a future grouped-attention change before attempting a fine-tuning adaptation. Your PyTorch background lets us keep the coaching concise; the schedule does not replace source evidence.

**Source identity to confirm:** the available local fixture is a grouped-attention projection fragment, not a complete decoder or generation stack. Please provide the official repository/local path and revision (or `not available`), plus Python, PyTorch version, and device (or `not available`). The selected transfer track is **Local LLM fine-tuning**.

**Evidence ledger**

- [source-confirmed] The fixture configuration sets `hidden_size=64`, `num_heads=4`, and `num_key_value_heads=2` at `llm-fixture@unresolved:evals/fixtures/llm/config.py:1-8`.
- [source-confirmed] Model construction passes those three fields into `GroupedAttention` at `llm-fixture@unresolved:evals/fixtures/llm/inference.py:10-15`.
- [source-confirmed] The module creates separate Q, K, and V projections, then reshapes each projected tensor at `llm-fixture@unresolved:evals/fixtures/llm/model.py:8-20`.
- [runtime-verified] none yet.
- [docs-stated] none yet.
- [inferred] This fixture isolates projection-and-reshape behavior; it does not establish the full decoder’s masking, attention computation, residual path, language-model head, tokenizer, or generation behavior.

**Boundary map**

```text
config.py
  → inference.py: build_model()
  → GroupedAttention(hidden_size, num_heads, num_key_value_heads)
  → Q/K/V projections and reshape
  → returned Q/K/V tensors

train_step.py
  → same construction path
  → synthetic projection loss
  → backward, optimizer step, optional checkpoint
```

The config-versus-code seam is `MODEL_CONFIG` flowing through `build_model()` into the attention constructor. The constructor’s blocking invariant couples hidden width, query-head count, and key/value-head count: both divisions checked at `model.py:8-10` must be exact. A changed topology also crosses a strict checkpoint boundary because inference loads `model_state` with `strict=True` at `inference.py:31-32`; existing projection weights may therefore be incompatible. Later, the core-replacement gate is to preserve and verify the module’s input/output tensor contract with forward, backward, and regression evidence.

**Prediction and one action:** without editing anything, trace the values from `MODEL_CONFIG` into the three `.view(...)` calls. For the proposed six query heads, return:

1. whether each constructor divisibility condition holds;
2. the symbolic Q, K, and V shapes in terms of `B`, `S`, and the resulting head dimension;
3. the smallest coupled configuration fields you believe must be reconsidered, without proposing replacement values; and
4. the official source/revision plus Python/PyTorch/device, using `not available` where needed.

**Return format:** four short numbered answers only.

**Resumable checkpoint:** `stage=scope`, `status=active`; evidence acquired: local config-to-constructor-to-projection map; `navigation=not_assessed`, `tensor_flow=not_assessed`, `parameter_causality=not_assessed`, `diagnosis=not_assessed`, `modification=not_assessed`, `transfer=not_assessed`; uncertainty: official decoder identity/version and runtime environment are absent, and the grouped-attention coupling has not yet been derived by you; next action: trace the proposed head-count change through the constructor constraints and reshape calls.

## Files read

- `<repo-root>/skills/learning-ai-architectures-from-source/SKILL.md`
- `<repo-root>/skills/learning-ai-architectures-from-source/references/repository-investigation.md`
- `<repo-root>/skills/learning-ai-architectures-from-source/references/socratic-assessment.md`
- `<repo-root>/skills/learning-ai-architectures-from-source/references/architecture-families.md`
- `<repo-root>/skills/learning-ai-architectures-from-source/references/task-transfer.md`
- `<repo-root>/evals/fixtures/llm/config.py`
- `<repo-root>/evals/fixtures/llm/model.py`
- `<repo-root>/evals/fixtures/llm/inference.py`
- `<repo-root>/evals/fixtures/llm/train_step.py`

## Retained failure signal

The response cites strict checkpoint loading at `inference.py:31-32`, but the actual strict load is at lines 36–39. It also does not explicitly label the projected checkpoint-compatibility consequence as `[inferred]`. This run triggered the current source-span audit; its independent criterion scores are recorded in `../scorecards.md`.
