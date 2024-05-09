
# John D Cyber's AWS EC2 Instance Counter

## Overview
This Python script enumerates all Amazon Web Services (AWS) EC2 instances across all regions associated with a given AWS account and writes the total count to a CSV file. This is useful for inventory management and monitoring of AWS resources.

## Features
- Enumerates EC2 instances across all AWS regions.
- Logs the total number of instances per region.
- Outputs the total number of instances to a CSV file named `ec2_counts_{account_id}.csv`.

## Requirements
- Python 3.x
- Boto3 (AWS SDK for Python)
- AWS credentials configured (via environment variables, AWS credentials file, or IAM role)

## Setup and Installation
1. **Install Python 3.x**: Ensure Python 3.x is installed on your system.

2. **Install Boto3**:
   ```bash
   pip install boto3
   ```

3. **Configure AWS Credentials**: Make sure your AWS credentials are configured. This can be done in several ways:
   - Configuring environment variables `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`
   - Using an AWS credentials file typically located at `~/.aws/credentials`
   - Using an IAM role with the necessary permissions if running on an AWS service (e.g., EC2, Lambda)

## Usage
Run the script using Python:
```bash
python johndcyber_ec2_instance_counter.py
```

## Output
The script will create a CSV file named `ec2_counts_{account_id}.csv` in the working directory, containing the account ID and the total number of EC2 instances.

## Logging
The script uses Python's built-in `logging` module to log informational and error messages. The logging level is set to INFO.

## Error Handling
The script includes error handling to catch and log exceptions that may occur during the execution, particularly when interacting with the AWS SDK.

## License
Specify the license under which the code is made available.
