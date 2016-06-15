#!/usr/bin/python
# -*- coding: utf8 -*-

import yaml
import sys
from foremanclient import foreman
import log



def main():
    global LOGLEVEL
    try:
        config_file = open(sys.argv[1], 'r')
        config = yaml.load(config_file)
        config_file.close()
    except:
        log.log(log.LOG_ERROR, "Failed to load/parse config")
        sys.exit(1)


    fm = foreman(config)
    fm.connect()

    # cleanup architecture
    fm.process_cleanup_arch()

    # cleanup compute profiles
    fm.process_cleanup_computeprfl()

    # cleanup medium
    fm.process_cleanup_medium()

    # cleanup partition table
    fm.process_cleanup_ptable()

    # cleanup provisioning template
    fm.process_cleanup_provisioningtpl()

    # setting
    fm.process_config_settings()

    # architecture
    fm.process_config_arch()

    # smart proxy
    fm.process_config_smartproxy()

    # domain
    fm.process_config_domain()

    # subnet
    fm.process_config_subnet()

    # environment
    fm.process_config_enviroment()

    # model
    fm.process_config_model()

    # medium
    fm.process_config_medium()

    # partition table
    fm.process_config_ptable()

    # operating system
    fm.process_config_os()

    # provisioning template
    fm.process_config_provisioningtpl()

    # hostgroup
    fm.process_config_hostgroup()

    # Link items to operating system
    fm.process_config_os_link()

    # Link template-combination-attribute
    fm.process_template_combination_attribute()

    # host
    fm.process_config_host()

    # enterprise edition only: ldap
    fm.process_auth_sources_ldap()

    # user groups
    fm.process_usergroups()

    # roles
    fm.process_roles()



if __name__ == '__main__':
    main()
