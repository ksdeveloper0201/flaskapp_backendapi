from flaskr.services.world_service import WorldService


class WorldProvider():
    def __init__(self):
        self.world_service = WorldService()

    def get_city_list(self):
        city_list = self.world_service.fetch_city()
        data = []
        for city in city_list:
            data.append({
                "id": city.id,
                "name": city.name,
                "country_code": city.country_code,
                "district": city.district,
                "population": city.population
            })
        return data
