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
            new_status = socialnetwork_model.StatusTable(status_id=status_id, user_id=user_id,
                                status_text=status_text)
            new_status.save()
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
        try:
            row = socialnetwork_model.StatusTable.get(socialnetwork_model.StatusTable.user_id==status_id)
            row.user_id = user_id
            row.status_text = status_text

            row.save()
            return True
        except IntegrityError:
            logger.exception("NEW EXCEPTION")
            return False

    @logger.catch(message="error in UserStatusCollection.delete_status() method")
    def delete_status(self, status_id):
        '''
        deletes the status message with id, status_id
        '''
        try:
            row = socialnetwork_model.StatusTable.get(socialnetwork_model.StatusTable.user_id==status_id)
            row.delete_instance()
            return True
        except IntegrityError:
            logger.exception("NEW EXCEPTION")
            return False

    @logger.catch(message="error in UserStatusCollection.search_status() method")
    def search_status(self, status_id):
        '''
        Find and return a status message by its status_id

        Returns an empty UserStatus object if status_id does not exist
        '''
        try:
            #row = socialnetwork_model.StatusTable.get(socialnetwork_model.StatusTable.user_id==status_id)
            query = (socialnetwork_model.StatusTable
                    .select(socialnetwork_model.StatusTable.status_text)
                    .join(socialnetwork_model.UsersTable)
                    .where(socialnetwork_model.StatusTable.status_id == status_id))

            for row in query:
                return row
            # return status
        except IntegrityError:
            logger.exception("NEW EXCEPTION")
            return False
