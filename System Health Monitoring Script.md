# Problem-Statement-2-Accuknox

1. System Health Monitoring Script: Develop a script that monitors the health of a Linux system. It should check CPU usage, memory usage, disk space, and running processes. If any ofthese metrics exceed predefined thresholds (e.g., CPU usage > 80%), the script should send an alert to the console or a log file.

Explanation:
1. Logging Configuration: The script uses Python's logging module to log alerts to both the console and a log file (system_health.log).

2. Thresholds: The thresholds for CPU, memory, and disk usage are set at 80%, 80%, and 90%, respectively. You can adjust these as needed.

3. Functions:
    log_alert: Logs a message to the log file and prints it to the console.
    check_cpu_usage: Checks the CPU usage and logs an alert if it exceeds the threshold.
    check_memory_usage: Checks the memory usage and logs an alert if it exceeds the threshold.
    check_disk_usage: Checks the disk usage and logs an alert if it exceeds the threshold.
    check_running_processes: Logs the number of running processes (this is a simple example, you can add more detailed process monitoring if needed).
    Monitor Loop: The monitor_system_health function continuously monitors the system's health, sleeping for 60 seconds between checks. You can adjust the sleep interval as needed.

Running the Script:
Save the script to a file, e.g., system_health_monitor.py, and run it using Python.
