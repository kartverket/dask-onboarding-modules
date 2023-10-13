output "schema_name" {
  description = "Name of the schema in the metstore"
  value       = databricks_schema.this.name
}
