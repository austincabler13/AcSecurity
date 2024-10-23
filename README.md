# AcSecurity

AcSecurity is a Python module designed to scan applications for common security vulnerabilities. It checks for hardcoded secrets, dependency vulnerabilities, and code quality issues.

## Table of Contents

- [AcSecurity](#acsecurity)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Example](#example)
  - [Features](#features)
  - [Contributing](#contributing)
  - [License](#license)

## Installation

You can install AcSecurity using `pip`. Open your terminal and run:

```bash
pip install AcSecurity
```

Ensure you have Python 3.12.0 and `pip` installed on your machine.

## Usage

After installing the module, you can use it to scan your application directory for vulnerabilities. Here’s how to do it:

1. Open your terminal or command prompt.
2. Run the scanner using the command below, replacing `/path/to/your/application` with the path to your application directory:

   ```bash
   acsecurity /path/to/your/application
   ```

3. The scanner will output any vulnerabilities found in your application.

### Example

```bash
acsecurity /home/user/my_project
```

## Features

- **Common Vulnerability Checks**: Scans for hardcoded secrets such as passwords or API keys in your code.
- **Dependency Vulnerability Checks**: Uses `pip-audit` to identify known vulnerabilities in your installed Python packages.
- **Code Quality Checks**: Uses `pylint` to identify code quality issues and ensure your code adheres to best practices.
- **Output**: All findings are written to `issues.txt` in the current directory.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new feature branch.
3. Make your changes.
4. Commit your changes with a clear message.
5. Push your branch to your fork.
6. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


[![Upload Python Package](https://github.com/austincabler13/AcSecurity/actions/workflows/python-publish.yml/badge.svg)](https://github.com/austincabler13/AcSecurity/actions/workflows/python-publish.yml)