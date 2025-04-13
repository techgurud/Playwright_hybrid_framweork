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
- 🔁 **API Testing** with `requests` and schema validation
- 📊 **Allure & HTML Reports**
- 🗃️ **Data-driven** (Excel, JSON, YAML)
- 🧪 **Pytest** test runner with plugins
- 🚀 **CI/CD Ready** (Jenkins, GitHub Actions)
- 🔄 **Retry + Wait + Logger utilities**
- 🔧 **Environment Management**
- 📬 **Email + Slack Notifications**
- 🧩 Easy to extend and plug into enterprise pipelines

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
project_root/
├── config/                             # Configuration management
│   ├── config.yaml                   # App/environment settings like URLs, credentials
│   ├── environment_manager.py       # Manages environment switching (dev, QA, prod)
│   └── config_reader.py             # Reads and provides access to config values
│
├── drivers/                            # WebDriver or browser setup
│   └── browser_manager.py           # Handles browser initialization and configuration
│
├── utils/                               # Utility and helper functions
│   ├── logger.py                     # Logging (console and file)
│   ├── wait_utils.py                # Explicit and smart wait wrappers
│   ├── element_utils.py             # Click, input, visibility checks etc.
│   ├── assertion_utils.py           # Hard and soft assertion wrappers
│   ├── date_time_utils.py           # Time and date manipulation utilities
│   ├── random_data_generator.py     # Fake/test data generation
│   ├── file_utils.py                # File operations (read/write JSON, Excel, etc.)
│   ├── screenshot_utils.py          # Capture screenshots (failures/debug)
│   ├── exception_handler.py         # Centralized exception capture and logging
│   ├── retry_utility.py             # Retry logic for flaky scenarios
│   ├── validation_utils.py          # Common validators (email format, range, etc.)
│   └── service_locator.py           # Dependency injector to decouple logic
│
├── data/                                # Test data sources
│   ├── test_data.json               # Static JSON-based test data
│   ├── excel_data.xlsx              # Structured data in Excel
│   ├── data_reader.py              # Reader class for JSON/Excel
│   └── json_yaml_parser.py         # Common parser for JSON/YAML files
│
├── api_utils/                            # API testing components
│   ├── api_client.py               # Base class for REST calls (GET/POST/PUT/DELETE)
│   ├── api_validator.py            # Schema and response assertion methods
│   └── mock_server_helper.py       # Stub/mocking support for API testing
│
├── db_utils/                             # Database access layer
│   ├── sql_connector.py            # SQL (MySQL, Postgres, etc.) DB connector
│   └── nosql_connector.py          # NoSQL (MongoDB, etc.) DB connector
│
├── reports/                             # Reporting and result sharing
│   ├── html_reporter.py            # Custom HTML reporting logic
│   ├── result_parser.py            # Parses test results to readable formats
│   ├── email_reporter.py           # Emails reports and test summary
│   └── allure_report_config.xml    # Allure integration config file
│
├── ci_cd/                               # CI/CD pipeline integration
│   ├── test_runner.py              # Main orchestrator to run test suites
│   ├── ci_trigger.py               # Integrate with Jenkins/GitLab etc.
│   └── notifier.py                 # Notify via Slack/Teams/email
│
├── tests/                                # Actual test cases
│   ├── test_login.py               # Test for login functionality
│   └── test_checkout.py            # Test for checkout flow
│
├── pages/                                # Page Object Model (POM)
│   ├── login_page.py              # Login page actions and locators
│   ├── dashboard_page.py          # Dashboard page POM
│   └── base_page.py               # Generic functions for all pages
│
├── resources/                            # Static files like locators
│   └── locators.yaml              # XPath/CSS selectors for POM use
│
├── requirements.txt                     # Python package dependencies
└── README.md                            # Project documentation and usage
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
python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```

Install required dependencies from `requirements.txt`:

```bash
pip3 install -r requirements.txt
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

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


---

## Conclusion

This hybrid test automation framework is designed for scalability and flexibility, leveraging **Playwright** for automation, **Pytest** for testing, **LambdaTest** for cloud grid testing, and **Oracle DB** for database validation. It follows modern best practices like the **Page Object Model** (POM), **data-driven** and **keyword-driven** testing, and **continuous integration** support.

