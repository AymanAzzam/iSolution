provider "google" {
    project = var.gcp-project
    region = var.region
    credentials = "${file("C:\\Users\\ayman\\Downloads\\secrets.json")}"
}

provider "google-beta" {
    project = var.gcp-project
    region = var.region
    credentials = "${file("C:\\Users\\ayman\\Downloads\\secrets.json")}"
}