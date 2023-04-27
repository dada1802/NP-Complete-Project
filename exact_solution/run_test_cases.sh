#!/bin/sh

# for test_case in test_cases/incomplete_graphs/*; do
#     echo "Running test case: $test_case"
#     python main.py < "$test_case"
#     echo
# done

for test_case in test_cases/complete_graphs/*; do
    echo "Running test case: $test_case"
    python complete_graphs.py < "$test_case"
    echo
done
