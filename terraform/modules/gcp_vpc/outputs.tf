output "vpc_name" {
  value = google_compute_network.vpc_network.name
}

output "subnetwork_name" {
  value = google_compute_subnetwork.network-with-private-secondary-ip-ranges.name
}
