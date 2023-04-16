Renew vault certificates
=========
> This repository is only a mirror. Development and testing is done on a private gitlab server.

This role install consul-template and configure a service to automate renewal of TLS certificates for Hashicorp Vault on **debian-based** distributions.

Requirements
------------

None.

Role Variables
--------------
Available variables are listed below, along with default values. A sample file for the default values is available in `default/hashicorp_vault.yml.sample` in case you need it for any `group_vars` or `host_vars` configuration.

```yaml
hashi_vault_install: true # by default, set to true
```
This variable defines if the vault package is to be installed or not before configuring. If you install vault using another task, you can set this to `false`.

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
    - ednxzu.hashicorp_vault
```

License
-------

MIT / BSD

Author Information
------------------

This role was created by Bertrand Lanson in 2023.
