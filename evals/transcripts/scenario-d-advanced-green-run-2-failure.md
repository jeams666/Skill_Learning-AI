# Scenario D — second GREEN run failure

- Date: 2026-08-31
- Phase: GREEN run 2 after route and inferred-map refactor
- Result: fail
- Responding context: fresh Codex subagent
- Fixture: `evals/fixtures/llm/`

## Raw response

You’ve earned the hardest calibration challenge, but experience and the 90-minute deadline change coaching depth—not the evidence required for a reliable transfer decision.

Current goal: determine whether the supplied local grouped-attention decoder is worth adapting for local fine-tuning.

- Official source: supplied local `evals/fixtures/llm` directory
- Official revision: `not available`
- Python/framework/device: `not available`
- Track: adapting the architecture for a real local fine-tuning task
- Learning route: `pending_calibration`

Evidence ledger:

- `[runtime-verified]` none yet
- `[source-confirmed]` none yet
- `[docs-stated]` none yet
- `[inferred]` decoder with grouped attention, based only on your request

Mental model: `not_started`. I won’t substitute a conventional Transformer sketch for repository evidence. Both the execution spine and architecture skeleton remain unclaimed until their source anchors are established.

Your one action: inspect the fixture and return a compact trace containing:

1. Official revision, or `not available`, plus Python/PyTorch/device.
2. Paths and line ranges for the target config, model construction entrypoint, architecture-bearing attention `forward`, and training or generation wrapper.
3. The shortest call chain from wrapper input to logits.
4. Symbolic tensor shapes through attention, including how query heads reach key/value heads.
5. One configuration change you would test for local fine-tuning, its coupled parameters, one predicted tensor consequence, and one compatibility risk.
6. The single unresolved repository edge you consider most decision-relevant.

Do not summarize generic grouped-query attention; make every conclusion traceable to this fixture. Your return will be scored separately for navigation, tensor reasoning, and parameter causality, then routed to `guided`, `standard`, or `accelerated`.

```yaml
status: active
learning_route: pending_calibration
calibration_evidence: none_returned
mental_model: not_started
stage: scope
stage_status: in_progress
evidence_acquired: none
gates:
  navigation: not_assessed
  tensor_flow: not_assessed
  parameter_causality: not_assessed
  diagnosis: not_assessed
  modification: not_assessed
  transfer: not_assessed
uncertainty: repository identity, revision, environment, and execution path remain unverified
next_action: return the six-part source trace above
```

Files read:

- `skills/learning-ai-architectures-from-source/SKILL.md`
- `superpowers/using-superpowers/SKILL.md`

## Why it failed

- Correctly kept the route pending and refused a generic mental model.
- Still delegated the agent-owned readable-source preflight to the learner.
- Did not attempt to read the fixture or record a source-access failure.
- Produced neither the required anchors nor the two-layer repository model.

The next refactor makes preflight non-delegable, distinguishes `not_attempted` from an actual failed read, and adds an explicit preflight record to the checkpoint schema.

