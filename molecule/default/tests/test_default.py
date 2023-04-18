"""Role testing files using testinfra."""


def test_hosts_file(host):
    """Validate /etc/hosts file."""
    etc_hosts = host.file("/etc/hosts")
    assert etc_hosts.exists
    assert etc_hosts.user == "root"
    assert etc_hosts.group == "root"

def test_consul_template_config(host):
    """Validate /etc/consul-template.d/vault/ files."""
    etc_consul_template_d_vault_config_hcl = host.file("/etc/consul-template.d/vault/vault_config.hcl")
    assert etc_consul_template_d_vault_config_hcl.exists
    assert etc_consul_template_d_vault_config_hcl.user == "vault"
    assert etc_consul_template_d_vault_config_hcl.group == "vault"
    assert etc_consul_template_d_vault_config_hcl.mode == 0o600

def test_template_files(host):
    """Validate /etc/consul-template.d/vault/templates/ files."""
    vault_cert_pem_tpl = host.file("/etc/consul-template.d/vault/templates/vault_cert.pem.tpl")
    vault_key_pem_tpl = host.file("/etc/consul-template.d/vault/templates/vault_key.pem.tpl")
    for file in vault_cert_pem_tpl, vault_key_pem_tpl:
        assert file.exists
        assert file.user == "vault"
        assert file.group == "vault"
        assert file.mode == 0o600

def test_vault_certs_service_file(host):
    """Validate vault-certs service file."""
    etc_systemd_system_vault_certs_service = host.file("/etc/systemd/system/vault-certs.service")
    assert etc_systemd_system_vault_certs_service.exists
    assert etc_systemd_system_vault_certs_service.user == "root"
    assert etc_systemd_system_vault_certs_service.group == "root"
    assert etc_systemd_system_vault_certs_service.mode == 0o644
    assert etc_systemd_system_vault_certs_service.content_string != ""

def test_vault_certs_service(host):
    """Validate vault-certs service."""
    vault_certs_service = host.service("vault-certs.service")
    assert vault_certs_service.is_enabled
    assert not vault_certs_service.is_running
    assert vault_certs_service.systemd_properties["Restart"] == "on-failure"
    assert vault_certs_service.systemd_properties["User"] == "vault"
    assert vault_certs_service.systemd_properties["Group"] == "vault"
    assert vault_certs_service.systemd_properties["FragmentPath"] == "/etc/systemd/system/vault-certs.service"
