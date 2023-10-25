variable "gcs_bucket_name" {
  description = "Name to the external volume to be registered in the metastore"
  type        = string
}

variable "env" {
  description = "Environment in which the resources are created"
  type        = string
}

variable "area_short_name" {
  description = "Short name of organization area team is organized in"
  type        = string
}

variable "team_name" {
  description = "Name of the product team"
  type        = string
}

variable "metastore_id" {
  description = "(Required for account-level) Unique identifier of the parent Metastore"
  type        = string
}
