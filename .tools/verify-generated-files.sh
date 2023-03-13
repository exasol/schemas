#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail

project_dir="$( cd "$(dirname "$0")/.." >/dev/null 2>&1 ; pwd -P )"

readme_file="$project_dir/README.md"
readonly readme_file
index_file="$project_dir/index.html"
readonly index_file

if [ "$readme_file" -nt "$index_file" ]; then
    echo "🛑 $readme_file is newer than $index_file. Please generate $index_file as described in doc/developers_guide.md"
    ls -lah "$readme_file" "$index_file"
    stat "$readme_file" "$index_file"
    exit 1
else
    echo "✅ $readme_file is older than $index_file"
    ls -lah "$readme_file" "$index_file"
    stat "$readme_file" "$index_file"
fi