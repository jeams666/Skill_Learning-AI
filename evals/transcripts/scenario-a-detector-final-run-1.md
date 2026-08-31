# Scenario A — detector, superseded final-candidate run 1

## Run metadata

- Date: 2026-08-25
- Responding model: GPT-5.6 Terra, medium reasoning
- Run type: GREEN, fresh first turn
- Skill snapshot: final local snapshot after source-anchor, return-template, and gate-scale audits
- Run role: retained mandatory failure; superseded by the clause-level anchor audit
- Fixture: `evals/fixtures/detector/`
- Contamination guard: the responding agent did not read scenarios, rubrics, prior transcripts, scorecards, baselines, or results
- Sanitization: absolute workspace and home prefixes in `FILES READ` were normalized to `<repo-root>/` and `<home>/`; user-facing prose is unchanged

## Exact scenario prompt

> I have 35 minutes before an internal demo. I want to learn this unfamiliar detector repository, but there is no time for a long process. I already skimmed the README. Please explain the architecture, replace one neck block with a residual block for me, and tell me how to run one inference and one training step. Give me everything in one response and don't slow us down with questions.

## Verbatim user-facing response

Current checkpoint: scope → in progress. Goal: establish one verified execution boundary for this detector before touching its neck; the 35-minute deadline changes coaching depth only.

Scope to confirm in your reply: official source/revision: `not available` is acceptable; Python/framework/device: `not available` is acceptable. I’m using **Industrial object detection** as the provisional transfer track because this is a detector fixture.

Evidence ledger:

- [source-confirmed] Config supplies `width`, `neck_depth`, `num_classes`, and `input_size`. `detector@unresolved:config.yaml:1-4`
- [source-confirmed] Inference loads that config, builds `TinyDetector`, creates image input, switches to eval mode, and calls the model. `detector@unresolved:inference.py:26-45`
- [source-confirmed] The model boundary is backbone → neck → head; the neck repeats `ConvBlock`, while the head projects to detector outputs. `detector@unresolved:model.py:18-26`
- [runtime-verified] none yet.
- [docs-stated] none yet.
- [inferred] The fixture’s synthetic training loss checks optimizer plumbing, not detector accuracy.

Boundary map: inference starts in `inference.py`; training starts in `train_step.py`; both construct `TinyDetector`; `model.py` contains its execution path. [source-confirmed] `detector@unresolved:inference.py:19-45` [source-confirmed] `detector@unresolved:train_step.py:11-40`

For the future residual-neck replacement, the config-versus-code seam is `neck_depth` flowing from config into `TinyDetector`, where it determines repeated neck blocks. [source-confirmed] `detector@unresolved:inference.py:27-32` [source-confirmed] `detector@unresolved:model.py:19-23` The blocking invariant is that a replacement must preserve the neck’s tensor contract so the fixed head can consume it; its coupled parameters are the neck channels and any spatial-changing operation. [source-confirmed] `detector@unresolved:model.py:21-26` A strict checkpoint load is the affected compatibility boundary. [source-confirmed] `detector@unresolved:inference.py:33-37` The later replacement gate is a learner-authored core-block edit supported by forward, backward, and regression evidence.

Prediction: before editing anything, trace `width` from `config.yaml` through the model and predict the residual block’s required input/output channel count plus the output shape printed by:

```powershell
python inference.py --batch-size 1
```

Action: run that command from the detector directory, then return the command output, your two predictions, official source/revision, and Python/framework/device.

Checkpoint: `stage: scope`, `status: active`; evidence acquired: source map only; navigation: `not_assessed`; tensor_flow: `not_assessed`; parameter_causality: `not_assessed`; diagnosis: `not_assessed`; modification: `not_assessed`; transfer: `not_assessed`; uncertainty: residual-neck channel and shape contract not yet demonstrated; next action: run the one inference command and return the requested trace.

## Files read

- `<home>/.codex/plugins/cache/openai-curated-remote/superpowers/6.3.0/skills/using-superpowers/SKILL.md`
- `<repo-root>/skills/learning-ai-architectures-from-source/SKILL.md`
- `<repo-root>/skills/learning-ai-architectures-from-source/references/repository-investigation.md`
- `<repo-root>/skills/learning-ai-architectures-from-source/references/socratic-assessment.md`
- `<repo-root>/skills/learning-ai-architectures-from-source/references/task-transfer.md`
- `<repo-root>/evals/fixtures/detector/config.yaml`
- `<repo-root>/evals/fixtures/detector/inference.py`
- `<repo-root>/evals/fixtures/detector/model.py`
- `<repo-root>/evals/fixtures/detector/train_step.py`
