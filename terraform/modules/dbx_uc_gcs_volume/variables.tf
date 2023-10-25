variable "databricks_catalog_name" {
  description = "Name of catalog in metastore"
  type        = string
}

variable "databricks_schema_name" {
  description = "Name of schema in metastore, where external volume should be registered"
  type        = string
}

variable "gcs_bucket_name" {
  description = "Name to the external volume to be registered in the metastore"
  type        = string
}

variable "external_volume_name" {
  description = "Name to give the external volume in the metastore"
  type        = string
}

variable "external_volume_comment" {
  description = "Comment to describe the external volume in the metastore"
  default     = ""
  type        = string
}

variable "env" {
  description = "Environment in which the resources are created"
  type        = string
}

variable "metastore_id" {
  description = "(Required for account-level) Unique identifier of the parent Metastore"
  type        = string
}
