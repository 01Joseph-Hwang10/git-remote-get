variable "github_owner" {
  type        = string
  description = <<EOT
    Variable for GitHub owner.

    This represents what account or organization the repository will be created under.
  EOT
}

variable "pypi_username" {
  type      = string
  sensitive = true
}

variable "pypi_password" {
  type      = string
  sensitive = true
}
