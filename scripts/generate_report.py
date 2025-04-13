import os
import allure
from datetime import datetime
from typing import Dict
from allure_commons.types import AttachmentType
from jinja2 import Template

def generate_report_with_allure(test_results: Dict, output_dir: str):
    """
    Generate a test report using Allure.

    :param test_results: Dictionary containing test results.
    :param output_dir: Directory to save the Allure report.
    """
    allure_dir = os.path.join(output_dir, "allure-results")
    os.makedirs(allure_dir, exist_ok=True)

    for test_name, result in test_results.items():
        with allure.step(f"Test: {test_name}"):
            if result["status"] == "passed":
                allure.attach(result["details"], name="Details", attachment_type=AttachmentType.TEXT)
            elif result["status"] == "failed":
                allure.attach(result["details"], name="Error", attachment_type=AttachmentType.TEXT)
                allure.attach(result["screenshot"], name="Screenshot", attachment_type=AttachmentType.PNG)

    os.system(f"allure generate {allure_dir} -o {output_dir}/allure-report --clean")

def generate_report_with_extent(test_results: Dict, output_file: str):
    """
    Generate a test report using ExtentReports.

    :param test_results: Dictionary containing test results.
    :param output_file: File path to save the Extent report.
    """

    template = Template("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Extent Report</title>
    </head>
    <body>
        <h1>Test Report</h1>
        <table border="1">
            <tr>
                <th>Test Name</th>
                <th>Status</th>
                <th>Details</th>
            </tr>
            {% for test_name, result in test_results.items() %}
            <tr>
                <td>{{ test_name }}</td>
                <td>{{ result.status }}</td>
                <td>{{ result.details }}</td>
            </tr>
            {% endfor %}
        </table>
    </body>
    </html>
    """)

    report_content = template.render(test_results=test_results)
    with open(output_file, "w") as report_file:
        report_file.write(report_content)

# Example usage
if __name__ == "__main__":
    test_results = {
        "test_case_1": {"status": "passed", "details": "Test passed successfully."},
        "test_case_2": {"status": "failed", "details": "Assertion error occurred.", "screenshot": "path/to/screenshot.png"}
    }
    output_dir = "./reports"
    generate_report_with_allure(test_results, output_dir)
    generate_report_with_extent(test_results, os.path.join(output_dir, "extent_report.html"))