variable "maskinporten_scope" {
  description = "The scope for the Maskinporten client. Format <ORGANIZATION_SCOPE:SUB_SCOPE>"
}

variable "org_number" {
  description = "The organization number that should be allowed to access the Skyporten integration"
}

variable "region" {
  description = "The region to deploy the resources in"
}

variable "workload_identity_pool_id" {
  description = "The ID of the workload pool to be used for the Skyporten integration"
}

variable "maskinporten_client_id" {
  description = "The Maskinporten client ID for the consumer"
}

variable "project_number" {
  description = "The project number of the project"
}