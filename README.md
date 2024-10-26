# AcSecurity

AcSecurity is a Python module designed to scan applications for common security vulnerabilities. It checks for hardcoded secrets, dependency vulnerabilities, and code quality issues.

## Table of Contents

- [AcSecurity](#acsecurity)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Example](#example)
  - [Version View and Help View](#version-view-and-help-view)
  - [Features](#features)
  - [Contributing](#contributing)
  - [License](#license)
- [**Founder**](#founder)
  - [Austin Cabler](#austin-cabler)
  - [**About the Founder**](#about-the-founder)
  - [**Acknowledgments**](#acknowledgments)
  - [Python Package](#python-package)
  - [Note](#note)

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

## Version View and Help View

```bash
acsecurity --version
acsecurity --help
```

## Features

- **Common Vulnerability Checks**: Scans for hardcoded secrets such as passwords or API keys in your code.
- **Dependency Vulnerability Checks**: Uses `pip-audit` to identify known vulnerabilities in your installed Python packages.
- **Code Quality Checks**: Uses `pylint` to identify code quality issues and ensure your code adheres to best practices.
- **Output**: All findings are written to `issues.txt` in the current directory.
- **Version:** you can know use ```--version``` and view the version you have
- **Help** you can know use ```--help``` and get Help and see what you can do.

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

**Founder**
================

[Austin Cabler](https://github.com/austincabler13)
----------------

Contact: [austin_cabler@icloud.com](mailto:austin_cabler@icloud.com)

**About the Founder**
--------------------

I am the Founder of AcSecurity, what I do for AcSecurity is create the Project I have edited, Created and Made AcSecurity has the only developer/person on the team I created AcSecurity to make Securtiy easy for people has Snyk is hard to use but has a developer and Founder I will try to always make AcSecurity easy for people.

**Acknowledgments**
-----------------

If you would like to help in this project please contact me and let me know has a solo developer I would love to get help from people thats into my Project.

## Python Package
[![Upload Python Package](https://github.com/austincabler13/AcSecurity/actions/workflows/python-publish.yml/badge.svg)](https://github.com/austincabler13/AcSecurity/actions/workflows/python-publish.yml)

## Note
- Please Do not copy rewrite, or sell this without my permission
