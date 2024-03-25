import unittest
from unittest.mock import AsyncMock
from datetime import datetime
from RESTAPIService import RESTAPIService

class CurrentTimeModelOperationTests(unittest.IsolatedAsyncioTestCase):
    async def test_get_current_time(self):
        # Mocking RESTAPIService for testing purposes
        rest_service = RESTAPIService("https://example.com")
        
        # Mocking the response from the API
        mock_response = {
            "currentTime": "2022-03-15T12:34:56Z"
        }
        
        # Patching the requests.get method to return the mock response
        with unittest.mock.patch('requests.get') as mock_get:
            mock_get.return_value.__aenter__.return_value.json = AsyncMock(return_value=mock_response)
            
            # Call the method being tested
            current_time = await rest_service.get_current_time()
            
            # Assertion
            self.assertEqual(current_time, datetime.fromisoformat("2022-03-15T12:34:56"))
