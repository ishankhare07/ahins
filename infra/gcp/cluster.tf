provider "google" {

  project = "tonal-baton-181908"
  region  = "asia-south1"
  zone    = "asia-south1-a"
}

resource "google_container_cluster" "primary" {
  name     = "ahins"
  location = "asia-south1"

  initial_node_count        = 1
  default_max_pods_per_node = 32

  remove_default_node_pool = true

  master_auth {
    username = ""
    password = ""

    client_certificate_config {
      issue_client_certificate = false
    }
  }

  private_cluster_config {
    enable_private_nodes    = true
    enable_private_endpoint = false
    master_ipv4_cidr_block  = var.node_ip_range
  }

  ip_allocation_policy {
    cluster_ipv4_cidr_block  = var.pod_ip_range
    services_ipv4_cidr_block = var.service_ip_range
  }
}

resource "google_container_node_pool" "primary" {
  name       = "primary-pool"
  location   = "asia-south1"
  cluster    = google_container_cluster.primary.name
  node_count = 1

  node_config {
    machine_type = "e2-small"
    disk_size_gb = "10"
    image_type   = "cos_containerd"

    metadata = {
      disable-legacy-endpoints = true
    }

    oauth_scopes = [
      "https://www.googleapis.com/auth/logging.write",
      "https://www.googleapis.com/auth/monitoring",
    ]
  }
}
