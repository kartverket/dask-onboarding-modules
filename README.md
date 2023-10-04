# dask-modules
Moduler som provisjonerer nødvendig infrastruktur i GCP-prosjektet til team som onboardes dataplattformen.

### Hvordan referere

Moduler i dette repoet kan refereres til på følgende måte:

````yaml
# Reference module defined in dbx_workspace_create
module "create_workspace" {
  source   = "git::https://github.com/kartverket/dask-onboarding-modules//modules/dbx_workspace_create?ref=TD-398-boilerplatekode-onboarding"
  # ...
}

# Reference a specific hash/tag/branch
module "create_workspace" {
  source   = "git::https://github.com/kartverket/dask-onboarding-modules//modules/dbx_workspace_create?ref=TD-398-boilerplatekode-onboarding?ref=<hash/tag/branch>"
  # ...
}
````
