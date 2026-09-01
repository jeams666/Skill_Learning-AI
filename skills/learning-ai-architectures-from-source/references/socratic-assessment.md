# Socratic assessment and remediation

Read this reference for learner calibration, mastery questions, remediation, and graduation decisions.

## Calibration

Do not infer skill from job title, confidence, or a list of completed courses. Read [learner-routing.md](learner-routing.md), then use one compact challenge drawn from the current repository that samples two or three of these observable abilities:

- navigate from a config key to its use site;
- predict a tensor shape through one operation;
- explain a forward/backward or train/eval distinction;
- identify the cause of a controlled error.

Assign a provisional learning route:

- Guided: smaller actions, explicit framework explanations, early hints.
- Standard: source-chain and causal-experiment emphasis.
- Accelerated: integrated evidence, fewer hints, more counterfactuals, design, and diagnosis.

Record the observed calibration evidence and route reason. The same graduation gates apply to every route; only the density of evidence per action changes. Route changes are local and evidence-driven: remediate a weak concept without discarding competence already demonstrated elsewhere.

## Question ladder

Ask one question at a time and adapt from the answer:

1. Locate: where does this behavior enter the code?
2. Trace: what calls it and what does it call?
3. Predict: what shape/state/result follows?
4. Explain: why does the design satisfy the problem constraint?
5. Counterfactual: what fails if it is removed or changed?
6. Diagnose: which assumption explains an observed mismatch?
7. Modify: what is the smallest compatible change?
8. Transfer: why does that change fit the selected real task?

Do not reveal the answer inside the question. After an incorrect answer, probe the reasoning before giving a hint.

## Pre-send answer-leak check

Before every learner question or action, compare it with everything already stated in the response. Revise when the response has already supplied any target value, target shape, candidate configuration, patch, diagnosis, or causal explanation that the learner is asked to derive. Audit headings and blank return templates too: a field named `invariant`, `failure`, or `diagnosis` still requests repetition when that fact was already stated. Give the source constraint and ask for its consequence; do not give the consequence and ask the learner to repeat it. If safety requires stating a failure such as `64 % 6 != 0`, do not then ask which divisibility check fails; ask for an unrevealed compatible-field set or symbolic downstream shape instead. A worked example must use different values or a different module.

Under one-shot pressure, stop after the earliest incomplete rung. A compact architecture map may orient the learner, but a combined architecture explanation, parameter table, repair, and transfer plan is a report—not a learning turn.

## Evidence rubric

Score each gate:

- 3 — correct, independently derived, and tied to source/runtime evidence;
- 2 — directionally correct but incomplete or lightly prompted;
- 1 — memorized conclusion without a valid derivation;
- 0 — missing or based on a misconception.

A gate passes at 3. A score below 3 records the misconception, routes to one targeted explanation or experiment, and asks a different transfer question. Repeating the original wording is not remediation.

## Stage transitions

Record a stage as `passed` only after its exit evidence exists:

1. scope — source identity/version, target config, environment, transfer track, and observable calibration;
2. repository_map — construction, forward, loss, training, inference, and final-output paths located or explicitly evidenced absent;
3. inference — learner prediction plus one real minimal inference observation;
4. training — learner-run forward, finite loss, backward, optimizer step, gradient evidence, and checkpoint/state behavior;
5. reconstruction — architecture map, one to three innovation annotations, and Feynman teach-back;
6. parameters — parameter ledger plus causal experiments and compatibility reasoning;
7. modification — learner-authored core-module replacement with tensor-contract forward/backward/regression evidence;
8. transfer — defended real-task adaptation and evaluation plan;
9. mastery — every gate below scores 3.

Do not skip an incomplete or blocked stage. On the accelerated route, one learner artifact may provide evidence for multiple adjacent stages, but score each stage against its own exit list and leave missing evidence incomplete. Only the mastery exit may set study `status: complete`.

## Mastery gates

The learner must demonstrate all six:

1. Navigation: find construction, `forward`, loss, and final output path.
2. Tensor flow: calculate critical shapes and invariants.
3. Parameter causality: explain use sites, coupling, cost, and compatibility.
4. Diagnosis: use evidence to localize a controlled failure.
5. Core-module modification: independently replace an architecture-bearing core module—not only a loss, config, adapter, wrapper, or training hook—and verify the preserved tensor contract with forward, backward, and regression evidence.
6. Transfer: defend one real-task adaptation and evaluation plan.

Reading a correct explanation, running copied commands, accepting an agent-authored patch, or receiving a production patch does not pass a gate.

## Pressure resistance

These statements are not mastery evidence:

- "There is no time for questions."
- "I have used PyTorch before."
- "Just give me the complete patch."
- "I understand from reading."
- "The demo works, so the architecture is learned."

Under deadline pressure, reduce the scope to one high-information action and save a checkpoint. Do not compress every stage into a report. If the user explicitly changes the goal to report-only or implementation-only, honor the new goal but state that the learning gates were not completed.

## Resumable checkpoint

End a session with current learning route and calibration evidence, rapid-mental-model status, current stage, evidence acquired, learner explanation, passed gates, misconceptions, unfinished experiment, and exactly one next action. Never infer completion merely because the conversation ended.

