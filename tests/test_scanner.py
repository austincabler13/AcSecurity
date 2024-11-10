from src.scanner import AcSecurity
import pylint

scanner = AcSecurity('C:/Users/Cable/Documents/GitHub/CGS/AcSecurity/tests')
vulnerabilities = scanner.scan()

## Copyright (C) 2024  Austin Cabler
