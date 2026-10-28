# Exercise 3: Azure Deployment

> Deploy ColdFusion to Azure.

## Objective

Learn to deploy ColdFusion applications to Microsoft Azure.

## Scenario

**Application:** Business management app
**Target:** Azure VMs with Azure SQL
**Requirements:** Hybrid connectivity, Windows-focused

## Instructions

### Part 1: Azure Architecture

Design the architecture:

```
┌─────────────────────────────────────────────────────────┐
│                        Azure                           │
│                                                         │
│  ┌─────────────┐                                       │
│  │ App Gateway │                                       │
│  └──────┬──────┘                                       │
│         │                                               │
│  ┌──────▼──────┐     ┌─────────────┐                  │
│  │ VM Scale    │────►│ Azure SQL   │                  │
│  │ Set         │     └─────────────┘                  │
│  └──────┬──────┘                                       │
│         │                                               │
│  ┌──────▼──────┐     ┌─────────────┐                  │
│  │ Azure Blob  │     │ Azure Cache │                  │
│  │ Storage     │     │ for Redis   │                  │
│  └─────────────┘     └─────────────┘                  │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Part 2: Azure Resources

Complete the Azure resource list:

| Resource | Purpose | Configuration |
|---------|---------|---------------|
| Virtual Network | | |
| Subnet | | |
| Network Security Group | | |
| Load Balancer | | |
| Virtual Machine Scale Set | | |
| Azure SQL | | |
| Azure Cache for Redis | | |
| Azure Blob Storage | | |

### Part 3: Infrastructure as Code

Create Terraform for the infrastructure:

```hcl
# Azure provider
provider "azurerm" {
    features {}
}

# Resource group
resource "azurerm_resource_group" "main" {
    name     = "cf-app-rg"
    location = "East US"
}

# What else is needed?

resource "azurerm_virtual_network" "main" {
    name                = "cf-vnet"
    address_space       = ["10.0.0.0/16"]
    location            = azurerm_resource_group.main.location
    resource_group_name = azurerm_resource_group.main.name
}

# Virtual Machine Scale Set

resource "azurerm_windows_virtual_machine_scale_set" "main" {
    # What configuration is needed?

    _______________________________________________________

}

# Azure SQL

resource "azurerm_mssql_server" "main" {
    # Configuration

    _______________________________________________________
    
}
```

### Part 4: ColdFusion Configuration

Configure CF for Azure:

```powershell
# In ColdFusion Administrator or via CLI

# Database connection to Azure SQL
cfadmin
    action="updateDatasource"
    type="MSSQL"
    name="AzureDB"
    host="#{env}.database.windows.net"
    database="appdb"
    port="1433"
    username="#{env}admin"
    password="#{env}PASSWORD"
    # SSL required for Azure SQL
    # What else?

_______________________________________________________
```

**Key Azure SQL considerations:**

1. ___________________________________________________
2. ___________________________________________________
3. ___________________________________________________

## Expected Outcome

1. Architecture diagram
2. Azure resource清单
3. Terraform configuration
4. CF configuration

## Evaluation Criteria

| Criteria | Points |
|----------|--------|
| Architecture sound | 25 |
| Resources appropriate | 25 |
| IaC logical | 25 |
| CF config correct | 20 |
| Professional presentation | 5 |
| **Total** | **100** |

**Passing Score:** 70/100
