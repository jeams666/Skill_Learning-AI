# Scenario E — schema-v1 resume baseline

- Date: 2026-08-31
- Phase: DEVELOPMENT PROBE using a pre-migration candidate
- Repository base commit: `11add70406fdab5dd7c4a509c18df639e1c1b6a8`
- Skill snapshot: not recorded; the worktree contained uncommitted candidate changes, so this artifact is excluded from reproducible/scored samples
- Responding context: fresh Codex subagent
- Model/reasoning: unavailable from the collaboration result
- Fixture: `evals/fixtures/llm/`

## Observed response

The response preserved the supplied stage and mastery evidence, continued at `parameters`, and kept the saved next action. Its migrated checkpoint nevertheless contained the conflicting state below:

```yaml
schema_version: 1
study:
  status: active
  coaching_depth: challenge
  learning_route: accelerated
  route_status: provisional
  current_stage: parameters
```

It also created preflight and mental-model data but omitted the required route-history and scoped-remediation fields.

The response's single learner action was a source-grounded counterfactual over `num_key_value_heads`, including shapes, parameter counts, state-dict compatibility, and checkpoint predictions. No earlier stage or gate was reset.

## Upgrade-baseline failures

- Did not set `schema_version: 2`.
- Retained `coaching_depth` after creating `learning_route`, leaving two route authorities.
- Did not initialize `route_history` or scoped remediation state.
- Had no explicit lossless-migration rule covering unknown legacy fields.

Files read: `SKILL.md`; `learner-routing.md`; `socratic-assessment.md`; fixture `config.py`, `inference.py`, `model.py`, and `train_step.py`.
