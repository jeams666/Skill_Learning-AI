# Scenario D — fourth GREEN run failure

- Date: 2026-08-31
- Phase: GREEN run 4 after targeted refactors
- Result: fail after code review found stage-skipping language
- Responding context: fresh Codex subagent
- Fixture: `evals/fixtures/llm/`
- Skill snapshot: `c8b8fabc60cad206e59a7c00c6de5b44e385b6cdcd37fbe0f9534fec54713173`

## Raw response

### Checkpoint and goal

Preflight succeeded. Route: `pending_calibration`. We’ll use one high-information probe to determine whether you qualify for the accelerated path. Your experience justifies the hardest initial challenge, but only repository-grounded work can skip stages.

The 90-minute endpoint is: you author one architecture-bearing replacement on the active path, verify its contract, then defend an adapt/do-not-adapt recommendation. This turn establishes whether we can take the compressed route.

### Scope lock

- Source candidate: `C:\Users\17738\Documents\Codex\2026-08-24\https-chatgpt-com-share-6a8c124e-6bc8\outputs\ai-architecture-learning-skill\evals\fixtures\llm`
- Revision: clean fixture at Git commit `11add70406fdab5dd7c4a509c18df639e1c1b6a8`; confirm in your return that this is the intended official source/revision, or provide the correction/`not available`.
- Target: the single `GroupedAttention` variant configured by `MODEL_CONFIG`.
- Environment: `not available` until your run; return Python, PyTorch, and device, or `not available`.
- Transfer track: local LLM fine-tuning, inferred directly from your stated task.

### Evidence ledger

- `[runtime-verified]` none yet.
- `[source-confirmed]` Construction passes three config fields into `GroupedAttention`; its active forward returns projected query, key, and value tensors. `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/inference.py:7-16`; `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/model.py:5-22`
- `[source-confirmed]` The inference wrapper explicitly identifies this as projection/reshape plumbing rather than full attention or generation; the training wrapper uses a synthetic squared-output loss rather than language-model fine-tuning. `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/inference.py:41-56`; `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/train_step.py:18-40`
- `[docs-stated]` none yet; the supplied tree has no documentation file.
- `[inferred]` No adaptation verdict is justified yet: the available source establishes a projection seam, not decoder quality or fine-tuning suitability.

### Rapid mental model — draft

- Execution spine: `MODEL_CONFIG → build_model → deterministic_hidden → GroupedAttention.forward → q/k/v output report`; the separate training branch adds synthetic loss, backward, SGD, and optional checkpoint saving. `[source-confirmed]` `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/config.py:1-8`; `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/inference.py:11-23`; `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/inference.py:33-56`; `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/train_step.py:18-37`
- Architecture skeleton: `hidden [B,S,H] → three learned projections → ? → query/key/value`; the masked edge is your calibration trace. `[source-confirmed]` `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/model.py:5-22`

This probe distinguishes familiarity with Transformers from fast, precise navigation of this implementation. A correct independent trace earns the provisional accelerated route; a miss triggers remediation only for the weak area.

### One calibration action

Trace `num_key_value_heads` from configuration through construction, validation, forward use, and observable output. Before running anything:

1. Derive symbolic query/key/value shapes in terms of `B`, `S`, and the relevant config symbols.
2. Instantiate those shapes for `B=2`, `S=5`, and the current config.
3. Counterfactually change only `num_key_value_heads` from `2` to `3`. Predict whether execution reaches the output-printing lines, identify the earliest decisive source location, and explain why.
4. State the hypothetical K/V projection parameter-count consequence, even if construction blocks.

Then run once from the fixture directory:

```powershell
python inference.py --batch-size 2
```

Return:

```text
official_source_revision: <confirm path@commit | correction | not available>
environment: <python, torch, device | exact error | not available>
source_chain: <path:line anchors>
symbolic_shapes: <derivation>
concrete_shapes: <B=2, S=5>
counterfactual: <prediction, earliest decisive location, reasoning>
parameter_effect: <derivation>
execution_spine_update: <one line>
architecture_skeleton_update: <one line>
remaining_uncertainty: <one item>
runtime_stdout: <exact output | exact error | not available>
```

### Resumable checkpoint

```yaml
preflight:
  source_access: succeeded
learning_route: pending_calibration
calibration_evidence: senior self-report only; hardest calibration selected
mental_model: draft
status: active
stage: scope
stage_status: in_progress
evidence_acquired: config, construction, forward, inference wrapper, training wrapper
gates:
  navigation: not_assessed
  tensor_flow: not_assessed
  parameter_causality: not_assessed
  diagnosis: not_assessed
  modification: not_assessed
  transfer: not_assessed
uncertainty: intended official source and runtime environment remain unconfirmed
next_action: complete the single num_key_value_heads trace-and-counterfactual probe
```

Files read: `SKILL.md`; `learner-routing.md`; `repository-investigation.md`; `socratic-assessment.md`; `architecture-families.md`; `task-transfer.md`; fixture `config.py`, `model.py`, `inference.py`, and `train_step.py`.

## Why it failed

The response said repository-grounded work could “skip stages.” That contradicts the invariant that evidence may satisfy several independently evaluated exits but never skip a stage. An initial independent audit scored the artifact 8/8, but later code review identified the contradiction; the artifact is retained as a failure and is not final evidence.
