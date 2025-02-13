resource "random_password" "db2opensharecode" {
  for_each = var.consumer_org_numbers

  length  = 16
  special = true
}

resource "databricks_recipient" "db2open" {
  provider = databricks.workspace

  for_each = var.consumer_org_numbers

  name                = "recipient_${each.key}"
  comment             = "Recipient av sb2open opprettet i Terraform for ${each.key}"
  authentication_type = "TOKEN"
  sharing_code        = random_password.db2opensharecode[each.key].result
}

resource "databricks_share" "ext_schema_share" {
  provider = databricks.workspace

  name = var.external_share_name
  object {
    name                        = var.schema_name_silver_ext
    data_object_type            = "SCHEMA"
    history_data_sharing_status = "ENABLED"
  }
}

resource "databricks_grants" "share_grants" {
  provider = databricks.workspace
  share    = databricks_share.ext_schema_share.name

  dynamic "grant" {
    for_each = databricks_recipient.db2open
    content {
      principal  = grant.value.name
      privileges = ["SELECT"]
    }
  }
}
