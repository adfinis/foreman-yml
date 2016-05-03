# foreman-yml

Configure Foreman with YAML files.

This library automatically resolves names so you can link templates, hosts, domains with only using their names. It's not required to know their ids beforehand.

## Installation
```
git clone https://github.com/adfinis-sygroup/foreman-yml
cd foreman-yml
sudo pip install .
```


## Usage

```
foreman-yml /path/to/config.yaml
```


### Configuration

Root node of YAML is allways `foreman`.
You can find an configuration example under `config/example.yml`


#### Section `auth`
```yaml
auth:
  url: "https://foreman.lab.local"
  user: username
  pass: password
```
- __url__          URL of your foreman instance
- __user__         Username for connecting to the API. User should have administrative rights
- __pass__         Password for the User


#### Section `setting`
```yaml
setting:
  - name: entries_per_page
    value: 42
  - name:  safemode_render
    value: false
```
Key/Value pair for global foreman settings

- __name__          Key
- __value__         Value


#### Section `architecture`
```yaml
architecture:
  - name: x86_64
  - name: i386
```
- __name__          Architecture string (Example: 'x86_64')


#### Section `environment`
```yaml
environment:
  - name: production
  - name: development
  - name: staging
```
- __name__          Environment name


#### Section `smart-proxy`
```yaml
smart-proxy:
  - name: smproxy01
    url: "http://localhost:8000/"
```
- __name__         Smart proxy name
- __url__          Smart proxy url


#### Section `domain`
```yaml
domain:
  - name: lab.local
    fullname: lab.local is a test domain
    dns-proxy: smproxy01
    parameters:
      - name:  keyname
        value: keyvalue
```
- __name__          Domain name
- __fullname__      Detailed description     
- __dns-proxy__     DNS proxy for the domain. Maps to `smart-proxy.name`
- __parameters__    Extra parameters, key/value pair
 - __name__         Key
 - __value__        Value


#### Section `subnet`
```yaml
subnet:
  - name: lab
    network: 192.168.122.0
    mask: 255.255.255.0
    gateway: 192.168.122.1
    dns-primary: 192.168.122.1
    dns-secondary: 8.8.8.8
    ipam: DHCP
    from: 192.168.122.10
    to: 192.168.122.50
    vlanid:
    domain:
      - name: lab.local
    dhcp-proxy: Smart Proxy
    tftp-proxy: Smart Proxy
    dns-proxy:
    boot-mode: DHCP
```
- __name__                 Subnet name
- __network__              Network address
- __mask__                 Network Netmask
- __gateway__              Network gateway
- __dns-primary__          Primary DNS server
- __dns-secondary__        Secondary DNS server
- __ipam__                 IP Address auto suggestion mode for this subnet, valid values are "DHCP", "Internal DB", "None"
- __from__                 Starting IP Address for IP auto suggestion
- __to__                   Ending IP Address for IP auto suggestion
- __vlanid__               VLAN ID for this subnet
- __domain__               Domains in which this subnet is part
 - __name__                Domain name, maps to `domain.name`
- __dhcp-proxy__           DHCP Proxy to use within this subnet, maps to `smart-proxy.name`
- __tftp-proxy__           TFTP Proxy to use within this subnet, maps to `smart-proxy.name`
- __dns-proxy__            DNS Proxy to use within this subnet, maps to `smart-proxy.name`
- __boot-mode__            Default boot mode for interfaces assigned to this subnet, valid values are "Static", "DHCP"


#### Section `model`
```yaml
model:
  - name: libvirt
    info: Virtual Machine
    vendor-class: vmware
    hardware-model: esxi6
```
- __name__                 Model name
- __info__                 Detailed description
- __vendor-class__         Hardware vendor
- __hardware-model__       Hardware model


#### Section `medium`
```yaml
medium:
  - name: Ubuntu Mirror
    path: "http://archive.ubuntu.com/ubuntu"
    os-family: Debian

```
- __name__                 Model name
- __path__                 The path to the medium, can be a URL or a valid NFS server (exclusive of the architecture)
- __os-family__            Operating system family, available values: AIX, Altlinux, Archlinux, Coreos, Debian, Freebsd, Gentoo, Junos, NXOS, Redhat, Solaris, Suse, Windows


#### Section `partition-table`
```yaml
partition-table:
  - name: Ubuntu Default
    os-family: Debian
    audit-comment: initial import
    layout: |
            #!ipxe
            <%#
            kind: iPXE
            name: RLC iPXE
            oses:
            - Ubuntu 14.04
            %>
            [...]
    locked: false
```
- __name__                  Partition table name
- __os-family__             Operating system family, available values: AIX, Altlinux, Archlinux, Coreos, Debian, Freebsd, Gentoo, Junos, NXOS, Redhat, Solaris, Suse, Windows
- __audit-comment__         Comment for the audit log
- __layout__                Partition layout
- __locked__                Whether or not the template is locked for editing


#### Section `provisioning-template`
```yaml
provisioning-template:
    name: Ubuntu Preseed
    template: |
               <%#
              kind: provision
              name: Ubuntu Preseed
              oses:
              - Debian 8.
              %>
              [...]
    snippet: false
    audit-comment: initial import
    template-kind-id: 3
    template-combination-attribute:
    os:
      - name: Debian 8
    locked: false
```
- __name__                  Partition table name
- __template__              The provisioning template itself
- __snippet__               Set to true if template is a snippet only
- __audit-comment__         Comment for the audit log
- __template_kind_id__      Template kind id
- __os__                    
 - __name__                 Operating system name, maps to `os.name`
- __locked__                Whether or not the template is locked for editing


#### Section `os`
```yaml
os:
  - name: Ubuntu
    major: 14
    minor: 4
    description: Ubuntu 14.04 LTS
    family: Debian
    release-name: trusty
    password-hash: SHA512
    architecture:
      - name: x86_64
    provisioning-template:
      - name: Ubuntu PXE
      - name: Ubuntu Preseed
    medium:
      - name: Ubuntu Mirror
    partition-table:
      - name: Ubuntu Default
    parameters:
      version: "14.04"
      codename: "trusty"
```
- __name__                  Operating system table name
- __major__                 The provisioning template itself
- __minor__                 Set to true if template is a snippet only
- __description__           Comment for the audit log
- __family__                Operating system family, available values: AIX, Altlinux, Archlinux, Coreos, Debian, Freebsd, Gentoo, Junos, NXOS, Redhat, Solaris, Suse, Windows
- __release-name__          OS release name
- __password-hash__         Root password hash function to use, one of MD5, SHA256, SHA512, Base64
- __architecture__        
  - __name__                Architecture name, maps to `architecture.name`
- __provisioning-template__
  - __name__                Provisioning template name, maps to `provisioning-template.name`
- __medium__
  - __ name__               Medium name, maps to `medium.name`
- __partition-table__
  - __name__                Ptable name, maps to `partition-table.name`
- __parameters__
  - __ key__                Additional OS settings in format 'keyname': 'keyvalue'


#### Section `hostgroup`
```yaml
hostgroup:
  - name: switzerland
    parent:
    environment: production
    os: Ubuntu 14.04 LTS
    architecture: x86_64
    medium: Ubuntu Mirror
    partition-table: Ubuntu Default
    subnet: lab
    domain: lab.local
```
- __name__                  Hostgroup name
- __parent__                Parent hostgroup
- __environment__           Environment name, maps to `environment.name`
- __os__                    Operating system name, maps to `os.name`
- __architecture__          Architecture name, maps to `architecture.name`
- __medium__                Media name, maps to `medium.name`
- __partition-table__       Ptable name, maps to `partition-table.name`
- __subnet__                Subnet name, maps to `subnet.name`
- __domain__                Domain name, maps to `domain.name`



#### Section `cleanup-[architecture|partition-table|provisioning-template]`
```yaml
cleanup-[architecture|partition-table|provisioning-template]:
  - name: foo
  - name: bar
```
Removes specified objects, mapping to object.name
- __name__                  architecture|partition-table|provisioning-template name to delete





## Hacking
```
virtualenv --system-site-packages venv-dev
source venv-dev/bin/activate
pip install -e .
```

## Future
- Dump current settings
- Better documentaion

## License
GNU AFFERO GENERAL PUBLIC LICENSE Version 3
