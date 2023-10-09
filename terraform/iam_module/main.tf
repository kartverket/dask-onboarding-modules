locals {
  landing_sa_roles = [
    "roles/storage.objectViewer",
    "roles/storage.legacyBucketReader",
  ]
}

module "workspace_create" {
  source = "./dbx_workspace_create/"
  providers = {
    databricks.accounts = databricks.accounts
  }
  databricks_account_id = var.databricks_account_id
  name_prefix           = var.name_prefix
  project_id            = var.project_id
  region                = var.region
}

resource "random_id" "bucket_suffix" {
  byte_length = 4
}

resource "google_storage_bucket" "landing_zone" {
  location = var.region
  name     = "landing-zone-${var.env}-${var.team}-${random_id.bucket_suffix.hex}"
}

resource "google_service_account" "service_account" {
  project      = var.project_id
  account_id   = "cluster-${var.team}-sa"
  display_name = "Service Account ${var.team}"
  description  = "Service account som bare tilhører ${var.team}. I utgangspunktet har denne kun tilgang til der felles init-scripts blir lagret."
}

resource "google_storage_bucket_iam_member" "member" {
  for_each = toset(local.landing_sa_roles)
  bucket   = google_storage_bucket.landing_zone.name
  role     = each.value
  member   = "serviceAccount:${google_service_account.service_account.email}"
}