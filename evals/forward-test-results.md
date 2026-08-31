# Exploratory forward-test results

Date: 2026-08-25

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

The final snapshot therefore has a passing exemplar for each scenario, but the sampled run-level result is **3/4**, not 4/4. The B failure is public and mandatory: 5.5/7 does not pass. These adaptively sampled runs are too few for a reliability estimate.

## What the failures changed

Development probes found several ways a polished answer could imitate teaching without measuring learning:

1. full architecture, parameter, transfer, or patch answers were delivered before a learner attempt;
2. a revealed value or invariant was repeated in the question or a blank return-template field;
3. `source-confirmed` text named files but omitted line ranges, used an incorrect range, or combined unsupported clauses;
4. an `@unresolved` anchor appeared before a declarative reason for the missing revision;
5. a qualifier such as `teacher-side` partially revealed a deliberately masked retrieval edge;
6. a config-only or loss-only edit could previously appear sufficient for modification mastery.

The final instructions now contain an answer-leak audit over both prose and return fields, clause-level source-span verification, a declarative unresolved-anchor rule, candidate-free masked edges, explicit 0–3 gate semantics, and an architecture-bearing core-module graduation requirement. Representative failures remain in [`transcripts/`](transcripts/); they are summarized in the scorecard.

## Fixture execution evidence

The three fixtures each provide deterministic synthetic inference and a one-step forward/backward/optimizer path. The six no-checkpoint commands completed successfully during review. Matching training checkpoints also loaded with `strict=True`, while a deliberately incompatible checkpoint produced a nonzero exit. The final verification procedure repeats these checks before handoff.

The printed `toy_plumbing_only...` labels are an evidence boundary: finite tensors, loss, and gradients verify local execution plumbing, not detector accuracy, DINO correctness, retrieval quality, language modeling, or fine-tuning quality.

## Interpretation boundary

This exploratory audit tests first-turn teaching behavior on three tiny PyTorch repositories. It does not establish multi-session retention, population-level learning outcomes, response reliability, support for every architecture repository, or downstream model-quality improvements. A reliability claim requires at least three fresh contexts per scenario, all completed responses reported, and no adaptive selection hidden from the result.
