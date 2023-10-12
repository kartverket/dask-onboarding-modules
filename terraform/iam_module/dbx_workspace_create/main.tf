locals {
  name_prefix = var.env == "prod" ? "" : "${var.env}-"
}

module "create_vpc_for_databricks" {
  source = "../gcp_vpc"

  name_prefix  = "${local.name_prefix}dbx"
  workspace_env = var.workspace_env
  project_id   = var.project_id
  region       = var.region
}

resource "databricks_mws_networks" "this" {
  provider     = databricks.accounts
  account_id   = var.databricks_account_id
  network_name = "${local.name_prefix}vpc-${var.workspace_env}"
  gcp_network_info {
    network_project_id    = var.project_id
    vpc_id                = module.create_vpc_for_databricks.vpc_name
    subnet_id             = module.create_vpc_for_databricks.subnetwork_name
    subnet_region         = var.region
    pod_ip_range_name     = "pods"
    service_ip_range_name = "svc"
  }
}

resource "databricks_mws_workspaces" "this" {
  provider       = databricks.accounts
  account_id     = var.databricks_account_id
  workspace_name = "${local.name_prefix}workspace-${var.workspace_env}"
  location       = var.region

  cloud_resource_container {
    gcp {
      project_id = var.project_id
    }
  }
  network_id = databricks_mws_networks.this.network_id
  gke_config {
    connectivity_type = "PRIVATE_NODE_PUBLIC_MASTER"
    master_ip_range   = "10.3.0.0/28"
  }
}

resource "databricks_metastore_assignment" "this" {
  provider     = databricks.workspace
  metastore_id = var.metastore_id
  workspace_id = databricks_mws_workspaces.this.workspace_id
}
