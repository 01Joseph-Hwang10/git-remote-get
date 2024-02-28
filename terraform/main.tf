resource "github_repository" "gget" {
  name       = "gget"
  visibility = "public"
}

resource "github_actions_secret" "pypi_username" {
  repository      = github_repository.gget.name
  secret_name     = "PYPI_USERNAME"
  plaintext_value = var.pypi_username
}

resource "github_actions_secret" "pypi_password" {
  repository      = github_repository.gget.name
  secret_name     = "PYPI_PASSWORD"
  plaintext_value = var.pypi_password
}
