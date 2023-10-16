output "schema_name" {
  description = "Name of the schema in the metstore"
  value       = databricks_schema.create_external_schema_in_catalog.name
}
