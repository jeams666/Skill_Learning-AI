# Architecture-family cues

Read only the section matching the current repository. These are search and reasoning cues, not claims about a repository that has not been inspected.

## CNN and detector repositories

Trace data/augmentation → backbone → multi-scale features → neck/fusion → detection head → assignment/loss → box decoding → NMS/export. Record spatial stride and channel changes at every feature level. Separate backbone capacity, feature fusion, head parameterization, label assignment, and post-processing.

Common coupled parameters include width/depth multipliers, input size, feature strides, class count, regression bins/anchors, thresholds, and augmentation. Confirm whether the implementation is anchor-based or anchor-free rather than inferring from a family name.

When the learner requests a detector-block replacement during scope, make the first calibration prediction the selected seam's input/output spatial and channel contract. Collect missing version/environment fields in the same return contract; do not substitute a config-name lookup for the tensor prediction.

## Vision Transformer repositories

Trace image/patch embedding → special or register tokens → position mechanism → repeated blocks → normalization/pooling → task head. Record patch/token count, hidden width, head count/head dimension, MLP ratio, and any window/local attention.

Distinguish an architectural ViT from a supervised, masked, contrastive, or distillation training recipe applied to it.

## Transformer and local LLM repositories

Trace tokenizer/data packing → embeddings → positional mechanism → decoder/encoder blocks → Q/K/V projection and mask → MLP → residual/norm → output head → loss → generation/cache. Record `[batch, sequence, hidden]`, `[batch, heads, sequence, head_dim]`, vocabulary logits, and cache shapes.

Check divisibility among hidden width, query heads, key/value heads, and parallel partitions. Check whether embeddings and output head are tied, whether normalization is pre/post, and whether changes invalidate checkpoints or quantization/adapters.

## Self-supervised and distillation repositories

Separate encoder architecture, projection/prediction heads, data views/masking, student/teacher paths, stop-gradient, EMA update, centering/temperature, objective, and downstream feature extraction. Confirm update ordering relative to optimizer steps.

A name such as DINO may primarily identify a training method; do not describe it as a standalone backbone. For retrieval, verify whether downstream embeddings come from a class token, pooled patch tokens, a projection head, or another layer.

If the scope calibration asks the learner to identify the retrieval feature source, mask that edge in every preceding map, evidence sentence, and explanation. Good: `image → ? → retrieval embedding`, followed by a source-reading prediction. Bad: showing `image → teacher encoder → retrieval embedding`, calling it `teacher-side`, or attaching any other candidate name and then asking whether the student/teacher encoder/head supplies it.

## Retrieval repositories

Trace encoder → pooling → projection → normalization → similarity → index → ranking/evaluation. Record embedding dimension and distance contract. Distinguish training representation from deployment representation and validate Recall@K/mAP against the actual task.

## Multimodal repositories

Trace each modality encoder, projector/resampler, fusion or token insertion, language/decoder interface, objective, freezing schedule, and generation/evaluation. Record where image/audio features become tokens compatible with the language hidden width. Distinguish contrastive alignment from generative conditioning.

## Mixture-of-experts repositories

Trace router inputs, expert selection, dispatch/combine, capacity/drop behavior, auxiliary balancing loss, communication, and dense fallback. Distinguish total parameters from parameters and FLOPs activated per token.
