from flask_script import Manager
from sqlalchemy import Column, String, Integer
from flask_migrate import Migrate, MigrateCommand
from datetime import datetime

from app import create_app
from models import db, Movie, Actor

app = create_app()

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


@manager.command
def seed():
    Movie(title='Terminator Dark Fate', release_date='2019-05-06').insert()
    Movie(title='Terminator Rise of the machines',
          release_date='2003-05-06').insert()

    Actor(name='Will Smith', age=40, gender='male').insert()
    Actor(name='Bruce Wills', age=50, gender='male').insert()


if __name__ == '__main__':
    manager.run()
