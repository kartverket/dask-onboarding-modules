variable "project_id" {
  description = "The Id of the project for the resources to create"
}

variable "env" {
  description = "Environment"
}

variable "deploy_service_account" {
  description = "Need to set this to Databricks account owner SA to use Databricks account API, and Databricks workspace owner to use Databricks workspace API."
}

variable "workspace_env" {
  description = "The environment of the workspace"
}

#variable "init_script_bucket_name" {
#  description = "The bucket name in GCP where the init scripts is stored. The service account associated to the workspace/team cluster will have read access to the init script base bucket."
#}
