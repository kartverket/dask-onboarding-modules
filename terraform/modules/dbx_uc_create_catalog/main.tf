locals {
  name_postfix           = var.env == "prod" ? "" : "-${var.env}"
  area_short_name_prefix = var.area_short_name == "" ? "" : "${var.area_short_name}-"
}

resource "databricks_storage_credential" "gcs_catalog_bucket_creds" {
  provider     = databricks.accounts
  name         = "catalog-creds-gcs-${var.gcs_bucket_name}${local.name_postfix}"
  metastore_id = var.metastore_id
  databricks_gcp_service_account {}
}

resource "google_storage_bucket_iam_member" "give_sa_admin_role" {
  bucket     = var.gcs_bucket_name
  role       = "roles/storage.legacyBucketOwner"
  member     = "serviceAccount:${databricks_storage_credential.gcs_catalog_bucket_creds.databricks_gcp_service_account[0].email}"
  depends_on = [databricks_storage_credential.gcs_catalog_bucket_creds]
}

resource "databricks_external_location" "external_location_to_add" {
  provider        = databricks.workspace
  name            = "gcs-${var.gcs_bucket_name}-${local.name_postfix}"
  url             = "gs://${var.gcs_bucket_name}"
  credential_name = databricks_storage_credential.gcs_catalog_bucket_creds.name
  depends_on      = [google_storage_bucket_iam_member.give_sa_admin_role]
}

resource "databricks_catalog" "create_team_metastore_catalog" {
  provider     = databricks.workspace
  metastore_id = var.metastore_id
  name         = "${local.area_short_name_prefix}${var.team_name}${local.name_postfix}"
  comment      = "Catalog for dataproducts from ${var.team_name}"
  properties = {
    team    = var.team_name
    purpose = "Collection of dataproducts from ${var.team_name}"
  }
  storage_root = "gs://${var.gcs_bucket_name}"

  depends_on = [databricks_external_location.external_location_to_add]
}

resource "databricks_grants" "grants_on_catalog" {
  catalog  = databricks_catalog.create_team_metastore_catalog.name
  provider = databricks.workspace
  grant {
    principal  = var.team_name
    privileges = ["ALL_PRIVILEGES"]
  }
}