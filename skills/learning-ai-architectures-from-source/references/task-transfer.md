# Task transfer tracks

Read only the track selected for the current study. Complete one track per learning loop.

Selecting a track during scope sets the project destination; it does not open the transfer stage. Use the destination to prioritize repository evidence, but do not deliver a full adaptation plan until navigation, tensor-flow, and parameter-causality gates have evidence.

## Shared transfer contract

The learner writes a plan containing:

1. Task input, output, user-visible success, and constraints.
2. Dataset size, label/interaction format, split, and failure cases.
3. Existing components that transfer unchanged, with source anchors.
4. Mismatches in representation, output space, objective, data, or deployment.
5. The smallest adaptation and at least one simpler baseline.
6. Frozen/trainable modules, checkpoint compatibility, and compute budget.
7. Primary metric, efficiency metric, qualitative failure review, and ablation.
8. Stop/rollback criteria.

Require a defense of why each changed component is necessary.

## Industrial object detection

Record class distribution, object scale, occlusion, background/domain shift, annotation quality, input resolution, throughput/latency, device, and export constraints. Establish an unchanged pretrained baseline first. Consider data and assignment/loss issues before replacing the backbone. Evaluate per-class AP/recall, small-object behavior, false positives, latency, memory, and representative production failures.

## Visual feature retrieval

Identify the exact source layer, pooling, projection, normalization, embedding dimension, and similarity/index contract. Keep query and gallery preprocessing aligned. Compare frozen features before fine-tuning. Evaluate Recall@K/mAP, index latency/memory, near-duplicate behavior, hard negatives, and domain shift.

## Multimodal adaptation

Specify modality encoders, projector/resampler, language-model interface, token budget, objective, frozen/trainable schedule, and alignment data. Start with the smallest connector that satisfies the hidden-width contract before modifying both encoders. Evaluate task quality, grounding failures, modality ablations, latency, and memory.

## Local LLM fine-tuning

Specify tokenizer and chat/data template, context length, packing, objective, adapter target modules, quantization, memory budget, and generation evaluation. Establish a base-model prompt baseline. Prefer a reversible adapter before altering core width/head topology unless the task requires an architectural experiment. Evaluate held-out loss plus task examples, overfitting, throughput, memory, and checkpoint/config reproducibility.

## Graduation defense

Ask the learner to present the baseline, chosen seam, expected causal effect, implementation evidence, metric result, failure cases, and next experiment. Challenge one assumption with a cheaper alternative and one with an out-of-distribution case.
