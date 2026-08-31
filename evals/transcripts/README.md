# Behavioral evaluation transcripts

These files preserve the first user-facing turn from fresh GREEN runs. Each transcript records the exact scenario prompt, run metadata, the response, and every file the responding agent reported reading.

The only sanitization permitted is replacing absolute workspace and user-home prefixes in `FILES READ` with `<repo-root>/` and `<home>/`. User-facing prose, claims, source anchors, omissions, and answer leaks remain unchanged. Diagnostic failures are retained instead of being silently replaced by a later passing sample.

See [`../run-protocol.md`](../run-protocol.md) for the neutral wrapper, contamination guard, independent scoring procedure, and interpretation limits. A run filename identifies its scenario and chronological attempt; the scorecard, not the filename or responding agent, determines pass/fail.
