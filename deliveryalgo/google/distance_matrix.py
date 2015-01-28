import json, requests

url = 'https://maps.googleapis.com/maps/api/distancematrix/json'

class DistanceMatrix(object):
    def __init__(self, api_key):
        self.api_key = api_key

    def distance(self, origin, destination):
        result = self.query(origin, destination)
        return self.extract(result, "distance", "value")

    def duration(self, origin, destination):
        result = self.query(origin, destination)
        return self.extract(result, "duration", "value")

    def extract(self, result, parent_key, child_key):
        for row in result["rows"]:
            for element in row["elements"]:
                if parent_key in element and child_key in element[parent_key]:
                    return element[parent_key][child_key]
        return None

    def query(self, origin, destination):
        params = {}
        params["key"] = self.api_key
        params["origins"] = self.parse_address(origin)
        params["destinations"] = self.parse_address(destination)
        resp = requests.get(url=url, params=params)
        result = json.loads(resp.text)
        return result

    def parse_address(self, address):
        # Placeholder method
        parsed_address = address
        return parsed_address
