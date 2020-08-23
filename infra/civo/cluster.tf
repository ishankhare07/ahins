provider "civo" {

}

resource "civo_kubernetes_cluster" "ahins" {
    name = "ahins"
    applications = "Traefik, Metrics"
    num_target_nodes = 4
    target_nodes_size = element(data.civo_instances_size.small.sizes, 0).name
}