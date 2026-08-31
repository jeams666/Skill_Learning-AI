# Baseline observations without the skill

Date: 2026-08-24

Three fresh agents inspected the fixtures without the proposed skill. They were technically capable: all three found meaningful shapes or parameter constraints, and the detector and self-supervised agents ran smoke checks. The failures were therefore teaching-process and evidence-contract failures rather than lack of general coding ability.

## Detector baseline

Observed strengths:

- Reconstructed `B×3×256×256 → B×64×64×64 → B×10×64×64`.
- Noted that the teaching fixture uses MSE rather than a production detector loss.
- Ran a real forward and training step.

Observed failures:

- Supplied the complete `ResidualBlock` and complete neck replacement immediately.
- Asked for no learner prediction, patch, explanation, or verification.
- Treated a one-shot architecture report plus commands as sufficient learning progress.
- Used filenames but not precise source anchors or evidence labels.

Representative output:

> "To replace one neck block with a residual block, add this class next to `ConvBlock`..."

## Self-supervised/retrieval baseline

Observed strengths:

- Correctly separated the 64-D encoder feature from the 256-D projection-head output.
- Distinguished the ViT-like encoder from the EMA self-distillation mechanism.
- Explicitly refused to claim details about an absent official repository.
- Ran shape and normalization smoke checks.

Observed failures:

- Delivered the entire architecture, loss, parameter table, and retrieval adaptation in one answer.
- Performed no learner calibration, prediction, teach-back, or mastery gate.
- Introduced advice such as a momentum starting value without marking it as external guidance or inference.
- Did not create a resumable learning checkpoint.

Representative output:

> "Recommended adaptation checklist: ..."

## Transformer/LLM baseline

Observed strengths:

- Found that `hidden_size=64` is incompatible with six query heads.
- Derived a coherent 72-wide alternative and explained GQA shapes.
- Checked parameter counts, output shapes, and checkpoint incompatibility.

Observed failures:

- Supplied the complete configuration change and fine-tuning plan rather than making the learner derive it.
- Used prior PyTorch experience as justification for skipping staged checks.
- Added training hyperparameter recommendations without separating repository evidence from general advice.
- Did not require a learner-authored patch or define a mastery gate.

Exact rationalization from the baseline self-report:

> "I used the user’s stated prior PyTorch experience and request for a one-shot, no-checkpoint explanation as evidence to give a direct technical walkthrough rather than quizzes or staged comprehension checks."

## Minimal guidance the skill must add

1. A learning request remains learner-led under time, authority, and deadline pressure.
2. Prior experience changes hint depth, not the requirement for observable mastery.
3. The default response advances one high-information learner action rather than completing every stage.
4. Official and comparison repositories have distinct evidence roles and pinned versions.
5. Source claims require anchors and evidence labels; general advice must be marked as such.
6. Modification requires prediction, learner-authored first patch, execution evidence, teach-back, and a resumable checkpoint.
7. A derivation or patch shown before the learner attempt cannot be recycled as a mastery question; the target answer must remain withheld.
