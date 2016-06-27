#!/usr/bin/python
# -*- coding: utf8 -*-


import sys
import logging
import log
from foremanclient.validator import Validator
from foreman.client import Foreman, ForemanException
from pprint import pprint


class ForemanBase:

    def __init__(self, config, loglevel=logging.INFO):
        logging.basicConfig(level=loglevel)
        self.config = config['foreman']
        self.loglevel = loglevel
        self.validator = Validator()


    def get_config_section(self, section):
        try:
            cfg = self.config[section]
        except:
            cfg = []
        return cfg


    def connect(self):
        try:
            logging.disable(logging.WARNING)
            self.fm = Foreman(self.config['auth']['url'], (self.config['auth']['user'], self.config['auth']['pass']), api_version=2, use_cache=False, strict_cache=False)
            # this is nescesary for detecting faulty credentials in yaml
            self.fm.architectures.index()
            logging.disable(self.loglevel-1)
        except:
            log.log(log.LOG_ERROR, "Cannot connect to Foreman-API")
            sys.exit(1)


    def get_api_error_msg(self, e):
        dr = e.res.json()
        try:
            msg = dr['error']['message']
        except KeyError:
            msg = dr['error']['full_messages'][0]

        return msg


    def get_host(self, host_id):
        host = self.fm.hosts.show(id=host_id)
        return host


    def remove_host(self, host_id):
        try:
            self.fm.hosts.destroy(id=host_id)
            return True
        except:
            return False


    def dict_underscore(self, d):
        new = {}
        for k, v in d.iteritems():
            if isinstance(v, dict):
                v = self.dict_underscore(v)
            new[k.replace('-', '_')] = v
        return new

    def dict_dash(self, d):
        new = {}
        for k, v in d.iteritems():
            if isinstance(v, dict):
                v = self.dict_dash(v)
            new[k.replace('_', '-')] = v
        return new


    def get_audit_ip(self, host_id):
        # this is hacky right now since the audits-api has an bug and does not return any audits whe passing host_id
        # host_audits = self.fm.hosts.audits_index(auditable_id=80)
        #ha = self.fm.hosts.index(auditable_id=81)
        host_audits = []
        host_ip = False
        all_audits = self.fm.audits.index(per_page=99999)['results']

        # get audits of specified host
        for audit in all_audits:
            if ( audit['auditable_type'] == 'Host') and (audit['auditable_id'] == host_id):
                host_audits.append(audit)

        # search for audit type audited_changes['build']
        for audit in host_audits:
            if 'installed_at' in audit['audited_changes']:
                try:
                    ll = len(audit['audited_changes']['installed_at'])
                    host_ip = audit['remote_address']
                    return host_ip
                except:
                    pass

        # nothing found, return False
        return False
