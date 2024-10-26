import src
from src.scanner import AcSecurity

scanner = src('C:/Users/Cable/Documents/GitHub/CGS/AcSecurity/tests')
vulnerabilities = scanner.scan()
