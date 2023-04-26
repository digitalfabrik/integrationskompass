#!/bin/bash

# This script can be used to format the Django HTML templates with djlint.

# Import utility functions
# shellcheck source=./tools/utils/_functions.sh
source "$(dirname "${BASH_SOURCE[0]}")/utils/_functions.sh"

require_installed

# Run djlint
echo "Starting code formatting with djlint..." | print_info
djlint --reformat --quiet --lint "${PACKAGE_DIR}"
echo "✔ Code formatting finished" | print_success
