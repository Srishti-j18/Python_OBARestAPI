import sys
sys.path.append("../OBAKitCore")  # Adjust the relative path as needed

from unittest.mock import AsyncMock
from RESTAPIService import RESTAPIService

class CurrentTimeModelOperationTests:
    async def test_get_current_time_success(self):
        # Mocking RESTAPIService for testing purposes
        rest_service = RESTAPIService("https://example.com")

        # Mocking the response from the API
        mock_response = {
            "currentTime": 1343587068277
        }

        # Patching the requests.get method to return the mock response
        with unittest.mock.patch('requests.get') as mock_get:
            mock_get.return_value.__aenter__.return_value.json = AsyncMock(return_value=mock_response)

            # Call the method being tested
            response = await rest_service.get_current_time()

            # Assertion
            assert response.currentTime == 1343587068277
