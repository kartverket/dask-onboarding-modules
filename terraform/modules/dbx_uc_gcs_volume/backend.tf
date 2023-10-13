terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = ">= 5.1.0"
    }
    databricks = {
      source                = "databricks/databricks"
      version               = ">= 1.27.0"
    }
  }
}
