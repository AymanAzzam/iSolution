# google_client_config and kubernetes provider must be explicitly specified like the following.
data "google_client_config" "default" {}

provider "kubernetes" {
  host                   = "https://${module.gke.endpoint}"
  token                  = data.google_client_config.default.access_token
  cluster_ca_certificate = base64decode(module.gke.ca_certificate)
}

module "gke" {
  source                     = "terraform-google-modules/kubernetes-engine/google"
  project_id                 = var.gcp-project
  name                       = "gke-test-1"
  region                     = var.region
  zones                      = ["${var.region}-a", "${var.region}-b"]
  network                    = module.vpc.network_name
  subnetwork                 = "public-subnet-1"
  ip_range_pods              = ""
  ip_range_services          = ""
  http_load_balancing        = false
  network_policy             = false
  horizontal_pod_autoscaling = true
  filestore_csi_driver       = false
  deletion_protection        = false

  node_pools = [
    {
      name                      = "default-node-pool"
      machine_type              = "e2-medium"
      min_count                 = 2
      max_count                 = 4
      initial_node_count        = 2
      local_ssd_count           = 0
    },
  ]

}