
# 🔒AcSecurity

AcSecurity is a Python module designed to scan applications for common security vulnerabilities. It checks for hardcoded secrets, dependency vulnerabilities, and code quality issues.

## 🤷‍♂️Table of Contents

- [🔒AcSecurity](#acsecurity)
  - [🤷‍♂️Table of Contents](#️table-of-contents)
  - [🆘Installation](#installation)
  - [🔨Usage](#usage)
    - [🔥Vulnerabilitie Scan](#vulnerabilitie-scan)
    - [🔨Command Line Options](#command-line-options)
    - [🗒️Versions](#️versions)
    - [🆘Help](#help)
    - [👍Backups](#backups)
  - [🔒Reports](#reports)
  - [😎Features](#features)
  - [💖Contributing](#contributing)
  - [⚖️License](#️license)
  - [🔨Founder](#founder)
    - [🧑‍💻About the Founder](#about-the-founder)
    - [🗒️Acknowledgments](#️acknowledgments)
  - [🐍Python Package](#python-package)

## 🆘Installation

You can install AcSecurity using `pip`. Open your terminal and run:

```bash
pip install AcSecurity
```

Ensure you have Python 3.12.0 and `pip` installed on your machine.

## 🔨Usage

### 🔥Vulnerabilitie Scan

```bash
  acsecurity /path/to/your/application
```

- Checks for Vulnerabilities in your Code

### 🔨Command Line Options

- version: Displays the version of AcSecurity.
- backup: Creates a backup of the application code.
- report: Generates a JSON report of the vulnerabilities found.

### 🗒️Versions

```bash
acsecurity --version
```

- Checks what Version you have

### 🆘Help

```bash
acsecurity --help
```

- See what you can do with This Module

### 👍Backups

```bash
python scanner.py /path/to/your/application --backup
```

- Creates a backup of your Code if you Deleted something or Messed something up

## 🔒Reports

```bash
python scanner.py /path/to/your/application --report
```

- Creates a Report/Overview of your Issues/Vulnerabilities in your project

## 😎Features

- **Common Vulnerability Checks:** Scans for hardcoded secrets such as passwords or API keys in your code.
- **Dependency Vulnerability Checks:** Uses `pip-audit` to identify known vulnerabilities in your installed Python packages.
- **Code Quality Checks:** Uses `pylint` to identify code quality issues and ensure your code adheres to best practices.
- **Output:** All findings are written to `issues.txt` in the current directory.
- **Version Info:** Use `--version` to view the version you have.
- **Help Info:** Use `--help` to get assistance and see what you can do.
- **Backups** Use `--backup` at the end of your command to allow a backup of your code
- **Reports:** Use `--report` to get a report/overview of your vulnerabilities

## 💖Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new feature branch.
3. Make your changes.
4. Commit your changes with a clear message.
5. Push your branch to your fork.
6. Submit a pull request.

## ⚖️License

This project is licensed under the GNU License. See the [LICENSE](LICENSE) file for details.

## 🔨Founder

**Austin Cabler**  
[GitHub Profile](https://github.com/austincabler13)  
Contact: [austin_cabler@icloud.com](mailto:austin_cabler@icloud.com)

### 🧑‍💻About the Founder

I am the founder of AcSecurity. As the sole developer on this project, I created AcSecurity to simplify security for users, as tools like Snyk can be challenging to use. I will always strive to make AcSecurity user-friendly.

### 🗒️Acknowledgments

If you would like to contribute to this project, please contact me or go to [Contribute](/CONTRIBUTING.md) . As a solo developer, I would love to receive help from individuals interested in my project.

## 📛Badges

- [![Snyk Security Analysis](https://github.com/austincabler13/AcSecurity/actions/workflows/snyk-security.yml/badge.svg)](https://github.com/austincabler13/AcSecurity/actions/workflows/snyk-security.yml)
- [![Python Package](https://github.com/austincabler13/AcSecurity/actions/workflows/python-publish.yml/badge.svg)](https://github.com/austincabler13/AcSecurity/actions/workflows/python-publish.yml)


Copyright (C) 2024  Austin Cabler
