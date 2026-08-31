# Learner-led labs

Read this reference before asking the learner to run inference, train, tune parameters, or modify architecture.

## Interaction invariant

One loop is:

```text
hypothesis → learner prediction → one command or patch
           → captured evidence → explanation → checkpoint
```

The agent may inspect source read-only. The learner runs instructional commands and authors the first experimental patch. Ask before installs, downloads, long training, or repository writes. Never hide a blocked or failed run; it becomes diagnostic evidence.

Before sending a lab, run an answer-leak check: the explanation may expose the invariant or source seam, but it must not contain the exact output, valid replacement configuration, or patch the learner is about to predict. Do not execute the instructional command on the learner's behalf before receiving that prediction.

## Hint ladder

When an answer or experiment is wrong:

1. Ask which assumption produced the result.
2. Point to the relevant module or dimension.
3. Reveal a partial shape, invariant, or call edge.
4. Show a minimal analogous fragment.
5. Give the full demonstration only on explicit request, then assign a different transfer check.

## Minimal inference lab

The learner must identify preprocessing, model construction, checkpoint loading, `eval`/no-grad behavior, one complete forward path, raw output, and post-processing. Before running, record expected class, keys, shapes, dtype, and device. After running, compare prediction with observation.

## Minimal training lab

Use the smallest safe data and model configuration that exercises:

```text
batch → forward → component losses → total loss
      → backward → optimizer step → state/checkpoint
```

Verify which parameters receive gradients, train/eval differences, and at least one finite loss. A toy loss may verify plumbing but not task correctness; label that distinction.

## Parameter lab

Choose one structural, one training, and one inference parameter when available. For each, the learner records a causal prediction before changing it, changes one primary variable, measures shape/parameters/memory/latency/metric as appropriate, and reconciles the result in the experiment log.

## Modification lab

Select an architecture-bearing core module on the active execution path, such as a block, neck, head, attention component, projector, or pooling layer. A loss-only, config-only, adapter-only, wrapper-only, or training-hook-only edit may be a useful experiment but cannot satisfy the modification gate. Before editing, require:

- original source anchor and call path;
- input/output tensor contract recorded before the replacement and preserved after it;
- expected parameter and compute change;
- coupled configuration;
- checkpoint compatibility prediction;
- minimal forward, backward, and regression checks that verify that contract.

The learner writes the first patch. Review the diff by asking the learner to explain each changed line and tensor invariant before running it. Record the original and replacement anchors plus before/after tensor evidence in the study state.

## Feynman checkpoint

After a successful or failed lab, ask the learner to explain the mechanism to a peer without repository jargon: problem, data flow, why the component exists, what changed, evidence, and remaining uncertainty. Repair only the gaps exposed by the explanation.
