#!/usr/bin/python3

import paramiko

ssh=paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

