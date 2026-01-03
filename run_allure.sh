#!/bin/bash

echo "===== RUNNING PYTEST WITH ALLURE ====="

cd /c/Users/Chinmay/PycharmProjects/pyse/demoqa-automation || exit 1

source venv/Scripts/activate

echo "Cleaning old Allure results"
rm -rf reports
mkdir -p reports/allure-results

echo "Running tests"
pytest --alluredir=reports/allure-results

echo "Starting Allure report server"
allure serve reports/allure-results
