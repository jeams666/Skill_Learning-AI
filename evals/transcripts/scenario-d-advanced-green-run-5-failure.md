# Scenario D — fifth GREEN run failure

- Date: 2026-08-31
- Responding context: fresh Codex subagent
- Model/reasoning: unavailable from the collaboration result
- Fixture: `evals/fixtures/llm/`
- Skill snapshot: `ed1c2a8125f17926c4ca65e647bd418dfa1022cb146c98edb27f98be7f7c5fca`
- Independent score: 7.5/8, fail

## Raw response

Start now: I’ll use one dense source challenge to determine whether you earn the accelerated route. Your experience and deadline justify harder calibration, but not an automatic stage pass. The endpoint is one learner-authored core-module replacement and an evidence-defended local fine-tuning decision.

### Preflight and scope

`preflight.source_access: succeeded`

Files inspected read-only: `config.py`, `model.py`, `inference.py`, and `train_step.py`. Config, construction, architecture-bearing `forward`, inference wrapper, and training wrapper anchors are present.

- Primary source: supplied local fixture. Its four target files match Git commit `11add70406fdab5dd7c4a509c18df639e1c1b6a8`; the surrounding worktree has unrelated changes.
- Official upstream source/revision: not supplied. In your return, confirm this local path and revision as authoritative, provide the official URL/revision, or write `not available`.
- Target: `MODEL_CONFIG`.
- Environment: not runtime-verified. Return intended Python/PyTorch/device, with `not available` accepted.
- Transfer track: **Local LLM fine-tuning**, inferred directly from your stated task; this selects the destination without opening the transfer stage.
- Learning route: `pending_calibration`.

### Evidence ledger

- `[runtime-verified]` none yet.
- `[source-confirmed]` The config feeds three attention dimensions into `build_model`; the core `forward` projects and reshapes hidden states; inference and one synthetic training-step wrappers exercise that module. `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/config.py:1-8`; `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/inference.py:7-16`; `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/model.py:5-22`; `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/train_step.py:6-36`
- `[docs-stated]` none yet.
- `[inferred]` A full-decoder transfer decision will require either additional primary source or explicit confirmation that this deliberately bounded fixture is the entire candidate.

### Rapid mental model — draft

Execution spine:

- `[source-confirmed]` Inference is `MODEL_CONFIG → build_model → deterministic hidden input → eval/inference-mode forward → printed tensor and checkpoint status`. `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/config.py:1-8`; `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/inference.py:7-23`; `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/inference.py:26-56`; `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/model.py:17-22`
- `[source-confirmed]` Training is `same builder/input → forward → synthetic scalar loss → backward → SGD step → optional checkpoint`; the wrapper explicitly disclaims language-modeling or fine-tuning correctness. `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/train_step.py:6-36`; `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/train_step.py:39-48`

Architecture skeleton:

- `[source-confirmed]` Hidden states enter three learned projections, are reshaped into query/key/value head structures, and are returned; this fixture explicitly ends at projection/reshape rather than full attention or generation. `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/model.py:5-22`; `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/inference.py:49-56`
- Unresolved edge: the symbolic tensor contract and the causal consequences of changing the key/value-head configuration.

### Calibration question and action

If only `num_key_value_heads` changes from `2` to `3`, what is the earliest observable outcome before any Q/K/V shapes are printed, and what exact dependency causes it?

Spend at most ten minutes on one read-only trace through `config.py:1-8`, `inference.py:11-16`, and `model.py:5-22`. Return:

1. Official source/revision confirmation and Python/PyTorch/device, allowing `not available`.
2. The exact source anchors you traversed.
3. Symbolic Q/K/V shapes, followed by the concrete instance for default batch and sequence settings.
4. Your counterfactual prediction for `num_key_value_heads = 3`, including the earliest responsible expression.
5. One sentence updating each mental-model layer.
6. One remaining uncertainty.

A correct, independently anchored return can supply evidence for several adjacent exits; none are skipped or pre-awarded.

```yaml
schema_version: 2
status: active
preflight:
  source_access: succeeded
study:
  learning_route: pending_calibration
  calibration_evidence: none_returned_yet
rapid_mental_model:
  status: draft
  unresolved_edge: symbolic Q/K/V contract and key/value-head counterfactual
current_stage:
  name: scope
  status: in_progress
evidence_acquired:
  - config, construction, forward, inference-wrapper, and training-wrapper anchors
gates:
  navigation: not_assessed
  tensor_flow: not_assessed
  parameter_causality: not_assessed
  diagnosis: not_assessed
  modification: not_assessed
  transfer: not_assessed
uncertainty:
  - authoritative source identity
  - execution environment
  - full-decoder boundary
next_action: Return the single six-part read-only calibration artifact above.
```

Files read: `SKILL.md`; `learner-routing.md`; `repository-investigation.md`; `socratic-assessment.md`; the Transformer/local-LLM section of `architecture-families.md`; the shared contract and Local LLM fine-tuning track of `task-transfer.md`; fixture `config.py`, `model.py`, `inference.py`, and `train_step.py`.

## Why it failed

The response retained prediction, learner-authored modification, and transfer defense, but its calibration action did not require an actual runtime observation or exact run error. Scenario D therefore scored 0.5 on the runtime-evidence requirement.

