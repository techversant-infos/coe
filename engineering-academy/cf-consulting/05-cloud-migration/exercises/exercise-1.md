# Exercise 1: AWS EC2 Deployment

> Deploy ColdFusion to AWS EC2.

## Objective

Learn to deploy ColdFusion applications to AWS EC2.

## Scenario

**Application:** E-commerce platform
**Target:** AWS EC2 with Windows Server
**Requirements:** High availability, auto-scaling

## Instructions

### Part 1: Architecture Design

Design the AWS architecture:

```
┌─────────────────────────────────────────────────────────┐
│                      AWS Cloud                          │
│                                                         │
│  ┌─────────────┐          ┌─────────────┐              │
│  │   Route 53  │          │   WAF      │              │
│  └──────┬──────┘          └─────────────┘              │
│         │                                                │
│  ┌──────▼──────┐                                        │
│  │  ALB        │                                        │
│  └──────┬──────┘                                        │
│         │                                                │
│  ┌──────▼──────┐          ┌─────────────┐              │
│  │ EC2 Auto    │◄─────────│  RDS        │              │
│  │ Scaling     │          │  (MSSQL)    │              │
│  │ Group       │          └─────────────┘              │
│  └──────┬──────┘                                        │
│         │                                                │
│  ┌──────▼──────┐          ┌─────────────┐              │
│  │ EFS         │          │ ElastiCache │              │
│  │ (Shared)    │          │ (Redis)     │              │
│  └─────────────┘          └─────────────┘              │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Part 2: EC2 Instance Configuration

**Requirements:**
- 4 vCPUs, 16GB RAM
- Windows Server 2019
- ColdFusion 2023

| Setting | Value |
|---------|-------|
| Instance Type | |
| AMI | |
| Storage | |
| Security Group | |

**Security Group Rules:**

| Port | Source | Purpose |
|------|--------|---------|
| 443 | | |
| 80 | | |
| 3389 | | |
| | | |

### Part 3: Installation Script

Create a PowerShell script for CF installation:

```powershell
# Download ColdFusion installer
$cfInstaller = "cf_installer.exe"

# Silent installation
# What parameters are needed?

$params = @(
    ""
)

# Install
Start-Process -FilePath $cfInstaller -ArgumentList $params -Wait
```

Complete the installation parameters:

```powershell
$params = @(
    "- silent",
    "- CF21_InstallDir=C:\ColdFusion2023",
    "- LicenseKey=${env:CF_LICENSE_KEY}",
    # What about these?
    "- EnableRDS=true",
    "- EnableIVS=true"
)
```

### Part 4: CloudWatch Monitoring

Configure monitoring:

```json
{
    "metrics": [
        "CPUUtilization",
        "Memory",
        "Disk",
        ""
    ],
    "alarms": {
        "HighCPU": {
            "threshold": 80,
            "period": 300,
            "action": ""
        }
    }
}
```

**What else should you monitor for ColdFusion?**

1. ___________________________________________________
2. ___________________________________________________
3. ___________________________________________________

## Expected Outcome

1. Architecture diagram
2. EC2 configuration
3. Installation script
4. Monitoring plan

## Evaluation Criteria

| Criteria | Points |
|----------|--------|
| Architecture sound | 25 |
| EC2 config appropriate | 25 |
| Script logical | 25 |
| Monitoring complete | 20 |
| Professional presentation | 5 |
| **Total** | **100** |

**Passing Score:** 70/100
