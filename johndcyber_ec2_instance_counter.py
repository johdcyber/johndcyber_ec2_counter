import boto3
import csv
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def get_ec2_count(region):
    try:
        # Initialize Boto3 EC2 client for the specified region
        ec2_client = boto3.client('ec2', region_name=region)

        # Retrieve all EC2 instances
        response = ec2_client.describe_instances()

        # Count the number of EC2 instances
        total_instances = sum(len(reservations['Instances']) for reservations in response['Reservations'])

        logging.info(f"Total EC2 instances in {region}: {total_instances}")
        return total_instances
    except Exception as e:
        logging.error(f"Error occurred while retrieving EC2 instances in {region}: {str(e)}")
        return 0


def write_to_csv(account_id, total_instances):
    csv_file_name = f"ec2_counts_{account_id}.csv"
    with open(csv_file_name, mode='w', newline='') as csv_file:
        fieldnames = ['Account ID', 'Total EC2 Instances']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'Account ID': account_id, 'Total EC2 Instances': total_instances})
    return csv_file_name


if __name__ == "__main__":
    try:
        # Initialize Boto3 STS client to get account ID
        sts_client = boto3.client('sts')
        account_id = sts_client.get_caller_identity()["Account"]

        # Initialize Boto3 EC2 client
        ec2_client = boto3.client('ec2')

        # Get all AWS regions
        regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]

        # Process EC2 instances in each region
        total_instances = 0
        for region in regions:
            total_instances += get_ec2_count(region)

        # Output the result to CSV
        csv_file_name = write_to_csv(account_id, total_instances)

        logging.info(f"Results have been written to {csv_file_name}")
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
