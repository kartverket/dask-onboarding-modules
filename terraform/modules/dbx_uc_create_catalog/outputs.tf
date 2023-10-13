output "catalog_name" {
  description = "Name of the catalog in the metstore"
  value       = databricks_catalog.this.name
}
