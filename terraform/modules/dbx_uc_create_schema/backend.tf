terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = ">= 5.1.0"
    }
    databricks = {
      source                = "databricks/databricks"
      configuration_aliases = [databricks.accounts]
      version               = ">= 1.27.0"
    }
  }
}
