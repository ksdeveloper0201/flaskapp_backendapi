from flaskr.database.database import db_operation


class WorldService(db_operation.DbOperation):
    def fetch_world(self):
        self.set_settion()
