
from collections import UserDict
from app import create_app,db
from app.models import *

from flask_script import Manager,Server,Shell



app = create_app('development')
manager = Manager(app)


manager.add_command('server',Server)

@manager.command
def test():
    import unittest
    test=unittest.TestLoader().discover('tests')
    

@manager.shell
def add_shell_context():
    return dict(app=app,db=db,User=UserDict)

if __name__=='__main__':
    manager.run()