# Scenario D — experienced learner baseline on the pre-upgrade skill

- Date: 2026-08-31
- Phase: UPGRADE BASELINE using the previous released skill
- Skill snapshot: pre-upgrade local commit `11add70406fdab5dd7c4a509c18df639e1c1b6a8`
- Responding context: fresh Codex subagent
- Fixture: `evals/fixtures/llm/`

## Prompt

> I am a senior AI engineer with five years of PyTorch experience. I have implemented YOLO variants, ViTs, and decoder-only Transformers, and I can read unfamiliar Python repositories quickly. I have 90 minutes before I must advise my team whether this local grouped-attention decoder is worth adapting for local fine-tuning. My manager expects a concrete recommendation today, and I do not want beginner explanations or a long curriculum. Build me a fast mental model of the repository, test whether I can skip material I already know, and route me through the shortest evidence-based path to one architecture modification and a transfer decision. Start now; do not ask me to choose a learning level.

## Raw response

Challenge-depth start. Your PyTorch background and 90-minute deadline make the coaching terse; they do not replace source evidence. Passing this first challenge lets us skip framework and basic Transformer material.

Current checkpoint: `scope / in_progress`  
Goal: verify source navigation and tensor reasoning before choosing one core modification or making a fine-tuning transfer recommendation.

Scope lock:

- Primary candidate: local `evals/fixtures/llm` source at Git commit `11add70406fdab5dd7c4a509c18df639e1c1b6a8`.
- Official source/revision: unconfirmed.
- Target: `GroupedAttention` with the complete `MODEL_CONFIG`.
- Python/framework/device: not available yet.
- Transfer track: Local LLM fine-tuning, selected from your explicit task.
- Comparison implementation: none.

Evidence ledger:

- `[runtime-verified]` none yet; no model execution has been used as evidence.
- `[source-confirmed]` configuration values flow through `build_model()` into `GroupedAttention`. `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/inference.py:7-16`
- `[source-confirmed]` the module returns three projected-and-reshaped tensors. `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/model.py:5-22`
- `[source-confirmed]` the supplied training path uses a synthetic squared-mean loss and one SGD step. `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/train_step.py:18-36`
- `[docs-stated]` none yet.
- `[inferred]` this fixture alone is not enough evidence for a full decoder adaptation recommendation.

Minimal boundary map:

- Inference: config → constructor → deterministic hidden input → module forward → tensor reporting.
- Training: same construction path → synthetic loss → backward/optimizer step → optional checkpoint.
- The boundary beyond these paths remains unresolved and matters to the eventual transfer decision.

One challenge—do not run the code yet:

For the default batch size and sequence length, derive the exact `q`, `k`, and `v` shapes from `config.py`, `build_model()`, and `GroupedAttention.forward()`. Show the symbolic derivation first, then concrete shapes, and cite the decisive lines.

Return exactly:

```text
official source/revision: <confirm the local source and commit are official, provide the real source/revision, or "not available">
Python/framework/device: <values or "not available">
construction chain: <config key → constructor argument → forward use, with line references>
symbolic shapes: <q, k, v>
concrete shapes: <q, k, v>
reasoning: <2–4 sentences>
```

Checkpoint:

```yaml
study_status: active
stage: scope
stage_status: in_progress
evidence_acquired: local revision, target fixture, minimal boundaries, local-LLM-fine-tuning track
gates:
  navigation: not_assessed
  tensor_flow: not_assessed
  parameter_causality: not_assessed
  diagnosis: not_assessed
  modification: not_assessed
  transfer: not_assessed
uncertainty: official-source status, runtime environment, and competence gates remain unverified
next_action: return the source-derived shape prediction and requested scope metadata
```

Files read: `SKILL.md`; `references/repository-investigation.md`; `references/socratic-assessment.md`; selected Local LLM sections of `references/task-transfer.md` and `references/architecture-families.md`; fixture `config.py`, `model.py`, `inference.py`, and `train_step.py`.

## Observed upgrade gaps

- The response chose challenge-depth language but did not record an explicit learning route, its evidence, or a rule for changing it.
- The boundary map described execution paths but did not produce a distinct architecture skeleton.
- The challenge tested navigation and tensor reasoning, but the response did not state which stage exit evidence could be bundled or how stages remain independently gated.
- The checkpoint had no rapid-mental-model state or calibration evidence field.

