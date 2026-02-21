#!/bin/bash

echo "===== CLEANING OLD UI REPORTS ====="
rm -rf reports/allure-results
rm -rf reports/allure-report
mkdir -p reports/allure-results

echo "===== RUNNING UI TESTS ====="
pytest -m ui -n 2 --alluredir=reports/allure-results

echo "===== GENERATING REPORT ====="
allure generate reports/allure-results -o reports/allure-report --clean

echo "===== OPENING REPORT ====="
allure open reports/allure-report