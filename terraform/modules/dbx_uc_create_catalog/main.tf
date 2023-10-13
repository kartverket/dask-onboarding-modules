locals {
  name_postfix = var.env == "prod" ? "" : "-${var.env}"
}

resource "databricks_storage_credential" "external" {
  name = "catalog-creds-gcs-${var.gcs_bucket_name}${local.name_postfix}"
  databricks_gcp_service_account {}
}

resource "google_storage_bucket_iam_member" "member" {
  bucket = var.gcs_bucket_name
  role   = "roles/storage.admin"
  member = "serviceAccount:${databricks_storage_credential.external.databricks_gcp_service_account}"
}

resource "databricks_catalog" "this" {
  name    = "${var.area_short_name}_${var.team_name}${local.name_postfix}"
  comment = "Catalog for dataproducts from ${var.team_name}"
  properties = {
    team = var.team_name, purpose = "Collection of dataproducts from ${var.team_name}"
  }
  storage_root = "gs://${var.gcs_bucket_name}"
}