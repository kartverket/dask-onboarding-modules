variable "name_prefix" {
  description = "String to be appended at the beginning of resource name properties."
}

variable "name_postfix" {
  default     = "tf-managed"
  description = "Name postfix for the vpc resources."
}

variable "project_id" {
  description = "The Id of the project for the resources to create"
}

variable "region" {
  description = "Region in which resources are created, see https://docs.gcp.databricks.com/resources/supported-regions.html for supported regions"
}
