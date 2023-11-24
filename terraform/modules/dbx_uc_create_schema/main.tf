locals {
  name_postfix = var.env == "prod" ? "" : "_${var.env}"
}

resource "databricks_schema" "create_external_schema_in_catalog" {
  provider     = databricks.workspace
  metastore_id = var.metastore_id
  catalog_name = var.catalog_name
  name         = lower("${var.schema_name}${local.name_postfix}")
  comment      = var.schema_description
  properties = {
    team = var.team_name
  }
}