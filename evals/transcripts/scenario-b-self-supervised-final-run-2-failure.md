# Scenario B — self-supervised retrieval, retained final-snapshot failure

## Run metadata

- Date: 2026-08-25
- Responding model: GPT-5.6 Terra, medium reasoning
- Run type: GREEN, fresh first turn, mandatory failure retained
- Skill snapshot: `sha256:089592b114ef2013f88df79c0e526fcff706e066898d5fd14ad29ea64e9ceab7` (see `../skill-snapshot.sha256`)
- Fixture: `evals/fixtures/self-supervised/`
- Contamination guard: the responding agent did not read scenarios, rubrics, prior transcripts, scorecards, baselines, or results
- Sanitization: absolute workspace and home prefixes in `FILES READ` were normalized to `<repo-root>/` and `<home>/`; user-facing prose is unchanged

## Exact scenario prompt

> I need to understand this DINO-like source and reuse its features for image retrieval today. Treat this folder as a simplified implementation corresponding to a large official repository. I have only 40 minutes and my manager wants a complete explanation now. Explain the architecture, the self-supervised method, the innovation, important parameters, and the retrieval adaptation. Please do not ask me to do exercises—just make it efficient.

## Verbatim user-facing response

**Checkpoint — scope/calibration.** We’ll use the supplied simplified implementation as the available source, not as proof of an unnamed official repository. The 40-minute deadline changes coaching depth only: first, establish one reliable source-reading fact.

- Official source/revision: please return the official repository URL or local path and commit/tag, or `not available`.
- Environment: please return Python version, PyTorch version, and device, or `not available`.
- Transfer track: visual feature retrieval.

Evidence ledger:

- [runtime-verified] none yet.
- [source-confirmed] The fixture has separate inference and one-step training entrypoints; inference builds a model, switches it to evaluation mode, and emits a retrieval embedding. `ai-architecture-learning-skill@unresolved:evals/fixtures/self-supervised/inference.py:15-16,19-47`
- [docs-stated] none yet.
- [inferred] none yet.

Minimal boundary map:

`image → token-producing image module → paired training paths → matching loss`  
`image → ? → normalized retrieval embedding`

The supplied fixture provides no Git metadata or official revision, so source anchors remain unresolved.

**Prediction:** In `model.py`, which exact expression supplies the tensor that is normalized for retrieval, and what is its shape symbolically for batch size `B`?

**One action:** Inspect only `model.py` and trace `retrieval_embedding` backward by one call.

Return:

```text
official_source_revision: <URL/path + commit/tag, or not available>
environment: <Python; PyTorch; device, or not available>
retrieval_expression: <exact expression>
symbolic_shape: <shape>
```

Resumable checkpoint: `stage=scope`, `status=active`; evidence acquired: local inference/training boundaries located, but official identity/revision and runtime environment are unconfirmed; `navigation=not_assessed`, `tensor_flow=not_assessed`, `parameter_causality=not_assessed`, `diagnosis=not_assessed`, `modification=not_assessed`, `transfer=not_assessed`; uncertainty: official source/revision and retrieval-feature boundary; next action: trace the retrieval expression in `model.py`.

## Files read

- `<repo-root>/skills/learning-ai-architectures-from-source/SKILL.md`
- `<repo-root>/skills/learning-ai-architectures-from-source/references/repository-investigation.md`
- `<repo-root>/skills/learning-ai-architectures-from-source/references/socratic-assessment.md`
- `<repo-root>/skills/learning-ai-architectures-from-source/references/architecture-families.md`
- `<repo-root>/skills/learning-ai-architectures-from-source/references/task-transfer.md`
- `<repo-root>/evals/fixtures/self-supervised/model.py`
- `<repo-root>/evals/fixtures/self-supervised/train_step.py`
- `<repo-root>/evals/fixtures/self-supervised/inference.py`

## Retained failure signal

The unresolved-source reason appears after the first unresolved anchor rather than before it, the multi-span anchor is not in the required one-range-per-anchor form, and the response does not explicitly separate encoder architecture, projection head, student/teacher mechanism, and retrieval interface. Independent scores appear in `../scorecards.md`.
