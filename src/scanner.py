# Important: This script creates the module and makes it work without it this will not work.🔴 DO NOT DELETE.

import os
import subprocess
import argparse
import logging
import shutil
import json

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AcSecurity:
    """Scanner for identifying security vulnerabilities and code quality issues in an application."""

    VERSION = "1.2.0"  # Without this the --version flag will not work.

    def __init__(self, app_path):
        self.app_path = app_path
        self.vulnerabilities = []
        self.backup_path = os.path.join(os.path.dirname(app_path), 'backups')  # Backup directory

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
        logging.info("Writing issues to file...")
        with open('issues.txt', 'w', encoding='utf-8') as f:
            if self.vulnerabilities:
                f.write("Vulnerabilities found:\n")
                for vulnerability in self.vulnerabilities:
                    f.write(f"{vulnerability}\n")
            else:
                f.write("No vulnerabilities found.\n")

    def backup_code(self):
        """Backup the application code."""
        if not os.path.exists(self.backup_path):
            os.makedirs(self.backup_path)

        # Copy files to the backup directory
        for root, dirs, files in os.walk(self.app_path):
            for file in files:
                file_path = os.path.join(root, file)
                shutil.copy(file_path, self.backup_path)

        logging.info(f"Backup completed. All files are backed up to: {self.backup_path}")

    def generate_report(self):
        """Generate a JSON report of the vulnerabilities found."""
        report = {
            "version": self.VERSION,
            "issues": self.vulnerabilities
        }
        with open('report.json', 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=4)
        logging.info("Report generated: report.json")

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
        # Create the scanner instance with the app_path argument
        scanner = AcSecurity(args.app_path)
        
        if args.backup:
            scanner.backup_code()

        scanner.scan()
        print("Scan completed. Check 'issues.txt' for details.")
        
        if args.report:
            scanner.generate_report()

if __name__ == "__main__":
    main()
