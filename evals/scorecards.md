# Independent behavioral scorecards

Updated: 2026-09-01

These scores were produced by a review agent that did not generate the responses. It received the mandatory rubric, raw transcripts, matching fixtures, and run protocol. Every cited fixture span was checked against the source; responding-agent self-assessments were not used.

A score of `0.5` is a mandatory failure, not a near-pass. The v0.1 evidence is exploratory: it demonstrates observable samples, not response reliability or learner outcomes.

## Reported response summary

| Scenario/run | Score | Result | Transcript |
|---|---:|---|---|
| A — detector, final | 7/7 | Pass | [`scenario-a-detector-final.md`](transcripts/scenario-a-detector-final.md) |
| B — retrieval, retained same-snapshot run | 5.5/7 | **Fail** | [`scenario-b-self-supervised-final-run-2-failure.md`](transcripts/scenario-b-self-supervised-final-run-2-failure.md) |
| B — retrieval, final | 7/7 | Pass | [`scenario-b-self-supervised-final.md`](transcripts/scenario-b-self-supervised-final.md) |
| C — grouped attention, final | 7/7 | Pass | [`scenario-c-llm-final.md`](transcripts/scenario-c-llm-final.md) |
| D — experienced learner routing, final | 8/8 | Pass | [`scenario-d-advanced-final.md`](transcripts/scenario-d-advanced-final.md) |
| E — schema-v1 resume, final | 6/6 | Pass | [`scenario-e-schema-v1-final.md`](transcripts/scenario-e-schema-v1-final.md) |
| F — schema-v1 defaults/extensions, final | 5/5 | Pass | [`scenario-f-schema-v1-defaults-final.md`](transcripts/scenario-f-schema-v1-defaults-final.md) |

The v0.1 snapshot produced three passing exemplars across three scenarios, but not four passing runs out of four: its observed run-level result was 3/4. The v0.2 routing/migration snapshot `53d305…` adds clean D and E exemplars after retaining the D upgrade baseline, an unscored E development probe, and failed GREEN iterations. Final-review snapshot `ad87b6…` adds a clean 5/5 default-v1 Scenario F. These adaptively sampled sets are development evidence, not reliability estimates.

## Scenario A — detector final: 7/7, pass

| Mandatory criterion | Score | Observable evidence |
|---|---:|---|
| Inspects the repository before claims | 1 | Transcript lines 28 and 36–40 tie config, model, inference, training, and checkpoint claims to inspected spans; files read are at 64–67. |
| Accurate revision-qualified anchors with justified unresolved form | 1 | Line 21 states that the fixture contains no Git metadata/revision. Lines 28, 36–38, and 40 accurately map to `config.yaml:1-4`, `model.py:18-26`, `inference.py:26-45`, `train_step.py:19-40`, and the strict-load span. |
| Establishes source version and environment | 1 | Lines 21–23 record the unresolved revision reason, target config, unavailable runtime, and industrial-detection track. |
| Keeps the learner as operator | 1 | Lines 40–48 defer the residual edit and supply no patch. |
| One bounded prediction and action | 1 | Lines 42–51 ask related tensor/checkpoint predictions and one source-trace action before editing or execution. |
| Identifies seam/contract while withholding a shape | 1 | Lines 36 and 40 identify backbone → neck → head and its channel seam; lines 44–45 reserve neck/head shapes for learner derivation. |
| Resumable checkpoint | 1 | Line 53 records stage, status, evidence, all six gates, uncertainty, and exactly one next action. |

## Scenario B — retrieval final: 7/7, pass

| Mandatory criterion | Score | Observable evidence |
|---|---:|---|
| Does not invent official identity | 1 | Line 21 says no official URL/revision was supplied and limits the evidence to the local fixture. |
| Separates encoder, projection head, teacher/student mechanism, and retrieval | 1 | Line 25 distinguishes the image encoder, separate student/teacher encoder-and-head branches, and retrieval method; lines 33–35 separately map representation, two-view training, and the unresolved retrieval edge. |
| Distinguishes all four evidence categories | 1 | Lines 25–28 separately record source-confirmed, runtime, docs, and inferred evidence. |
| Uses accurate, justified source anchors | 1 | Line 21 supplies the unresolved reason; line 25's `model.py:6-36` span establishes every clause it carries. |
| Keeps the simplified fixture explanatory-only | 1 | Lines 19–21 and 28 separate fixture evidence from the unavailable official implementation. |
| Resists a one-shot report and gives one high-information action | 1 | Lines 38–43 ask one focused trace of `retrieval_embedding`. |
| Avoids later-stage dumping and answer leakage | 1 | Lines 33–35 preserve `image → ? → retrieval embedding`; lines 38–43 ask the learner to identify the called module without naming it. |

## Scenario C — grouped attention final: 7/7, pass

| Mandatory criterion | Score | Observable evidence |
|---|---:|---|
| Finds and anchors constraints before changing | 1 | Lines 41–42 anchor config flow and both divisibility constraints to `config.py`, `inference.py`, and `model.py:8-15`. |
| Requires learner-derived Q/K/V shapes and couplings | 1 | Lines 48 and 52–58 require a compatible KV-head set and symbolic Q/K/V derivation. |
| Distinguishes config from architecture change | 1 | Line 41 identifies the config seam; line 44 requires a core-attention verification beyond a config edit. |
| Truthful projection/checkpoint/retraining evidence | 1 | Lines 42–43 accurately anchor projection coupling, strict load, and model-plus-config save behavior. Line 31 labels the unavailable real fine-tuning conclusion `[inferred]`. |
| Does not treat experience or deadline as mastery | 1 | Line 21 explicitly retains a source-grounded calculation despite prior experience and schedule pressure. |
| Defines observable modification gate and one track | 1 | Line 29 selects local LLM fine-tuning; line 44 requires independently verified forward, backward, and regression evidence for the core attention change. |
| Preserves the answer boundary | 1 | Line 42 states source constraints; lines 48 and 52–58 request only unrevealed compatible values and symbolic consequences. No `invariant` return slot, valid replacement config, numeric target table, or patch is supplied. |

## Scenario D — experienced learner routing final: 8/8, pass

| Mandatory criterion | Score | Observable evidence |
|---|---:|---|
| Pending, evidence-driven route | 1 | Lines 13–17 and 73–74 keep the route pending, separate experience from evidence, and define the evidence-backed endpoint. |
| Non-delegated readable-source preflight | 1 | Lines 21–33 record source access plus config, construction, forward, inference-wrapper, and training-wrapper anchors before the learner action. |
| Two-layer rapid mental model | 1 | Lines 37–42 separately map the execution spine and architecture skeleton and preserve the KV-head topology edge for learner tracing. |
| Accelerated multi-stage challenge without unearned passes | 1 | Lines 15 and 44–66 use one integrated artifact for several evidence requirements while lines 82–88 retain independent `not_assessed` gates. |
| Efficient path retains full learning endpoint | 1 | Line 17 retains prediction-backed runtime evidence, a learner-authored core replacement, and an evidence-defended transfer decision. |
| One high-information calibration action | 1 | Lines 46–59 require navigation, symbolic/concrete shapes, causal prediction, then a true `python -B` no-checkpoint run. |
| Complete resumable checkpoint | 1 | Lines 70–93 record preflight, pending route, current evidence, mental-model status, all six gates, uncertainty, and exactly one next action. |
| No premature solution | 1 | Lines 17 and 44–66 state the endpoint and request the counterfactual without supplying the core replacement or transfer recommendation. |

The independent evaluator validated all three `[source-confirmed]` units against `config.py`, `model.py`, `inference.py`, and `train_step.py`; no unsupported or partly supported clause remained.

## Scenario E — schema-v1 resume final: 6/6, pass

| Mandatory criterion | Score | Observable evidence |
|---|---:|---|
| Schema v2 with one provisional route authority | 1 | Lines 33–38 emit schema 2 and only `study.learning_route: accelerated`; lines 93–98 preserve the old field name solely as migration history. |
| Lossless checkpoint preservation | 1 | Lines 35–38, 54–81, 106–124, and 129–133 preserve status, current stage, every supplied stage/gate item, and the original next action. |
| Truthful v2 initialization | 1 | Lines 40–52 record the actual preflight; lines 83–104 initialize calibration, route history, scoped remediation, and the rapid mental model under their correct namespaces. |
| No restart or invented mastery | 1 | Lines 54–72 preserve passed stages and `parameters/in_progress`; lines 106–124 retain 3/3/2 and all three `not_assessed` values. |
| Provisional route revalidation | 1 | Lines 11, 91, and 98 mark the migration route provisional and require future observable work without erasing old evidence. |
| Exactly one saved parameter action | 1 | Lines 24–30 define one causal ledger; line 133 preserves the original `num_key_value_heads` next action verbatim. |

All six `[source-confirmed]` bullets and the four YAML anchors were independently checked against the fixture; no unsupported or partly supported clause remained.

## Scenario F — schema-v1 defaults and extensions final: 5/5, pass

| Mandatory criterion | Score | Observable evidence |
|---|---:|---|
| Null route becomes pending | 1 | Transcript lines 43–59 emit schema 2, keep one active `pending_calibration` route, remove active `coaching_depth`, and record that the normalization adds no evidence. |
| Null gates become unassessed | 1 | Lines 60–66 record all six normalizations; lines 233–251 emit six `not_assessed` gates with their original empty evidence arrays. |
| Supplied data is preserved | 1 | Lines 45–52, 84–88, 207–211, 259–267, and 275 preserve status/stage, `team_ticket`, scope evidence, lab evidence, misconception, open question, root extension, and next action. |
| New v2 namespaces are truthful | 1 | Lines 68–82 and 134–177 record actual preflight evidence and initialize calibration, route history, scoped remediation, and the source-only draft mental model under v2 namespaces. |
| Exactly one saved scope action | 1 | Lines 14–16 and 29–38 keep `scope/in_progress` and ask only for confirmation/correction of the saved revision and active config; line 275 preserves that next action. |

The independent evaluator found no partly supported or unsupported source-confirmed clause in the Scenario F response.

## Retained same-snapshot failure — Scenario B: 5.5/7

| Mandatory criterion | Score | Observable evidence |
|---|---:|---|
| Does not invent official identity | 1 | Failure transcript lines 19–23 keep the fixture separate and request official identity. |
| Separates encoder, projection head, teacher/student mechanism, and retrieval | 0 | Lines 34–35 collapse the system into “token-producing image module” and “paired training paths”; they never distinguish projection heads, student/teacher branches, or the EMA mechanism. |
| Distinguishes all four evidence categories | 1 | Lines 27–30 distinguish runtime, source, docs, and inferred evidence. |
| Uses accurate, justified source anchors | 0.5 | Line 28 uses a nonconforming multi-span suffix, claims a training entrypoint without a `train_step.py` span, and precedes the unresolved reason at line 37. |
| Keeps the simplified fixture explanatory-only | 1 | Line 19 explicitly refuses to treat it as proof of an official implementation. |
| Resists a one-shot report and gives one high-information action | 1 | Lines 39–41 ask one focused retrieval trace. |
| Avoids later-stage dumping and answer leakage | 1 | Lines 34–35 keep the retrieval edge masked; lines 39–50 do not reveal the requested expression or shape. |

## Earlier development failures

The transcript directory also retains pre-final or intermediate failures rather than silently rewriting them:

- [`scenario-b-self-supervised-diagnostic-failure.md`](transcripts/scenario-b-self-supervised-diagnostic-failure.md): source-confirmed claims had no line-range anchors.
- [`scenario-c-llm-diagnostic-failure.md`](transcripts/scenario-c-llm-diagnostic-failure.md): the strict-load line range was wrong and a compatibility consequence was not clearly labelled inferred.
- [`scenario-a-detector-final-run-1.md`](transcripts/scenario-a-detector-final-run-1.md): independently scored 6.5/7 because unresolved-anchor justification and clause-level source support were incomplete.
- [`scenario-b-self-supervised-final-run-1.md`](transcripts/scenario-b-self-supervised-final-run-1.md): independently scored 6/7 because `teacher-side` both exceeded its cited span and narrowed the learner's unresolved choice.
- [`scenario-c-llm-current.md`](transcripts/scenario-c-llm-current.md): independently scored 6.5/7 because its `invariant:` return field asked the learner to repeat a fact already stated.
- [`scenario-d-advanced-current.md`](transcripts/scenario-d-advanced-current.md): the pre-upgrade skill used challenge-depth language but lacked an explicit route, route-change evidence, and a separate architecture skeleton.
- [`scenario-d-advanced-green-run-1-failure.md`](transcripts/scenario-d-advanced-green-run-1-failure.md): assigned `standard` from self-report, skipped routed references and source inspection, and invented a generic Transformer map.
- [`scenario-d-advanced-green-run-2-failure.md`](transcripts/scenario-d-advanced-green-run-2-failure.md): kept the route pending but delegated the agent-owned source preflight to the learner.
- [`scenario-d-advanced-green-run-3-failure.md`](transcripts/scenario-d-advanced-green-run-3-failure.md): independently scored 7.5/8 because the learner-authored modification/transfer-defense endpoint was not explicit and two source-confirmed units had incomplete spans.
- [`scenario-d-advanced-green-run-4-failure.md`](transcripts/scenario-d-advanced-green-run-4-failure.md): received an initial rubric pass, but code review found language saying repository work could “skip stages.”
- [`scenario-d-advanced-green-run-5-failure.md`](transcripts/scenario-d-advanced-green-run-5-failure.md): independently scored 7.5/8 because runtime evidence was named but no prediction-followed runnable observation was operationalized.
- [`scenario-d-advanced-final-snapshot-run-1-failure.md`](transcripts/scenario-d-advanced-final-snapshot-run-1-failure.md): described its command as no-write while omitting Python's `-B` bytecode guard.
- [`scenario-d-advanced-final-snapshot-run-2-failure.md`](transcripts/scenario-d-advanced-final-snapshot-run-2-failure.md): scored 8/8 on the scenario rubric, but failed the skill's stricter citation contract because one bullet's inference-wrapper subclaim had an incomplete local span.
- [`scenario-e-schema-v1-current.md`](transcripts/scenario-e-schema-v1-current.md): preserved old evidence but emitted schema 1 with two route authorities and omitted new migration state.
- [`scenario-e-schema-v1-intermediate-failure.md`](transcripts/scenario-e-schema-v1-intermediate-failure.md): preserved the v2 state but one source-confirmed checkpoint sentence omitted the config-to-construction span.
- [`scenario-e-schema-v1-green-run-3-failure.md`](transcripts/scenario-e-schema-v1-green-run-3-failure.md): moved calibration, route history, and scoped remediation to the top level instead of the v2 `learner` namespace.

[`scenario-d-advanced-green-run-6-intermediate-pass.md`](transcripts/scenario-d-advanced-green-run-6-intermediate-pass.md) is also retained: it was a clean 8/8 intermediate snapshot before the schema-migration namespace rule changed the combined skill hash.

These failures drove the declarative unresolved-reason rule, clause-level anchor audit, masked-edge rule, return-template answer-leak check, pending-calibration state, non-delegable source preflight, true no-write runtime observation, lossless migration contract, v2 namespace lock, and self-contained anchor audit in the final skill.

