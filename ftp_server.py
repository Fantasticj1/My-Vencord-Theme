    from pyftpdlib.authorizers import DummyAuthorizer
    from pyftpdlib.handlers import FTPHandler
    from pyftpdlib.servers import FTPServer

    authorizer = DummyAuthorizer()
    authorizer.add_user('user', 'password', '.', perm='elradfmw') # user, password, home directory, permissions
    authorizer.add_anonymous('.') # anonymous access, '.' is the current directory

    handler = FTPHandler
    handler.authorizer = authorizer

    server = FTPServer(('0.0.0.0', 21), handler) # listen on all interfaces, port 21
    server.serve_forever()
