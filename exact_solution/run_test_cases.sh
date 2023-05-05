#!/bin/sh

for test_case in complete_graphs/*; do
    echo "Running test case: $test_case"
    time python main.py < "$test_case"
    echo
done

read -n1 -r -p "Press any key to continue..." key
