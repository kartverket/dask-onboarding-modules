variable "consumer_org_numbers" {
  description = "List of valid consumer organization numbers."
}

variable "schema_name_silver_ext" {
  type        = string
  description = "The schema name to share."
}

variable "external_share_name" {
  description = "Name of share for external schema"
  type        = string
}
