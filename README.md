# Learning AI Architectures from Source

A learner-led, source-first Agent Skill for understanding unfamiliar PyTorch AI architecture repositories deeply enough to trace, explain, tune, modify, and transfer their architectures to real tasks.

## Contents

- [Overview](#overview)
- [What You Will Learn](#what-you-will-learn)
- [How It Works](#how-it-works)
- [Learning Methodology](#learning-methodology)
- [Learning Routes](#learning-routes)
- [Supported Architecture Families](#supported-architecture-families)
- [Prerequisites](#prerequisites)
- [Key Capabilities](#key-capabilities)
- [Repository Structure](#repository-structure)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Evaluation](#evaluation)
- [Limitations](#limitations)
- [Contributing](#contributing)
- [License](#license)

## Overview

Learning an architecture from a paper or diagram is useful, but it does not tell you where that architecture actually lives in a repository, how configuration reaches the model, which tensors cross each boundary, or what will break when you change it.

This skill turns an unfamiliar repository into a resumable, evidence-driven learning project. It guides the learner from entry points and configuration through inference, training, parameter causality, architecture modification, and real-task transfer. Important explanations are tied to source locations, while small runtime experiments are used to confirm behavior that static reading alone cannot establish.

It is not a one-shot repository summarizer and it does not replace the learner with an automatically generated patch. The learner remains at the keyboard, makes predictions before seeing results, performs bounded source or runtime tasks, and demonstrates understanding before advancing.

## What You Will Learn

By completing a study cycle, a learner should be able to:

- locate configuration files, model builders, registries, entry points, forward paths, losses, and training loops;
- reconstruct the active call chain instead of relying only on class names or directory structure;
- track tensor shape, layout, dtype, device, and semantic meaning across architecture boundaries;
- explain what important hyperparameters control, which parameters are coupled, and what failure modes invalid values create;
- identify an architecture's mechanism-bearing implementation and distinguish it from wrappers, adapters, logging, and training utilities;
- run minimal inference and training experiments that isolate one causal question at a time;
- replace an architecture-bearing core module while preserving and verifying its input/output tensor contract;
- adapt the architecture to a real task and defend the resulting data, training, evaluation, and deployment decisions.

## How It Works

Each repository study progresses through a nine-stage learning loop:

```text
scope → repository map → inference → training → reconstruction
      → parameters → modification → transfer → mastery
```

Each teaching turn follows a smaller evidence loop:

```text
source evidence → learner prediction → one bounded action
                → runtime evidence → explanation → mastery checkpoint
```

The skill first builds a two-layer mental model:

1. **Execution spine** — the active path from configuration or input to model construction, forward execution, outputs, loss, and optimization.
2. **Architecture skeleton** — the roles of the major mechanism-bearing components and the tensor contracts connecting them.

Important claims are labeled as `[source-confirmed]`, `[runtime-verified]`, `[docs-stated]`, or `[inferred]`. Source-confirmed architecture claims use repository, commit, path, and line anchors so the learner can inspect the exact implementation rather than trusting a detached explanation.

Progress is saved in a resumable checkpoint containing stage status, evidence, misconceptions, open questions, six mastery-gate scores, and exactly one next action.

## Learning Methodology

This Skill is built around a **Harness Engineering** approach to learning. The AI assistant is only one component of the learning system; reliable progress also depends on the surrounding harness: pinned source code, repository-navigation tools, executable environments, bounded experiments, tensor-contract checks, evidence labels, saved state, evaluation gates, and feedback loops. The harness turns an open-ended request to “understand this architecture” into a sequence of observable, reproducible learning outcomes.

Four design principles work together inside that harness:

| Method | How the Skill applies it | Evidence produced by the learner |
| --- | --- | --- |
| **Harness Engineering** | Organizes source access, tools, runtime environments, checkpoints, experiments, and mastery gates around the learner and the target repository | Reproducible source traces, captured command output, experiment records, tensor-contract checks, and resumable state |
| **First-Principles Reasoning** | Reduces an architecture to the problem it solves, its inputs and outputs, data transformations, state, objectives, constraints, and invariants before relying on paper terminology or repository naming | Derived tensor shapes, parameter couplings, causal predictions, and explanations of why each mechanism must exist |
| **Socratic Questioning** | Uses predictions, counterfactuals, diagnosis questions, and teach-back before revealing answers; hints become more specific only when the learner's evidence shows a real blockage | Independent explanations, corrected misconceptions, defended design choices, and answers grounded in source or runtime evidence |
| **Project-Driven Learning** | Selects a real transfer destination during scope and uses it to prioritize what the learner traces, tests, modifies, and evaluates without prematurely supplying the final solution | A learner-authored core-module change, project-relevant experiments, evaluation results, failure analysis, and a defended transfer plan |

The combined loop is:

```text
real project → source trace → first-principles model → Socratic prediction
             → minimal experiment → evidence → architecture change
             → project evaluation → reflection and next checkpoint
```

Project-driven learning is therefore a first-class path through the Skill, not an optional exercise at the end. A learner may start from industrial detection, visual retrieval, multimodal adaptation, or local LLM fine-tuning; the chosen project supplies context and priorities throughout the study, while the same evidence and mastery standards prevent “finishing the demo” from being mistaken for understanding the architecture.

## Learning Routes

The first repository task is a small observable calibration challenge. The result selects a provisional route; job title, confidence, or self-rating alone never determines placement.

| Route | Intended learner experience | Teaching style |
| --- | --- | --- |
| `guided` | Needs support connecting Python/PyTorch code to architecture concepts | Smaller actions, explicit framework bridges, and earlier hints |
| `standard` | Can read ordinary model code but needs a structured source-learning process | Stage-sized call-chain traces, tensor derivations, and causal experiments |
| `accelerated` | Demonstrates independent navigation, tensor reasoning, and causal diagnosis | Integrated challenges, fewer hints, counterfactuals, and design trade-offs |

An accelerated learner may produce one artifact that supplies evidence for several adjacent stages, but every stage is evaluated independently. All routes use the same graduation standard, and weak concepts receive targeted remediation without erasing unrelated demonstrated competence.

## Supported Architecture Families

The current version is PyTorch-first and teaches recurring source patterns rather than assuming one universal repository layout.

| Family | Representative focus | Included transfer direction |
| --- | --- | --- |
| CNN and YOLO-style detectors | Backbone, neck, detection head, target assignment, decoding, and losses | Industrial object detection |
| Vision Transformers and decoder LLMs | Tokenization, attention, residual paths, normalization, masking, and generation | Vision adaptation and local LLM fine-tuning |
| DINO-like self-supervised systems | Student/teacher paths, projection heads, state updates, and representation extraction | Visual feature retrieval |
| Retrieval architectures | Embedding production, normalization, indexing boundaries, and similarity evaluation | Visual search and feature retrieval |
| Multimodal architectures | Encoders, projectors/connectors, alignment objectives, and modality interfaces | Multimodal adaptation |
| Mixture-of-experts models | Router decisions, expert dispatch, capacity, and auxiliary objectives | Architecture analysis and controlled modification |

## Prerequisites

- Basic Python programming ability.
- Basic command-line usage, including navigating files and running Python commands.
- Access to the repository being studied, preferably at a pinned commit.
- A Python/framework/device environment when runtime verification begins. Limited hardware is acceptable because the skill starts with minimal, high-information experiments.

Prior PyTorch experience is helpful but not required. Calibration is based on observable source-reading and tensor-reasoning evidence, and the skill follows the learner's language unless asked otherwise.

## Key Capabilities

When a learner asks for everything at once, an ordinary coding agent often gives a polished report and a complete patch. This skill instead requires:

- an official repository or local path and pinned commit, or a documented unresolved-anchor exception with its reason;
- distinct roles for official and comparison implementations;
- `repo@commit:path:start-end` anchors for every source-confirmed architecture claim and deep annotation;
- evidence labels: `[runtime-verified]`, `[source-confirmed]`, `[docs-stated]`, and `[inferred]`;
- learner predictions before commands or edits;
- observable learner calibration, a provisional route, and evidence-driven route changes;
- a rapid execution-spine plus architecture-skeleton mental model before deep study;
- an answer boundary that prevents a solved shape table or patch from being reused as a fake mastery question;
- minimal inference and training performed by the learner;
- a learner-authored replacement of an architecture-bearing core module—not a loss-only, config-only, adapter-only, wrapper-only, or training-hook-only edit—with its tensor contract verified;
- Socratic diagnosis, Feynman teach-back, and six observable mastery gates;
- a saved checkpoint with exactly one next action.

Graduation requires all six mastery gates to score 3: `navigation`, `tensor_flow`, `parameter_causality`, `diagnosis`, `modification`, and `transfer`. The learner must independently trace the execution path, derive critical tensor shapes, explain coupled parameters, replace and verify an architecture-bearing core module while preserving its tensor contract, and defend a real-task transfer plan. Only then may the saved study status become `complete`.

## Repository Structure

```text
skills/learning-ai-architectures-from-source/
├── SKILL.md
├── agents/openai.yaml
├── assets/
│   ├── experiment-log-template.md
│   ├── parameter-ledger-template.md
│   └── study-state-template.yaml
└── references/
    ├── architecture-families.md
    ├── learner-routing.md
    ├── learner-led-labs.md
    ├── repository-investigation.md
    ├── socratic-assessment.md
    ├── source-annotation.md
    └── task-transfer.md
evals/
├── baseline-observations.md
├── forward-test-results.md
├── run-protocol.md
├── scenarios.md
├── scorecards.md
├── skill-snapshot.sha256
├── transcripts/
└── fixtures/
    └── README.md
examples/
└── example-study-checkpoint.md
```

`SKILL.md` stays compact and loads only the reference needed for the current stage. This follows Codex's progressive-disclosure model and official skill directory format. See the [OpenAI skill documentation](https://learn.chatgpt.com/docs/build-skills).

## Installation

An Agent Skill packages instructions, references, assets, and optional scripts in a directory anchored by `SKILL.md`. Codex discovers repository-scoped skills from `.agents/skills` and user-wide skills from `$HOME/.agents/skills`; see the [official OpenAI Skill documentation](https://learn.chatgpt.com/docs/build-skills).

### Install with Skill Installer

In Codex, invoke `$skill-installer` and ask it to install:

```text
https://github.com/jeams666/Skill_Learning-AI/tree/main/skills/learning-ai-architectures-from-source
```

### Install manually for one repository

Copy `skills/learning-ai-architectures-from-source` to:

```text
<repository>/.agents/skills/learning-ai-architectures-from-source/
```

### Install manually for user-wide discovery

Copy the same directory to:

```text
$HOME/.agents/skills/learning-ai-architectures-from-source/
```

Codex normally detects skill changes automatically. Restart Codex if the skill does not appear after installation.

## Quick Start

Explicit invocation is recommended for a learning session:

```text
$learning-ai-architectures-from-source

Help me study this repository from source. Target model/config: ...
Official repository and commit: ...
Environment/device: ...
Transfer track: industrial detection | retrieval | multimodal | local LLM
```

On the first turn, the skill should scope the source and give one calibration or investigation action. It should not deliver the entire course, architecture patch, and transfer plan immediately.

To resume, provide the saved YAML state or compact chat checkpoint and ask the skill to continue from the earliest incomplete stage.

## Evaluation

The [`evals`](evals/) directory contains six adversarial teaching scenarios and tiny runnable fixtures:

1. A detector request under demo deadline pressure.
2. A DINO-like retrieval request with no official source supplied.
3. An incompatible grouped-attention head-count change.
4. An experienced learner requesting the shortest evidence-based route and rapid mental model.
5. A schema-v1 study checkpoint that must resume under schema v2 without losing evidence.
6. An untouched schema-v1 default with null routes/gates, lab evidence, and unknown extension fields.

[`baseline-observations.md`](evals/baseline-observations.md) records the development baseline without the skill. [`scenarios.md`](evals/scenarios.md) defines mandatory observable criteria, [`run-protocol.md`](evals/run-protocol.md) documents the contamination guard and independent audit procedure, and [`transcripts/`](evals/transcripts/) preserves current responses plus diagnostic failures. The evaluated skill files are pinned by [`skill-snapshot.sha256`](evals/skill-snapshot.sha256). The final per-criterion evidence is in [`scorecards.md`](evals/scorecards.md), with interpretation in [`forward-test-results.md`](evals/forward-test-results.md).

The v0.1 exploratory audit contains four completed final-snapshot responses across three scenarios: three pass every mandatory criterion and one retained retrieval response fails. Version 0.2 adds upgrade-baseline/GREEN campaigns for advanced routing and schema migration. Clean responses score D 8/8, E 6/6, and F 5/5; F specifically verifies null normalization and preservation of supplied lab, misconception, open-question, and extension data. Baselines, failed candidates, and stricter evidence-contract failures remain public. This is behavioral evidence rather than a statistical learning-outcome claim. These tests cover first-turn teaching behavior and evidence discipline on toy repositories, not long-session outcomes, every real repository, or model-quality gains.

## Limitations

- The skill teaches from the repository in front of it; it does not claim one universal code layout.
- Version 0.2 is PyTorch-first and does not promise TensorFlow or JAX repository coverage.
- Comparison repositories may explain mechanisms but never establish official behavior.
- Toy inference/training can verify plumbing, not task quality.
- Advice not established by the pinned repository must be labeled as documentation, runtime evidence, or inference.
- If the user explicitly switches to report-only or implementation-only mode, the agent may comply, but that work cannot advance a learning stage or graduation status.

## Contributing

Useful contributions include architecture-family cues, new transfer tracks, and adversarial eval scenarios. Keep the core learner-led invariant intact, add observable pass criteria, and distinguish repository evidence from general guidance.

## License

Apache-2.0. See [LICENSE](LICENSE).
