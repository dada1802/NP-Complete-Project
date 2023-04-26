#!/bin/sh

for test_case in test_cases/*; do
    echo "Running test case: $test_case"
    python main.py < "$test_case"
    python complete.py < "$test_case"
    echo
done
