variable "workspace_env" {
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

variable "deploy_service_account" {
  description = "Need to set this to Databricks account owner SA to use Databricks account API, and Databricks workspace owner to use Databricks workspace API."
}

#variable "init_script_bucket_name" {
#  description = "The bucket name in GCP where the init scripts is stored. The service account associated to the workspace/team cluster will have read access to the init script base bucket."
#}

variable "read_bucket_content_role" {
  description = "The custom role created to grant read access to both content and metadata of a GCS bucket"
}
