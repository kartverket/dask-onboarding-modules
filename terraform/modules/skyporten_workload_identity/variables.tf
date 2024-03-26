variable "workload_pool_id" {
  description = "The ID of the workload pool to be used for the Skyporten integration"
}

variable "provider_id" {
  description = "The provider ID for the OICD identity pool provider"
}

variable "required_audience" {
  description = "The required audience for the OICD identity pool provider. Does not need to be a valid domain"
}

variable "consumer_org_numbers" {
  description = "The organization numbers that should be allowed to access the Skyporten integration"
}

variable "maskinporten_scope" {
  description = "The scope for the Maskinporten client. Format <ORGANIZATION_SCOPE:SUB_SCOPE>"
}

variable "region" {
  description = "The region to deploy the resources in"
}

variable "project_number" {
  description = "The project number of the project"
}

variable "project_id" {
  description = "The project ID of the project"
}