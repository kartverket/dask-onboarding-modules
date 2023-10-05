# dask-modules
This repo contains terraform modules maintained by DASK. The modules are used to provision infrastructure for the teams being onboarded to the dataplatform.

### How to use the modules from other repos
Modules must be referenced in the source definition as follows:

````yaml
# Reference module defined in dbx_workspace_create
module "create_workspace" {
  source   = "git::https://github.com/kartverket/dask-modules//terraform/modules/dbx_workspace_create"
  # ...
}

# Reference a specific hash/tag/branch
module "create_workspace" {
  source   = "git::https://github.com/kartverket/dask-modules//terraform/modules/dbx_workspace_create?ref=<hash/tag/branch>"
  # ...
}
````
