'''
main driver for a simple social network project
'''
from csv import DictReader
import users
import user_status
import pandas as pd

def init_user_collection():
    '''
    Creates and returns a new instance of UserCollection
    '''
    user = users.UserCollection()
    return user



def init_status_collection():
    '''
    Creates and returns a new instance of UserStatusCollection
    '''
    status = user_status.UserStatusCollection()
    return status

def load_users(filename, user_collection):
    '''
    Opens a CSV file with user data and
    adds it to an existing instance of
    UserCollection

    Requirements:
    - If a user_id already exists, it
    will ignore it and continue to the
    next.
    - Returns False if there are any errors
    (such as empty fields in the source CSV file)
    - Otherwise, it returns True.
    '''
    try:
        with open(filename, mode ='r', encoding='utf-8') as file:
            csv_dict_reader = DictReader(file)
            for row in csv_dict_reader:
                user_collection.add_user(row['USER_ID'],row['EMAIL'],row['NAME'],row['LASTNAME'])
    except FileNotFoundError:
        print('Error! File not found')
    return True


def load_status_updates(filename, status_collection):
    '''
    Opens a CSV file with status data and adds it to an existing
    instance of UserStatusCollection

    Requirements:
    - If a status_id already exists, it will ignore it and continue to
      the next.
    - Returns False if there are any errors(such as empty fields in the
      source CSV file)
    - Otherwise, it returns True.
    '''
    pass


def add_user(user_id, email, user_name, user_last_name, user_collection):
    '''
    Creates a new instance of User and stores it in user_collection
    (which is an instance of UserCollection)

    Requirements:
    - user_id cannot already exist in user_collection.
    - Returns False if there are any errors (for example, if
      user_collection.add_user() returns False).
    - Otherwise, it returns True.
    '''
    new_user = user_collection.add_user(user_id,email,user_name,user_last_name)
    return new_user


def update_user(user_id, email, user_name, user_last_name, user_collection):
    '''
    Updates the values of an existing user

    Requirements:
    - Returns False if there any errors.
    - Otherwise, it returns True.
    '''
    updated_user = user_collection.modify_user(user_id, email, user_name, user_last_name)
    return updated_user


def delete_user(user_id, user_collection):
    '''
    Deletes a user from user_collection.

    Requirements:
    - Returns False if there are any errors (such as user_id not found)
    - Otherwise, it returns True.
    '''
    purge_id = user_collection.delete_user(user_id)
    return purge_id

def search_user(user_id, user_collection):
    '''
    Searches for a user in user_collection(which is an instance of
    UserCollection).

    Requirements:
    - If the user is found, returns the corresponding User instance.
    - Otherwise, it returns None.
    '''
    find_user = user_collection.search_user(user_id)
    return find_user


def add_status(user_id, status_id, status_text, status_collection):
    '''
    Creates a new instance of UserStatus and stores it in
    user_collection(which is an instance of UserStatusCollection)

    Requirements:
    - status_id cannot already exist in user_collection.
    - Returns False if there are any errors (for example, if
      user_collection.add_status() returns False).
    - Otherwise, it returns True.
    '''
    new_status = status_collection.add_status(user_id, status_id, status_text)
    return new_status


def update_status(status_id, user_id, status_text, status_collection):
    '''
    Updates the values of an existing status_id

    Requirements:
    - Returns False if there any errors.
    - Otherwise, it returns True.
    '''
    modify_status = status_collection.modify_status(user_id, status_id, status_text)
    return modify_status


def delete_status(status_id, status_collection):
    '''
    Deletes a status_id from user_collection.

    Requirements:
    - Returns False if there are any errors (such as status_id not found)
    - Otherwise, it returns True.
    '''
    purge_id = status_collection.delete_status(status_id)
    return purge_id


def search_status(status_id, status_collection):
    '''
    Searches for a status in status_collection

    Requirements:
    - If the status is found, returns the corresponding
    UserStatus instance.
    - Otherwise, it returns None.
    '''
    find_status = status_collection.search_status(status_id)
    return find_status
