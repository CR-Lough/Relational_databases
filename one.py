from sqlite3 import IntegrityError
import socialnetwork_model
from loguru import logger
import pandas as pd

# load_dict = pd.read_csv('status_updates.csv')
# load_dict.columns = load_dict.columns.str.lower()
# load_dict = load_dict.to_dict(orient='records')

# with socialnetwork_model.db.atomic():
#     for idx in range(0, len(load_dict), 100):
#         socialnetwork_model.StatusTable.insert_many(load_dict[idx:idx+100]).execute()

query = (socialnetwork_model.StatusTable
        .select(socialnetwork_model.StatusTable.status_text)
        .join(socialnetwork_model.UsersTable)
        .where(socialnetwork_model.StatusTable.status_id == 'Nelli.Wayolle71_708'))
# for row in query:
#     print(f'{row.status_text}')
print(query)
