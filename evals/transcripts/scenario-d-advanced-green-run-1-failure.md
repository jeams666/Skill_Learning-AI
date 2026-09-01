# Scenario D — first GREEN run failure

- Date: 2026-08-31
- Phase: GREEN run 1 for learner routing and rapid mental models
- Result: fail
- Responding context: fresh Codex subagent
- Fixture: `evals/fixtures/llm/`

## Raw response

Current checkpoint: new study; `scope` in progress. Goal: reach one learner-authored architecture modification and a defensible local fine-tuning transfer decision within 90 minutes. Your experience justifies a compressed calibration challenge, but stage skips require repository evidence.

Identity and scope:

- Official source: local fixture at `outputs/ai-architecture-learning-skill/evals/fixtures/llm`
- Official revision: `not available`
- Python/framework/device: `not available`
- Transfer track: adapt this decoder for local fine-tuning, then recommend adopt / adapt cautiously / reject

Evidence ledger:

- `[runtime-verified]` none yet
- `[source-confirmed]` none yet
- `[docs-stated]` none yet
- `[inferred]` The likely execution spine is configuration → model construction → decoder blocks → grouped attention → logits/loss.
- `[inferred]` The architecture skeleton likely separates embeddings, repeated decoder layers, grouped query/key-value projections, normalization/residual paths, and output projection.

Provisional route: `standard`, with advanced coaching depth. I will promote it immediately to `accelerated` if your first artifact demonstrates navigation, symbolic tensor flow, and parameter causality together.

Prediction: before inspecting deeply, where do you expect the first tensor-shape divergence between query heads and key/value heads, and what later operation must reconcile it?

One action—spend at most 10 minutes tracing the grouped-attention path. Use:

```powershell
rg -n "num_(attention|key_value)_heads|group|repeat_kv|forward|past_key_value|cache" outputs/ai-architecture-learning-skill/evals/fixtures/llm
```

Return only:

```text
official source/revision: <path + commit, or not available>
Python/framework/device: <versions/device, or not available>
entrypoint -> decoder block -> attention forward: <file:line chain>
Q/K/V symbolic shapes: <before and after head grouping>
reconciliation operation: <file:line + what it changes>
one coupled consequence of changing the grouping parameter: <your reasoning>
```

Checkpoint: `status=active`; `route=standard`; calibration evidence=`senior background reported, source competence not yet demonstrated`; mental model=`generic spine drafted, repository boundaries unresolved`; stage=`scope/in_progress`; acquired evidence=`none`; gates=`navigation:not_assessed, tensor_flow:not_assessed, parameter_causality:not_assessed, diagnosis:not_assessed, modification:not_assessed, transfer:not_assessed`; uncertainty=`revision and runtime environment unknown`; next action=`return the bounded grouped-attention trace above`.

Files read:

- `skills/learning-ai-architectures-from-source/SKILL.md`
- `superpowers/using-superpowers/SKILL.md`

## Why it failed

- Assigned `standard` from self-reported seniority before observable calibration work returned.
- Did not read the required learner-routing reference or inspect the supplied fixture.
- Filled both mental-model layers with generic Transformer components not established by the local source.
- Included no source-confirmed anchor in either layer.
- Asked for decoder, cache, and grouping operations that the small fixture may not contain.

The resulting refactor adds a new-study preflight, requires `pending_calibration`, and requires at least one source-confirmed boundary in each mental-model layer.

