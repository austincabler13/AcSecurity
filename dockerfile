FROM python:3.12.3

# Set the working directory
WORKDIR /app

# Copy the scanner script and test script
COPY scanner.py .
COPY test_scanner.py .

# Install pip-audit and pylint
RUN pip install pip-audit pylint

# Command to run when the container starts
CMD ["python3", "test_scanner.py"]
