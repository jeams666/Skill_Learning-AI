# Scenario D — final GREEN run

- Date: 2026-08-31
- Responding context: fresh Codex subagent
- Model/reasoning: unavailable from the collaboration result
- Fixture: `evals/fixtures/llm/`
- Skill snapshot: `53d305a82698cbc6ed9e616690c155f9e72f25ce58a649403c2463eefcf45f95`
- Result: 8/8 clean pass for the routing snapshot; the later final snapshot changes only schema-v1 null-default migration rules

## Raw response

## Current checkpoint and goal

`status: active` · `stage: scope / in_progress` · `learning_route: pending_calibration`

Your experience warrants the hardest compact calibration, but it does not assign the accelerated route by itself. A strong return can satisfy several adjacent evidence requirements; none are silently skipped.

The 90-minute endpoint is one prediction-backed runtime trace, a learner-authored core-module replacement, and an evidence-defended local-fine-tuning decision. This first turn establishes whether the shortest accelerated path is justified.

## Preflight and scope

- Source access: `succeeded`
- Supplied implementation: `C:\Users\17738\Documents\Codex\2026-08-24\https-chatgpt-com-share-6a8c124e-6bc8\outputs\ai-architecture-learning-skill`
- Revision: `11add70406fdab5dd7c4a509c18df639e1c1b6a8`
- Official upstream status: unresolved; this Git repository has no configured remote.
- Target: `evals/fixtures/llm/config.py::MODEL_CONFIG`
- Environment: Python/framework/device not yet runtime-observed.
- Transfer track: local LLM fine-tuning, selected from your explicit task.
- Comparison implementation: none.

Evidence ledger:

- `[runtime-verified]` Model execution: none yet.
- `[source-confirmed]` Config, construction, forward, inference-wrapper, and training-wrapper anchors were acquired from the four fixture files. `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/config.py:1-8`; `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/inference.py:11-56`; `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/model.py:5-22`; `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/train_step.py:10-48`
- `[docs-stated]` Repository documentation evidence: none yet.
- `[inferred]` Transfer suitability: undetermined; the supplied fixture alone is not yet evidence for adapting a complete decoder.

## Fast mental model

- `[source-confirmed]` Execution spine: `MODEL_CONFIG → build_model → deterministic_hidden → GroupedAttention.forward → raw (query, key, value) → printed shapes`; the training branch reuses that construction/input path, forms a toy mean-square loss from the three outputs, performs backward plus one SGD step, and optionally saves a checkpoint. `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/config.py:1-8`; `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/inference.py:11-56`; `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/model.py:17-22`; `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/train_step.py:18-48`
- `[source-confirmed]` Architecture skeleton: a hidden tensor flows through three bias-free projections and is reshaped onto distinct query-head and key/value-head axes before returning a raw tuple. The traced inference path ends at those tensors and explicitly identifies its scope as projection/reshape only, not full attention or generation. `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/inference.py:19-23`; `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/model.py:13-22`; `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/inference.py:41-55`

The unresolved edge is the exact tensor and parameter consequence of changing the KV-head topology. That is your calibration target.

## Prediction and one action

Before executing anything, write:

1. The anchored source trace from `num_key_value_heads` in the config through construction to both active use sites.
2. Symbolic query/key/value shapes in terms of batch, sequence, hidden width, query heads, and KV heads.
3. Their concrete shapes for batch size `3` and the current config.
4. The exact output-shape effects and trainable-parameter delta if only `num_key_value_heads` changed from `2` to `1`; also derive whether construction would accept that counterfactual.

Then run exactly this read-only command from the repository root:

```powershell
python -B .\evals\fixtures\llm\inference.py --seed 0 --batch-size 3
```

`-B` disables bytecode-file creation, and omitting `--checkpoint` avoids checkpoint I/O. Do not edit the config for the counterfactual.

Return:

- Whether the supplied path/revision is the official source; provide the official URL/revision or `not available`.
- Your four prediction items, with source anchors.
- Exact stdout, or the exact error. If execution is unavailable, report Python/framework/device as `not available`.
- A one-sentence execution-spine correction, a one-sentence architecture-skeleton correction, and remaining uncertainty.

## Resumable checkpoint

```yaml
preflight:
  source_access: succeeded
learning_route: pending_calibration
calibration_evidence: senior-level self-report only; observable repository work pending
rapid_mental_model:
  status: draft
stage:
  name: scope
  status: in_progress
evidence_acquired:
  - config, construction, forward, inference, and toy-training anchors
gates:
  navigation: not_assessed
  tensor_flow: not_assessed
  parameter_causality: not_assessed
  diagnosis: not_assessed
  modification: not_assessed
  transfer: not_assessed
uncertainty:
  - official upstream identity
  - Python, PyTorch, and device
  - predicted tensor and parameter consequences
next_action: Return the anchored prediction, exact no-write inference output or error, and two-layer correction.
```

## Actual files read

- `C:\Users\17738\.codex\plugins\cache\openai-curated-remote\superpowers\6.3.0\skills\using-superpowers\SKILL.md` — complete
- `C:\Users\17738\Documents\Codex\2026-08-24\https-chatgpt-com-share-6a8c124e-6bc8\outputs\ai-architecture-learning-skill\skills\learning-ai-architectures-from-source\SKILL.md` — complete
- `...\references\learner-routing.md` — complete
- `...\references\repository-investigation.md` — complete
- `...\references\socratic-assessment.md` — complete
- `...\references\learner-led-labs.md` — complete
- `...\references\task-transfer.md` — headings, shared contract lines 1–21, and Local LLM fine-tuning lines 34–37
- `...\references\architecture-families.md` — headings, preface lines 1–4, and Transformer/local-LLM section lines 19–24
- `...\evals\fixtures\llm\config.py` — complete
- `...\evals\fixtures\llm\model.py` — complete
- `...\evals\fixtures\llm\inference.py` — complete
- `...\evals\fixtures\llm\train_step.py` — complete
