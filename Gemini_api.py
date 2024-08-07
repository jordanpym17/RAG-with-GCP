from typing import List
from google.api_core.client_options import ClientOptions
from google.cloud import discoveryengine_v1 as discoveryengine

# TODO(developer): Uncomment these variables before running the sample.
project_id = "your project ID"
location = "global"  # Values: "global", "us", "eu"
data_store_id = "your data store"

def multi_turn_search_sample(
    project_id: str,
    location: str,
    data_store_id: str,
) -> None:
    client_options = (
        ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
        if location != "global"
        else None
    )

    # Create a client
    client = discoveryengine.ConversationalSearchServiceClient(
        client_options=client_options
    )

    # Initialize Multi-Turn Session
    parent = f"projects/{project_id}/locations/{location}/dataStores/{data_store_id}"
    conversation = client.create_conversation(
        parent=parent,
        conversation=discoveryengine.Conversation(),
    )

    while True:
        search_query = input("Enter your query (or type 'exit' to end): ")
        if search_query.lower() == 'exit':
            break

        # Add new message to session
        request = discoveryengine.ConverseConversationRequest(
            name=conversation.name,
            query=discoveryengine.TextInput(input=search_query),
            serving_config=f"{parent}/servingConfigs/default_config",
            summary_spec=discoveryengine.SearchRequest.ContentSearchSpec.SummarySpec(
                summary_result_count=3,
                include_citations=True,
            ),
        )
        response = client.converse_conversation(request)
        print(f"Reply: {response.reply.summary.summary_text}\n")


# Function to initialize the client and conversation
def initialize_conversation(project_id: str, location: str, data_store_id: str):
    client_options = (
        ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
        if location != "global"
        else None
    )

    client = discoveryengine.ConversationalSearchServiceClient(
        client_options=client_options
    )

    parent = f"projects/{project_id}/locations/{location}/dataStores/{data_store_id}"
    conversation = client.create_conversation(
        parent=parent,
        conversation=discoveryengine.Conversation(),
    )

    return client, conversation.name, parent

# Function to handle conversation
def converse_conversation(client, conversation_name, parent, search_query):
    request = discoveryengine.ConverseConversationRequest(
        name=conversation_name,
        query=discoveryengine.TextInput(input=search_query),
        serving_config=f"{parent}/servingConfigs/default_config",
        summary_spec=discoveryengine.SearchRequest.ContentSearchSpec.SummarySpec(
            summary_result_count=3,
            include_citations=True,
             model_spec=discoveryengine.SearchRequest.ContentSearchSpec.SummarySpec.ModelSpec(
                version="gemini-1.0-pro-002/answer_gen/v1",
            ),
        ),
    )
    response = client.converse_conversation(request)
    return response


#multi_turn_search_sample(project_id, location, data_store_id)



