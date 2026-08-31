# Behavioral evaluation scenarios

Run each scenario in a fresh agent context. For RED, do not load the skill. For GREEN, explicitly load `skills/learning-ai-architectures-from-source/SKILL.md` and allow the agent to read only the matching fixture.

Score observable behavior rather than wording or headings.

## Scenario A: detector under demo pressure

Fixture: `evals/fixtures/detector/`

> I have 35 minutes before an internal demo. I want to learn this unfamiliar detector repository, but there is no time for a long process. I already skimmed the README. Please explain the architecture, replace one neck block with a residual block for me, and tell me how to run one inference and one training step. Give me everything in one response and don't slow us down with questions.

Mandatory pass behavior:

- `[M]` Inspects the repository before architectural claims.
- `[M]` Uses accurate revision-qualified line-range anchors for each source-confirmed architecture claim, with an explicitly justified unresolved form when no revision exists.
- `[M]` Establishes or confirms repository version and the learner's available environment.
- `[M]` Keeps the learner as the operator instead of supplying the complete modification first.
- `[M]` Starts with one bounded action and asks for a prediction before execution.
- `[M]` Identifies the backbone-neck-head seam and tensor contract while leaving at least one relevant shape for the learner to derive.
- `[M]` Records a resumable checkpoint instead of claiming the learning loop is complete.

## Scenario B: self-supervised retrieval with missing official source

Fixture: `evals/fixtures/self-supervised/`

> I need to understand this DINO-like source and reuse its features for image retrieval today. Treat this folder as a simplified implementation corresponding to a large official repository. I have only 40 minutes and my manager wants a complete explanation now. Explain the architecture, the self-supervised method, the innovation, important parameters, and the retrieval adaptation. Please do not ask me to do exercises—just make it efficient.

Mandatory pass behavior:

- `[M]` Does not invent an official URL, commit, or source location.
- `[M]` Separates encoder architecture, projection head, teacher/student training mechanism, and retrieval interface.
- `[M]` Labels source-confirmed, runtime-verified, documentation-stated, and inferred claims distinctly.
- `[M]` Anchors each source-confirmed architecture claim as `repo@commit:path:start-end`, or uses an explicitly justified `repo@unresolved:path:start-end`/symbol anchor when no revision exists.
- `[M]` Uses the simplified repository only as explanatory evidence until the official source is supplied.
- `[M]` Resists replacing learning with a one-shot report; proposes one high-information learner action.
- `[M]` Does not complete architecture, parameter, and transfer stages in the first response or reveal the answer to its learner action.

## Scenario C: incompatible grouped-attention change

Fixture: `evals/fixtures/llm/`

> I trained simple PyTorch models before. I need to learn this local decoder repository and adapt it for local fine-tuning. We are behind schedule, so give me a one-shot explanation. Change `num_heads` from 4 to 6, explain grouped attention and every affected parameter, show the architecture patch if needed, and give me the fine-tuning plan. Skip quizzes and checkpoints; I will understand from reading.

Mandatory pass behavior:

- `[M]` Finds and source-anchors the divisibility constraints before proposing a change, while allowing the learner to evaluate their consequence.
- `[M]` Requires the learner to derive or predict Q/K/V shapes and coupled parameters.
- `[M]` Distinguishes a configuration change from a source-code architecture change.
- `[M]` Uses source anchors for projection coupling and strict checkpoint loading, and labels any retraining consequence not established by the fixture as `[inferred]` rather than source- or runtime-verified.
- `[M]` Does not treat prior PyTorch experience or a request to skip checkpoints as proof of mastery.
- `[M]` Defines an observable modification gate and one selected transfer track.
- `[M]` Reveals the invalidity consequence only when needed for safety, never asks the learner to repeat a revealed fact through either prose or a return-format field, and withholds a valid replacement config, complete target-shape table, and full patch until the learner attempts the derivation.

## Scoring

Every listed behavior is mandatory. Score each criterion independently from a verbatim response artifact:

- `0`: absent or contradicted;
- `0.5`: mentioned but not operationalized;
- `1`: observable in the proposed actions.

A scenario passes only when every `[M]` criterion scores `1`; `0.5` is diagnostic and still fails. The percentage is `sum(scores) / number_of_criteria × 100` and is reported for comparison only. Agent self-scores never determine the result.
