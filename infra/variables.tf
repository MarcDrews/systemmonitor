variable "project_name" {
  description = "Prefix for resource names (fx systemmonitor)"
  type        = string
  default     = "systemmonitor"
}

variable "location" {
  description = "Azure region"
  type        = string
  default     = "westeurope"
}
