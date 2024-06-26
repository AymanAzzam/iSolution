module "vpc" {
    source  = "terraform-google-modules/network/google"
    version = "~> 9.1"

    project_id   = var.gcp-project
    network_name = "isolution-vpc"
    routing_mode = "GLOBAL"

    subnets = [
        {
            subnet_name           = "public-subnet-1"
            subnet_ip             = "10.10.10.0/24"
            subnet_region         = var.region
            subnet_flow_logs      = "true"
            description           = "This is a public subnet"
        },
    ]

    secondary_ranges = {
        public-subnet-1 = [
            {
                range_name    = "public-subnet-1-secondary"
                ip_cidr_range = "192.168.64.0/24"
            },
        ]
    }

    routes = [
        {
            name                   = "egress-internet"
            description            = "route through IGW to access internet"
            destination_range      = "0.0.0.0/0"
            tags                   = "egress-inet"
            next_hop_internet      = "true"
        }
    ]
}