# Important: This script creates the module and makes it work without it this will not work.🔴 DO NOT DELETE.

import os
import subprocess
import argparse

class AcSecurity:
    """Scanner for identifying security vulnerabilities and code quality issues in an application."""

    VERSION = "0.4.13"  ## Without this the --version flag will not work.

    def __init__(self, app_path):
        self.app_path = app_path
        self.vulnerabilities = []

    def scan(self):
        """Conducts a full scan for common vulnerabilities, dependency issues, and code quality."""
        self.check_for_common_vulnerabilities()
        self.check_for_dependency_vulnerabilities()
        self.check_code_quality()
        self.write_issues_to_file()
        return bool(self.vulnerabilities)

    def check_for_common_vulnerabilities(self):
        """Check files in the app path for hardcoded secrets or passwords."""
        for root, _, files in os.walk(self.app_path):
            if 'venv' in root:
                continue
            for file in files:
                if file.endswith(('.py', '.js', '.java', '.html', '.c', '.cs', '.cpp', '.lua')):
                    self.check_file(os.path.join(root, file))

    def check_file(self, file_path):
        """Check a specific file for hardcoded sensitive information."""
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            if 'secret' in content or 'password' in content:
                self.vulnerabilities.append(f'Potential hardcoded secret found in: {file_path}')

    def check_for_dependency_vulnerabilities(self):
        """Run pip-audit to check for dependency vulnerabilities."""
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
        try:
            result = subprocess.run(['pylint', self.app_path], capture_output=True, text=True, check=True)
            if result.stdout:
                self.vulnerabilities.append(f"Code quality issues found:\n{result.stdout.strip()}")
            else:
                self.vulnerabilities.append("No code quality issues found.")
        except Exception as e:
            self.vulnerabilities.append(f"Error checking code quality: {e}")

    def write_issues_to_file(self):
        """Write the found vulnerabilities and issues to issues.txt file."""
        with open('issues.txt', 'w', encoding='utf-8') as f:
            if self.vulnerabilities:
                f.write("Vulnerabilities found:\n")
                for vulnerability in self.vulnerabilities:
                    f.write(f"{vulnerability}\n")
            else:
                f.write("No vulnerabilities found.\n")

def main():
    parser = argparse.ArgumentParser(description='AcSecurity - Scan applications for security vulnerabilities.')
    parser.add_argument('--version', action='version', version=f'AcSecurity {AcSecurity.VERSION}')
    parser.add_argument('app_path', nargs='?', type=str, help='Path to the application to scan')

    args = parser.parse_args()

    if args.app_path is None and not args.version:
        print("Error: app_path is required to run a scan.")
        parser.print_help()
        return

    if args.app_path:
        # Create the scanner instance with the app_path argument
        scanner = AcSecurity(args.app_path)
        scanner.scan()
        print("Scan completed. Check 'issues.txt' for details.")

if __name__ == "__main__":
    main()
