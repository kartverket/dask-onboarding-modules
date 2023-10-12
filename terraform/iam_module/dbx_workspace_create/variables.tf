variable "workspace_env" {
  description = "String to be appended at the end of resource name properties (dev/test/prod)"
}

variable "project_id" {
  description = "The Id of the project for the resources to create"
}

variable "region" {
  description = "Location for Databricks workspace / region for GCP vpc. Databricks location should match vpc region."
}

variable "databricks_account_id" {
  description = "Account ID found on https://accounts.gcp.databricks.com/"
}

variable "env" {
  description = "Environment for the resources to create"
}
