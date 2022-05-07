from datetime import date
import os
from peewee import *
import peewee
from loguru import logger

db = SqliteDatabase('twitter.db')

class UsersTable(Model):
    user_id = CharField(primary_key=True, max_length=30, unique=True)
    user_name = CharField(max_length=30)
    user_last_name = CharField(max_length=100)
    user_email = TextField()

    class Meta:
        database = db  # This model uses the "twitter.db" database.
        constraints = [peewee.Check("LENGTH(user_id) < 30"),
                        peewee.Check("LENGTH(user_name) < 30"),
                        peewee.Check("LENGTH(user_last_name) < 100")]

class StatusTable(Model):
    status_id = CharField(primary_key=True, unique=True)
    user_id = ForeignKeyField(UsersTable, backref='statuses', on_delete='CASCADE')
    status_text = TextField()

    class Meta:
        database = db  # this model uses the "twitter.db" database

def create_tables(database):
    database.create_tables([UsersTable, StatusTable])


# def add_data():
#     new_user = UsersTable(user_id='1', user_name='bob', user_last_name='murphy', user_email='bm.gmail.com')
#     new_user.save()  # bob is now stored in the database

#     # alt
#     grandma = Person.create(name='Grandma', birthday=date(1935, 3, 1))
#     herb = Person.create(name='Herb', birthday=date(1950, 5, 5))
#     grandma.save()
#     herb.save()
#     return uncle_bob, grandma, herb


# def update_data(grandma):
#     grandma.name = 'Grandma L.'
#     grandma.save()  # Update grandma's name in the database.


# def set_pet_owners():
#     bob_kitty = Pet.create(owner=uncle_bob, name='Kitty', animal_type='cat')
#     herb_fido = Pet.create(owner=herb, name='Fido', animal_type='dog')
#     herb_mittens = Pet.create(owner=herb, name='Mittens', animal_type='cat')
#     herb_mittens_jr = Pet.create(
#         owner=herb, name='Mittens Jr', animal_type='cat')
#     return bob_kitty, herb_fido, herb_mittens, herb_mittens_jr


# def delete_pet(herb_mittens):

#     herb_mittens.delete_instance()


# def show_someones_pets():
#     # 1
#     Person.get(Person.name == 'Grandma L.')

#     for person in Person.select():
#         print(person.name)

#     # 2
#     query = (Pet
#              .select(Pet, Person)
#              .join(Person)
#              .where(Pet.animal_type == 'cat'))

#     for pet in query:
#         print(pet.name, pet.owner.name)

#     # 3
#     for pet in Pet.select().join(Person).where(Person.name == 'Bob'):
#         print(pet.name)

# if __name__ == "__main__":
#     db.connect()
#     create_tables(db)
# #     uncle_bob, grandma, herb = add_data()
# #     update_data(grandma)
# #     bob_kitty, herb_fido, herb_mittens, herb_mittens_jr = set_pet_owners()
# #     delete_pet(herb_mittens)
# #     show_someones_pets()
#     db.close()
