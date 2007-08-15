#!/usr/bin/env python
# basic_ftpd.py

"""A basic FTP server which uses a DummyAuthorizer for managing 'virtual
users', defining a customized set of messages to provide to client
and setting a limit for incoming connections.
"""

import os
from pyftpdlib import FTPServer

if __name__ == "__main__":

    # Import a dummy authorizer for managing 'virtual users' 
    authorizer = FTPServer.DummyAuthorizer()
    authorizer.add_user('user', '12345', os.getcwd(), perm=('r', 'w'))
    authorizer.add_anonymous(os.getcwd())

    # Instantiate FTP handler class
    ftp_handler = FTPServer.FTPHandler
    ftp_handler.authorizer = authorizer

    # Define a customized set of messages to provide to client
    ftp_handler.msg_connect = "This is pyftpdlib %s." %FTPServer.__ver__
    ftp_handler.msg_login = "Welcome in."
    ftp_handler.msg_quit = "Goodbye."

    # Instantiate FTP server class and listen to localhost:21
    address = ('127.0.0.1', 21)
    ftpd = FTPServer.FTPServer(address, ftp_handler)

    # set a limit for connections
    ftpd.max_cons = 256
    ftpd.max_cons_per_ip = 5

    # start ftp server
    ftpd.serve_forever()
