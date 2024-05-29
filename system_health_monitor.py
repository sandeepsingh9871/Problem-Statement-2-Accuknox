import psutil
import logging
from datetime import datetime
import time

# Configure logging
logging.basicConfig(filename='system_health.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Define thresholds
CPU_THRESHOLD = 80.0
MEMORY_THRESHOLD = 80.0
DISK_THRESHOLD = 90.0

def log_alert(message):
    logging.info(message)
    print(message)

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        log_alert(f"ALERT: High CPU usage detected: {cpu_usage}%")

def check_memory_usage():
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    if memory_usage > MEMORY_THRESHOLD:
        log_alert(f"ALERT: High memory usage detected: {memory_usage}%")

def check_disk_usage():
    disk_info = psutil.disk_usage('/')
    disk_usage = disk_info.percent
    if disk_usage > DISK_THRESHOLD:
        log_alert(f"ALERT: High disk usage detected: {disk_usage}%")

def check_running_processes():
    # Example: log the number of running processes
    process_count = len(psutil.pids())
    log_alert(f"INFO: Number of running processes: {process_count}")

def monitor_system_health():
    while True:
        check_cpu_usage()
        check_memory_usage()
        check_disk_usage()
        check_running_processes()
        # Sleep for a specified interval before the next check (e.g., 60 seconds)
        time.sleep(60)

if __name__ == "__main__":
    monitor_system_health()
