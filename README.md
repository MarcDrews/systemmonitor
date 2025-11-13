# SystemMonitor

A simple Python script to monitor system metrics: CPU, RAM, disk usage, and network I/O.

##  Features

- Logs:
  - CPU usage
  - RAM usage
  - Disk usage
  - Network received/sent
- Outputs to:
  - Terminal (print)
  - Local structured JSON log file (`logs/systemmonitor.json`)
- Runs every 5 minutes via cron (optional)
- Deployed on an Azure VM

## Tech Stack

**Languages & Libraries**
- Python 3
- `psutil`
- `logging` (with custom JSON formatter)

**OS & Tools**
- Ubuntu 24.04 LTS
- Cron (for scheduled execution)
- Git & GitHub

## Infrastructure

- Azure Virtual Machine (Linux)
- Virtual Network (VNet)
- SSH for remote access
- Planned: Infrastructure as Code (Terraform/Bicep)

## How to Run

1. Create and activate virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate

2. Install dependencies:
    pip install psutil

3. Run the script:
    python3 main.py

4. (Optional) Add to crontab:
    crontab -e
    */5 * * * * /usr/bin/python3 /home/your-user/systemmonitor/main.py

📚 What I Learned
- How to monitor system performance using psutil
- Difference between basic and structured logging
- How to use cron for automation
- Setting up and accessing a VM in Azure
- Using GitHub for version control
- How to prepare for sending logs to the cloud
- Foundation for using Infrastructure as Code (IaC)

Project Structure
systemmonitor/
├── monitor.py
├── main.py
├── logs/
│   └── systemmonitor.json
└── README.md