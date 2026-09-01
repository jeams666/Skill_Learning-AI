# Behavioral evaluation scenarios

Run each scenario in a fresh agent context. For a new-skill-creation RED baseline, do not load any version of the skill. For an upgrade baseline, load the last released skill but withhold the candidate changes and label the run `UPGRADE BASELINE`, not `RED`. For GREEN, explicitly load the candidate `skills/learning-ai-architectures-from-source/SKILL.md` and allow the agent to read only the matching fixture.

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

## Scenario D: experienced learner requesting the shortest evidence-based route

Fixture: `evals/fixtures/llm/`

> I am a senior AI engineer with five years of PyTorch experience. I have implemented YOLO variants, ViTs, and decoder-only Transformers, and I can read unfamiliar Python repositories quickly. I have 90 minutes before I must advise my team whether this local grouped-attention decoder is worth adapting for local fine-tuning. My manager expects a concrete recommendation today, and I do not want beginner explanations or a long curriculum. Build me a fast mental model of the repository, test whether I can skip material I already know, and route me through the shortest evidence-based path to one architecture modification and a transfer decision. Start now; do not ask me to choose a learning level.

Mandatory pass behavior:

- `[M]` Keeps the initial route pending until observable calibration evidence returns, states the exact evidence required for an accelerated route, and makes later route changes evidence-driven rather than seniority- or self-selected.
- `[M]` Performs the readable-source preflight itself before responding and records anchored config, construction, forward, and wrapper evidence instead of delegating initial repository inspection to the learner.
- `[M]` Builds a compact two-layer orientation consisting of an execution spine and an architecture skeleton, source-anchors known boundaries, and preserves at least one unresolved edge for the learner to trace.
- `[M]` Uses an accelerated challenge when the learner demonstrates strong evidence: one bounded learner action may collect exit evidence for multiple adjacent early stages, but no stage passes without its own recorded exit evidence.
- `[M]` Avoids beginner exposition and redundant exercises while retaining prediction, runtime evidence, learner-authored modification, and transfer-defense requirements.
- `[M]` Gives one high-information action that tests at least source navigation and tensor reasoning before accepting the advanced route.
- `[M]` Records `pending_calibration`, current calibration evidence, mental-model status, all six mastery gates, and exactly one next action in the resumable checkpoint.
- `[M]` Does not provide the complete architecture modification or transfer recommendation before the learner's attempt.

## Scenario E: resume a schema-v1 challenge checkpoint

Fixture: `evals/fixtures/llm/`

> Resume this saved study checkpoint after upgrading the skill. Do not restart my study or discard evidence. Continue with exactly one next action.
>
> ```yaml
> schema_version: 1
> study:
>   status: active
>   coaching_depth: challenge
>   current_stage: parameters
> stage_progress:
>   scope: {status: passed, exit_evidence: [source identity and environment recorded]}
>   repository_map: {status: passed, exit_evidence: [construction and forward paths traced]}
>   inference: {status: passed, exit_evidence: [prediction and runtime shapes recorded]}
>   training: {status: passed, exit_evidence: [finite loss, gradients, optimizer step recorded]}
>   reconstruction: {status: passed, exit_evidence: [architecture map and teach-back recorded]}
>   parameters: {status: in_progress, exit_evidence: []}
> mastery_gates:
>   navigation: {score: 3, evidence: [independent source trace]}
>   tensor_flow: {score: 3, evidence: [independent Q/K/V derivation]}
>   parameter_causality: {score: 2, evidence: [head coupling partly explained]}
>   diagnosis: {score: not_assessed, evidence: []}
>   modification: {score: not_assessed, evidence: []}
>   transfer: {score: not_assessed, evidence: []}
> session_checkpoint:
>   next_action: predict parameter and checkpoint effects of changing num_key_value_heads
> ```

Mandatory pass behavior:

- `[M]` Migrates to schema version 2 and maps `coaching_depth: challenge` to provisional `learning_route: accelerated` without retaining two conflicting route fields.
- `[M]` Preserves the study status, current stage, every stage status and exit-evidence item, all six mastery scores/evidence, and the existing next action unless source evidence makes it unsafe.
- `[M]` Initializes new preflight, calibration, route-history, scoped-remediation, and rapid-mental-model fields truthfully; it does not claim that legacy data proves the new preflight or mental-model requirements.
- `[M]` Does not restart at scope, reset passed gates, or convert historical `not_assessed` values to numeric mastery evidence.
- `[M]` Explains that the migrated accelerated route is provisional and will be revalidated from future observable work without erasing preserved evidence.
- `[M]` Continues from `parameters/in_progress` with exactly one learner action tied to the saved `num_key_value_heads` prediction.

## Scenario F: resume an untouched schema-v1 default with extensions

Fixture: `evals/fixtures/llm/`

> Resume this untouched schema-v1 checkpoint after upgrading the skill. Preserve every supplied value, including fields the new template does not know. Do not restart the study. Continue with exactly one next action.
>
> ```yaml
> schema_version: 1
> study:
>   status: active
>   coaching_depth: null
>   current_stage: scope
>   team_ticket: ARCH-17
> stage_progress:
>   scope: {status: in_progress, exit_evidence: [repository path supplied]}
> labs:
>   minimal_inference:
>     status: not_started
>     evidence: [learner reserved a CPU-only window]
> mastery_gates:
>   navigation: {score: null, evidence: []}
>   tensor_flow: {score: null, evidence: []}
>   parameter_causality: {score: null, evidence: []}
>   diagnosis: {score: null, evidence: []}
>   modification: {score: null, evidence: []}
>   transfer: {score: null, evidence: []}
> misconceptions:
>   - grouped attention is identical to full multi-head attention
> open_questions:
>   - which active path uses num_key_value_heads?
> custom_extension:
>   owner: vision-platform
>   review_required: true
> session_checkpoint:
>   next_action: confirm the repository revision and active config
> ```

Mandatory pass behavior:

- `[M]` Emits schema version 2, removes the active `coaching_depth` field, and maps its null value to `learning_route: pending_calibration` rather than inventing an earned route.
- `[M]` Normalizes all six legacy null gate scores to `not_assessed`, preserves their evidence arrays, and does not count the normalization as mastery evidence.
- `[M]` Preserves the non-empty lab evidence, misconception, open question, nested unknown `study.team_ticket`, root `custom_extension`, study status, current stage, scope status/evidence, and saved next action.
- `[M]` Initializes preflight, `learner.calibration`, `learner.route_history`, `learner.scoped_remediation`, and `rapid_mental_model` truthfully under the v2 namespaces.
- `[M]` Continues from `scope/in_progress` with exactly one learner action tied to confirming the saved repository revision and active config.

## Scoring

Every listed behavior is mandatory. Score each criterion independently from a verbatim response artifact:

- `0`: absent or contradicted;
- `0.5`: mentioned but not operationalized;
- `1`: observable in the proposed actions.

A scenario passes only when every `[M]` criterion scores `1`; `0.5` is diagnostic and still fails. The percentage is `sum(scores) / number_of_criteria × 100` and is reported for comparison only. Agent self-scores never determine the result.

