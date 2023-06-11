#! /bin/sh
echo "Testing the data pipeline..."

echo "$PWD"

cd main

echo "$PWD"

python project/test_pipeline.py

echo "End of test"