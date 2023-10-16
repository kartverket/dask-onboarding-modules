output "catalog_name" {
  description = "Name of the catalog in the metstore"
  value       = databricks_catalog.create_team_metastore_catalog.name
}

output "gcp_service_account_key" {
  value = databricks_storage_credential.gcs_catalog_bucket_creds.gcp_service_account_key
}

output "gcs_catalog_bucket_creds_name" {
  value = databricks_external_location.external_location_to_add.name
}

output "gcs_catalog_bucket_creds_id" {
  value = databricks_storage_credential.gcs_catalog_bucket_creds.id
}
