#! /bin/sh
echo "Testing the data pipeline..."

echo "$PWD"

cd main

echo "$PWD"

pip install pandas

python project/test_pipeline.py

echo "End of test"