resource "azurerm_virtual_network" "vnet" {
  name                = var.vnet_name
  address_space       = var.vnet_address_space
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
}
resource "azurerm_subnet" "subnet" {
    name                 = var.subnet_name
    resource_group_name  = var.resource_group_name
    virtual_network_name = azurerm_virtual_network.vnet.name
    address_prefixes     = [var.subnet_prefix]
}
resource "azurerm_public_ip" "public_ip" {
  name                = "pip-${var.vm_name}"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  allocation_method   = "Static"
  sku                 = "Basic"
  
}
resource "azurerm_network_interface" "nic" {
    name                = "nic-${var.vm_name}"
    location            = azurerm_resource_group.rg.location
    resource_group_name = azurerm_resource_group.rg.name
    
    ip_configuration {
        name                          = "ipconfig1"
        subnet_id                     = azurerm_subnet.subnet.id
        private_ip_address_allocation = "Dynamic"
        public_ip_address_id          = azurerm_public_ip.public_ip.id
    } 
}
