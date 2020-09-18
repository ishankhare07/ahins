provider "google" {
  project = "tonal-baton-181908"
  region  = "asia-south1"
  zone    = "asia-south1-a"
}

terraform {
  backend "gcs" {
    bucket = "ahins"
    prefix = "infra-box"
  }
}
