resource "google_storage_bucket" "catalog_bucket" {
  project  = var.project_id
  location = var.location
  name     = "catalog-${var.project_id}"
  labels = {
    team    = var.team_name
    purpose = "metastore-catalog-bucket"
  }
}

resource "google_storage_bucket" "landing_zone_bucket" {
  project  = var.project_id
  location = var.location
  name     = "landing-zone-${var.project_id}"
  labels = {
    team    = var.team_name
    purpose = "landing-zone-bucket"
  }
}

module "create_uc_catalog" {
  source = "../modules/dbx_uc_create_catalog"
  providers = {
    databricks.accounts  = databricks.accounts,
    databricks.workspace = databricks.workspace
  }
  area_short_name = var.area_short_name
  team_name       = var.team_name
  env             = var.env
  gcs_bucket_name = google_storage_bucket.catalog_bucket.name
  metastore_id    = var.metastore_id
}

module "create_uc_schema" {
  source = "../modules/dbx_uc_create_schema"
  providers = {
    databricks.workspace = databricks.workspace
  }
  catalog_name       = module.create_uc_catalog.catalog_name
  env                = var.env
  schema_description = "Schema for external resources and volumes"
  schema_name        = "EXTERNAL"
  team_name          = var.team_name
  metastore_id       = var.metastore_id
}

module "register_gcs_bucket_unity_catalog" {
  source = "../modules/dbx_uc_gcs_volume"
  providers = {
    databricks.accounts  = databricks.accounts,
    databricks.workspace = databricks.workspace
  }
  databricks_catalog_name = module.create_uc_catalog.catalog_name
  databricks_schema_name  = module.create_uc_schema.schema_name
  env                     = var.env
  external_volume_comment = var.external_volume_comment
  external_volume_name    = var.external_volume_name
  gcs_bucket_name         = google_storage_bucket.landing_zone_bucket.name
  metastore_id            = var.metastore_id
}
