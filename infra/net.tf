resource "google_compute_router_nat" "nat" {
  name                               = "ahins-nat"
  router                             = google_compute_router.router.name
  region                             = google_compute_router.router.region
  nat_ip_allocate_option             = "AUTO_ONLY"
  source_subnetwork_ip_ranges_to_nat = "ALL_SUBNETWORKS_ALL_IP_RANGES"
}

resource "google_compute_router" "router" {
  name    = "router"
  network = "default"
  region  = "asia-south1"
}
