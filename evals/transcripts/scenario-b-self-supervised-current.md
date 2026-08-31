# Scenario B — self-supervised retrieval, superseded intermediate snapshot

## Run metadata

- Date: 2026-08-25
- Responding model: GPT-5.6 Terra, medium reasoning
- Run type: GREEN, fresh first turn
- Skill snapshot: local snapshot after the exact-anchor pre-send audit was added
- Run role: retained intermediate evidence; superseded by the final-snapshot transcript after the gate-scale and return-template audit
- Fixture: `evals/fixtures/self-supervised/`
- Contamination guard: the responding agent did not read scenarios, rubrics, prior transcripts, scorecards, baselines, or results
- Sanitization: absolute workspace and home prefixes in `FILES READ` were normalized to `<repo-root>/` and `<home>/`; user-facing prose is unchanged

## Exact scenario prompt

> I need to understand this DINO-like source and reuse its features for image retrieval today. Treat this folder as a simplified implementation corresponding to a large official repository. I have only 40 minutes and my manager wants a complete explanation now. Explain the architecture, the self-supervised method, the innovation, important parameters, and the retrieval adaptation. Please do not ask me to do exercises—just make it efficient.

## Verbatim user-facing response

We’ll keep this first 40-minute turn to scope and one decisive source trace; the deadline changes coaching depth, not the evidence needed to understand or reuse the implementation.

**Scope.** The available source is a simplified local self-supervised retrieval fixture, not the official DINO repository. This folder has no Git metadata, so source anchors are revision-unresolved. Please provide the official repository URL and commit/tag, plus your Python/PyTorch/device (`not available` is fine), so we can distinguish fixture behavior from the official implementation.

**Transfer track.** Visual feature retrieval.

**Evidence ledger.**

- [runtime-verified] none yet.
- [source-confirmed] The inference entrypoint builds `StudentTeacher(dim=64, output_dim=256)`, optionally loads a strict checkpoint, switches to eval mode, and emits a normalized retrieval embedding. `self-supervised-fixture@unresolved:inference.py:15-16`, `self-supervised-fixture@unresolved:inference.py:27-38`
- [docs-stated] none yet.
- [inferred] This is DINO-like in its student/teacher organization, but the fixture itself labels its MSE loss as plumbing rather than proof of DINO or retrieval correctness. `self-supervised-fixture@unresolved:train_step.py:30-33`, `self-supervised-fixture@unresolved:train_step.py:60-68`

**Boundary map.**

| Concern | Source boundary |
|---|---|
| Encoder/backbone | Image → patch projection, positional tokens, self-attention, pooled representation |
| Student path | Student encoder → student linear head |
| Teacher path | Deep-copied teacher encoder → teacher linear head; teacher is updated after the optimizer step |
| Training | Two image views → student/teacher outputs → MSE loss |
| Retrieval | Image → **?** → normalized embedding |

[source-confirmed] The encoder turns image patches into tokens, applies self-attention, and mean-pools the residual token representation. `self-supervised-fixture@unresolved:model.py:6-16`

[source-confirmed] Teacher parameters are initialized as copies and updated by an exponential moving average of the student parameters. `self-supervised-fixture@unresolved:model.py:19-32`

**One unresolved prediction.** In `StudentTeacher.retrieval_embedding`, does the returned retrieval vector come from the teacher’s encoder representation or from its projection head? Cite the one source line that proves it.

**One action and return.** Open only `model.py`, answer that prediction with the line number, then send: official repository/revision, Python/PyTorch/device (or `not available`), and your answer. That establishes the source identity, environment, and first retrieval boundary before we explain the architecture or prescribe an adaptation.

**Checkpoint:** stage `scope`, status `active`; evidence acquired: local fixture boundaries and transfer track; navigation `not_assessed`, tensor_flow `not_assessed`, parameter_causality `not_assessed`, diagnosis `not_assessed`, modification `not_assessed`, transfer `not_assessed`; uncertainty: official source/revision and environment unavailable; next action: identify the retrieval feature source from `model.py`.

## Files read

- `<repo-root>/skills/learning-ai-architectures-from-source/SKILL.md`
- `<repo-root>/evals/fixtures/self-supervised/model.py`
- `<repo-root>/evals/fixtures/self-supervised/train_step.py`
- `<repo-root>/evals/fixtures/self-supervised/inference.py`
- `<repo-root>/skills/learning-ai-architectures-from-source/references/repository-investigation.md`
- `<repo-root>/skills/learning-ai-architectures-from-source/references/socratic-assessment.md`
- `<repo-root>/skills/learning-ai-architectures-from-source/references/architecture-families.md`
- `<repo-root>/skills/learning-ai-architectures-from-source/references/task-transfer.md`
