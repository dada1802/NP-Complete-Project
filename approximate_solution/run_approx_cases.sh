#!/bin/sh

for test_case in test_cases/*; do
    echo "Running test case: $test_case"
    python cs412_mingraphcolor_approx.py < "$test_case"
    echo
done

read -n1 -r -p "Press any key to continue..." key
