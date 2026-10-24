ansible-role-needrestart
================

[![Build Status](https://github.com/systemli/ansible-role-needrestart/workflows/Integration/badge.svg?branch=main)](https://github.com/systemli/ansible-role-needrestart/actions?query=workflow%3AIntegration)
[![Ansible Galaxy](http://img.shields.io/badge/ansible--galaxy-needrestart-blue.svg)](https://galaxy.ansible.com/systemli/needrestart/)

Role to install & maintain needrestart

Role Variables
--------------

Defaults:

    # Admins should be informed via email
    needrestart_notifyd_disable_email: 0
    
    # All other notifications should be disabled
    needrestart_notifyd_disable_write_tty: 1
    needrestart_notifyd_disable_needrestart_session: 1
    needrestart_notifyd_disable_notify_send: 1
    
    # Restart services (l)ist only, (i)nteractive or (a)utomatically.
    needrestart_action: l
    
    # Enable/disable (1/0) CPU microcode update hints; default: 1=enable
    needrestart_ucodehints: 1

    # Email which will be notified
    needrestart_mail_address: $NR_USERNAME
    
    # Services which should be ignored for restart
    # Note: services listed here will not be automatically restarted but will be still reported
    #       in order to ignore services completely incl. nagios check, use needrestart_blacklist_rc
    # Example:
    # needrestart_ignorelist:
    #   onlyoffice:
    #     - rabbitmq-server\.service
    needrestart_ignorelist: {}

    # Services blacklisted as regex
    # Example:
    # needrestart_blacklist_rc:
    #   - cron\.service
    needrestart_blacklist_rc: []
    
    # Blacklist binaries as regex
    # Example:
    # needrestart_blacklist_bin:
    #   - /opt/.*/java
    needrestart_blacklist_bin: []

    # Blacklist files as regex
    # Example:
    # needrestart_blacklist_interp:
    #   - /nexus-data/.*/bundle.jar
    needrestart_blacklist_interp: []

    # needrestart check_mk related
    needrestart_checkmk_localcheckdir: /usr/lib/check_mk_agent/local
    needrestart_checkmk_localcheck: False
    needrestart_checkmk_mrpe: False

    # Override old needrestart.conf
    needrestart_update_needrestart_conf: False

    # Custom needrestart scripts
    # Example:
    # needrestart_restartd:
    #   - name: unbound
    #     script: "systemctl restart unbound.service"
    needrestart_restartd: []

Download
--------

Download latest release with `ansible-galaxy`

	ansible-galaxy install systemli.needrestart

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: systemli.needrestart }

Extended Variables Example
--------------------------

   
    # Admins should be informed via email
    needrestart_notifyd_disable_email: 0 
    
    ## Restart services (l)ist only, (i)nteractive or (a)utomatically. 
    needrestart_action: a
    
    # Email which will be notified, when a service should be restarted 
    needrestart_mail_address: admin@mydomain.com
    
    # Ignore services below during automatic restart
    needrestart_ignorelist:
      groupname:
         - servicename
      Databases:
         - mysql
         - mongodb
      Mail:
         - exim4
         - dovecot
      Webservers:
        - apache2

Testing & Development
---------------------

Molecule with the Docker driver and GitHub Actions is used for continuous
testing. CI runs the role on Debian 13 (trixie) and Debian 12 (bookworm).
On the local environment you can test the role (Debian 13 container) with

    molecule test

or keep the container around while developing:

    molecule converge
    molecule login

This requires Docker (or a compatible container runtime), `molecule`,
`molecule-plugins[docker]` and `ansible-lint` to be installed.

License
-------

GPLv3

Author Information
------------------

https://www.systemli.org
