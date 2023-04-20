#!/bin/bash

# This script can be used to run pylint

# Import utility functions
# shellcheck source=./tools/utils/_functions.sh
source "$(dirname "${BASH_SOURCE[0]}")/utils/_functions.sh"

require_installed

# Run pylint
echo "Starting code linting with pylint..." | print_info
# Explicitly include cli which does not have a .py ending
pylint . integreat_compass/integreat-compass-cli
echo "✔ Linting finished" | print_success
