#!/bin/bash -e
echo ""
echo ""
echo "🔨🔨🔨🔨🔨🔨🔨🔨 UNITEST 🔨🔨🔨🔨🔨🔨🔨🔨🔨🔨"

if [ -d "./build" ]; then
    echo "-> 🚮 Removing old build directory..."
    rm -rf ./build/*
else
    echo "-> 👷 Creating build directory..."
    mkdir build
fi

# Compile Assembly code
nasm -f elf32 float_int.asm

# Compile and link unit tests with Unity and Assembly code
gcc -m32 -o build/tests external/unity/src/unity.c test.c float_int.o -Iexternal/unity/src

# Run unit tests
./build/tests

echo ""
echo ""

echo "🛸🛸🛸🛸🛸🛸🛸🛸 COVERAGE 🛸🛸🛸🛸🛸🛸🛸🛸🛸🛸"

# Enable coverage
RUN_COVERAGE=true

if [ "$RUN_COVERAGE" = true ]; then
    # Generate coverage report
    LCOV_PATH=$(which lcov)
    GCOV_PATH=$(which gcov)
    GENHTML_PATH=$(which genhtml)

    if [ -z "$LCOV_PATH" ] || [ -z "$GCOV_PATH" ] || [ -z "$GENHTML_PATH" ]; then
        echo "❌ Error: One or more coverage tools not found! Aborting... ❌"
        exit 1
    fi

    # Compile test files with coverage
    gcc -fprofile-arcs -ftest-coverage -m32 -o build/tests external/unity/src/unity.c test.c float_int.o -Iexternal/unity/src

    # Run tests again
    ./build/tests

    # Generate coverage report
    lcov -c -d . -o build/coverage.info
    genhtml build/coverage.info -o build/coverage_report

    # Open coverage report in default web browser
    xdg-open build/coverage_report/index.html
else
    echo "Coverage disabled"
fi
