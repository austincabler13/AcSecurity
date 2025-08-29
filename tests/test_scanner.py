from src.scanner import AcSecurity
from pathlib import Path
import pylint  # ensure dependency is installed

# Use the directory containing this test file so the tests run on any machine
tests_dir = Path(__file__).resolve().parent
scanner = AcSecurity(str(tests_dir))
vulnerabilities = scanner.scan()

## Copyright (C) 2024  Austin Cabler
