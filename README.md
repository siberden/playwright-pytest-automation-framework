# Playwright + Pytest Automation Framework

A scalable and production-ready end-to-end (E2E) test automation framework built with:

- ✅ Playwright
- ✅ Pytest
- ✅ Allure Reporting
- ✅ Parallel Execution (pytest-xdist)
- ✅ GitHub Actions CI/CD
- ✅ Automatic Screenshot on Failure

---

## Features

- Cross-browser support (Chromium)
- Parallel test execution
- Headless execution in CI
- Allure HTML reports
- Screenshot capture on failure
- GitHub Pages auto-deployment
- CI pipeline ready (Ubuntu 22.04)

---

## Tech Stack

- Python 3.12
- Playwright
- Pytest
- Allure
- GitHub Actions

---

## Project Structure

```text
playwright-pytest-automation-framework/
│
├── .github/
│   └── workflows/
│       └── ci.yml                 # GitHub Actions CI pipeline
│
├── pages/                         # Page Object Model layer
│   ├── base_page.py               # Reusable browser actions & waits
│   ├── home_page.py               # Home page interactions
│   ├── checkout_page.py           # Checkout flow logic
│   └── inventory_page.py          # Inventory interactions
│
├── tests/                         # Test cases (business flows)
│   ├── test_login.py
│   ├── test_checkout.py
│   ├── test_inventory.py
│   └── test_smoke.py
│
├── utils/                         # Helper utilities
│   ├── locators.py
│   ├── data.py
│   └── config.py
│
├── conftest.py                    # Pytest fixtures & driver setup
├── pytest.ini                     # Markers & configuration
├── requirements.txt               # Dependencies
└── README.md
```
### Architecture Overview

- **Tests Layer** → Contains business-level test scenarios.
- **Page Layer (POM)** → Encapsulates UI interactions.
- **Base Page** → Common reusable Selenium/Playwright actions.
- **Utils Layer** → Configuration, test data, and locator management.
- **CI Layer** → Automated execution via GitHub Actions.


---

## Installation

Clone the repository:

```bash
git clone https://github.com/siberden/playwright-pytest-automation-framework.git
cd playwright-pytest-automation-framework
```

Create virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate     # Windows
```
Install dependencies:
```bash
pip install -r requirements.txt
playwright install


Running Tests

Run all tests:
```bash
pytest
```
Run in headed mode (local only):
```bash
pytest --headed
```

Run smoke tests:
```bash
pytest -n auto
```
Run in parallel:
```bash
pytest -n auto
```
Allure Reporting

Generate report locally:
```bash
pytest --alluredir=allure-results
allure serve allure-results
```
##### Screenshot on Failure

If a test fails:

A screenshot is automatically captured

Attached to the Allure report

### CI/CD Pipeline

#### GitHub Actions workflow:

Runs on push & pull request

Installs dependencies

Runs tests in headless mode

Generates Allure report

Deploys report to GitHub Pages

