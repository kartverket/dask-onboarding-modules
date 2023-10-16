locals {
  name_postfix = var.env == "prod" ? "" : "-${var.env}"
}

resource "databricks_storage_credential" "create_external_location_creds" {
  provider     = databricks.accounts
  name         = "volume-creds-gcs-${var.external_volume_name}${local.name_postfix}"
  metastore_id = var.metastore_id
  databricks_gcp_service_account {}
}

#resource "google_storage_bucket_iam_member" "member" {
#  bucket = var.gcs_bucket_name
#  role   = "roles/storage.admin"
#  member = "serviceAccount:${databricks_storage_credential.create_external_location_creds.databricks_gcp_service_account[0].email}"
#}

resource "databricks_external_location" "external_location_to_add" {
  provider        = databricks.workspace
  name            = "gcs-${var.gcs_bucket_name}-${var.external_volume_name}-${local.name_postfix}"
  url             = "gs://${var.gcs_bucket_name}"
  credential_name = databricks_storage_credential.create_external_location_creds.name
}

resource "databricks_volume" "add_external_volume_to_schema" {
  provider         = databricks.workspace
  name             = var.external_volume_name
  catalog_name     = var.databricks_catalog_name
  schema_name      = var.databricks_schema_name
  volume_type      = "EXTERNAL"
  storage_location = databricks_external_location.external_location_to_add.url
  comment          = var.external_volume_comment
}