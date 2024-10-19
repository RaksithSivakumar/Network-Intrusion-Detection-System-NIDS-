import csv
import os
import time

def log_intrusion(alert_type, src_ip, dst_ip, src_port=None, dst_port=None):
    log_folder = "logs"
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)

    log_file = os.path.join(log_folder, "intrusion_logs.csv")

    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    # If the file doesn't exist, create it and write the header
    if not os.path.exists(log_file):
        with open(log_file, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "Alert Type", "Source IP", "Destination IP", "Source Port", "Destination Port"])

    # Append the intrusion details
    with open(log_file, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, alert_type, src_ip, dst_ip, src_port or "", dst_port or ""])

    print(f"[ALERT] {alert_type}: {src_ip} -> {dst_ip}")
