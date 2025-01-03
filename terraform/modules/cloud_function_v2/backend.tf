terraform {
  required_providers {
    archive = {
      source  = "hashicorp/archive"
      version = "~> 2.7.0"
    }
    google = {
      source  = "hashicorp/google"
      version = "~> 6.14.0"
    }
  }
}
