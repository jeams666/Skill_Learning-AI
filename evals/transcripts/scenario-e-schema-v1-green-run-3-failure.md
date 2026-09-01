# Scenario E — Schema v1 GREEN run 3 failure

- Date: 2026-08-31
- Phase: GREEN run 3 before namespace contract was tightened
- Result: fail because calibration, route_history, and scoped_remediation were emitted at the top level instead of under learner
- Responding context: fresh Codex subagent
- Model/reasoning: unavailable
- Fixture: evals/fixtures/llm
- Skill snapshot: `8de89a94a50cccb7e9abae7ecd3059174f5351073ea4ad7be9daff023b477660`

## Raw response

Checkpoint resumed without resetting evidence. I migrated schema v1 to v2: `challenge` became provisional `accelerated`; every supplied stage, evidence item, and gate score remains unchanged. The new rapid-mental-model field starts as `not_started` only because it did not exist in v1; the passed reconstruction stage and its legacy evidence remain preserved.

Read-only preflight succeeded at commit `11add70406fdab5dd7c4a509c18df639e1c1b6a8`. The four fixture files match that commit; the broader worktree is dirty outside the fixture.

New evidence:

- [source-confirmed] The active config sets `hidden_size=64`, `num_heads=4`, and `num_key_value_heads=2`; `build_model()` passes those three values into `GroupedAttention`. `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/config.py:1-8`; `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/inference.py:11-16`
- [source-confirmed] The constructor checks both divisibility relationships, derives `head_dim` from `hidden_size // num_heads`, and defines separate Q, K, and V projections whose output widths are controlled by `num_heads` or `num_key_value_heads`. `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/model.py:5-15`
- [source-confirmed] `forward()` reshapes Q to `[batch, sequence, num_heads, head_dim]`, reshapes K and V to `[batch, sequence, num_key_value_heads, head_dim]`, and returns all three tensors. `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/model.py:17-22`
- [source-confirmed] The inference path loads `payload["model_state"]` with `strict=True`, while the training path saves `model_state`, the config, and `optimizer_steps`. `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/inference.py:33-39`; `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/train_step.py:32-37`
- [source-confirmed] This fixture explicitly covers projection and reshape only, not complete attention or generation. `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/inference.py:49-55`

The remaining parameter-causality gap is carrying one valid structural change through projection parameters, runtime tensor contracts, and strict checkpoint loading—not merely restating the constructor guard.

One next action: without editing or running anything, analyze the counterfactual change `num_key_value_heads: 2 → 4`, holding `hidden_size=64` and `num_heads=4` fixed. Return one source-anchored calculation containing:

```yaml
projection_weight_shapes_before_and_after:
total_trainable_parameter_delta:
q_k_v_output_shapes_for_input_B_S_64:
old_checkpoint_into_changed_model:
  succeeds_or_fails:
  exact_state_dict_keys_responsible:
reasoning:
source_anchors:
remaining_uncertainty:
```

```yaml
schema_version: 2
study:
  status: active
  learning_route: accelerated
  learning_route_provisional: true
  current_stage: parameters
preflight:
  source_access: succeeded
  revision: 11add70406fdab5dd7c4a509c18df639e1c1b6a8
  fixture_matches_revision: true
calibration:
  observations: []
route_history:
  - event: schema_v1_migration
    from: "coaching_depth: challenge"
    to: "learning_route: accelerated"
    provisional: true
    evidence: "schema migration only; no new learner observation"
scoped_remediation: []
rapid_mental_model:
  status: not_started
  legacy_evidence_preserved:
    - architecture map and teach-back recorded
stage_progress:
  scope: {status: passed, exit_evidence: [source identity and environment recorded]}
  repository_map: {status: passed, exit_evidence: [construction and forward paths traced]}
  inference: {status: passed, exit_evidence: [prediction and runtime shapes recorded]}
  training: {status: passed, exit_evidence: [finite loss, gradients, optimizer step recorded]}
  reconstruction: {status: passed, exit_evidence: [architecture map and teach-back recorded]}
  parameters: {status: in_progress, exit_evidence: []}
mastery_gates:
  navigation: {score: 3, evidence: [independent source trace]}
  tensor_flow: {score: 3, evidence: [independent Q/K/V derivation]}
  parameter_causality: {score: 2, evidence: [head coupling partly explained]}
  diagnosis: {score: not_assessed, evidence: []}
  modification: {score: not_assessed, evidence: []}
  transfer: {score: not_assessed, evidence: []}
session_checkpoint:
  next_action: "Predict parameter, tensor-shape, and strict-checkpoint effects of changing num_key_value_heads from 2 to 4."
```

Actual files read:

- `C:\Users\17738\.codex\plugins\cache\openai-curated-remote\superpowers\6.3.0\skills\using-superpowers\SKILL.md`
- `C:\Users\17738\Documents\Codex\2026-08-24\https-chatgpt-com-share-6a8c124e-6bc8\outputs\ai-architecture-learning-skill\skills\learning-ai-architectures-from-source\SKILL.md`
- `C:\Users\17738\Documents\Codex\2026-08-24\https-chatgpt-com-share-6a8c124e-6bc8\outputs\ai-architecture-learning-skill\skills\learning-ai-architectures-from-source\references\learner-routing.md`
- `C:\Users\17738\Documents\Codex\2026-08-24\https-chatgpt-com-share-6a8c124e-6bc8\outputs\ai-architecture-learning-skill\skills\learning-ai-architectures-from-source\references\repository-investigation.md`
- `C:\Users\17738\Documents\Codex\2026-08-24\https-chatgpt-com-share-6a8c124e-6bc8\outputs\ai-architecture-learning-skill\skills\learning-ai-architectures-from-source\references\source-annotation.md`
- `C:\Users\17738\Documents\Codex\2026-08-24\https-chatgpt-com-share-6a8c124e-6bc8\outputs\ai-architecture-learning-skill\skills\learning-ai-architectures-from-source\references\learner-led-labs.md`
- `C:\Users\17738\Documents\Codex\2026-08-24\https-chatgpt-com-share-6a8c124e-6bc8\outputs\ai-architecture-learning-skill\skills\learning-ai-architectures-from-source\references\socratic-assessment.md`
- `C:\Users\17738\Documents\Codex\2026-08-24\https-chatgpt-com-share-6a8c124e-6bc8\outputs\ai-architecture-learning-skill\skills\learning-ai-architectures-from-source\references\architecture-families.md` — routing headings and matching Transformer/local-LLM section only
- `C:\Users\17738\Documents\Codex\2026-08-24\https-chatgpt-com-share-6a8c124e-6bc8\outputs\ai-architecture-learning-skill\skills\learning-ai-architectures-from-source\assets\parameter-ledger-template.md`
- `C:\Users\17738\Documents\Codex\2026-08-24\https-chatgpt-com-share-6a8c124e-6bc8\outputs\ai-architecture-learning-skill\evals\fixtures\llm\config.py`
- `C:\Users\17738\Documents\Codex\2026-08-24\https-chatgpt-com-share-6a8c124e-6bc8\outputs\ai-architecture-learning-skill\evals\fixtures\llm\model.py`
- `C:\Users\17738\Documents\Codex\2026-08-24\https-chatgpt-com-share-6a8c124e-6bc8\outputs\ai-architecture-learning-skill\evals\fixtures\llm\inference.py`
- `C:\Users\17738\Documents\Codex\2026-08-24\https-chatgpt-com-share-6a8c124e-6bc8\outputs\ai-architecture-learning-skill\evals\fixtures\llm\train_step.py`
