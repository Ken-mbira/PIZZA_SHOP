from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

from app.models import Orders, Pizza, Roles, Size, Toppings, User
from app import app,db

manager = Manager(app)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User,Roles = Roles,Pizza = Pizza,Size = Size,Toppings = Toppings,Orders = Orders)

if __name__ == '__main__':
    manager.run()