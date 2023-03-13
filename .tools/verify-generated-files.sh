#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail

project_dir="$( cd "$(dirname "$0")/.." >/dev/null 2>&1 ; pwd -P )"

cd "$project_dir"
if [[ $(git status --porcelain) ]]; then
  echo "🛑 Please generate files as described in doc/developers_guide.md"
  echo "git status --no-pager"
  git status
  echo "git diff --no-pager"
  git diff
  exit 1
else
  echo "✅ All files up-to-date"
fi
