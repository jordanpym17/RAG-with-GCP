# GCP-based Retrieval-Augmented Generation (RAG) System

<p style="color:blue; font-size:20px;">Welcome to the GCP-based Retrieval-Augmented Generation (RAG) System repository. This project leverages Google Cloud Platform (GCP) to build a scalable RAG system for handling large amounts of data. The data, originating from various formats and conditions, undergoes preprocessing before being ingested into a GCP Datastore. The system uses the Gemini API for data search and summary, with a user interface built using Streamlit.</p>

## Overview

This project involves several key steps:

1. **Local Database Creation**: Build a local version of the company's database.
2. **Data Preprocessing**: Convert and format data files from various formats (doc, pdf) to a consistent format.
3. **Cloud Storage**: Store the processed data in GCP Cloud Buckets.
4. **Datastore Creation**: Use GCP Console to create a scalable Datastore, serving as the vector database.
5. **API Integration**: Utilize the Vertexai API for data search and summary generation.
6. **User Interface**: Implement a Streamlit-based UI for interaction.


## Google Cloud Console

1. **GCP account setup**:
   - Create Google cloud account
   - Upload documents to cloud storage bucket (only .pdf/doc)
   - Create data store and import storage bucket (use ** after path to include sub-directories)
   - Create a search app in agent builder and link to data store
   - Test search bot in preview tap

## Installation for local deployment 

1. **Install Google cloud CLI**:

I used the SDK installer: https://cloud.google.com/sdk/docs/install#installation_instructions
This is for Authorization during development. Be sure to setup the CLI in the SDK manager with your google accound and setup the ADC. 

2. **Clone the repository**:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. **Create a virtual environment**:

First navigate to project directory 
    ```sh
    python -m venv search_venv   # On Windows
    python -m venv search_venv   # Activate environment
    ```

5. **Install the dependencies**:

    ```sh
    pip install -r .\requirements.txt
    ```
6. **Fill in project details**
Fill in project_id, location, engine_id, data_store_id in the app.py, api_call_test.py and Gemini_api.py file

6. **Enable APIs and IAM permissions**
-Enable VertexAI api, Discovery engine
-Verify API is working by running api_call_test.py

7. **Run Streamlit app**:
```sh
    streamlit run app.py
    ```
## Installation for deployment on Cloud Run

TBD




