#!/bin/bash

# This script can be used to format the static files with prettier

# Import utility functions
# shellcheck source=./tools/utils/_functions.sh
source "$(dirname "${BASH_SOURCE[0]}")/utils/_functions.sh"

# Run prettier
echo "Starting code formatting with prettier..." | print_info
npx prettier --write .
echo "✔ Code formatting finished" | print_success
