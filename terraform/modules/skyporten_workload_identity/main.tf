# Set up the IAM workload identity pool and provider for Skyporten integration
resource "google_iam_workload_identity_pool" "maskinporten" {
  workload_identity_pool_id = var.workload_pool_id
  display_name              = var.workload_pool_id
}

resource "google_iam_workload_identity_pool_provider" "maskinporten" {
  workload_identity_pool_id          = google_iam_workload_identity_pool.maskinporten.workload_identity_pool_id
  workload_identity_pool_provider_id = var.provider_id
  attribute_mapping = {
    "attribute.maskinportenscope" = "assertion.scope"
    "google.subject"              = "assertion.consumer.ID"
    "attribute.clientaccess"      = "\"client::\" + assertion.consumer.ID + \"::\" + assertion.scope"
  }
  display_name = "Test admin enheter provider"
  description  = "OIDC identity pool provider for Maskinporten"
  oidc {
    allowed_audiences = [var.required_audience]
    issuer_uri        = "https://test.sky.maskinporten.no"
  }
}

# Define consumers and access levels
module "skyporten_consumer" {
  source   = "./skyporten_consumers"
  for_each = var.consumer_org_numbers

  maskinporten_scope     = var.maskinporten_scope
  maskinporten_client_id = "0192:${each.value}"
  region                 = var.region
  org_number             = each.value
  project_number         = var.project_number

  workload_identity_pool_id = google_iam_workload_identity_pool.maskinporten.workload_identity_pool_id
  providers = {
    google = google
  }
  depends_on = [ google_iam_workload_identity_pool.maskinporten, google_iam_workload_identity_pool_provider.maskinporten ]
}