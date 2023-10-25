variable "env" {
  description = "Environment in which the resources are created"
  type        = string
}

variable "team_name" {
  description = "Name of the product team"
  type        = string
}

variable "catalog_name" {
  description = "Name of the catalog in the metastore to register the schema in"
  type        = string
}

variable "schema_name" {
  description = "Name of the schema to create"
  type        = string
}

variable "schema_description" {
  description = "Purpose of the schema to be created"
  type        = string
}

variable "metastore_id" {
  description = "(Required for account-level) Unique identifier of the parent Metastore"
  type        = string
}
