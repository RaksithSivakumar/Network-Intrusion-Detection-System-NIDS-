# Smart Network Security Monitor

## Overview

The Smart Network Security Monitor is an advanced application designed to provide real-time monitoring of network traffic for suspicious activities and potential threats. Utilizing an intuitive Streamlit dashboard, this tool alerts users to any anomalies and maintains detailed logs for further analysis.

## Features
### Real-time Traffic Analysis: 
Continuously monitors network data to detect unauthorized access and malicious activities.

### Alert Notifications: 
Provides immediate alerts for detected intrusions, enabling prompt response actions.

### Comprehensive Logging: 
Keeps a detailed log of detected intrusions, including timestamps, source and destination IP addresses, and severity levels.

### User-Friendly Dashboard: 
Offers an interactive interface for visualizing network activity and intrusion logs.

### Heartbeat Mechanism: 
Monitors the application's operational status and logs the last active timestamp.

## Technology Stack
- #### Frontend: 
   Streamlit for creating the user interface.

- #### Backend: 
   Python for data processing and analysis.

- #### Data Storage: 
   CSV files for logging detected intrusions and system activities.

- #### Libraries: 
    Utilizes libraries like Pandas and NumPy for data handling.


### Installation

To set up the project locally, follow these steps:

##### Clone the repository:
``` bash 
git clone https://github.com/RaksithSivakumar/NIDS.git
```
#### Navigate to the project directory:
``` bash 
cd NIDS
```
#### Install the required dependencies:
``` bash
pip install -r requirements.txt
```
#### Run the Streamlit application:
``` bash
streamlit run streamlit_dashboard.py
```
### Usage

Launch the Streamlit app to access the Smart Network Security Monitor dashboard.
The dashboard will display the current operational status and any detected intrusions.
Review the logs for insights into network activities and potential threats.

### Contributing

Contributions are welcome! If you would like to contribute to the project, please fork the repository and submit a pull request. For any issues or feature requests, feel free to create an issue in the GitHub repository.
