terraform {
  required_providers {
    databricks = {
      source                = "databricks/databricks"
      configuration_aliases = [databricks.workspace]
    }
    google = {
      source = "hashicorp/google"
    }
  }
}
