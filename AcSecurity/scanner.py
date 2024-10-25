import os
import subprocess
import argparse

class AcSecurity:
    """Scanner for checking security vulnerabilities in specified applications."""

    def __init__(self, app_path):
        self.app_path = app_path
        self.vulnerabilities = []

    def scan(self):
        """Performs a complete scan for vulnerabilities and code quality issues."""
        self.check_for_common_vulnerabilities()
        self.check_for_dependency_vulnerabilities()
        self.check_code_quality()
        self.write_issues_to_file()  # Write issues to a file
        return bool(self.vulnerabilities)

    def check_for_common_vulnerabilities(self):
        """Scans files for common hardcoded secrets."""
        for root, _, files in os.walk(self.app_path):
            if 'venv' in root:  # Skip venv directory
                continue
            for file in files:
                if file.endswith(('.py', '.js', '.java', '.html', '.c', '.cs', '.cpp', '.lua')):
                    self.check_file(os.path.join(root, file))

    def check_file(self, file_path):
        """Checks a file for hardcoded secrets like 'password' or 'secret'."""
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            if 'secret' in content or 'password' in content:
                self.vulnerabilities.append(f'Potential hardcoded secret found in: {file_path}')

    def check_for_dependency_vulnerabilities(self):
        """Runs pip-audit to check for dependency vulnerabilities."""
        try:
            result = subprocess.run(['pip-audit'], capture_output=True, text=True, cwd=self.app_path)
            if result.stdout:
                self.vulnerabilities.append(f"Dependency vulnerabilities found:\n{result.stdout.strip()}")
            else:
                self.vulnerabilities.append("No dependency vulnerabilities found.")
        except subprocess.CalledProcessError as e:
            self.vulnerabilities.append(f"Error checking dependencies: {e}")

    def check_code_quality(self):
        """Uses pylint to check code quality issues in the specified application path."""
        try:
            result = subprocess.run(['pylint', self.app_path], capture_output=True, text=True)
            if result.stdout:
                self.vulnerabilities.append(f"Code quality issues found:\n{result.stdout.strip()}")
            else:
                self.vulnerabilities.append("No code quality issues found.")
        except subprocess.CalledProcessError as e:
            self.vulnerabilities.append(f"Error checking code quality: {e}")

    def write_issues_to_file(self):
        """Writes all identified vulnerabilities and issues to 'issues.txt'."""
        with open('issues.txt', 'w', encoding='utf-8') as f:
            if self.vulnerabilities:
                f.write("Vulnerabilities found:\n")
                for vulnerability in self.vulnerabilities:
                    f.write(f"{vulnerability}\n")
            else:
                f.write("No vulnerabilities found.\n")

def main():
    """Parses command-line arguments and initiates a security scan."""
    parser = argparse.ArgumentParser(description='Scan applications for common security vulnerabilities.')
    parser.add_argument('app_path', type=str, help='Path to the application to scan')
    args = parser.parse_args()

    # Create the scanner instance with the app_path argument
    scanner = AcSecurity(args.app_path)
    vulnerabilities_found = scanner.scan()
    print("Scan completed. Check 'issues.txt' for details.")
    if vulnerabilities_found:
        for v in scanner.vulnerabilities:
            print(v)

if __name__ == "__main__":
    main()
