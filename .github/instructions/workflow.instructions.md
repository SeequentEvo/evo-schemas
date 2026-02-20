---
applyTo: "**"
---
# Workflow and collaboration

## Collaborative approach

This repository values careful, reviewed changes. When working on non-trivial tasks:

- **Discuss before implementing.** For tasks that involve design decisions, structural changes, or multi-file modifications, first outline the approach and confirm it with the user before writing code. Ask clarifying questions early — it is better to ask than to assume.
- **Work step-by-step.** Break implementation into discrete, reviewable steps. Execute one step at a time — propose, review, adjust, approve — before moving to the next.
- **Ask between steps.** After completing each logical step, pause and check in with the user before proceeding. Offer to continue with the next step, and allow the user to request changes, ask questions, or redirect. Never silently move to the next step on multi-step work.
- **Be additive, not rewriting.** Existing human-authored content should be preserved. Expansions add context; they don't restructure or replace prose unless explicitly asked.

## Commit conventions

- **Atomic commits**: Each logical change gets its own commit. Group related changes (e.g., expanding all variogram descriptions) but keep unrelated changes separate.
- **Per-family commits for review**: When making changes across domain-specific families (e.g., variogram structures, resistivity-IP components), commit each family separately so subject-matter experts can review them independently.
- **Stage before review**: Stage changes with `git add` and show the diff with `git --no-pager diff --cached` so the reviewer sees exactly what will be committed.
- **Signed commits**: All commits must be signed with verified signatures.
- **Run validation before presenting**: Always run tests and linting before presenting a step for review. The review should be of verified, passing code.

## Information boundaries

This repository is open source under Apache 2.0. Everything — code, docs, instructions, issues, PRs — is public.

- **Do** reference anything already public: this repo, its issues/PRs, other public `SeequentEvo` repos, the [Seequent Developer Portal](https://developer.seequent.com/).
- **Do not** reference private repositories, internal tooling, CI/CD pipelines, or non-public infrastructure — even if you have access.
