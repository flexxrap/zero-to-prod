# Auth token is read from the YC_TOKEN env var, not from tfvars.
# Run `export YC_TOKEN=$(yc iam create-token)` before terraform apply.
provider "yandex" {
  cloud_id  = var.cloud_id
  folder_id = var.folder_id
  zone      = var.zone
}
