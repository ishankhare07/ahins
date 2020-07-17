resource "google_compute_instance" "ahins" {
  name         = "test"
  machine_type = "f1-micro"
  zone         = "asia-south1-a"

  boot_disk {
    initialize_params {
      image = "ubuntu-minimal-2004-lts/ubuntu-minimal-2004-focal-v20200702"
    }
  }

  network_interface {
    network = "default"

    access_config {
      // Ephemeral IP
    }
  }

  service_account {
    scopes = ["userinfo-email", "compute-ro", "storage-ro"]
  }
}
