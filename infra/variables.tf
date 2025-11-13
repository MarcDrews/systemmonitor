variable "location" {
  description = "Azure region"
  type        = string
  default     = "westeurope"
}

variable "resource_group_name" {
  description = "Name of the resource group"
  type        = string
  default     = "rg-systemmonitor"
}

variable "vnet_name" {
  description = "Name of the virtual network"
  type        = string
  default     = "vnet-systemmonitor"
}

variable "vnet_address_space" {
  description = "Address space for the VNet"
  type        = list(string)
  default     = ["10.0.0.0/16"]
}

variable "subnet_name" {
  description = "Name of the subnet"
  type        = string
  default     = "subnet-systemmonitor"
}

variable "subnet_prefix" {
  description = "Subnet IP range"
  type        = string
  default     = "10.0.1.0/24"
}

variable "vm_name" {
  description = "Name of the virtual machine"
  type        = string
  default     = "vm-systemmonitor"
}

variable "vm_size" {
  description = "Size of the virtual machine"
  type        = string
  default     = "Standard_B1s"
}

variable "admin_username" {
  description = "Admin username for the VM"
  type        = string
  default     = "drew"
}

variable "ssh_public_key_path" {
  description = "Path to your SSH public key"
  type        = string
  default     = "~/.ssh/id_rsa.pub"
}