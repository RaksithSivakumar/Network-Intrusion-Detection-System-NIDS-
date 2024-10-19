import os
import time
import streamlit as st

# Title of the app
st.title("Network Intrusion Detection System - Status")

# Log file to store last active timestamp
log_file = "app_status.log"

# Write the current timestamp to the log file (indicating the app is active)
current_time = time.strftime('%Y-%m-%d %H:%M:%S')
with open(log_file, "w") as f:
    f.write(f"App last active: {current_time}\n")

# Display current status in the app
st.write(f"### App Status: Running")
st.write(f"Last Heartbeat: {current_time}")

# Check if log file exists and display its content
if os.path.exists(log_file):
    with open(log_file, "r") as f:
        last_active = f.read()
        st.write("#### Last Active Log Entry:")
        st.write(last_active)
else:
    st.write("No activity logged yet.")

# Optional: Add your NIDS logic below (like reading and showing intrusion logs)
log_file_path = "logs/intrusion_logs.csv"
if os.path.exists(log_file_path):
    df = pd.read_csv(log_file_path)
    st.write("### Detected Intrusions:")
    st.dataframe(df)
else:
    st.warning("No intrusions have been detected yet.")
