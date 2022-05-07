'''
Classes for user information for the social network project
'''
# pylint: disable=R0903
from sqlite3 import IntegrityError
import socialnetwork_model
from loguru import logger

logger.add("out_{time:YYYY.MM.DD}.log", backtrace=True, diagnose=True)

class UserCollection():
    '''
    Contains a collection of Users objects
    '''
    @logger.catch(message="error in UserCollection __init__")
    def __init__(self):
        self.database = {}

    @logger.catch(message="error in UserCollection.add_user() method")
    def add_user(self, user_id, email, user_name, user_last_name):
        '''
        Adds a new user to the collection
        '''
        try:

        # if user_id in self.database:
        #     # Rejects new status if status_id already exists
        #     return False
            new_user = socialnetwork_model.UsersTable(user_id=user_id, user_email=email,
                                                    user_name=user_name,
                                                    user_last_name=user_last_name)
            new_user.save()
            return True
        except IntegrityError:
            logger.exception("NEW EXCEPTION")
            return False
   #     self.database[user_id] = new_user
        # return True

    @logger.catch(message="error in UserCollection.modify_user() method")
    def modify_user(self, user_id, email, user_name, user_last_name):
        '''
        Modifies an existing user
        '''
        if user_id not in self.database:
            return False
        self.database[user_id].email = email
        self.database[user_id].user_name = user_name
        self.database[user_id].user_last_name = user_last_name
        return True

    @logger.catch(message="error in UserCollection.delete_user() method")
    def delete_user(self, user_id):
        '''
        Deletes an existing user
        '''
        if user_id not in self.database:
            return False
        del self.database[user_id]
        return True

    @logger.catch(message="error in UserCollection.search_user() method")
    def search_user(self, user_id):
        '''
        Searches for user data
        '''
        if user_id not in self.database:
            return Users(None, None, None, None)
        return self.database[user_id]
