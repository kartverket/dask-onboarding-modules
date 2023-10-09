variable "name_prefix" {
  description = "String to be appended at the beginning of resource name properties."
}

variable "name_postfix" {
  description = "String to be appended at the end of resource name properties."
  default     = "tf-managed"
}

variable "project_id" {
  description = "The Id of the project for the resources to create"
}

variable "region" {
  description = "Location for Databricks workspace / region for GCP vpc. Databricks location should match vpc region."
  default     = "europe-west1"
}

variable "databricks_account_id" {
  description = "Account ID found on https://accounts.gcp.databricks.com/"
}

variable "env" {
  description = "Environment for the resources to create"
}

variable "team" {
  description = "Team for the resources to create"
}
