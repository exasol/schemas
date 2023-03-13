#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail

project_dir="$( cd "$(dirname "$0")/.." >/dev/null 2>&1 ; pwd -P )"

readme_file="$project_dir/README.md"
readonly readme_file
index_file="$project_dir/index.html"
readonly index_file

readme_timestamp=$(git log -1 --pretty="format:%ct" "$readme_file")
readonly readme_timestamp
index_timestamp=$(git log -1 --pretty="format:%ct" "$index_file")
readonly index_timestamp

print_git_log() {
    echo "🗒️ git log -1 $readme_file:"
    git log -1 "$readme_file"
    echo "🗒️ git log -1 $index_file:"
    git log -1 "$index_file"
}

if [ "$readme_timestamp" -gt "$index_timestamp" ]; then
    echo "🛑 $readme_file is newer than $index_file. Please generate $index_file as described in doc/developers_guide.md"
    print_git_log
    exit 1
else
    echo "✅ $readme_file is not newer than $index_file"
    print_git_log
fi
