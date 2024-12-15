# Hybrid Test Automation Framework

This repository contains a **hybrid test automation framework** built using **Playwright**, **Python**, **Pytest**, **LambdaTest**, and **Oracle DB** for automating end-to-end web testing, cross-browser testing, and database validation. The framework follows best practices with modular components, reusable keywords, Page Object Model (POM), and both data-driven and keyword-driven testing approaches.

---

## Table of Contents
- [Overview](#overview)
- [Technologies](#technologies)
- [Folder Structure](#folder-structure)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Usage](#usage)
- [Running Tests](#running-tests)
- [Reporting](#reporting)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

The framework is designed to provide robust and scalable test automation solutions that can be used for:
- **End-to-End Web Testing** using Playwright.
- **Cross-Browser Testing** through LambdaTest integration.
- **Database Validation** with Oracle DB.

It allows easy integration of automated tests into continuous integration (CI) pipelines, including support for cloud-based services like **LambdaTest** for parallel cross-browser testing.

---

## Technologies

This framework utilizes the following technologies:

- **Python** – Primary programming language for writing test scripts.
- **Playwright** – For browser automation (headless testing and cross-browser testing).
- **Pytest** – Testing framework for test execution, assertions, and reporting.
- **LambdaTest** – For running tests on cloud-based Selenium grids.
- **Oracle DB** – For database validation and queries.
- **Page Object Model (POM)** – For organizing test scripts and maintaining clean, reusable code.
- **Data-Driven and Keyword-Driven Testing** – Hybrid approach for flexibility and scalability.

---

## Folder Structure

The framework is organized as follows:

```
/test-automation-framework
├── /config                        # Configuration files (Playwright, LambdaTest, Oracle DB, etc.)
├── /drivers                       # Browser drivers and LambdaTest configuration
├── /tests                         # Test cases (Login, Search, Database validation)
├── /pages                         # Page Object Model (POM) design for Playwright
├── /keywords                      # Reusable keyword-driven test components
├── /utils                         # Utility functions for Playwright, DB, LambdaTest, etc.
├── /testdata                      # Test data for data-driven testing
├── /reports                       # Test reports and logs
├── /scripts                       # Automation scripts for setup, execution, and reporting
├── /requirements                  # Python dependencies
├── /testsuite                     # Pytest configuration
└── README.md                      # Framework documentation
```

---

## Prerequisites

Before using the framework, ensure that the following prerequisites are met:

- **Python 3.x** – Make sure Python is installed on your system.
- **Playwright** – Browser automation library for web testing.
- **Oracle Client** – Required for interacting with Oracle databases.
- **LambdaTest Account** – For executing tests on the LambdaTest grid.
- **Pytest** – Python testing framework for test execution and reporting.

---

## Setup

### 1. Clone the repository:
```bash
git clone https://github.com/yourusername/test-automation-framework.git
cd test-automation-framework
```

### 2. Install dependencies:
Create and activate a Python virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```

Install required dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 3. Configure the framework:
- Modify the **`config.yaml`** file for your global settings (e.g., base URL, LambdaTest API key, Oracle DB credentials).
- Update **`playwright_config.json`** and **`lambdatest_config.json`** with appropriate configurations for browser execution and cloud testing.
- If you need to connect to an Oracle database, update **`db_config.yaml`** with connection details (username, password, host, port).

---

## Usage

This framework supports both **data-driven** and **keyword-driven** testing. You can create test cases in the `/tests` directory using **Pytest**.

### Running Tests Locally
1. **Test a specific module (e.g., login tests):**
   ```bash
   pytest tests/login/test_login.py
   ```

2. **Run all tests:**
   ```bash
   pytest tests/
   ```

3. **Run tests with specific tags or markers:**
   You can use markers in Pytest to categorize your tests (e.g., smoke, regression, etc.):
   ```bash
   pytest -m "smoke"
   ```

### Cross-Browser Testing with LambdaTest
To run tests on LambdaTest’s cloud grid, ensure you have configured **LambdaTest credentials** in `lambdatest_config.json`.

Once configured, you can run tests remotely using LambdaTest as part of your Pytest commands.

---

## Running Tests

The framework uses **Playwright** for browser automation, so tests can be run in local headless mode or on a cloud grid (via **LambdaTest**). Here’s how you can run tests:

- **Locally (on your machine)**: The default browser (e.g., Chrome) is used for local testing.
- **On LambdaTest (cloud grid)**: Set `run_on_lambdatest: true` in the configuration, and the framework will automatically execute tests on LambdaTest’s grid.

### Example Command to Run Tests on LambdaTest:
```bash
pytest --run_on_lambdatest=True
```

---

## Reporting

The framework generates test reports in the **`/reports/html`** directory. You can view the HTML reports after test execution. By default, **pytest-html** is used for generating these reports, which include detailed results, screenshots (on failure), and logs.

### Example of generating HTML reports:
```bash
pytest --html=reports/html/report.html
```

The **`/logs`** folder will store all log files, and **`/screenshots`** will contain screenshots taken during test failures for easier debugging.

---

## Contributing

We welcome contributions to enhance the framework. If you want to contribute, follow these steps:

1. Fork the repository.
2. Create a new branch for your changes.
3. Implement your changes.
4. Write test cases for any new functionality.
5. Submit a pull request with a clear description of your changes.

---



---

## Conclusion

This hybrid test automation framework is designed for scalability and flexibility, leveraging **Playwright** for automation, **Pytest** for testing, **LambdaTest** for cloud grid testing, and **Oracle DB** for database validation. It follows modern best practices like the **Page Object Model** (POM), **data-driven** and **keyword-driven** testing, and **continuous integration** support.

