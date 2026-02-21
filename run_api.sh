#!/bin/bash

echo "===== CLEANING OLD API REPORTS ====="
rm -rf reports/allure-results
rm -rf reports/allure-report
mkdir -p reports/allure-results

echo "===== RUNNING API TESTS ====="
pytest -m api -n 2 --alluredir=reports/allure-results

echo "===== GENERATING REPORT ====="
allure generate reports/allure-results -o reports/allure-report --clean

echo "===== OPENING REPORT ====="
allure open reports/allure-report