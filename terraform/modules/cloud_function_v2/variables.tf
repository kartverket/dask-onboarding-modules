variable "project_id" {
  description = "The project ID to deploy the Cloud Function to"
}

variable "name" {
  description = "The name of the Cloud Function"
}

variable "source_dir" {
  description = "The directory containing the source code for the Cloud Function"
}

variable "region" {
  description = "The region to deploy the GCS bucket and Cloud Function to"
}

variable "environment_variables" {
  description = "Runtime environment variables to set on the Cloud Function"
  type        = map(string)
}

variable "schedule" {
  description = "The cron schedule for the Cloud Scheduler job"
}

variable "service_account_email" {
  description = "The email of the service account to use for the Cloud Function"
}

variable "runtime" {
  description = "The runtime to use for the Cloud Function"
}