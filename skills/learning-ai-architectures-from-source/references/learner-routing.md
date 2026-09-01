# Learner routing and rapid mental models

Read this reference before initial calibration, when changing a learning route, and when an experienced learner asks for the shortest path through an unfamiliar repository.

## Route from evidence

Set a new learner's route to `pending_calibration`. Assign a route only from observable returned work in the current repository, not from title, confidence, years of experience, completed courses, or self-selection. Start with one compact calibration challenge that samples:

1. navigation — trace a config value through construction to its active use;
2. tensor reasoning — derive one symbolic shape or invariant;
3. causal reasoning — predict one downstream effect of a parameter or state change.

Use the smallest route that does not waste the learner's demonstrated ability:

| Route | Entry evidence | Teaching behavior |
|---|---|---|
| Guided | Cannot yet complete two calibration elements independently | Small actions, framework bridges, early hint-ladder use, one concept per check |
| Standard | Completes two elements with sound reasoning or only localized hints | Stage-sized source traces and causal experiments |
| Accelerated | Completes all three independently with accurate source anchors and no answer-bearing hint | Integrated challenges, terse explanations, counterfactuals, diagnosis, and design tradeoffs |

Record the route, evidence, and reason. State that it is provisional. Promote after new independent evidence shows the harder route is appropriate. Record global route changes in `route_history`.

If an accelerated learner needs answer-bearing hints or exposes a blocking misconception, keep the global route and append a `scoped_remediation` entry with the affected topic/stage, temporary guided or standard route, trigger evidence, exit condition, and status. Remove or close that override when its exit evidence is met; do not erase unrelated demonstrated competence.

Every route uses the same stage exit evidence and mastery gates. A route changes the granularity and information density of practice, never the definition of competence.

## Rapid mental model

Before detailed study, create a two-layer orientation. Keep it compact, source-anchored, and explicitly incomplete.

### Layer 1: execution spine

Map the repository path actually used by the target task:

```text
config/build → input or preprocessing → forward path
             → loss/backward/state update → raw output/postprocess
```

Mark a branch `absent` when the repository does not contain it and `unresolved` when it has not been traced. Do not invent a conventional training or inference path.

### Layer 2: architecture skeleton

Map mechanism roles rather than every class:

```text
input representation → core repeated transforms
                     → interaction/state across tokens, scales, views, or modalities
                     → objective or task head → deployable output
```

Use repository-specific names only after source confirmation. Preserve at least one important edge, tensor contract, or representation choice as the learner's unresolved trace. The learner then explains the skeleton in plain language and repairs it from source or runtime evidence.

Record the model as `draft`, `verified`, or `revised`. It becomes `verified` only when the learner has source-traced the unresolved edge and reconciled the map with one runtime observation where execution is available.

## Route through stages

| Stage group | Guided | Standard | Accelerated |
|---|---|---|---|
| Scope and repository map | Separate identity, environment, entrypoint, and call-chain actions | One bounded map-building task | One orientation challenge may collect scope, navigation, tensor, and skeleton evidence together |
| Inference and training | Predict and run each boundary separately | One minimal run per stage | Combine predictions and high-signal instrumentation, but retain real inference and forward/backward/optimizer evidence |
| Reconstruction and parameters | Teach back one mechanism, then test one parameter | Architecture map plus causal parameter experiments | Defend the two-layer model with counterfactuals and choose only parameters that could falsify it |
| Modification and transfer | Patch a localized core seam with close review | Replace and verify one core module, then defend transfer | Propose alternatives, learner-authors the chosen core replacement, and defend the task decision with measured tradeoffs |

An accelerated action may produce evidence for several adjacent stages. After the learner returns, evaluate every affected stage independently and record exactly which exit evidence passed. Missing evidence remains incomplete. Static source reasoning cannot pass runtime inference or training; copied code cannot pass modification; a plausible recommendation cannot pass transfer without defense.

## Accelerated challenge contract

Use one coherent learner action, not a bundle of unrelated exercises. Its return contract contains:

- the source path and anchors traversed;
- one symbolic tensor or state derivation and its concrete instance;
- one causal or counterfactual prediction;
- after that prediction, one minimal no-write runtime observation with exact stdout or exact error when a runnable path is available;
- the learner's two-layer mental-model update;
- remaining uncertainty.

Do not pre-label the route as earned before this return. Keep `pending_calibration` in the first checkpoint. A strong resume or self-description justifies starting with the harder calibration challenge, not awarding its evidence.

## Common mistakes

- **Advanced means skip evidence:** it means denser evidence per action.
- **Mental model means architecture summary:** it must separate execution flow from mechanism roles and retain an unresolved learner trace.
- **One challenge means one stage automatically:** evidence can be shared, but stage decisions remain separate.
- **Compressed route means skipped stages:** one artifact may satisfy multiple exits; every stage is still evaluated and recorded.
- **One mistake means downgrade the learner:** remediate the affected concept and preserve unrelated evidence.
- **Fast route means agent-authored patch:** the learner still authors the first architecture modification.
