resource "google_service_account" "skyporten_consumer" {
  account_id   = "skyporten-consumer-${var.org_number}"
  display_name = "Skyporten consumer (org. ${var.org_number}) for scope ${var.maskinporten_scope}"
}

data "google_iam_policy" "clientaccess" {
  binding {
    role = "roles/iam.workloadIdentityUser"

    members = [
      "principalSet://iam.googleapis.com/projects/${var.project_number}/locations/global/workloadIdentityPools/${var.workload_identity_pool_id}/attribute.clientaccess/client::${var.maskinporten_client_id}::${var.maskinporten_scope}",
    ]
  }
}

resource "google_service_account_iam_policy" "foo" {
  service_account_id = google_service_account.skyporten_consumer.name
  policy_data        = data.google_iam_policy.clientaccess.policy_data
}

resource "google_storage_bucket" "skyporten_bucket" {
  name     = "skyporten-test-${var.org_number}"
  location = var.region
  uniform_bucket_level_access = true
}

resource "google_storage_bucket_iam_member" "legacy_bucket_reader" {
  bucket   = google_storage_bucket.skyporten_bucket.name
  role     = "roles/storage.legacyBucketReader"
  member   = "serviceAccount:${google_service_account.skyporten_consumer.email}"
}

resource "google_storage_bucket_iam_member" "object_admin" {
  bucket   = google_storage_bucket.skyporten_bucket.name
  role     = "roles/storage.objectAdmin"
  member   = "serviceAccount:${google_service_account.skyporten_consumer.email}"
}