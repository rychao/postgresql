provider "google" {
  version = "~> 2.0"
  project = "iron-circuit-301707"
  #region  = var.region
}

resource "google_sql_database_instance" "instance" {
  name   = "my-postgres-instance"
  database_version = "POSTGRES_11"
  region = "us-central1"

  settings {
    tier = "db-f1-micro"

    ip_configuration {
      ipv4_enabled = true
      # require_ssl = true

      authorized_networks {
        name = "The Network"
        value = <REDACTED>
      }
    }
  }

}

resource "google_sql_user" "users" {
  name     = "admin"
  instance = google_sql_database_instance.instance.name
  password = <REDACTED>
}

resource "google_sql_database" "database" {
  name     = "my-postgres"
  instance = google_sql_database_instance.instance.name
}

output "public_ip" {
  value = google_sql_database_instance.instance.public_ip_address
}

output "connection_name" {
  value = google_sql_database_instance.instance.connection_name
}
