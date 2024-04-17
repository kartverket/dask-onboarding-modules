variable "ad_group_names" {
  description = "Set of AD group names to grant access to the catalog"
  type        = set(string)
}

variable "full_table_name" {
  description = "Name of the table to grant access to"
  type        = string
}

variable "table_privileges" {
  description = "List of privileges to grant on the table. Can be APPLY_TAG, MODIFY, SELECT, ALL_PRIVILEGES, or a combination of these"
  type        = list(string)
}