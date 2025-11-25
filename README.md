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
- Infrastructure as Code

**Azure Services**
- Linux VM
- VNet / Subnet
- NCG
- Azure Monitor Agent (AMA)
- Data Collection Rules (DCR)
- Log Analytics Workspace
- Microsoft Defender for Cloud (CSPM + ARM alerts)
- Microsoft Sentinel (SIEM)

# Infrastructure (Azure + Terraform)

This project includes a complete Infrastructure-as-Code setup located in the `infra/` folder.

Terraform is used to deploy:
- Resource Group  
- Virtual Network (VNet)  
- Subnet  
- Public IP  
- Network Interface  
- Linux Virtual Machine (Ubuntu)

This makes the deployment repeatable, automated, and version-controlled.

infra/
├── main.tf # Entry for main resources (resource group, networking, VM)
├── providers.tf # Terraform + Azure provider configuration
├── variables.tf # Input variables (project_name, location, etc.)
├── network.tf # VNet + Subnet
├── vm.tf # NIC + Public IP + Virtual Machine
├── outputs.tf # Values displayed after terraform apply
└── (state files ignored via .gitignore)

# How to deploy infrastructur

1. Navigate to the IaC folder

  cd infra
2. Initialize Terraform

  terraform init
3. Preview infrastructure changes

  terraform plan
4. Apply the deployment

  terraform apply

# Running the Monitoring Script

1. Create and activate virtual environment:
   python3 -m venv venv
   source venv/bin/activate

2. Install dependencies:
    pip install psutil

3. Run the script:
    python3 main.py

4. (Optional) Add to crontab:
    crontab -e
    */5 * * * * /usr/bin/python3 /home/your-user/systemmonitor/main.py

# What I Learned
  Python & Monitoring
  - Using psutil to collect system metrics
  - Difference between basic and structured JSON logging
  - How to schedule scripts using cron

  Azure Infrastructure
  - Deploying and accessing Linux VMs
  - Basics of VNets, subnets, public IPs

  Git & Version Control
  - Structuring projects
  - Cleaning repos using .gitignore

  Infrastructure-as-Code (IaC)
  - Writing Terraform configurations
  - Using providers (azurerm)
  - Managing variables and outputs
  - Running init → plan → apply workflow

  Cloud Security, Logging & SIEM (integrated into SystemMonitor)
  - Enabled Microsoft Defender for Cloud (CSPM) to assess and secure the environment
  - Triggered intentional misconfigurations (e.g., removing/deleting NSG) to validate Defender posture findings and ARM-level security alerts
  - Configured Azure Monitor Agent (AMA) through Data Collection Rules (DCR) to ingest:
    - Linux Syslog
    - Performance metrics
    - Heartbeat
  - Built a full telemetry pipeline: VM → AMA → Log Analytics Workspace → Microsoft Sentinel
  - Activated Sentinel and validated ingestion of:
    - Syslog
    - Perf counters
    - Heartbeat
    - SecurityAlert (ARM-based alerts)
  - Used KQL for log analysis and security investigation inside Sentinel

Project Structure
systemmonitor/

├── main.py
├── monitor.py
├── logs/
│   └── systemmonitor.json
├── infra/
│   ├── main.tf
│   ├── providers.tf
│   ├── variables.tf
│   ├── network.tf
│   ├── vm.tf
│   ├── outputs.tf
└── README.md