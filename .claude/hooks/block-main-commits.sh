#!/usr/bin/env bash
# Sacred Workflow enforcement: refuse `git commit` / `git push` while on main.
# Wired up via .claude/settings.json PreToolUse on the Bash tool.
# Exit 2 blocks the tool call and surfaces stderr to Claude.

set -uo pipefail

input=$(cat || true)
[ -z "$input" ] && exit 0

tool=$(printf '%s' "$input" | jq -r '.tool_name // ""' 2>/dev/null || echo "")
[ "$tool" = "Bash" ] || exit 0

cmd=$(printf '%s' "$input" | jq -r '.tool_input.command // ""' 2>/dev/null || echo "")
[ -n "$cmd" ] || exit 0

# Match `git commit` or `git push` as a whole word, anywhere in the command
# (handles chains like `git add . && git commit -m ...`). Avoids matching
# `gh`, `gitleaks`, `git-foo`, etc.
if printf '%s' "$cmd" | grep -qE '(^|[^[:alnum:]_./-])git[[:space:]]+(commit|push)([[:space:]]|$)'; then
  branch=$(git -C "${CLAUDE_PROJECT_DIR:-.}" branch --show-current 2>/dev/null || echo "")
  if [ "$branch" = "main" ] || [ "$branch" = "master" ]; then
    cat >&2 <<EOM
Sacred Workflow violation: refusing git commit/push on '${branch}'.

This repo's CLAUDE.md and inputs/# Purpose of work.md require all changes
to flow through Issues + branches + draft PRs. The change history is itself
part of the performance-review deliverable.

Do this instead:

  gh issue create --title "..." --body "..."
  git checkout -b <type>/<short-slug>
  # ... make changes, commit on the branch ...
  gh pr create --draft --title "..." --body "Closes #<n>"

If this is a genuine emergency that must bypass the workflow, disable this
hook in .claude/settings.json and document the reason in the commit body.
EOM
    exit 2
  fi
fi

exit 0
