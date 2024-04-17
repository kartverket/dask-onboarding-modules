# Module for granting access to one (or more) tables for one (or more) product teams in Databricks
# The tables have to be in the same schema and catalog

resource "databricks_grant" "catalog_grants" {
  for_each = var.ad_group_names

  principal  = each.value
  privileges = ["USE_CATALOG"]
  catalog    = var.catalog_name
}

resource "databricks_grant" "schema_grants" {
  for_each = var.ad_group_names

  principal  = each.value
  privileges = ["USE_SCHEMA"]
  schema     = "${var.catalog_name}.${var.schema_name}"
}

module "grant_access_to_tables" {
  source           = "./dbx_grant_table_access"
  for_each         = var.tables_privileges_map
  ad_group_names   = var.ad_group_names
  full_table_name  = "${var.catalog_name}.${var.schema_name}.${each.key}"
  table_privileges = each.value
}
