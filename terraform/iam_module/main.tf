module "workspace_create" {
  source    = "./dbx_workspace_create/"
  providers = {
    databricks.accounts = databricks.accounts
  }
  databricks_account_id = var.databricks_account_id
  project_id            = var.project_id
  region                = var.region
  env                   = var.env
  name_postfix           = var.name_postfix
}

module "create_cluster_for_ws" {
  source                   = "./dbx_workspace_cluster_create"
  project_id               = var.project_id
  env                      = var.env
  deploy_service_account   = var.deploy_service_account
  read_bucket_content_role = var.read_bucket_content_role
  #init_script_bucket_name  = var.init_script_bucket_name

  providers = {
    databricks.workspace = databricks.workspace
  }
}
