# Source annotation and architecture reconstruction

Read this reference when explaining the architecture, an innovation, tensor flow, or parameters.

## Architecture lenses

Reconstruct the model through these distinct lenses:

1. Problem contract: input, output, objective, constraints, and metric.
2. Representation: pixels, patches, tokens, features, embeddings, or latent state.
3. Topology: stem/embedding, repeated blocks, skips, neck/decoder, head, and branches.
4. Interaction: convolution, attention, recurrence, routing, pooling, or alignment.
5. Training mechanism: supervision, loss, assignment, distillation, masking, or contrast.
6. Inference mechanism: decoding, generation, cache, NMS, retrieval, or export.
7. State: parameters, buffers, EMA teacher, optimizer, scheduler, and checkpoint.
8. Systems cost: shapes, FLOPs, memory, latency, communication, and precision.
9. Extension seams: configurable components and stable input/output contracts.
10. Failure boundary: invalid shapes, incompatible weights, and train/eval divergence.

Distinguish backbone architecture, task topology, training objective, and systems optimization. A shared name may describe only one of these.

## Innovation card

Deeply annotate only the one to three functions that carry the central mechanism. For each:

```text
Concept:
Source anchor: repo@commit:path:start-end
Callers and callees:
Input/output shapes:
Controlling config:
Mathematical operation:
Why this design exists:
What removal or replacement changes:
Training/inference difference:
Checkpoint and downstream impact:
Evidence label:
```

Explain ordinary surrounding code with anchors and call relationships rather than copying whole files.

Every `[source-confirmed]` architecture claim—not only each innovation card—uses `repo@commit:path:start-end`, and every clause in that claim must be established by the cited span. Split source facts from derived implications and label the latter `[inferred]`. If no commit exists, record the exact declarative reason before the first unresolved anchor and use `repo@unresolved:path:start-end` plus the symbol or a distinctive expression. If lines are unstable, state why before using `repo@unresolved:path:symbol` plus the expression.

For each selected function, give detailed commentary by statement or tight line range without editing the repository by default:

| Source anchor | Operation | Tensor/state effect | Why it exists | Invariant or change risk | Evidence label |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

Quote only the minimum code needed to orient the learner. Do not use the unresolved-anchor exception silently or merely for convenience.

## Paper or design-doc mapping

Treat papers and design documents as claims about intent, not proof of repository behavior. Map each central equation or named mechanism to its configuration, forward operation, loss/state update, and inference use site. Record missing pieces and implementation differences explicitly; do not call code paper-equivalent merely because names match.

## Tensor trace

Record symbolic and concrete shapes together. State where batch, sequence/spatial, channel/hidden, head, and vocabulary/class dimensions change. Require the learner to calculate the next shape before revealing runtime output.

For every reshape, transpose, concatenate, repeat, up/downsample, or broadcast, explain the invariant that makes it valid.

## Parameter ledger

For each consequential parameter record definition site, use site, default/type, mathematical meaning, shape effect, compute/memory effect, coupled parameters, valid constraints, retraining need, checkpoint compatibility, expected experiment result, and evidence.

Group parameters as structural, training, data, inference, or system. A name translation without use-site evidence and coupling is not a completed entry.

## First-principles prompts

Use one at the relevant code point:

- What problem exists if this module is removed?
- What is the smallest mechanism that satisfies the tensor contract?
- Which inductive bias is encoded here?
- What extra cost buys the claimed benefit?
- Which simpler alternative would preserve the output contract?
