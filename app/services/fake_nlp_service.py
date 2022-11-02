from fastapi import HTTPException
from ..mocks.mock_request import mock_get_response, mock_init_resources, mock_init_actions
from smskillsdk.models.api import MemoryScope

class FakeNLPService:
    first_credentials: str
    second_credentials: str

    def __init__(self, first_credentials, second_credentials):
        self.first_credentials = first_credentials
        self.second_credentials = second_credentials
        self.__authenticate()
  
    def __authenticate(self):
        """
        Example of using credentials to authenticate
        """

        if (not (self.first_credentials and self.second_credentials)):
          raise HTTPException(status_code = 401, detail = "Unauthenticated")
        print("Authenticated!")

    def init_actions(self):
        """
        Example of initializing Skill-specific actions on third party NLP call
        """

        return mock_init_actions()

    def init_session_resources(self, session_id: str):
        """
        Example of initializing resources with third party NLP call 
        """
        
        return mock_init_resources(session_id)


    def persist_credentials(self, session_id: str):
        """
        Example of persisting credentials during session endpoint with third party NLP call 
        """

        credentials = {
          "first_credentials": self.first_credentials, "second_credentials": self.second_credentials
        }

        credentials_memory = {
          "key": "credentials",
          "value": credentials,
          "session_id": session_id,
          "scope": MemoryScope.PRIVATE,
        }

        return credentials_memory

    def send(self, user_input: str):
        """
        Example of sending input to the third party NLP call 
        """

        return mock_get_response(user_input)