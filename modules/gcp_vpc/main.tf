resource "google_compute_network" "vpc_network" {
  project                 = var.project_id
  name                    = "${var.name_prefix}-vpc-${var.name_postfix}"
  auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "network-with-private-secondary-ip-ranges" {
  name          = "${var.name_prefix}-ip-ranges-${var.name_postfix}"
  ip_cidr_range = "10.0.0.0/16"
  region        = var.region
  network       = google_compute_network.vpc_network.id
  secondary_ip_range {
    range_name    = "pods"
    ip_cidr_range = "10.1.0.0/16"
  }
  secondary_ip_range {
    range_name    = "svc"
    ip_cidr_range = "10.2.0.0/20"
  }
  private_ip_google_access = true
}

resource "google_compute_router" "router" {
  name    = "${var.name_prefix}-router-${var.name_postfix}"
  region  = var.region
  network = google_compute_network.vpc_network.id
}

resource "google_compute_router_nat" "nat" {
  name                               = "${var.name_prefix}-router-nat-${var.name_postfix}"
  router                             = google_compute_router.router.name
  region                             = var.region
  nat_ip_allocate_option             = "AUTO_ONLY"
  source_subnetwork_ip_ranges_to_nat = "ALL_SUBNETWORKS_ALL_IP_RANGES"
}



output "vpc_name" {
  value = google_compute_network.vpc_network.name
}

output "subnetwork_name" {
  value = google_compute_subnetwork.network-with-private-secondary-ip-ranges.name
}
