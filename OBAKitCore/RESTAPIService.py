import requests
from datetime import datetime

class RESTAPIService:
    def __init__(self, base_url):
        self.base_url = base_url

    async def get_current_time(self):
        """
        Retrieves the current system time of the OneBusAway server.
        """
        url = f"{self.base_url}/api/where/current-time.json"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            # Extract and parse the time from the response
            time_str = data.get('currentTime')
            if time_str:
                return datetime.fromisoformat(time_str)
            else:
                return None
        else:
            # Handle error cases
            print(f"Failed to fetch current time. Status code: {response.status_code}")
            return None
