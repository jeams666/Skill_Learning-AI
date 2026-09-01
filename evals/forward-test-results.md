# Exploratory forward-test results

Updated: 2026-09-01

## What was tested

Fresh GPT-5.6 Terra agents at medium reasoning loaded the skill and inspected only the matching fixture plus references routed by the skill. The orchestrator supplied the exact scenario prompt; responding agents could not read the rubric, previous transcripts, baseline, scorecard, or results. They made no repository edits.

The complete procedure is in [`run-protocol.md`](run-protocol.md), raw responses and files-read lists are in [`transcripts/`](transcripts/), and the independent per-criterion audit is in [`scorecards.md`](scorecards.md). Responding-agent self-scores were not used.

## Final-snapshot observations

| Scenario/run | Independent score | Result | Main observation |
|---|---:|---|---|
| A — detector | 7/7 | Pass | Preserved the learner as operator, accurately anchored backbone → neck → head, and withheld the residual contract/shape derivation and patch. |
| B — retrieval, first retained final-snapshot sample | 5.5/7 | **Fail** | Kept the retrieval answer hidden but over-compressed encoder, projection-head, and teacher/student boundaries; its unresolved anchor was also malformed and justified too late. |
| B — retrieval, next fresh sample | 7/7 | Pass | Separated the major boundaries, declared why anchors were unresolved, masked the retrieval edge, and assigned one source trace. |
| C — grouped attention | 7/7 | Pass | Anchored configuration, projection, strict-load, and checkpoint-save seams; asked only for unrevealed compatible values and symbolic shapes. |
| D — experienced learner routing | 8/8 | Pass | Kept routing pending until evidence, performed source preflight, built a source-confirmed two-layer mental model, and assigned one accelerated calibration artifact without weakening graduation. |
| E — schema-v1 resume | 6/6 | Pass | Migrated to the v2 namespace without resetting evidence, kept the route provisional, and resumed the saved parameter action. |
| F — untouched schema-v1 defaults | 5/5 | Pass | Mapped null route/gates deterministically and preserved supplied lab, misconception, open-question, nested extension, root extension, stage, and next-action data. |

The v0.1 snapshot produced three passing exemplars from four reported runs; the retained B run at 5.5/7 is a mandatory failure. The v0.2 `53d305…` snapshot adds one clean D pass and one clean E pass after adaptive upgrade-baseline/GREEN development; final snapshot `ad87b6…` adds a clean 5/5 default-v1 migration probe. These sets answer different development questions and must not be combined into a success-rate estimate.

All material D/E failures are retained. They include premature route assignment, delegated preflight, incomplete learning endpoints, stage-skipping language, missing runtime evidence, a nominal no-write command without `-B`, incomplete self-contained citation spans, conflicting v1/v2 route state, and incorrect v2 field namespaces. The clean final responses independently passed D at 8/8 and E at 6/6 with no partly supported source-confirmed clause. This is adaptive design evidence, not response reliability.

## What the failures changed

Development probes found several ways a polished answer could imitate teaching without measuring learning:

1. full architecture, parameter, transfer, or patch answers were delivered before a learner attempt;
2. a revealed value or invariant was repeated in the question or a blank return-template field;
3. `source-confirmed` text named files but omitted line ranges, used an incorrect range, or combined unsupported clauses;
4. an `@unresolved` anchor appeared before a declarative reason for the missing revision;
5. a qualifier such as `teacher-side` partially revealed a deliberately masked retrieval edge;
6. a config-only or loss-only edit could previously appear sufficient for modification mastery.
7. challenge-depth wording did not create a persistent learning route or distinct architecture skeleton;
8. an agent could label a route from seniority, infer a conventional Transformer map, or delegate initial source inspection;
9. a rapid map could look complete while its own citation spans omitted named execution edges.
10. a v1 resume could preserve scores while emitting two route authorities or moving new v2 fields outside `learner`.
11. a command described as no-write could still omit Python's `-B` bytecode guard.

The final instructions now contain an answer-leak audit over both prose and return fields, clause-level source-span verification, a declarative unresolved-anchor rule, candidate-free masked edges, explicit 0–3 gate semantics, an architecture-bearing core-module graduation requirement, evidence-based routes, a non-delegable source preflight, and a two-layer rapid mental model. Representative failures remain in [`transcripts/`](transcripts/); they are summarized in the scorecard.

## Fixture execution evidence

The three fixtures each provide deterministic synthetic inference and a one-step forward/backward/optimizer path. The six no-checkpoint commands completed successfully during review. Matching training checkpoints also loaded with `strict=True`, while a deliberately incompatible checkpoint produced a nonzero exit. The final verification procedure repeats these checks before handoff.

The printed `toy_plumbing_only...` labels are an evidence boundary: finite tensors, loss, and gradients verify local execution plumbing, not detector accuracy, DINO correctness, retrieval quality, language modeling, or fine-tuning quality.

## Interpretation boundary

This exploratory audit tests first-turn teaching behavior across six adversarial scenarios on three tiny PyTorch repositories. It does not establish multi-session retention, population-level learning outcomes, response reliability, support for every architecture repository, or downstream model-quality improvements. A reliability claim requires at least three fresh contexts per scenario, all completed responses reported, and no adaptive selection hidden from the result.
