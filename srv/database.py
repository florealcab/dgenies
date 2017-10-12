import datetime
from config_reader import AppConfigReader
from pony.orm import Database, Required, Optional

config_reader = AppConfigReader()
file_path = config_reader.get_database()

db = Database()
db.bind(provider='sqlite', filename=file_path, create_db=True)


class Job(db.Entity):
    id_job = Required(str)
    email = Required(str)
    id_process = Optional(int)
    batch_type = Required(str)
    status = Required(str, default="submitted")
    date_created = Required(datetime.datetime)


db.generate_mapping(create_tables=True)