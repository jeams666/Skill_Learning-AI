# Scenario E — intermediate confirmation failure

- Date: 2026-08-31
- Responding context: fresh Codex subagent
- Model/reasoning: unavailable from the collaboration result
- Fixture: `evals/fixtures/llm/`
- Skill snapshot: `8de89a94a50cccb7e9abae7ecd3059174f5351073ea4ad7be9daff023b477660`
- Result: fail under the skill evidence contract because one source-confirmed checkpoint sentence omitted the config-to-construction span

## Raw response

You’re resuming—not restarting—at `parameters`. All supplied stage evidence and mastery scores are preserved. The v1 `coaching_depth: challenge` field has been migrated to a provisional `learning_route: accelerated`.

- `[source-confirmed]` The current config supplies `hidden_size`, query-head count, and key/value-head count through `build_model()` into `GroupedAttention`; its constructor applies two divisibility checks and uses those values to define the projection layers. `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/config.py:1-8`; `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/inference.py:11-16`; `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/model.py:5-15`
- `[source-confirmed]` The forward path reshapes Q using the query-head count and K/V using the key/value-head count. `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/model.py:17-22`
- `[source-confirmed]` Training checkpoints contain `model_state` plus the config, while inference rebuilds from the current config before loading `model_state` with `strict=True`. `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/train_step.py:32-37`; `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/inference.py:26-39`

`num_key_value_heads` therefore crosses constructor validity, projection/tensor structure, and strict checkpoint loading. The derived effects remain withheld until the learner predicts them.

Exactly one next action: without editing or running the fixture, predict the consequences of changing only `num_key_value_heads` from `2` to `1`, holding `hidden_size=64`, `num_heads=4`, batch size `2`, and sequence length `5` constant. Return one causal ledger with source anchors, constructor derivation, before/after Q/K/V projection and output shapes, parameter-count delta, strict-load prediction, implicated state-dict keys, and remaining uncertainty.

```yaml
schema_version: 2
study:
  status: active
  learning_route: accelerated
  learning_route_provisional: true
  current_stage: parameters
preflight:
  source_access: succeeded
  files_read: [config.py, model.py, inference.py, train_step.py]
learner:
  calibration:
    observations: []
    route_reason: provisional schema-v1 migration; revalidate from future observable work
  route_history:
    - from: "coaching_depth: challenge"
      to: "learning_route: accelerated"
      evidence: supplied schema-v1 checkpoint
      reason: schema-version-2 migration mapping
      timestamp: null
  scoped_remediation: []
rapid_mental_model:
  status: not_started
  legacy_evidence_preserved: [architecture map and teach-back recorded]
stage_progress:
  scope: {status: passed, exit_evidence: [source identity and environment recorded]}
  repository_map: {status: passed, exit_evidence: [construction and forward paths traced]}
  inference: {status: passed, exit_evidence: [prediction and runtime shapes recorded]}
  training: {status: passed, exit_evidence: [finite loss, gradients, optimizer step recorded]}
  reconstruction: {status: passed, exit_evidence: [architecture map and teach-back recorded]}
  parameters: {status: in_progress, exit_evidence: []}
  modification: {status: not_started, exit_evidence: []}
  transfer: {status: not_started, exit_evidence: []}
  mastery: {status: not_started, exit_evidence: []}
mastery_gates:
  navigation: {score: 3, evidence: [independent source trace]}
  tensor_flow: {score: 3, evidence: [independent Q/K/V derivation]}
  parameter_causality: {score: 2, evidence: [head coupling partly explained]}
  diagnosis: {score: not_assessed, evidence: []}
  modification: {score: not_assessed, evidence: []}
  transfer: {score: not_assessed, evidence: []}
session_checkpoint:
  learner_explanation: null
  acquired_evidence: [current source preflight completed read-only]
  unfinished_experiment: parameter and checkpoint prediction not yet returned
  next_action: predict parameter and checkpoint effects of changing num_key_value_heads
```

Files read: `SKILL.md`; `learner-routing.md`; `repository-investigation.md`; `source-annotation.md`; `learner-led-labs.md`; `socratic-assessment.md`; the matching Transformer/local-LLM section of `architecture-families.md`; `study-state-template.yaml`; `parameter-ledger-template.md`; `experiment-log-template.md`; fixture `config.py`, `model.py`, `inference.py`, and `train_step.py`.

