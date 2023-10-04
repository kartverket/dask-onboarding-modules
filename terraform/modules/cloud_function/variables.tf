variable "function_folder_location" {
  description = "The relative location of the folder for the cloud function that should be deployed to GCP"
  type        = string
}

variable "name" {
  description = "A user-defined name of the function."
  type        = string
}

variable "location" {
  description = "The location of this cloud function."
  type        = string
  default     = "europe-west1"
}

variable "description" {
  description = "User-provided description of a function."
  type        = string
  default     = "Cloud function managed by Terraform"
}

variable "project" {
  description = "The ID of the project in which the resource belongs. If it is not provided, the provider project is used."
  type        = string
}

variable "labels" {
  description = "A set of key/value label pairs associated with this Cloud Function."
  type        = map(string)
  default     = {}
}

variable "runtime" {
  description = "The runtime in which to run the function. Required when deploying a new function, optional when updating an existing function."
  type        = string
  default     = "python39"
}

variable "entry_point" {
  description = "The name of the function (as defined in source code) that will be executed. Defaults to the resource name suffix, if not specified. For backward compatibility, if function with given name is not found, then the system will try to use function named \"function\". For Node.js this is name of a function exported by the module specified in source_location."
  type        = string
  default     = "main"
}

variable "min_instance_count" {
  description = "(Optional) The limit on the minimum number of function instances that may coexist at a given time."
  type        = number
  default     = 1
}

variable "max_instance_count" {
  description = "(Optional) The limit on the maximum number of function instances that may coexist at a given time."
  type        = number
  default     = 1
}

variable "timeout_seconds" {
  description = "(Optional) The function execution timeout. Execution is considered failed and can be terminated if the function is not completed at the end of the timeout period. Defaults to 60 seconds."
  type        = number
  default     = 600
}

variable "environment_variables" {
  description = "(Optional) Environment variables that shall be available during function execution."
  type        = map(string)
}

variable "ingress_settings" {
  description = "(Optional) Available ingress settings. Defaults to \"ALLOW_ALL\" if unspecified. Default value is ALLOW_ALL. Possible values are ALLOW_ALL, ALLOW_INTERNAL_ONLY, and ALLOW_INTERNAL_AND_GCLB."
  type        = string
  default     = "ALLOW_ALL"
}

variable "all_traffic_on_latest_revision" {
  description = "(Optional) Whether 100% of traffic is routed to the latest revision. Defaults to true."
  type        = bool
  default     = true
}

variable "bucket_id" {
  description = "The bucket id for the bucket where the cloud function code will be stored"
  type        = string
}

variable "bucket_name" {
  description = "The bucket name for the bucket where the cloud function code will be stored"
  type        = string
}

variable "excludes" {
  description = "Files to exclude from the cloud function src directory"
  type        = list(string)
  default = [
    "node_modules",
    "README.md"
  ]
}

variable "schedule" {
  description = "The cron job schedule for when the cloud function should be triggered. On the format * * * * *. For instance */5 * * * * means every 5th minute. See https://crontab.guru/ for more information."
}

variable "service_account_email" {}
