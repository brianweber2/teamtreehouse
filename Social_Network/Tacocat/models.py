from flask_login import UserMixin
from flask_bcrypt import generate_password_hash, check_password_hash
from peewee import *


DATABASE = SqliteDatabase('tacos.db')

class User(UserMixin, Model):
    email = CharField(unique=True)
    password = CharField(max_length=100)
    
    class Meta:
        database = DATABASE
        
    @classmethod
    def create_user(cls, email, password):
        try:
            with DATABASE.transaction():
                cls.create(
                    email=email,
                    password=generate_password_hash(password)
                )
        except IntegrityError:
            raise ValueError("User already exists.")
        
        
class Taco(Model):
    user = ForeignKeyField(
        rel_model=User,
        related_name='tacos'
    )
    protein = CharField()
    shell = CharField()
    cheese = BooleanField()
    extras = TextField()
    
    class Meta:
        database = DATABASE
        
    @classmethod
    def taco_creation(cls, user, protein, shell, cheese, extras):
        with DATABASE.transaction():
            cls.create(
                user=user,
                protein=protein,
                shell=shell,
                cheese=cheese,
                extras=extras
            )
        
        
def intialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Taco], safe=True)
    DATABASE.close()