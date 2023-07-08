from flaskr.database.db_operation import DbOperation
from flaskr.models.world import City
from flaskr.responses import api_response


class WorldService(DbOperation):
    def __init__() -> None:
        super().__init__()

    def fetch_city(self):
        try:
            self.set_session()
            return self.session().query(City).all()

        except Exception as e:
            print(e)
            return api_response.handle_exception("error発生")
        finally:
            pass
        self.close_session()
