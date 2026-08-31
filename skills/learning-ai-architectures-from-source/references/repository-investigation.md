# Repository investigation

Read this reference when starting a study, changing repository/version, or tracing an execution path.

## Scope lock

Record before teaching architecture:

- official repository URL or local path;
- exact commit, tag, or explicit dirty-working-tree status;
- one model variant and its complete config;
- inference and training entrypoints;
- optional comparison implementation and its separate version;
- hardware, network, dependency, weight, and dataset constraints.

If an official source is absent, say so. Continue with the available implementation only under its real identity.

## Primary and comparison sources

The official pinned repository answers "what this implementation does." A comparison repository answers "what a smaller or different implementation makes easier to see." Trace the official implementation first. Open the comparison only for a named confusion, then return to the official source and record the difference.

Compare these fields: mathematical operation, module boundary, tensor contract, configuration, training support, inference optimization, and behavior. Do not mix file anchors across repositories.

## Build the map

Start with `rg --files`, manifests, dependency files, configuration, entrypoints, tests, export/deployment files, and documentation. Prefer `rg` searches for model names, `forward`, builders, registries, loss, optimizer, checkpoint, inference, post-processing, and configuration keys.

Produce a compact map:

| Concern | Entrypoint | Construction path | Core files | Evidence |
|---|---|---|---|---|
| inference |  |  |  |  |
| training |  |  |  |  |
| model |  |  |  |  |
| data |  |  |  |  |
| loss |  |  |  |  |

End every source-confirmed map row or ledger bullet with its own revision-qualified line-range anchor. Immediately before responding, reread those numbered spans; do not reuse an approximate range from memory. Require every clause—not only the main clause—to be supported by those spans; split a derived consequence into an `[inferred]` claim. When the source has no revision, state a declarative reason before using `repo@unresolved:path:start-end`; a request for the missing revision or an uncertainty list does not count. A symbol-only fallback is valid only when line numbers are genuinely unstable and the response says why.

README claims are orientation, not runtime proof.

## Trace one real path

Follow one selected config through:

```text
config → registry/factory → constructor → data/preprocess
       → forward → loss or postprocess → user-visible output
```

For dynamic evidence, have the learner run the smallest supported input and capture actual classes, shapes, dtype, device, train/eval mode, output keys, and errors. Avoid downloading large weights or datasets without permission. If runtime work is blocked, mark the trace source-confirmed rather than runtime-verified.

## Stop condition

Repository reconnaissance passes only when the learner can locate the selected inference entrypoint, training entrypoint, model constructor, core `forward`, loss, and final post-processing without being given the answer.
