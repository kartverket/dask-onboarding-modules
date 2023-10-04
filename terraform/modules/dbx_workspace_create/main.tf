module "create_vpc_for_databricks" {
  source = "../gcp_vpc"

  name_prefix  = "${var.name_prefix}-dbx"
  name_postfix = var.name_postfix
  project_id   = var.project_id
  region       = var.region
}

resource "databricks_mws_networks" "this" {
  provider     = databricks.accounts
  account_id   = var.databricks_account_id
  network_name = "${var.name_prefix}-vpc-${var.name_postfix}"
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
  workspace_name = "${var.name_prefix}-dbxws-${var.name_postfix}"
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
