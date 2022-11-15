"""
These functions use Promises and setTimeouts to mock HTTP requests to a third part NLP service
and should be replaced with the actual HTTP calls when implementing.
"""

from typing import List
from smskillsdk.models.api import Memory, MemoryScope, Intent


def mock_init_actions():
    """
    Example of an action performed by the Initalize ednpoint
    """

    print("Pre-training initialized. . .")
    print("Pre-training completed")

def mock_init_resources(session_id: str) -> List[Memory]:
    """
    Example of an action performed by the Session ednpoint
    """

    private_memory = Memory(**{
        "session_id": session_id,
        "name": "private json memory",
        "value": { "example": "object" },
        "scope": MemoryScope.PRIVATE,
    })
    public_memory = Memory(**{
        "session_id": session_id,
        "name": "public string memory",
        "value": "This is to be persisted",
        "scope": MemoryScope.PUBLIC,
    })

    return [private_memory, public_memory]

def mock_get_response(user_input: str):
    """
    Example of an action performed by the Execute ednpoint
    """

    print(f"User said: {user_input}")

    # Response to be spoken by your Digital Person
    response = "Hello! @showcards(card) Here is a kitten."

    # Add your Cards as required
    cards = {
        "card": {
            "type": "image",
            "data": {
                "url": "https://placekitten.com/200/200",
                "alt": "An adorable kitten",
            },
        },
    }

    # Add your Intent as required
    intent = Intent(
        name="Welcome",
        confidence=1,
    )
  
    # If applicable, add your conversation annotations to see metrics for your Skill on Studio Insights
    annotations = {
        "conv_tag": "Skill.BaseTemplate", 
        "conv_id": intent.name, 
        "conv_intent": intent.name, 
        "conv_type": "Entry",
    }

    return response, cards, intent, annotations