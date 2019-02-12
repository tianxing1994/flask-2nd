from flask_script import Manager
from flask_migrate import MigrateCommand
from app import createapp
from app import apis

app = createapp()
manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()