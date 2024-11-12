import os
import subprocess
import argparse
import logging
import shutil
import json
import openai  # Make sure to install this package
import uuid

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AcSecurity:
    """Scanner for identifying security vulnerabilities and code quality issues in an application."""

    VERSION = "1.2.3"

    def __init__(self, app_path):
        self.app_path = app_path
        self.vulnerabilities = []
        self.backup_path = os.path.join(os.path.dirname(app_path), 'backups')

    def scan(self):
        """Conducts a full scan for common vulnerabilities, dependency issues, and code quality."""
        logging.info("Starting scan...")
        self.check_for_common_vulnerabilities()
        self.check_for_dependency_vulnerabilities()
        self.check_code_quality()
        self.write_issues_to_file()
        logging.info("Scan completed.")
        return bool(self.vulnerabilities)

    def check_for_common_vulnerabilities(self):
        """Check files in the app path for hardcoded secrets or passwords."""
        logging.info("Checking for common vulnerabilities...")
        for root, _, files in os.walk(self.app_path):
            if 'venv' in root:
                continue
            for file in files:
                if file.endswith(('.py', '.js', '.java', '.html', '.c', '.cs', '.cpp', '.lua')):
                    self.check_file(os.path.join(root, file))

    def check_file(self, file_path):
        """Check a specific file for hardcoded sensitive information."""
        logging.info(f"Checking file: {file_path}")
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            if 'secret' in content or 'password' in content:
                self.vulnerabilities.append(f'Potential hardcoded secret found in: {file_path}')

    def check_for_dependency_vulnerabilities(self):
        """Run pip-audit to check for dependency vulnerabilities."""
        logging.info("Checking for dependency vulnerabilities...")
        try:
            result = subprocess.run(['pip-audit'], capture_output=True, text=True, cwd=self.app_path, check=True)
            if result.stdout:
                self.vulnerabilities.append(f"Dependency vulnerabilities found:\n{result.stdout.strip()}")
            else:
                self.vulnerabilities.append("No dependency vulnerabilities found.")
        except Exception as e:
            self.vulnerabilities.append(f"Error checking dependencies: {e}")

    def check_code_quality(self):
        """Run pylint to check code quality issues."""
        logging.info("Checking code quality...")
        result = subprocess.run(
            ['pylint', '--rcfile=.pylintrc', self.app_path],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            self.vulnerabilities.append("No code quality issues found.")
        elif result.returncode in (28,):  # Adjust as needed for specific exit codes
            self.vulnerabilities.append(f"Code quality issues (non-fatal):\n{result.stdout.strip()}")
        else:
            self.vulnerabilities.append(f"Code quality issues found:\n{result.stdout.strip()}")

    def write_issues_to_file(self):
        """Write the found vulnerabilities and issues to issues.txt file with suggestions for fixing."""
        logging.info("Writing issues to file...")
        with open('issues.txt', 'w', encoding='utf-8') as f:
            if self.vulnerabilities:
                f.write("Vulnerabilities found:\n")
                for vulnerability in self.vulnerabilities:
                    f.write(f"{vulnerability}\n")
                    if 'hardcoded secret' in vulnerability:
                        f.write("Suggestion: Remove any hardcoded secrets or passwords from your code.\n")
                    elif 'Dependency vulnerabilities' in vulnerability:
                        f.write("Suggestion: Run 'pip install --upgrade [package]' to update vulnerable packages.\n")
                    elif 'Code quality issues' in vulnerability:
                        f.write("Suggestion: Review the reported issues and improve your code accordingly.\n")
            else:
                f.write("No vulnerabilities found.\n")

    def generate_report(self):
        """Generate a JSON report of the vulnerabilities found with better error messages."""
        report = {
            "version": self.VERSION,
            "issues": [],
        }
        
        for issue in self.vulnerabilities:
            issue_details = {"message": issue}
            if 'hardcoded secret' in issue:
                issue_details['suggestion'] = "Remove any hardcoded secrets or passwords from your code."
            elif 'Dependency vulnerabilities' in issue:
                issue_details['suggestion'] = "Run 'pip install --upgrade [package]' to update vulnerable packages."
            elif 'Code quality issues' in issue:
                issue_details['suggestion'] = "Review the reported issues and improve your code accordingly."
            report["issues"].append(issue_details)

        with open('report.json', 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=4)
        logging.info("Report generated: report.json")

    def fix_code_with_ai(self, code_snippet):
        """Use ChatGPT to suggest fixes for the provided code snippet."""
        openai.api_key = "YOUR_API_KEY"  # Add your OpenAI API key

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": f"Here is a code snippet with issues:\n{code_snippet}\nPlease suggest fixes."
                }
            ]
        )

        return response['choices'][0]['message']['content']

    def interact_with_user(self):
        """Allow user to interact and decide whether to fix issues or not."""
        for issue in self.vulnerabilities:
            print(issue)
            user_choice = input("Would you like to get AI suggestions for this issue? (yes/no): ")
            if user_choice.lower() == 'yes':
                code_snippet = input("Please provide the code snippet to fix:\n")
                ai_suggestion = self.fix_code_with_ai(code_snippet)
                print(f"AI Suggestion:\n{ai_suggestion}")
                apply_fix = input("Would you like to apply this fix? (yes/no): ")
                if apply_fix.lower() == 'yes':
                    pass  # Implement applying fix if necessary
                else:
                    print("Fix not applied.")
            else:
                print("No AI suggestions requested.")

    def backup_code(self):
        """Backup the application code."""
        if not os.path.exists(self.backup_path):
            os.makedirs(self.backup_path)

        for root, _, files in os.walk(self.app_path):
            for file in files:
                file_path = os.path.join(root, file)
                backup_file_path = os.path.join(self.backup_path, f"{uuid.uuid4()}_{file}")
                shutil.copy(file_path, backup_file_path)

        logging.info(f"Backup completed. All files are backed up to: {self.backup_path}")

def main():
    parser = argparse.ArgumentParser(description='AcSecurity - Scan applications for security vulnerabilities.')
    parser.add_argument('--version', action='version', version=f'AcSecurity {AcSecurity.VERSION}')
    parser.add_argument('app_path', nargs='?', type=str, help='Path to the application to scan')
    parser.add_argument('--backup', action='store_true', help='Create a backup of the application code')
    parser.add_argument('--report', action='store_true', help='Generate a report of the vulnerabilities found')

    args = parser.parse_args()

    if args.app_path is None and not args.version:
        print("Error: app_path is required to run a scan.")
        parser.print_help()
        return

    if args.app_path:
        scanner = AcSecurity(args.app_path)
        
        if args.backup:
            scanner.backup_code()

        scanner.scan()
        print("Scan completed. Check 'issues.txt' for details.")
        
        if args.report:
            scanner.generate_report()

        scanner.interact_with_user()

if __name__ == "__main__":
    main()
## Copyright (C) 2024  Austin Cabler
