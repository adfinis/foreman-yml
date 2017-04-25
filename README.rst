foreman-yml
===========

|PyPi| |License|

.. |PyPi| image:: https://img.shields.io/pypi/v/foreman-yml.svg?style=flat-square
   :target: https://pypi.python.org/pypi/foreman-yml
.. |License| image:: https://img.shields.io/badge/license-GPLv3-blue.svg?style=flat-square
   :target: LICENSE

Make automated foreman configuration as easy as pie.

This script automatically resolves names so you can link templates,
hosts, domains with only using their names. It's not required to know
their ids beforehand.

Installation
------------

::

    git clone https://github.com/adfinis-sygroup/foreman-yml --recursive
    cd foreman-yml
    sudo pip install .

Note CentOS/RHEL
~~~~~~~~~~~~~~~~

::
    sudo yum install gcc python-devel python-pip python-argparse -y

Usage
-----

::

    foreman-yml [import|dump|cleanup] /path/to/config.yaml

Configuration
~~~~~~~~~~~~~

Root node of YAML is always ``foreman``. You can find an configuration
example under ``config/example.yml``

Dump current configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~

foreman-yml supports dumping the whole configuration of a remote foreman
instance to sdout. Use ``foreman-yml dump`` for this feauture.

For dumping, provide an config file with auth settings:

.. code:: yaml

    foreman:
      auth:
        url: "https://foreman.lab.local"
        user: username
        pass: password

Then run foreman-yml like this to dump configuration:

::

    foreman-yml dump /path/to/config.yml > foreman_dump.yml

Import settings into foreman
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If no keyword or ``import`` is provided to ``foreman-yml``, the script
tries to import settings provided by yaml-file.

::

    foreman-yml /path/to/config.yml
    foreman-yml dump /path/to/config.yml

The following config sections are supported:

Section ``auth``
^^^^^^^^^^^^^^^^

.. code:: yaml

    auth:
      url: "https://foreman.lab.local"
      user: username
      pass: password

-  **url** URL of your foreman instance
-  **user** Username for connecting to the API. User should have
   administrative rights
-  **pass** Password for the User

Section ``setting``
^^^^^^^^^^^^^^^^^^^

.. code:: yaml

    setting:
      - name: entries_per_page
        value: 42
      - name:  safemode_render
        value: false

Key/Value pair for global foreman settings

-  **name** Key
-  **value** Value

Section ``architecture``
^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: yaml

    architecture:
      - name: x86_64
      - name: i386

-  **name** Architecture string (Example: 'x86\_64')

Section ``environment``
^^^^^^^^^^^^^^^^^^^^^^^

.. code:: yaml

    environment:
      - name: production
      - name: development
      - name: staging

-  **name** Environment name

Section ``smart-proxy``
^^^^^^^^^^^^^^^^^^^^^^^

.. code:: yaml

    smart-proxy:
      - name: smproxy01
        url: "http://localhost:8000/"

-  **name** Smart proxy name
-  **url** Smart proxy url

Section ``domain``
^^^^^^^^^^^^^^^^^^

.. code:: yaml

    domain:
      - name: lab.local
        fullname: lab.local is a test domain
        dns-proxy: smproxy01
        parameters:
          - name:  keyname
            value: keyvalue

-  **name** Domain name
-  **fullname** Detailed description
-  **dns-proxy** DNS proxy for the domain. Maps to ``smart-proxy.name``
-  **parameters** Extra parameters, key/value pair
-  **name** Key
-  **value** Value

Section ``subnet``
^^^^^^^^^^^^^^^^^^

.. code:: yaml

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
        network-type: IPv4

-  **name** Subnet name
-  **network** Network address
-  **mask** Network Netmask
-  **gateway** Network gateway
-  **dns-primary** Primary DNS server
-  **dns-secondary** Secondary DNS server
-  **ipam** IP Address auto suggestion mode for this subnet, valid
   values are "DHCP", "Internal DB", "None"
-  **from** Starting IP Address for IP auto suggestion
-  **to** Ending IP Address for IP auto suggestion
-  **vlanid** VLAN ID for this subnet
-  **domain** Domains in which this subnet is part
-  **name** Domain name, maps to ``domain.name``
-  **dhcp-proxy** DHCP Proxy to use within this subnet, maps to
   ``smart-proxy.name``
-  **tftp-proxy** TFTP Proxy to use within this subnet, maps to
   ``smart-proxy.name``
-  **dns-proxy** DNS Proxy to use within this subnet, maps to
   ``smart-proxy.name``
-  **boot-mode** Default boot mode for interfaces assigned to this
   subnet, valid values are "Static", "DHCP"
-  **network-type** Type or protocol, IPv4 or IPv6, defaults to IPv4,
   valid values are "IPv4", "IPv6"

Section ``model``
^^^^^^^^^^^^^^^^^

.. code:: yaml

    model:
      - name: libvirt
        info: Virtual Machine
        vendor-class: vmware
        hardware-model: esxi6

-  **name** Model name
-  **info** Detailed description
-  **vendor-class** Hardware vendor
-  **hardware-model** Hardware model

Section ``medium``
^^^^^^^^^^^^^^^^^^

.. code:: yaml

    medium:
      - name: Ubuntu Mirror
        path: "http://archive.ubuntu.com/ubuntu"
        os-family: Debian

-  **name** Model name
-  **path** The path to the medium, can be a URL or a valid NFS server
   (exclusive of the architecture)
-  **os-family** Operating system family, available values: AIX,
   Altlinux, Archlinux, Coreos, Debian, Freebsd, Gentoo, Junos, NXOS,
   Redhat, Solaris, Suse, Windows

Section ``partition-table``
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: yaml

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

-  **name** Partition table name
-  **os-family** Operating system family, available values: AIX,
   Altlinux, Archlinux, Coreos, Debian, Freebsd, Gentoo, Junos, NXOS,
   Redhat, Solaris, Suse, Windows
-  **audit-comment** Comment for the audit log
-  **layout** Partition layout
-  **locked** Whether or not the template is locked for editing

Section ``provisioning-template``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: yaml

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

-  **name** Partition table name
-  **template** The provisioning template itself
-  **snippet** Set to true if template is a snippet only
-  **audit-comment** Comment for the audit log
-  **template\_kind\_id** Template kind id
-  **os**
-  **name** Operating system name, maps to ``os.name``
-  **locked** Whether or not the template is locked for editing

Section ``os``
^^^^^^^^^^^^^^

.. code:: yaml

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

-  **name** Operating system table name
-  **major** The provisioning template itself
-  **minor** Set to true if template is a snippet only
-  **description** Comment for the audit log
-  **family** Operating system family, available values: AIX, Altlinux,
   Archlinux, Coreos, Debian, Freebsd, Gentoo, Junos, NXOS, Redhat,
   Solaris, Suse, Windows
-  **release-name** OS release name
-  **password-hash** Root password hash function to use, one of MD5,
   SHA256, SHA512, Base64
-  **architecture**
-  **name** Architecture name, maps to ``architecture.name``
-  **provisioning-template**
-  **name** Provisioning template name, maps to
   ``provisioning-template.name``
-  **medium**
-  \_\_ name\_\_ Medium name, maps to ``medium.name``
-  **partition-table**
-  **name** Ptable name, maps to ``partition-table.name``
-  **parameters**
-  \_\_ key\_\_ Additional OS settings in format 'keyname': 'keyvalue'

Section ``hostgroup``
^^^^^^^^^^^^^^^^^^^^^

.. code:: yaml

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
        parameters:
          - keyname:  keyvalue

-  **name** Hostgroup name
-  **parent** Parent hostgroup
-  **environment** Environment name, maps to ``environment.name``
-  **os** Operating system name, maps to ``os.name``
-  **architecture** Architecture name, maps to ``architecture.name``
-  **medium** Media name, maps to ``medium.name``
-  **partition-table** Ptable name, maps to ``partition-table.name``
-  **subnet** Subnet name, maps to ``subnet.name``
-  **domain** Domain name, maps to ``domain.name``
-  **parameters** Dict of params -**keyname** Value of param

Section ``host``
^^^^^^^^^^^^^^^^

.. code:: yaml

    host:
      - name: testhost
        domain: lab.local
        architecture: x86_64
        hostgroup: switzerland
        environment: production
        os: Ubuntu 14.04 LTS
        media: Ubuntu Mirror
        partition: Ubuntu Default
        model: VMWare VM
        mac: 00:11:22:33:44:55
        root-pass: supersecret42
        parameters:
          env: prod
          kernel_params: quiet

-  **name** Host name
-  **domain** Domain name, maps to ``domain.name``
-  **architecture** Architecture name, maps to ``architecture.name``
-  **hostgroup** Hostgroup name, maps to ``hostgroup.name``
-  **environment** Environment name, maps to ``environment.name``
-  **os** Operating system name, maps to ``os.name``
-  **media** Media name, maps to ``medium.name``
-  **partition** Ptable name, maps to ``partition.name``
-  **model** Hardware model name, maps to ``model.name``
-  **mac** MAC address
-  **root-pass** Root password
-  **parameters** Dict of params
-  **keyname** Value of param

Section ``roles``
^^^^^^^^^^^^^^^^^

.. code:: yaml

    roles:
      - name: testrole
        permissions:
          architecture:
            - view_architectures
            - edit_architectures
          compute_resources:
            - view_compute_resources
            - create_compute_resources
            - destroy_compute_resources

-  **name** Role name
-  **permissions**
-  **groupname** Name of permission group (not applied to foreman), only
   for clarity

   -  **permission\_name** Permission name, maps to ``permission.name``
   -  **permission\_name** Permission name, maps to ``permission.name``
   -  **permission\_name** Permission name, maps to ``permission.name``
   -  ... ...

Section ``users``
^^^^^^^^^^^^^^^^^

.. code:: yaml

    users:
      - login: testhaaaans
        password: schmetterling42
        mail: haaaans@example.com
        auth-source: ldap-is-not-web-scale
        firstname: Test
        lastname: Haaaaaans
        admin: true
        timezone: UTC
        locale: en

-  **login** User login
-  **password** Password of user
-  **auth-source** Name of auth source or 'INTERNAL' for foreman-own
   auth source
-  **firstname** First name of user
-  **lastname** Last name of user
-  **admin** If ``true``, user will be created with admin permissions
-  **timezone** Timezone for the user
-  **locale** WebUI locale for the user

Section ``usergroups``
^^^^^^^^^^^^^^^^^^^^^^

.. code:: yaml

    usergroups:
      - name: api-test2
        admin: false
        users:
          - name: foo
          - name: burlson
        groups:
          - name: api-testgroup
        ext-usergroups:
          - name: foremangroup
            auth-source-ldap: ldap-is-not-web-scale
        roles:
          - name: foo

-  **name** Usergroup name
-  **admin** If set to true or 1, group is has admin permissions
-  **users** List of users
-  **name** Username, maps to ``users.name``
-  **groups** List of groups
-  **name** Groupname, maps to ``usergroups.name``
-  **ext-usergroups** List of external usergroups
-  **name** Name of the external usergroup
-  **auth-source-ldap** Name of the external auth source, maps to
   ``auth-source-ldap.name``
-  **roles** List of roles
-  **name** Role name, maps to ``role.name``

Section ``auth-source-ldap``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: yaml

    auth-source-ldap:
      - name: ldap-is-not-web-scale
        host: 10.11.12.13
        port: 389
        account: uid=binduser,cn=users,dc=test,dc=example,dc=com
        account-password: 123qwe
        base-dn: dc=test,dc=example,dc=com
        attr-login: uid
        attr-firstname: firstName
        attr-lastname: lastName
        attr-mail: mail
        attr-photo: picture
        onthefly-register: false
        usergroup-sync: false
        tls: false
        groups-base: cn=groups,dc=test,dc=example,dc=com
        ldap-filter:
        server-type: posix

-  **name** Name of the authsource
-  **host** LDAP host
-  **port** Server port
-  **account** Bind account user
-  **account-password** Bind account password
-  **base-dn** LDAP Base DN
-  **attr-login** LDAP attribute for username, required if
   onthefly-register is true
-  **attr-firstname** LDAP attribute for first name, required if
   onthefly-register is true
-  **attr-lastname** LDAP attribute for last name, required if
   onthefly-register is true
-  **attr-mail** LDAP attribute for mail, required if onthefly-register
   is true
-  **attr-photo** LDAP attribute for user photo
-  **onthefly-register** Register users on the fly if ``true`` or ``1``
-  **usergroup-sync** Sync external user groups on login if ``true`` or
   ``1``
-  **tls** If ``true`` or ``1``, use SSL to connect to the server
-  **groups-base** groups base DN
-  **ldap-filter** LDAP filter
-  **server-type** LDAP Server type, valid are ``free_ipa``,
   ``active_directory`` and ``posix``

Cleanup (delete) settings
~~~~~~~~~~~~~~~~~~~~~~~~~

If the keyword ``cleanup`` is provided to foreman-yml, it will try to
delete items specified by its name.

::

    foreman-yml cleanup /path/to/config.yml

Section ``cleanup-[architecture|compute-profile|partition-table|provisioning-template]``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: yaml

    cleanup-[architecture|compute-profile|partition-table|provisioning-template]:
      - name: foo
      - name: bar

Removes specified objects, mapping to object.name - **name**
architecture\|compute-profile\|partition-table\|provisioning-template
name to delete

Hacking
-------

::

    virtualenv --system-site-packages venv-dev
    source venv-dev/bin/activate
    pip install -e .

Future
------

-  Dump current settings
-  Better documentaion

License
-------

GNU GENERAL PUBLIC LICENSE Version 3
