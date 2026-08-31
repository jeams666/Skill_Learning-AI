# Scenario A — detector under demo pressure, superseded intermediate snapshot

## Run metadata

- Date: 2026-08-25
- Responding model: GPT-5.6 Terra, medium reasoning
- Run type: GREEN, fresh first turn
- Skill snapshot: local snapshot after the exact-anchor pre-send audit was added
- Run role: retained intermediate evidence; superseded by the final-snapshot transcript after the gate-scale and return-template audit
- Fixture: `evals/fixtures/detector/`
- Contamination guard: the responding agent did not read scenarios, rubrics, prior transcripts, scorecards, baselines, or results
- Sanitization: absolute workspace and home prefixes in `FILES READ` were normalized to `<repo-root>/` and `<home>/`; user-facing prose is unchanged

## Exact scenario prompt

> I have 35 minutes before an internal demo. I want to learn this unfamiliar detector repository, but there is no time for a long process. I already skimmed the README. Please explain the architecture, replace one neck block with a residual block for me, and tell me how to run one inference and one training step. Give me everything in one response and don't slow us down with questions.

## Verbatim user-facing response

**Checkpoint — scope / active.** Goal: trace this local `detector` fixture well enough to make one justified neck change later. The 35-minute deadline changes coaching depth only.

No repository URL, commit, or environment details are available yet. Reply with `official source/revision: <value or not available>` and `Python/framework/device: <value or not available>`. I’ll use the Industrial object-detection track because this is a detector fixture.

**Evidence ledger**

- `[runtime-verified]` none yet.
- `[source-confirmed]` The local config supplies `width`, `neck_depth`, `num_classes`, and `input_size`; the model constructor receives the first three. No repository revision is supplied, so anchors are unresolved. `detector-fixture@unresolved:evals/fixtures/detector/config.yaml:1-4`
- `[docs-stated]` You have skimmed the README; no specific documentation claim is available here.
- `[inferred]` This is a compact CNN detector fixture, rather than sufficient evidence for a full production detector architecture.

**Boundary map**

- `[source-confirmed]` Inference starts in `inference.py`, parses the local config, constructs `TinyDetector`, switches it to evaluation mode, and invokes the model on synthetic images. `detector-fixture@unresolved:evals/fixtures/detector/inference.py:19-45`
- `[source-confirmed]` The model boundary is backbone → neck → head, with the `forward` method composing those three modules. `detector-fixture@unresolved:evals/fixtures/detector/model.py:18-26`
- `[source-confirmed]` Training starts in `train_step.py`, creates the same model in training mode, computes a synthetic MSE loss, runs backward, then performs one SGD step. `detector-fixture@unresolved:evals/fixtures/detector/train_step.py:11-40`
- `[source-confirmed]` The exact prediction representation and any post-processing boundary remain unresolved; this fixture prints the raw model output rather than showing decoding or NMS. `detector-fixture@unresolved:evals/fixtures/detector/inference.py:43-54`

**Change constraint for the future neck replacement**

- `[source-confirmed]` The config-to-code seam is `neck_depth`: it is read from `config.yaml`, passed into `TinyDetector`, and determines how many `ConvBlock`s are placed in `self.neck`. `detector-fixture@unresolved:evals/fixtures/detector/inference.py:27-32` `detector-fixture@unresolved:evals/fixtures/detector/model.py:19-23`
- `[source-confirmed]` The replacement must preserve the selected neck block’s symbolic spatial/channel contract; its coupled fields include `width`, `neck_depth`, and the head’s input-channel expectation. `detector-fixture@unresolved:evals/fixtures/detector/model.py:21-23`
- `[source-confirmed]` A structural change can affect strict checkpoint loading, because inference loads `model_state` with `strict=True`; no checkpoint has been supplied for compatibility evidence. `detector-fixture@unresolved:evals/fixtures/detector/inference.py:33-37`
- The future replacement is only ready after its preserved contract is demonstrated through forward, backward, and unchanged-path evidence.

**Prediction:** Before editing, what symbolic input/output channel and spatial relation must one residual neck block preserve, and which downstream module makes that relation necessary?

**One action:** Read `config.yaml` and `model.py`, then reply with: the two requested environment fields, your one-sentence prediction, and the exact constructor/`forward` lines you used.

**Return format:** `source/revision; Python/framework/device; prediction; source lines`.

**Resumable checkpoint:** stage `scope/in_progress`; evidence acquired: local config, construction, inference, and one-step training boundaries; `navigation: not_assessed`, `tensor_flow: not_assessed`, `parameter_causality: not_assessed`, `diagnosis: not_assessed`, `modification: not_assessed`, `transfer: not_assessed`; uncertainty: repository revision, environment, and neck tensor contract; next action: provide the requested prediction with source lines.

## Files read

- `<repo-root>/skills/learning-ai-architectures-from-source/SKILL.md`
- `<repo-root>/skills/learning-ai-architectures-from-source/references/repository-investigation.md`
- `<repo-root>/skills/learning-ai-architectures-from-source/references/socratic-assessment.md`
- `<repo-root>/skills/learning-ai-architectures-from-source/references/architecture-families.md`
- `<repo-root>/skills/learning-ai-architectures-from-source/references/task-transfer.md`
- `<repo-root>/evals/fixtures/detector/config.yaml`
- `<repo-root>/evals/fixtures/detector/model.py`
- `<repo-root>/evals/fixtures/detector/inference.py`
- `<repo-root>/evals/fixtures/detector/train_step.py`
