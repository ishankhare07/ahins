terraform {
  backend "gcs" {
    bucket = "ahins"
    prefix = "infra-box"
  }
}
