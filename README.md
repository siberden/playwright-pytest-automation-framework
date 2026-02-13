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

