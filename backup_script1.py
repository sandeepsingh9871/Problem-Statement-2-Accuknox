import os
import shutil
import boto3
import datetime
import logging

# Configure logging
logging.basicConfig(filename='backup_report.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s:%(message)s')

def backup_directory_to_s3(directory_path, bucket_name, s3_prefix):
    """
    Back up a specified directory to an S3 bucket.

    Args:
    directory_path (str): The local directory to back up.
    bucket_name (str): The S3 bucket where the backup will be stored.
    s3_prefix (str): The S3 prefix (folder path in the bucket) to store the backup.
    """
    try:
        # Ensure the directory exists
        if not os.path.isdir(directory_path):
            logging.error(f"The directory {directory_path} does not exist.")
            print(f"The directory {directory_path} does not exist.")
            return
        
        # Create a zip file of the directory
        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        backup_filename = f"{os.path.basename(directory_path)}_{timestamp}.zip"
        shutil.make_archive(backup_filename, 'zip', directory_path)
        logging.info(f"Successfully created backup archive: {backup_filename}.zip")
        print(f"Successfully created backup archive: {backup_filename}.zip")
        
        # Upload the zip file to S3
        s3_client = boto3.client('s3')
        s3_backup_path = os.path.join(s3_prefix, backup_filename + '.zip')
        s3_client.upload_file(backup_filename + '.zip', bucket_name, s3_backup_path)
        logging.info(f"Successfully uploaded {backup_filename}.zip to s3://{bucket_name}/{s3_backup_path}")
        print(f"Successfully uploaded {backup_filename}.zip to s3://{bucket_name}/{s3_backup_path}")

        # Clean up the local zip file
        os.remove(backup_filename + '.zip')
        logging.info(f"Successfully removed local backup file: {backup_filename}.zip")
        print(f"Successfully removed local backup file: {backup_filename}.zip")
        
        print(f"Backup completed successfully. Report is logged in backup_report.log.")
    except Exception as e:
        logging.error(f"Backup failed: {e}")
        print(f"Backup failed: {e}. Check backup_report.log for details.")

if __name__ == "__main__":
    # Replace these with your actual values
    directory_to_backup = r'C:\Users\sande\OneDrive\Desktop\trial1'  # The local directory to back up
    s3_bucket_name = 'your-s3-bucket-name'                          # Your S3 bucket name
    s3_backup_prefix = 'backups/'                                   # Prefix in the S3 bucket

    backup_directory_to_s3(directory_to_backup, s3_bucket_name, s3_backup_prefix)
