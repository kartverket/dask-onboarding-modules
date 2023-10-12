variable "databricks_catalog_name" {
  description = "Name of catalog in metastore"
}

variable "databricks_schema_name" {
  description = "Name of schema in metastore, where external volume should be registered"
}

variable "gcs_bucket_name" {
  description = "Path to the external volume to be registered in the metastore"
}

variable "external_volume_name" {
  description = "Name to give the external volume in the metastore"
}

variable "external_volume_comment" {
  description = "Comment to describe the external volume in the metastore"
  default     = ""
}

variable "env" {
  description = "Environment for the resources to create"
}
