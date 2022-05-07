'''
classes to manage the user status messages
'''
# pylint: disable=R0903
from sqlite3 import IntegrityError
import socialnetwork_model
from loguru import logger

logger.add("out_{time:YYYY.MM.DD}.log", backtrace=True, diagnose=True)

class UserStatusCollection():
    '''
    Collection of UserStatus messages
    '''
    @logger.catch(message="error in UserStatusCollection __init__")
    def __init__(self):
        self.database = {}

    @logger.catch(message="error in UserStatusCollection.add_status() method")
    def add_status(self, status_id, user_id, status_text):
        '''
        add a new status message to the collection
        '''
        try:
            new_user = socialnetwork_model.UsersTable(user_id=user_id, user_email=email,
                                                    user_name=user_name,
                                                    user_last_name=user_last_name)
            new_user.save()
            return True
        except IntegrityError:
            logger.exception("NEW EXCEPTION")
            return False

    @logger.catch(message="error in UserStatusCollection.modify_status() method")
    def modify_status(self, status_id, user_id, status_text):
        '''
        Modifies a status message

        The new user_id and status_text are assigned to the existing message
        '''
        if status_id not in self.database:
            # Rejects update is the status_id does not exist
            return False
        self.database[status_id].user_id = user_id
        self.database[status_id].status_text = status_text
        return True

    @logger.catch(message="error in UserStatusCollection.delete_status() method")
    def delete_status(self, status_id):
        '''
        deletes the status message with id, status_id
        '''
        if status_id not in self.database:
            # Fails if status does not exist
            return False
        del self.database[status_id]
        return True

    @logger.catch(message="error in UserStatusCollection.search_status() method")
    def search_status(self, status_id):
        '''
        Find and return a status message by its status_id

        Returns an empty UserStatus object if status_id does not exist
        '''
        if status_id not in self.database:
            # Fails if the status does not exist
            return UserStatus(None, None, None)
        return self.database[status_id]
