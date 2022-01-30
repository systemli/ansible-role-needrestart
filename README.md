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
    
    # Email which will be notified
    needrestart_mail_address: $NR_USERNAME
    
    # Services which should be ignored
    needrestart_ignorelist: []

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
    needrestart_disable_email: 0 
    
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

Tests
-----

Molecule, Docker and Github Actions is used for continous testing.
On the local environment you can easily test the role with

    molecule test 

This requires Molecule, Vagrant and `python-vagrant` to be installed.

License
-------

GPLv3

Author Information
------------------

https://www.systemli.org
