resource "databricks_grant" "table_grants" {
  for_each = var.ad_group_names

  principal  = each.value
  privileges = var.table_privileges
  table      = var.full_table_name
}