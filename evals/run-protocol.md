# Reproducible behavioral evaluation protocol

This protocol makes the public scorecards auditable. Agent responses are nondeterministic, so it reproduces the procedure rather than promising byte-identical prose.

## Record before each run

- date and agent/model identifier;
- clean skill repository commit, or an explicit local snapshot identifier;
- scenario name and fixture path;
- whether no skill is loaded (`RED`), the last released skill is loaded without candidate changes (`UPGRADE BASELINE`), or the candidate skill is loaded (`GREEN`);
- every skill/reference/fixture file the responding agent read;
- the complete raw user-facing response.

The v0.1 report used GPT-5.6 Terra at medium reasoning on 2026-08-24/25. It is explicitly an exploratory audit, not release-grade behavioral evidence or a statistical reliability estimate. Its final-snapshot set contains four completed responses across three scenarios—A once, B twice, and C once—and retains the mandatory B failure alongside three passing exemplars. Earlier development failures are also retained. Before making a reliability or release-grade evaluation claim, run every scenario in at least three fresh contexts and report every completed response, including failures.

The v0.2 upgrade added Scenario D (advanced routing) and Scenario E (schema-v1 challenge resume) on 2026-08-31, followed by Scenario F (untouched v1 defaults and extensions) during final review. D uses an `UPGRADE BASELINE` against the previous released skill. The early E pre-contract artifact lacks an exact skill snapshot and is retained only as an unscored `DEVELOPMENT PROBE`, not a protocol-compliant baseline. Material GREEN failures and clean responses are retained. D independently scored 8/8 and passed a separate self-contained citation audit; E scored 6/6 for the supplied challenge checkpoint. E does not by itself establish arbitrary-field losslessness; F separately scored 5/5 for null defaults, lab evidence, misconceptions, open questions, and unknown nested/root fields. Attempts terminated by the agent-service usage limit before producing a response are not behavioral samples. These adaptive campaigns demonstrate the design/test loop, not response reliability.

The exact evaluated skill file set is recorded in [`skill-snapshot.sha256`](skill-snapshot.sha256); each final-snapshot transcript carries its combined snapshot ID.

## Responding-agent procedure

1. Start a fresh agent context with no prior scenario conversation or study checkpoint.
2. For `RED`, expose no skill. For `UPGRADE BASELINE`, expose only the last released skill and record its commit/snapshot. For `GREEN`, instruct the agent to read the candidate `skills/learning-ai-architectures-from-source/SKILL.md` completely and then follow its progressive-disclosure routing.
3. Give read-only access only to the matching fixture plus references selected by the skill. Do not permit repository edits.
4. Have the orchestrator paste the scenario prompt from `scenarios.md` verbatim. Do not expose the scenarios file, mandatory criteria, prior transcripts, scorecards, baselines, or results to the responding agent.
5. Request only the first user-facing response of the multi-session study. Do not request a self-score or evaluator notes; those can bias or contaminate the response.
6. Save the response verbatim under `transcripts/` together with the run metadata and files-read list. Do not silently clean up answer leaks or unsupported claims.

Use this neutral wrapper around the selected scenario:

```text
Read the named skill completely and follow it. Inspect the matching fixture read-only.
Respond to the exact scenario as the first turn of the study. Do not modify files.
Return only the user-facing response and a list of files actually read; do not self-score.
```

## Independent scoring procedure

1. Use a separate fresh evaluator that did not generate the response.
2. Give it only `scenarios.md`, the matching fixture, the raw transcript, and this protocol.
3. For each `[M]` criterion, assign `0`, `0.5`, or `1` and quote or anchor the observable response evidence. Validate cited source spans against the fixture rather than awarding credit for anchor-shaped text alone.
4. Treat an agent's self-assessment, confidence, headings, or claimed compliance as no evidence.
5. A scenario passes only if every mandatory criterion equals `1`. Record partial scores for diagnosis, never to override that rule.
6. Save the completed per-criterion audit in `scorecards.md`. A changed response or rubric requires a new scorecard; do not reuse an old score.

## Fixture execution check

From `evals/fixtures`, run the no-write smoke paths:

```text
python -B detector/inference.py
python -B detector/train_step.py
python -B self-supervised/inference.py
python -B self-supervised/train_step.py
python -B llm/inference.py
python -B llm/train_step.py
```

Then use `--checkpoint` with paths outside the source tree and confirm that the matching inference script reports `checkpoint=loaded_strict`. Also try one deliberately incompatible checkpoint and require a nonzero exit. See `fixtures/README.md` for structural outputs and the limits of the toy losses.

## Interpretation boundary

These tests evaluate first-turn teaching behavior, evidence discipline, and answer withholding on small PyTorch fixtures. They do not prove long-session retention, learning outcomes across a population, coverage of every real repository, or model-quality improvements. Publish those claims only after separate longitudinal or user studies.
