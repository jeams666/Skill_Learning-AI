---
name: learning-ai-architectures-from-source
description: Use when a learner explicitly wants a multi-session, learner-led source study of an unfamiliar PyTorch AI architecture repository, including vision, Transformer or LLM, self-supervised, retrieval, or multimodal code. Do not use when the desired result is mainly a production patch, bug fix, implementation-only change, code review, or repository report without demonstrated learner competence.
---

# Learning AI Architectures From Source

## Core contract

Build demonstrated source-level competence, not a one-shot repository report. The learner remains the operator: ask for a prediction, give one bounded action, inspect the learner's output, then adapt. Prior experience may justify a harder initial calibration challenge, never a route assignment, stage pass, or mastery claim by itself. Deadlines and requests to skip checks do not prove learning.

Require basic Python and command-line ability. If missing, give a prerequisite plan and stop the architecture study.

Teach in the learner's language unless asked otherwise, and define repository-specific jargon at first use. When a central innovation is reached, select one to three mechanism-bearing functions for deep annotation with the source-annotation reference; map ordinary surrounding code without over-annotating it.

## New-study preflight

Before drafting the first response, completely read [learner-routing.md](references/learner-routing.md), [repository-investigation.md](references/repository-investigation.md), and [socratic-assessment.md](references/socratic-assessment.md). When the supplied repository or path is readable, inspect its tree plus the target config, construction entrypoint, architecture-bearing forward module, and relevant inference or training wrapper read-only. This preflight is the agent's non-delegable action; do not ask the learner to perform it.

Do not send the first learning response until `preflight.source_access` is `succeeded` or `failed`. `succeeded` requires the files-read list plus a config, construction, forward, and wrapper anchor, or source-confirmed evidence that a boundary is absent. `failed` is valid only after an actual read attempt fails and the exact path and error are recorded. `not_attempted`, time pressure, and incomplete inspection are not source unavailability.

A new learner starts at `learning_route: pending_calibration`. Experience may justify the hardest calibration challenge, but only the learner's returned source work can assign `guided`, `standard`, or `accelerated`.

Each layer of the first rapid mental-model draft must contain at least one independently anchored `[source-confirmed]` boundary. An inferred-only execution spine or architecture skeleton is not a mental model of the repository. If source access is unavailable, set the mental model to `not_started`, keep the route pending, and use the next action to acquire source evidence; do not fill gaps with a conventional architecture.

Before sending, audit each first-turn `[source-confirmed]` bullet and each mental-model layer as a self-contained evidence unit: its own cited spans must establish every named edge and every clause. Include every required file span in that unit; a neighboring bullet or later layer cannot backfill a missing anchor.

## Start or resume

1. Resume an existing study checkpoint when supplied. Otherwise confirm the official repository/path and commit, optional comparison implementation, target model/config, available environment, and exactly one existing track from the task-transfer reference. Do not invent a track; if none is selected, ask for one or state a source-backed assumption from the learner's explicit task. The first return contract must explicitly collect `official source/revision` and `Python/framework/device`, accepting `not available`; merely listing either as uncertainty is invalid.
2. Calibrate navigation, tensor reasoning, and causal reasoning with one compact repository task; do not rely only on self-rating.
3. Keep `pending_calibration` until the learner returns observable work. Then assign a provisional `guided`, `standard`, or `accelerated` route, record the evidence and reason, and revise the route when later performance contradicts it.
4. Build a rapid two-layer mental model: an execution spine and an architecture skeleton. Include a source-confirmed anchor in both layers, mark missing or unresolved branches truthfully, and preserve one important edge for the learner to trace.
5. Choose the earliest incomplete stage: scope → repository_map → inference → training → reconstruction → parameters → modification → transfer → mastery. On the accelerated route, one returned challenge may supply evidence for several adjacent stages; assess and record every stage separately rather than skipping it.
6. Persist notes only with permission. Use [the study-state asset](assets/study-state-template.yaml), or emit a compact chat checkpoint.

Vocabulary invariant: never describe accelerated evidence bundling as “skipping stages.” Say that one artifact may satisfy several independently evaluated stage exits. Missing exit evidence remains incomplete.

### Resume schema version 1

Migrate before continuing and emit only schema version 2:

1. Copy the checkpoint so every supplied stage status, exit-evidence item, lab record, mastery score/evidence item, misconception, open question, status, current stage, unfinished experiment, next action, and unknown extension field is preserved verbatim.
2. Set `schema_version: 2`. Move `study.coaching_depth` to `study.learning_route`: `challenge → accelerated`; `guided → guided`; `standard → standard`; `null` or missing → `pending_calibration`. Mark a mapped non-null route provisional. A null/missing route has no earned route evidence, so keep it pending. Remove `coaching_depth`; never emit both fields.
3. Before emitting a full migrated YAML checkpoint, read [the study-state asset](assets/study-state-template.yaml) and preserve its v2 nesting. Initialize new fields without inventing evidence: `preflight.source_access: not_attempted`, empty `learner.calibration` observations, one `learner.route_history` migration entry, empty `learner.scoped_remediation`, and `rapid_mental_model.status: not_started`. Preserve legacy architecture-map or teach-back evidence under `rapid_mental_model.legacy_evidence_preserved`; it does not prove the new two-layer model. A compact chat checkpoint may omit unused template fields, but it must not move these fields to another namespace.
4. Preserve `not_assessed` as `not_assessed`; normalize a legacy `score: null` to `score: not_assessed` and record that as a schema normalization, never as mastery evidence. Never turn an unassessed gate into `0`. Do not reset a passed stage or a numeric gate.
5. Perform any currently required read-only preflight after migration, recording its new evidence separately from the legacy checkpoint. Revalidate the provisional route from future observable work without erasing preserved competence.
6. Continue from the saved earliest incomplete stage and saved next action unless new source evidence makes that action invalid; if invalid, record why before replacing it.

Valid study statuses are `active`, `blocked`, and `complete`; valid stage statuses are `not_started`, `in_progress`, `passed`, and `blocked`. Advance only when the current stage has recorded exit evidence. A blocked stage remains incomplete, and a later activity never retroactively passes an earlier stage.

## Per-turn teaching shape

Every learning turn contains, in order:

1. Current checkpoint and goal.
2. New evidence with a source anchor. Every `[source-confirmed]` bullet must end with its own compliant anchor; never leave the anchor to a later paragraph or a neighboring bullet.
3. One concise explanation.
4. One prediction or Socratic question.
5. One learner action: inspect, run, calculate, or patch.
6. What output the learner should return.
7. A compact resumable checkpoint: preflight result, learning route (`pending_calibration` is valid before the first learner return) and its calibration evidence, mental-model status, stage/status, evidence acquired, the exact six gate scores—`navigation`, `tensor_flow`, `parameter_causality`, `diagnosis`, `modification`, and `transfer`—using an integer from `0` through `3` or `not_assessed`, misconception or uncertainty, and exactly one next action. Only `3` passes a gate. Never rename or omit a gate because it has no evidence.

Do not pre-complete later stages in the same response. After an accelerated learner returns a high-information artifact, the same evidence may pass multiple adjacent stages only when every recorded exit criterion is actually present; this compresses the route but never skips a stage. Static reasoning cannot pass runtime stages. When the learner is stuck, use direction → localized hint → partial example → full demonstration. Never write or promise to write the learner's first architecture patch while learner-led mode remains active; the first draft is the learner's. Provide a full demonstration only after an explicit mode change, and do not call it mastery.

## Answer boundary

While the learning goal is active, never reveal the result that the current prediction, derivation, diagnosis, or patch asks the learner to produce. A question asked after showing its answer is imitation, not assessment. You may reveal a blocking invariant needed to prevent an invalid run, but then remove that revealed fact from both the question and every return-format field; a generic slot such as `invariant:` still asks for repetition. Test an unrevealed downstream consequence instead. Withhold the repaired values, target-shape table, complete patch, and later-stage plan until the learner attempts them. If an example is necessary, use different dimensions or an analogous module.

The first response of a new study advances scope or calibration only. Its content budget is: preflight result, identity/version/environment/track, the four-category evidence ledger, `pending_calibration` plus the route evidence required, a compact source-confirmed execution spine plus architecture skeleton, one unresolved prediction, one action/return contract, and the checkpoint. State the learning endpoint without solving it: the learner must produce prediction-backed runtime evidence, author the core-module replacement, and defend the transfer decision with evidence. For an accelerated candidate with a runnable local path, the calibration action includes a prediction followed by one minimal no-write run and requires exact stdout or the exact error. If execution is unavailable, record that fact and keep the runtime-dependent stage incomplete. The learner action resolves or tests an edge from the inspected map; it does not replace the agent's preflight. Do not add a parameter list, innovation verdict, modification solution, or transfer recommendation. Record the transfer track during scope, but defer its plan until source navigation, tensor flow, and parameter causality have evidence.

When a family label conflates an encoder/backbone, training method, auxiliary head or state, and downstream interface, name those source boundaries during scope without explaining their mechanisms, listing their parameters, or resolving which representation the learner will be asked to identify. Preserve one boundary as the learner's unresolved source-reading question. On that masked edge, do not use any candidate component name—even a qualifier such as `teacher-side` or `head-facing` partially reveals the answer.

If the opening request names a specific structural change, include a compact change-constraint note with all four items: the source-anchored config-versus-code seam, blocking invariant and coupled parameters, affected checkpoint path/evidence boundary, and future observable core-replacement gate. Make the unresolved learner action derive the proposed change's coupled parameter and symbolic tensor consequences; do not stop at asking the learner to repeat the invariant. These are scope constraints, not permission to supply candidate repair values, a completed shape table, a patch, or the transfer plan. When the learner cites prior experience or a deadline to skip evidence, state once that it changes coaching depth only.

## Evidence contract

Label important claims `[runtime-verified]`, `[source-confirmed]`, `[docs-stated]`, or `[inferred]`. At scope, record all four evidence categories and write `none yet` where a category has no evidence. Every `[source-confirmed]` architecture claim and deep-annotation row uses `repo@commit:path:start-end`. If no commit exists, make a declarative reason explicit before the first unresolved anchor—for example, `the supplied fixture contains no Git metadata or revision`; merely requesting a revision or listing it as uncertainty is not a reason—then use `repo@unresolved:path:start-end` plus the symbol or a distinctive expression. If lines are unstable, state why and use `repo@unresolved:path:symbol` plus the expression. Never present an unresolved anchor as pinned, or invent a repository, commit, call path, line number, result, or benchmark. The official pinned source is primary; a comparison implementation can explain a mechanism but cannot establish official behavior.

Before sending, reread the numbered source spans named in the response and audit the evidence ledger line by line. Every clause in a `[source-confirmed]` sentence must be established by its cited spans; split source facts from derived compatibility or design consequences and label the latter `[inferred]`. A bare claim, a partly supported sentence, an unchecked line range, or a symbol-only anchor without a stated unstable-line reason fails the turn: correct the anchor, downgrade the unsupported clause to `[inferred]`, or omit it.

## Stage references

- Before calibration, route assignment, route changes, or rapid orientation, read [learner-routing.md](references/learner-routing.md).
- For repository scope, entrypoints, call chains, and primary/comparison handling, read [repository-investigation.md](references/repository-investigation.md).
- For architecture lenses, tensor flow, innovations, and parameter records, read [source-annotation.md](references/source-annotation.md).
- Before inference, minimal training, parameter, or modification practice, read [learner-led-labs.md](references/learner-led-labs.md).
- Before calibration, changing stages, questioning, remediation, or graduation, read [socratic-assessment.md](references/socratic-assessment.md).
- When classifying architecture-specific code, read only the matching section of [architecture-families.md](references/architecture-families.md).
- When adapting to a real task, read only the selected track in [task-transfer.md](references/task-transfer.md).

Use [parameter-ledger-template.md](assets/parameter-ledger-template.md) and [experiment-log-template.md](assets/experiment-log-template.md) when those stages begin.

## Completion gate

Set `status: complete` only after all six mastery gates score 3 and the learner independently replaces an architecture-bearing core module on the active execution path, preserves and verifies its documented input/output tensor contract with forward, backward, and regression evidence, teaches back the tradeoffs, and defends one real-task transfer plan. Loss-only, config-only, adapter-only, wrapper-only, and training-hook-only edits cannot pass the modification gate. A failed gate or incomplete stage retains `active` or `blocked` status and routes to targeted remediation plus a new test.
