# Independent behavioral scorecards

Date: 2026-08-25

These scores were produced by a review agent that did not generate the responses. It received the mandatory rubric, raw transcripts, matching fixtures, and run protocol. Every cited fixture span was checked against the source; responding-agent self-assessments were not used.

A score of `0.5` is a mandatory failure, not a near-pass. The v0.1 evidence is exploratory: it demonstrates observable samples, not response reliability or learner outcomes.

## Final-snapshot summary

| Scenario/run | Score | Result | Transcript |
|---|---:|---|---|
| A — detector, final | 7/7 | Pass | [`scenario-a-detector-final.md`](transcripts/scenario-a-detector-final.md) |
| B — retrieval, retained same-snapshot run | 5.5/7 | **Fail** | [`scenario-b-self-supervised-final-run-2-failure.md`](transcripts/scenario-b-self-supervised-final-run-2-failure.md) |
| B — retrieval, final | 7/7 | Pass | [`scenario-b-self-supervised-final.md`](transcripts/scenario-b-self-supervised-final.md) |
| C — grouped attention, final | 7/7 | Pass | [`scenario-c-llm-final.md`](transcripts/scenario-c-llm-final.md) |

Thus, the final snapshot produced three passing exemplars across the three scenarios, but not four passing runs out of four: the observed run-level result is 3/4. Do not interpret that small, adaptively sampled result as a reliability estimate.

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

The transcript directory also retains pre-final-snapshot failures rather than silently rewriting them:

- [`scenario-b-self-supervised-diagnostic-failure.md`](transcripts/scenario-b-self-supervised-diagnostic-failure.md): source-confirmed claims had no line-range anchors.
- [`scenario-c-llm-diagnostic-failure.md`](transcripts/scenario-c-llm-diagnostic-failure.md): the strict-load line range was wrong and a compatibility consequence was not clearly labelled inferred.
- [`scenario-a-detector-final-run-1.md`](transcripts/scenario-a-detector-final-run-1.md): independently scored 6.5/7 because unresolved-anchor justification and clause-level source support were incomplete.
- [`scenario-b-self-supervised-final-run-1.md`](transcripts/scenario-b-self-supervised-final-run-1.md): independently scored 6/7 because `teacher-side` both exceeded its cited span and narrowed the learner's unresolved choice.
- [`scenario-c-llm-current.md`](transcripts/scenario-c-llm-current.md): independently scored 6.5/7 because its `invariant:` return field asked the learner to repeat a fact already stated.

These failures drove the declarative unresolved-reason rule, clause-level anchor audit, masked-edge rule, and return-template answer-leak check in the final skill.
