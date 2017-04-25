#!/usr/bin/python
# -*- coding: utf8 -*-


from voluptuous import Schema, Required, All, Optional, Any


class Validator:

    def __init__(self):

        self.arch = Schema({
            Required('name'):                           All(str),
        })

        self.domain = Schema({
            Required('name'):                           All(str),
            Optional('fullname'):                       Any(str, None),
            Optional('dns-proxy'):                      Any(str, None),
            Optional('parameters'):                     Any(dict, None)
        })

        self.enviroment = Schema({
            Required('name'):                           All(str)
        })

        self.model = Schema({
            Required('name'):                           All(str),
            Optional('info'):                           Any(str, None),
            Optional('vendor-class'):                   Any(str, None),
            Optional('hardware-model'):                 Any(str, None)
        })

        self.medium = Schema({
            Required('name'):                           All(str),
            Required('path'):                           All(str),
            Required('os-family'):                      All(str),
        })

        self.ptable = Schema({
            Required('name'):                           All(str),
            Required('layout'):                         All(str),
            Optional('snippet'):                        Any(bool,None),
            Optional('os-family'):                      Any(str,None),
            Optional('audit-comment'):                  Any(str,None),
            Optional('locked'):                         Any(bool,None),
        })

        self.provt = Schema({
            Required('name'):                           All(str),
            Required('template'):                       All(str),
            Optional('snippet'):                        Any(bool,None),
            Optional('audit-comment'):                  Any(str,None),
            Optional('template-kind-id'):               Any(int,None),
            Optional('template-combination-attribute'): Any(int, list, dict, None),
            Optional('locked'):                         Any(bool,None),
            Optional('os'):                             Any(None, Schema([{
                Required('name'):                       All(str)
            }]))
        })

        self.os = Schema({
            Required('name'):                           All(str),
            Required('major'):                          Any(str, int),
            Required('minor'):                          Any(str, int),
            Optional('description'):                    Any(str, None),
            Optional('family'):                         Any(str, None),
            Optional('release-name'):                   Any(str, None),
            Optional('parameters'):                     Any(dict, None),
            Optional('password-hash'):                  Any(
                                                            'MD5',
                                                            'SHA256',
                                                            'SHA512',
                                                            'Base64',
                                                            None
                                                            ),
            Optional('architecture'):                   Any(None, Schema([{
                Required('name'):                       All(str)
            }])),
            Optional('provisioning-template'):          Any(None, Schema([{
                Required('name'):                       All(str)
            }])),
            Optional('medium'):                         Any(None, Schema([{
                Required('name'):                       All(str)
            }])),
            Optional('partition-table'):                Any(None, Schema([{
                Required('name'):                       All(str)
            }]))
        })

        self.host = Schema({
            Required('name'):                           All(str),
            Required('template'):                       All(str),
            Optional('snippet'):                        Any(bool, None),
            Optional('audit-comment'):                  Any(str, None),
            Optional('mac'):                            Any(str, None),
            Optional('template-kind-id'):               Any(int, None),
            Optional('template-combination-attribute'): Any(int, None),
            Optional('locked'):                         Any(bool, None),
            Optional('hostgroup'):                      Any(str, None),
            Optional('location'):                       Any(str, None),
            Optional('organization'):                   Any(str, None),
            Optional('parameters'):                     Any(dict, None),
            Optional('os'):                             Any(None, Schema([{
                Required('name'):                       All(str)
            }]))
        })

        self.hostgroup = Schema({
            Required('name'):                           All(str),
            Optional('parent'):                         Any(str, None),
            Optional('environment'):                    Any(str, None),
            Optional('os'):                             Any(str, None),
            Optional('architecture'):                   Any(str, None),
            Optional('medium'):                         Any(str, None),
            Optional('partition-table'):                Any(str, None),
            Optional('domain'):                         Any(str, None),
            Optional('subnet'):                         Any(str, None),
            Optional('parameters'):                     Any(dict, None)
        })

        self.smartproxy = Schema({
            Required('name'):                           All(str),
            Required('url'):                            All(str),
        })

        self.setting = Schema({
            Required('name'):                           All(str),
            Optional('value'):                          Any(list, str, bool,
                                                            int, None),
        })

        self.subnet =  Schema({
            Required('name'):                           All(str),
            Required('network'):                        All(str),
            Required('mask'):                           All(str),
            Optional('gateway'):                        Any(str, None),
            Optional('dns-primary'):                    Any(str, None),
            Optional('dns-secondary'):                  Any(str, None),
            Optional('ipam'):                           Any('DHCP', 'Internal DB', 'None', None),
            Optional('from'):                           Any(str, None),
            Optional('to'):                             Any(str, None),
            Optional('vlanid'):                         Any(str, int, None),
            Optional('domain'):                         Any(None, Schema([{
                Required('name'):                       All(str)
            }])),
            Optional('dhcp-proxy'):                     Any(str, None),
            Optional('tftp-proxy'):                     Any(str, None),
            Optional('dns-proxy'):                      Any(str, None),
            Optional('boot-mode'):                      Any('Static', 'DHCP', None),
            Optional('boot-mode'):                      Any('Static', 'DHCP', None),
            Optional('network-type'):                   Any('IPv4', 'IPv6', None),
        })

        self.cleanup_arch = Schema({
            Required('name'):                           All(str)
        })

        self.cleanup_computeprfl = Schema({
            Required('name'):                           All(str)
        })

        self.cleanup_medium = Schema({
            Required('name'):                           All(str)
        })

        self.cleanup_ptable = Schema({
            Required('name'):                           All(str)
        })

        self.cleanup_provt = Schema({
            Required('name'):                           All(str)
        })

        self.role = Schema({
            Required('name'):                           All(str),
            Optional('permissions'):                    Any(list, dict, None)
        })

        self.usergroup = Schema({
            Required('name'):                           All(str),
            Optional('users'):                          Any(list, None),
            Optional('groups'):                         Any(list, None),
            Optional('ext-usergroups'):                 Any(list, None),
            Optional('roles'):                          Any(list, None),
            Optional('admin'):                          Any(bool, None)
        })

        self.user = Schema({
            Required('login'):                         All(str),
            Required('password'):                      All(str),
            Required('mail'):                          All(str),
            Optional('auth-source'):                   Any(str, None),
            Optional('firstname'):                     Any(str, None),
            Optional('lastname'):                      Any(str, None),
            Optional('admin'):                         Any(bool, None),
            Optional('timezone'):                      Any(str, None),
            Optional('locale'):                        Any(str, None),
        })

        self.auth_source_ldaps = Schema({
            Required('name'):                           All(str),
            Required('host'):                           All(str),
            Optional('port'):                           Any(int, str, None),
            Optional('account'):                        Any(str, None),
            Optional('account-password'):               Any(str, None),
            Optional('base-dn'):                        Any(str, None),
            Optional('attr-login'):                     Any(str, None),
            Optional('attr-firstname'):                 Any(str, None),
            Optional('attr-lastname'):                  Any(str, None),
            Optional('attr-mail'):                      Any(str, None),
            Optional('attr-photo'):                     Any(str, None),
            Optional('onthefly-register'):              Any(bool, int, None),
            Optional('usergroup-sync'):                 Any(bool, int, None),
            Optional('tls'):                            Any(bool, int, None),
            Optional('groups-base'):                    Any(str, None),
            Optional('ldap-filter'):                    Any(str, None),
            Optional('server-type'):                    Any('free_ipa',
                                                            'active_directory',
                                                            'posix',
                                                            None
                                                            )
        })
