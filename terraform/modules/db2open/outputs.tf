output "delta_sharing_config_urls" {
  value = {
    for key, recipient in databricks_recipient.db2open :
    key => recipient.tokens[0].activation_url
  }
  sensitive   = true
  description = "URLs to download the Delta Sharing configuration for each recipient."
}

output "databricks_recipient_data" {
  value = {
    for key, recipient in databricks_recipient.db2open :
    key => {
      name           = recipient.name
      tokens         = recipient.tokens
      sharing_code   = recipient.sharing_code
      activation_url = try(recipient.tokens[0].activation_url, "No activation URL available")
    }
  }
  sensitive   = true
  description = "Data for each Databricks recipient, including activation URLs and sharing codes."
}

output "external_share_name" {
  value       = databricks_share.ext_schema_share.name
  description = "The name of the external share."
}
