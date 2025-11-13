terraform {
    required_providers {
      azurerm = {
        source = "hashicorp/azurerm"
        version = "~> 3.98.0"
      }
    }
}
provider "azurerm" {
    features {}
}
resource "azurerm_resource_group" "rg" {
    name     = "rg-systemonitor-dev"
    location = "West Europe"
}
