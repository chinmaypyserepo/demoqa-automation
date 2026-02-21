# DemoQA Automation Framework

This is a Python-based automation framework built using Selenium, Pytest, and Requests.  
It supports UI and API automation with data-driven testing, cross-browser execution, headless mode, and parallel execution.

---

## 🚀 Tech Stack

- Python
- Pytest
- Selenium WebDriver
- Requests (API testing)
- OpenPyXL (Excel data-driven testing)
- Pytest-xdist (Parallel execution)
- Allure Reporting
- Pytest-HTML Reporting

---

## 📂 Project Structure

demoqa-automation/
│
├── api/                # API test cases
├── ui/                 # UI test cases
├── utils/              # Utilities (Excel reader, schema validation, etc.)
├── config/             # Configuration settings
├── testdata/           # Excel test data
├── reports/            # Execution reports
├── conftest.py         # Fixtures and browser setup
├── pytest.ini          # Pytest configuration
├── requirements.txt
└── README.md

---

## 🏗 Framework Architecture

```
                    ┌──────────────────────┐
                    │      Pytest CLI      │
                    │  (pytest commands)   │
                    └────────────┬─────────┘
                                 │
                                 ▼
                    ┌──────────────────────┐
                    │      pytest.ini      │
                    │   Markers & Config   │
                    └────────────┬─────────┘
                                 │
                                 ▼
                    ┌──────────────────────┐
                    │     conftest.py      │
                    │  Browser Fixtures    │
                    │  Headless Handling   │
                    └────────────┬─────────┘
                                 │
        ┌────────────────────────┼────────────────────────┐
        ▼                        ▼                        ▼
┌───────────────┐      ┌─────────────────┐      ┌──────────────────┐
│   UI Tests    │      │   API Tests     │      │   Test Data      │
│  (POM Based)  │      │  (Requests)     │      │   (Excel Files)  │
└───────┬───────┘      └─────────┬───────┘      └─────────┬────────┘
        │                        │                          │
        ▼                        ▼                          ▼
┌───────────────┐      ┌─────────────────┐      ┌──────────────────┐
│  Page Objects │      │  API Client     │      │ Excel Reader     │
└───────────────┘      └─────────────────┘      └──────────────────┘
                                 │
                                 ▼
                    ┌──────────────────────┐
                    │   Reports Generated  │
                    │  HTML / Allure       │
                    └──────────────────────┘
```

---

## 🔄 Execution Flow

1. Pytest command is triggered.
2. `pytest.ini` loads markers and configuration.
3. `conftest.py` initializes selected browser.
4. Base URLs are loaded from `config/settings.py`.
5. UI tests execute using Page Object Model.
6. API tests execute using reusable API client.
7. Excel-driven data is read dynamically.
8. Failures capture screenshots.
9. Reports are generated (HTML / Allure).

---

## ▶️ How to Run Tests

### Run All Tests
pytest

### Run Only UI Tests
pytest -m ui

### Run Only API Tests
pytest -m api

---

## 🌍 Cross-Browser Execution

Chrome:
pytest -m ui --browser=chrome

Firefox:
pytest -m ui --browser=firefox

Edge:
pytest -m ui --browser=edge

---

## 🖥 Headless Mode

pytest -m ui --browser=chrome --headless

---

## ⚡ Parallel Execution

pytest -n auto

---

## 🔁 Retry Failed Tests

pytest --reruns 2

---

## 📊 Generate HTML Report

pytest --html=reports/report.html --self-contained-html

---

## 📈 Allure Report

pytest --alluredir=reports/allure-results  
allure serve reports/allure-results

---

## 🖥 Shell Scripts

### run_ui.sh

```bash
#!/bin/bash
pytest -m ui --browser=chrome --headless -n auto --html=reports/ui_report.html --self-contained-html
```

Run:
```bash
sh run_ui.sh
```

---

### run_api.sh

```bash
#!/bin/bash
pytest -m api -n auto --reruns 2 --html=reports/api_report.html --self-contained-html
```

---

### run_all.sh

```bash
#!/bin/bash
pytest -n auto --reruns 2 --alluredir=reports/allure-results
allure serve reports/allure-results
```

---

## 📦 Install Dependencies

pip install -r requirements.txt

---

## 🧪 Run Failed Tests Only

pytest --lf

---

## 🏁 CI/CD Ready

Framework supports:

- Headless execution
- Parallel execution
- Retry mechanism
- Screenshot capture
- HTML & Allure reporting

It can be integrated with:

- Jenkins
- GitHub Actions
- Docker
- Selenium Grid

---

## 👨‍💻 Author

Chinmay Panda  
Automation Test Engineer