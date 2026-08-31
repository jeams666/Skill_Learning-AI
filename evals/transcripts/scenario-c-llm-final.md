# Scenario C — grouped-attention change, final snapshot

## Run metadata

- Date: 2026-08-25
- Responding model: GPT-5.6 Terra, medium reasoning
- Run type: GREEN, fresh first turn
- Skill snapshot: `sha256:089592b114ef2013f88df79c0e526fcff706e066898d5fd14ad29ea64e9ceab7` (see `../skill-snapshot.sha256`)
- Fixture: `evals/fixtures/llm/`
- Contamination guard: the responding agent did not read scenarios, rubrics, prior transcripts, scorecards, baselines, or results
- Sanitization: absolute workspace and home prefixes in `FILES READ` were normalized to `<repo-root>/` and `<home>/`; user-facing prose is unchanged

## Exact scenario prompt

> I trained simple PyTorch models before. I need to learn this local decoder repository and adapt it for local fine-tuning. We are behind schedule, so give me a one-shot explanation. Change `num_heads` from 4 to 6, explain grouped attention and every affected parameter, show the architecture patch if needed, and give me the fine-tuning plan. Skip quizzes and checkpoints; I will understand from reading.

## Verbatim user-facing response

### Current checkpoint and goal

Scope — in progress. We will first identify the supplied implementation, its execution boundaries, and the compatibility constraints around your proposed attention change; your PyTorch background sets a standard coaching depth, but we still need one source-grounded calculation before changing architecture.

The supplied fixture contains no Git metadata or revision, so its source anchors are marked `@unresolved`.

### Evidence ledger

- [source-confirmed] The active configuration sets `hidden_size`, `num_heads`, and `num_key_value_heads`; inference passes those values into `GroupedAttention`. `llm-fixture@unresolved:config.py:3-5`; `llm-fixture@unresolved:inference.py:11-16`
- [source-confirmed] The module projects hidden states into separate query, key, and value tensors, then reshapes each projection; this fixture explicitly limits its scope to projection and reshape, rather than full attention or text generation. `llm-fixture@unresolved:model.py:17-22`; `llm-fixture@unresolved:inference.py:50-55`
- [docs-stated] The selected transfer track is local LLM fine-tuning; it calls for tokenizer/template, context and packing, objective, adapter targets, resource budget, baseline, and reproducible evaluation planning. `learning-ai-architectures-from-source@unresolved:references/task-transfer.md:34-36`
- [runtime-verified] none yet.
- [inferred] A realistic local fine-tuning plan cannot be established from this fixture alone because its training script labels its loss as synthetic plumbing rather than fine-tuning correctness. `llm-fixture@unresolved:train_step.py:21-30`; `llm-fixture@unresolved:train_step.py:39-48`

### Minimal boundary map

`config.py` → `inference.py:build_model()` → `GroupedAttention` → `(query, key, value)`.

The separate training entrypoint builds the same model, performs one synthetic optimizer step, and can save model state plus configuration. `llm-fixture@unresolved:train_step.py:18-37`

### Change constraint for `num_heads = 6`

- Config-versus-code seam: the config value flows through `build_model()` into the attention constructor. `llm-fixture@unresolved:config.py:3-5`; `llm-fixture@unresolved:inference.py:11-16`
- Blocking constraint: the constructor requires both the hidden width to divide evenly by the query-head count and the query-head count to divide evenly by the key/value-head count; these fields jointly determine per-head width and the projection/reshape contract. `llm-fixture@unresolved:model.py:8-15`
- Checkpoint boundary: inference loads model state strictly, while training saves model state together with the configuration, so an architecture change must be treated as a checkpoint-compatibility boundary. `llm-fixture@unresolved:inference.py:36-39`; `llm-fixture@unresolved:train_step.py:32-37`
- Future observable gate: after the source map and tensor contract are evidenced, the core attention change must be independently verified with forward, backward, and regression evidence—not only a configuration edit.

### One unresolved prediction

For the requested query-head count, which compatible key/value-head count(s) can satisfy both constructor constraints, and what are the symbolic output shapes for query, key, and value for input `(B, S, H)`?

### One action

Without editing code, calculate that compatibility set and the three symbolic shapes. Return:

```text
official source/revision: <path or URL and commit; “not available” accepted>
environment: Python=<...>, PyTorch=<...>, device=<...>; “not available” accepted
compatible key/value-head count(s): <your derivation>
Q/K/V shapes: <your derivation>
```

### Resumable checkpoint

`stage: scope / in_progress`  
`evidence acquired: config → constructor → projection outputs; synthetic training and strict checkpoint boundaries located`  
`navigation: not_assessed; tensor_flow: not_assessed; parameter_causality: not_assessed; diagnosis: not_assessed; modification: not_assessed; transfer: not_assessed`  
`misconception or uncertainty: official source/revision and runtime environment are unknown; compatibility and tensor consequences are unobserved`  
`next action: return the requested compatibility and symbolic-shape calculation`

## Files read

- `<repo-root>/skills/learning-ai-architectures-from-source/SKILL.md`
- `<repo-root>/skills/learning-ai-architectures-from-source/references/repository-investigation.md`
- `<repo-root>/skills/learning-ai-architectures-from-source/references/socratic-assessment.md`
- `<repo-root>/skills/learning-ai-architectures-from-source/references/task-transfer.md`
- `<repo-root>/evals/fixtures/llm/config.py`
- `<repo-root>/evals/fixtures/llm/model.py`
- `<repo-root>/evals/fixtures/llm/inference.py`
- `<repo-root>/evals/fixtures/llm/train_step.py`
