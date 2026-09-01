# Scenario D — intermediate clean GREEN run

- Date: 2026-08-31
- Responding context: fresh Codex subagent
- Model/reasoning: unavailable from the collaboration result
- Fixture: `evals/fixtures/llm/`
- Skill snapshot: `8de89a94a50cccb7e9abae7ecd3059174f5351073ea4ad7be9daff023b477660`
- Result: 8/8 clean pass on an intermediate snapshot; superseded by the later final routing transcript

## Raw response

We’ll use one high-information calibration artifact. Your experience and 90-minute deadline justify terse, integrated work, but no stage is pre-passed; one strong artifact may satisfy several independently evaluated exits.

**Checkpoint and endpoint**

- Current stage: `scope`, `in_progress`
- Learning route: `pending_calibration`
- Endpoint: prediction-backed runtime evidence, your own architecture-bearing core replacement, and an evidence-defended local fine-tuning transfer decision.

**Preflight: `source_access: succeeded`**

Working source is the supplied local `evals/fixtures/llm` fixture. All four fixture files match Git commit `11add70406fdab5dd7c4a509c18df639e1c1b6a8`; the containing repository has unrelated working-tree changes. Treating this fixture as the working implementation is an assumption until you confirm whether it is official. Target config is `MODEL_CONFIG`; inference and training wrappers are `inference.py` and `train_step.py`. No comparison implementation was supplied. A local Python command exists; framework version and device remain unverified. Transfer track is **Local LLM fine-tuning**, selected from your stated task.

**Evidence ledger**

- `[runtime-verified]` none yet; I have deliberately not run the instructional command before your prediction.
- `[source-confirmed]` The config feeds three structural values through `build_model()` into `GroupedAttention`; its forward performs three projections, reshapes them, and returns three tensors. `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/config.py:1-8`; `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/inference.py:7-16`; `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/model.py:5-22`
- `[docs-stated]` none yet.
- `[inferred]` This fixture alone cannot establish whether adapting a complete decoder is worthwhile; it can establish evidence about the grouped-projection seam and expose exactly what full-decoder evidence is still missing.

**Rapid mental model — draft**

- Execution spine `[source-confirmed]`: `MODEL_CONFIG → build_model → GroupedAttention`; the inference branch creates deterministic hidden states, enters eval/inference mode, calls the module, and prints shape/status output. The training branch calls the same module, forms a synthetic loss, backpropagates, takes one SGD step, and optionally saves state. `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/config.py:1-8`; `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/inference.py:7-16`; `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/inference.py:19-23`; `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/inference.py:26-60`; `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/train_step.py:10-52`
- Architecture skeleton `[source-confirmed]`: hidden-state tensor → three linear projection paths → head-axis reshapes → three returned tensors. This active forward stops there; the inference wrapper labels its scope projection/reshape-only rather than full attention or generation, and the training wrapper labels its loss toy plumbing rather than language-model or fine-tuning correctness. `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/model.py:5-22`; `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/inference.py:41-56`; `ai-architecture-learning-skill@11add70406fdab5dd7c4a509c18df639e1c1b6a8:evals/fixtures/llm/train_step.py:18-48`

**Your one calibration action**

Before executing anything, trace `num_key_value_heads` from definition through construction to every active use. Derive the symbolic and configured concrete output-shape triple for batch size 2 and the fixture’s sequence length. Then predict the complete tensor, projection-weight, and strict-checkpoint consequences of mentally setting only `num_key_value_heads` to `1`. Do not edit any file.

After recording the prediction, run this no-checkpoint, bytecode-disabled command:

```powershell
python -B "C:\Users\17738\Documents\Codex\2026-08-24\https-chatgpt-com-share-6a8c124e-6bc8\outputs\ai-architecture-learning-skill\evals\fixtures\llm\inference.py" --batch-size 2 --seed 0
```

Return one compact artifact containing:

1. `official source/revision`: confirm the supplied path and commit, provide the correct identity, or write `not available`.
2. `Python/framework/device`: copy the emitted values, or write `not available`; if execution fails, paste the exact error.
3. The traversed `repo@commit:path:start-end` anchors.
4. Your symbolic derivation and configured concrete shapes.
5. Your counterfactual prediction and checkpoint reasoning.
6. Exact stdout or exact error.
7. Your corrected two-layer mental model and one remaining uncertainty.

```yaml
checkpoint:
  preflight:
    source_access: succeeded
    files_read: [config.py, model.py, inference.py, train_step.py]
  learning_route: pending_calibration
  calibration_evidence:
    self_report: senior PyTorch experience
    observable_repository_work: none_returned_yet
  rapid_mental_model:
    status: draft
    unresolved_edge: grouped projection tensor and checkpoint consequences
  stage: scope
  stage_status: in_progress
  evidence_acquired: read_only_source_preflight
  gates:
    navigation: not_assessed
    tensor_flow: not_assessed
    parameter_causality: not_assessed
    diagnosis: not_assessed
    modification: not_assessed
    transfer: not_assessed
  uncertainty: official-source status and runtime environment are unconfirmed
  next_action: return the single calibration artifact specified above
  status: active
```

Files read: `SKILL.md`; `learner-routing.md`; `repository-investigation.md`; `socratic-assessment.md`; `learner-led-labs.md`; `source-annotation.md`; the shared contract and Local LLM fine-tuning section of `task-transfer.md`; the Transformer and local LLM section of `architecture-families.md`; fixture `config.py`, `model.py`, `inference.py`, and `train_step.py`.
