import argparse
from AcSecurity.scanner import AcSecurity

def main():
    parser = argparse.ArgumentParser(description='Scan applications for common security vulnerabilities.')
    parser.add_argument('app_path', type=str, help='Path to the application to scan')
    args = parser.parse_args()

    scanner = AcSecurity(args.app_path)
    vulnerabilities = scanner.scan()

    if vulnerabilities:
        print("Vulnerabilities found:")
        for vulnerability in vulnerabilities:
            print(vulnerability)
    else:
        print("No vulnerabilities found.")

if __name__ == "__main__":
    main()
