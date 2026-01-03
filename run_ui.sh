#!/bin/bash
cd /c/Users/Chinmay/PycharmProjects/pyse/demoqa-automation || exit 1
source venv/Scripts/activate
rm -rf reports
mkdir -p reports/allure-results
pytest -m ui --alluredir=reports/allure-results
allure serve reports/allure-results
