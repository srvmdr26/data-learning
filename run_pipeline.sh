#!/bin/bash

set -e

echo "================================"
echo "Starting data pipeline"
echo "================================"

# Make sure the script runs from the project root
cd "$(dirname "$0")"

echo ""
echo "Step 1: Ingesting customer data..."
python python/ingest_customers.py

echo ""
echo "Step 2: Running dbt models..."
cd dbt/data_learning_dbt
dbt run

echo ""
echo "Step 3: Running dbt tests..."
dbt test

echo ""
echo "================================"
echo "Pipeline completed successfully!"
echo "================================"