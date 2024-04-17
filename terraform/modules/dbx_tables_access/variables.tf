variable "ad_group_names" {
  description = "Set of AD group names to grant access to the catalog"
  type        = set(string)
}

variable "catalog_name" {
  description = "Name of the catalog to grant access to"
  type        = string
}

variable "schema_name" {
  description = "Name of the schema to grant access to"
  type        = string
}

variable "tables_privileges_map" {
  description = "Map of table names to privileges to grant on the table. Can be APPLY_TAG, MODIFY, SELECT, ALL_PRIVILEGES, or a combination of these"
  type        = map(list(string))
}