# Example resumable checkpoint

This is an illustrative checkpoint built from the included miniature grouped-attention fixture. It demonstrates the level of specificity expected; it is not a completed study.

## Scope

- Repository role: teaching fixture, not an official upstream implementation.
- Source snapshot: `fixture@unresolved`; this portable example does not embed the enclosing Git commit, so it must be replaced with the learner's actual pinned revision when used.
- Target: `evals/fixtures/llm/model.py` with `config.py`.
- Transfer track: local LLM fine-tuning.
- Coaching depth: standard.

## Evidence acquired

- `[source-confirmed]` `GroupedAttention.__init__` rejects configurations where `hidden_size % num_heads != 0` or `num_heads % num_key_value_heads != 0`. `fixture@unresolved:evals/fixtures/llm/model.py:5-15` (`GroupedAttention.__init__`).
- `[source-confirmed]` Q uses `num_heads`; K and V use `num_key_value_heads`. `fixture@unresolved:evals/fixtures/llm/model.py:13-21` (`q_proj`, `k_proj`, `v_proj`, and their reshape expressions).
- `[source-confirmed]` the current configuration is hidden width 64, four query heads, and two key/value heads. `fixture@unresolved:evals/fixtures/llm/config.py:1-8` (`MODEL_CONFIG`).
- `[inferred]` increasing query heads from four to six without changing hidden width will fail construction before a forward pass.

## Learner explanation

"The model groups several query heads over fewer key/value heads. The query-head count determines `head_dim`, so changing only `num_heads` changes a divisibility invariant and the Q projection shape. It is not yet a valid experiment until I account for hidden width, KV grouping, and checkpoint shapes."

## Mastery state

| Gate | Score | Evidence |
|---|---:|---|
| Navigation | 3 | Located config, constructor guard, projections, reshape, and returned output. |
| Tensor flow | 2 | Correct qualitative account; has not independently written every Q/K/V shape. |
| Parameter causality | 2 | Found two couplings; has not calculated parameter-count or checkpoint changes. |
| Diagnosis | 1 | Predicted the exception but has not run and localized it. |
| Modification | 0 | No learner-authored patch. |
| Transfer | 0 | Fine-tuning plan not defended. |

## Misconception to repair

The learner initially treated a head-count edit as an isolated tuning parameter. The source shows it is a structural contract with coupled dimensions.

## Exactly one next action

Before running code, write the Q, K, and V shapes for batch 2, sequence 16 under the current configuration, then predict the first observable failure after changing only `num_heads` to 6. Return the derivation, not just the final dimensions.
