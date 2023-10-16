output "catalog_bucket_url" {
  value = google_storage_bucket.catalog_bucket.url
}

output "landing_zone_bucket_url" {
  value = google_storage_bucket.landing_zone_bucket.url
}

output "catalog_name" {
  description = "Name of the catalog in the metstore"
  value       = module.create_uc_catalog.catalog_name
}

output "gcp_service_account_key" {
  value = module.create_uc_catalog.gcp_service_account_key
}

output "gcs_catalog_bucket_creds_name" {
  value = module.create_uc_catalog.gcs_catalog_bucket_creds_name
}

output "gcs_catalog_bucket_creds_id" {
  value = module.create_uc_catalog.gcs_catalog_bucket_creds_id
}
