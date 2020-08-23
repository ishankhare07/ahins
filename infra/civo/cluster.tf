provider "civo" {
    token = var.civo_token
}

resource "civo_kubernetes_cluster" "ahins" {
    name = "ahins"
    applications = "-Traefik Metrics"
    num_target_nodes = 4
    target_nodes_size = "g2.small"
}
