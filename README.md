Renew vault certificates
=========
> This repository is only a mirror. Development and testing is done on a private gitlab server.

This role install consul-template and configure a service to automate renewal of TLS certificates for Hashicorp Vault on **debian-based** distributions.

Requirements
------------

This role assume that you already have installed a vault server on the host, and is only here to assist in automating the certificate renewal process.

Role Variables
--------------
Available variables are listed below, along with default values. A sample file for the default values is available in `default/renew_vault_certificates.yml.sample` in case you need it for any `group_vars` or `host_vars` configuration.

```yaml
renew_vault_certificates_config_dir: /etc/consul-template.d/vault # by default, set to /etc/consul-template.d/vault
```
This variable defines where the files for the role are stored (consul-template configuration + templates).

```yaml
renew_vault_certificates_vault_user: vault # by default, set to vault
```
This variable defines the user that'll be running the certificate renewal service. Defaults to `vault`, and should be present on the host prior to playing this role (ideally when installing vault).

```yaml
renew_vault_certificates_vault_group: vault # by default, set to vault
```
This variable defines the group that'll be running the certificate renewal service. Defaults to `vault`, and should be present on the host prior to playing this role (ideally when installing vault).

```yaml
renew_vault_certificates_vault_addr: https://127.0.0.1:8200 # by default, set to https://127.0.0.1:8200
```
This variable defines the address the consul-template service will query to get the new certificates. Defaults to localhost, but can be changed if vault isnt reachable on localhost (because of missing certificates SANs for example).

```yaml
renew_vault_certificates_vault_token: mysupersecretvaulttokenthatyoushouldchange # by default, set to a dummy string
```
This variable defines the vault token top use to access vault and renew the certificate. Default is a dummy string to pass unit tests.

```yaml
renew_vault_certificates_vault_token_unwrap: false # by default, set to false
```
Defines whether or not the token is wrapped and should be unwrapped (this is an enterprise-only feature of vault at the moment).

```yaml
renew_vault_certificates_vault_token_renew: true # by default, set to true
```
This variable defines whether or not to renew the vault token. It should probably be `true`, and you should have a periodic token to handle this.

```yaml
renew_vault_certificates_cert_dest: /opt/vault/tls/cert.pem # by default, set to /opt/vault/tls/cert.pem
```
This variable defines where to copy the certificates upon renewal. Default to `/opt/vault/tls/cert.pem` but should be changed depending on where you store the certificates.

```yaml
renew_vault_certificates_key_dest: /opt/vault/tls/key.pem # by default, set to /opt/vault/tls/cert.pem
```
This variable defines where to copy the private keys upon renewal. Default to `/opt/vault/tls/key.pem` but should be changed depending on where you store the keys.

```yaml
renew_vault_certificates_info: # by default, set to:
  issuer_path: pki/issue/your-issuer
  common_name: vault01.example.com
  ttl: 90d
  include_consul_service: false
```
This variable defines the path on vault to retrieve the certificates, as well as the common name and TTL to use for it. It can also include vault aliases in case you have registered vault services in a consul cluster (`active.vault.service.consul,` `standby.vault.service.consul`, `vault.service.consul`).

```yaml
renew_vault_certificates_consul_service_name: vault.service.consul # by default, set to vault.service.consul
```
This variable defines the vault service name in consul. Default is `vault.service.consul`

```yaml
renew_vault_certificates_start_service: false
```
This variable defines whether or not to start the service after creating it. By default, it is only enabled, but not started, in case you're building golden images (in which case you probably don't want a certificate generated during the build process).

Dependencies
------------

This role has a task that installs its own dependencies located in `task/prerequisites.yml`, so that you don't need to manage them. This role requires both `ednxzu.manage_repositories` and `ednxzu.manage_apt_packages` to install vault.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:
```yaml
# calling the role inside a playbook with either the default or group_vars/host_vars
- hosts: servers
  roles:
    - ednxzu.renew_vault_certificates
```

License
-------

MIT / BSD

Author Information
------------------

This role was created by Bertrand Lanson in 2023.
