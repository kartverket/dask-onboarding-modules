locals {
  python_packages = [
    "shapely",
    "apache-sedona",
  ]
}

data "databricks_node_type" "smallest" {
  provider    = databricks.workspace
  local_disk  = true
  min_cores   = 4
  gb_per_core = 1
}

data "databricks_spark_version" "latest_lts" {
  provider          = databricks.workspace
  long_term_support = true
}

resource "google_service_account" "service_account" {
  project      = var.project_id
  account_id   = "cluster-${var.project_id}-sa"
  display_name = "Service Account ${var.project_id}"
  description  = "Service account som bare tilhører ${var.project_id}. I utgangspunktet har denne kun tilgang til der felles init-scripts blir lagret."
}

resource "google_storage_bucket_iam_member" "member" {
  bucket = var.init_script_bucket_name
  role   = "roles/storage.objectViewer"
  member = "serviceAccount:${google_service_account.service_account.email}"
}

resource "databricks_cluster" "shared_autoscaling" {
  provider                = databricks.workspace
  cluster_name            = "${var.project_id}-kluster"
  spark_version           = data.databricks_spark_version.latest_lts.id
  node_type_id            = data.databricks_node_type.smallest.id
  data_security_mode      = "USER_ISOLATION"
  autotermination_minutes = 60
  autoscale {
    min_workers = 1
    max_workers = 2
  }
  #   init_scripts {
  #     gcs {
  #       destination = "gs://${var.init_script_bucket_name}/dask-dbx-init.sh"
  #     }
  #   }
  #   spark_conf = {
  #     "spark.kryo.registrator" : "org.apache.sedona.core.serde.SedonaKryoRegistrator",
  #     "spark.serializer" : "org.apache.spark.serializer.KryoSerializer",
  #     "spark.sql.extensions" : "org.apache.sedona.viz.sql.SedonaVizExtensions,org.apache.sedona.sql.SedonaSqlExtensions",
  #   }
  dynamic "library" {
    for_each = toset(local.python_packages)
    content {
      pypi {
        package = library.value
      }
    }
  }
  gcp_attributes {
    availability           = "PREEMPTIBLE_WITH_FALLBACK_GCP"
    zone_id                = "AUTO"
    google_service_account = google_service_account.service_account.email
  }

}
