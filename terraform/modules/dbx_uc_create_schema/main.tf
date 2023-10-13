locals {
  name_postfix = var.env == "prod" ? "" : "-${var.env}"
}

resource "databricks_schema" "this" {
  catalog_name = var.catalog_name
  name         = "${var.schema_name}${local.name_postfix}"
  comment      = var.schema_description
  properties = {
    team = var.team_name
  }
}