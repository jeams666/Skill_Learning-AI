# Scenario B — diagnostic source-anchor failure

## Run metadata

- Date: 2026-08-25
- Responding model: GPT-5.6 Terra, medium reasoning
- Run type: GREEN, fresh first turn, retained diagnostic failure
- Skill snapshot: local snapshot before the exact-anchor pre-send audit was added
- Fixture: `evals/fixtures/self-supervised/`
- Contamination guard: the responding agent did not read scenarios, rubrics, prior transcripts, scorecards, baselines, or results
- Sanitization: absolute workspace and home prefixes in `FILES READ` were normalized to `<repo-root>/` and `<home>/`; user-facing prose is unchanged

## Exact scenario prompt

> I need to understand this DINO-like source and reuse its features for image retrieval today. Treat this folder as a simplified implementation corresponding to a large official repository. I have only 40 minutes and my manager wants a complete explanation now. Explain the architecture, the self-supervised method, the innovation, important parameters, and the retrieval adaptation. Please do not ask me to do exercises—just make it efficient.

## Verbatim user-facing response

**Checkpoint — scope, active.** With 40 minutes, we’ll use a guided first pass; the deadline changes coaching depth only. This folder is a simplified implementation, not the official DINO repository, so the official source/revision is currently **not available**.

**Scope to confirm:** reply with your official DINO repository URL/path and commit/tag (or `not available`), plus Python, PyTorch, and device (or `not available`). Your selected transfer track is **visual feature retrieval**.

**Evidence ledger**

- [runtime-verified] none yet
- [source-confirmed] this fixture has distinct student and teacher encoders/heads; training enters through `train_step.py`, inference through `inference.py`.
- [docs-stated] none yet
- [inferred] it is DINO-like student–teacher scaffolding, not a complete official DINO implementation.

**Boundary map**

```text
training views → student path → projection output → loss
training views → teacher path → target output
optimizer step → EMA teacher update

image → ? → normalized retrieval embedding
```

The encoder begins with patch projection, positional state, self-attention, and pooling (`evals/fixtures/self-supervised/model.py`, `Encoder`). The student–teacher wrapper owns separate encoders and heads plus an EMA update (`StudentTeacher`). The fixture’s training loss explicitly labels itself as toy plumbing rather than DINO or retrieval correctness (`train_step.py`).

**Prediction:** inspect `StudentTeacher.retrieval_embedding` and state whether retrieval uses the teacher encoder output or the projection head, then give the resulting symbolic embedding shape for a batch of `B` images.

**One action:** open `evals/fixtures/self-supervised/model.py` and return one sentence containing the feature source and symbolic shape.

**Checkpoint:** stage/status: `scope / in_progress`; evidence acquired: source map only; `navigation: not_assessed`, `tensor_flow: not_assessed`, `parameter_causality: not_assessed`, `diagnosis: not_assessed`, `modification: not_assessed`, `transfer: not_assessed`; uncertainty: official source revision and runtime environment unknown; next action: identify the retrieval feature source and symbolic shape.

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

The `[source-confirmed]` ledger bullet and the architectural prose name files or symbols but provide no revision-qualified line-range anchor. This run triggered the exact-anchor pre-send audit added to the current skill snapshot; its independent criterion scores are recorded in `../scorecards.md`.
