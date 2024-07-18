# GCP-based Retrieval-Augmented Generation (RAG) System

Welcome to the GCP-based Retrieval-Augmented Generation (RAG) System repository. This project leverages Google Cloud Platform (GCP) to build a scalable RAG system for handling large amounts of data. The data, originating from various formats and conditions, undergoes preprocessing before being ingested into a GCP Datastore. The system uses the Gemini API for data search and summary, with a user interface built using Streamlit.

## Table of Contents

- [Overview](#overview)
- [Folder Structure](#folder-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Requirements](#requirements)
- [License](#license)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)

## Overview

This project involves several key steps:

1. **Data Preprocessing**: Convert and format data files from various formats (doc, pdf) to a consistent format.
2. **Local Database Creation**: Build a local version of the company's database.
3. **Data Ingestion**: Sequentially process the files and make necessary format changes.
4. **Cloud Storage**: Store the processed data in GCP Cloud Buckets.
5. **Datastore Creation**: Use GCP Console to create a scalable Datastore, serving as the vector database.
6. **API Integration**: Utilize the Gemini API for data search and summary generation.
7. **User Interface**: Implement a Streamlit-based UI for interaction.

## Folder Structure


Yes, you can simply copy and paste the markdown content into your README.md file. The markdown syntax will render properly on GitHub, presenting a nicely formatted readme for your repository.

If you also want to include custom CSS for further styling, GitHub's Markdown rendering does not support custom CSS directly within the README.md file. However, you can use HTML tags within your Markdown and apply inline styles.

Here's how you can do it:

Markdown Content: Copy and paste the provided markdown content into your README.md file.

Adding Inline Styles: If you want to add some specific styles, you can use HTML tags and inline styles within your Markdown. For example:

markdown
Copy code
# GCP-based Retrieval-Augmented Generation (RAG) System

<p style="color:blue; font-size:20px;">Welcome to the GCP-based Retrieval-Augmented Generation (RAG) System repository. This project leverages Google Cloud Platform (GCP) to build a scalable RAG system for handling large amounts of data. The data, originating from various formats and conditions, undergoes preprocessing before being ingested into a GCP Datastore. The system uses the Gemini API for data search and summary, with a user interface built using Streamlit.</p>

## Table of Contents

- [Overview](#overview)
- [Folder Structure](#folder-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Requirements](#requirements)
- [License](#license)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)

## Overview

This project involves several key steps:

1. **Data Preprocessing**: Convert and format data files from various formats (doc, pdf) to a consistent format.
2. **Local Database Creation**: Build a local version of the company's database.
3. **Data Ingestion**: Sequentially process the files and make necessary format changes.
4. **Cloud Storage**: Store the processed data in GCP Cloud Buckets.
5. **Datastore Creation**: Use GCP Console to create a scalable Datastore, serving as the vector database.
6. **API Integration**: Utilize the Gemini API for data search and summary generation.
7. **User Interface**: Implement a Streamlit-based UI for interaction.

## Folder Structure

project-root/
│
├── Doc_ingestion/
│ ├── script1.py
│ ├── script2.py
│ └── script3.py
│
├── requirements.txt
├── main.py
└── README.md


- **Doc_ingestion/**: Contains scripts for data preprocessing and formatting.
- **requirements.txt**: Lists the necessary Python libraries.
- **main.py**: Main application script.
- **README.md**: This readme file.

## Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. **Create a virtual environment**:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

4. **Install Google Cloud SDK**:

    Follow the instructions to install the [Google Cloud SDK](https://cloud.google.com/sdk/docs/install).

5. **Authenticate with Google Cloud**:

    After installing the SDK, authenticate with your Google Cloud account:

    ```sh
    gcloud auth login
    gcloud config set project [YOUR_PROJECT_ID]
    ```

## Usage

1. **Preprocess and Ingest Data**:
   - Modify and run the scripts in the `Doc_ingestion` folder to preprocess and format your data.

2. **Upload Data to GCP**:
   - Store the processed data in GCP Cloud Buckets.

3. **Create Datastore**:
   - Use the GCP Console to create a Datastore for your project. Remember to replace `ProjectID`, `Location`, and `Datastore` with your project-specific details.

4. **Run the Application**:
   - Use Streamlit to launch the UI and interact with your data.

    ```sh
    streamlit run main.py
    ```

## Requirements

The `requirements.txt` file includes all the necessary libraries for this project. Make sure to install them in your virtual environment.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any enhancements or bug fixes.

## Acknowledgements

- Thanks to Google Cloud Platform for providing robust and scalable cloud services.
- Special thanks to the Streamlit team for the easy-to-use UI framework.

## Notes

- Replace `ProjectID`, `Location`, and `Datastore` with your specific project details when setting up the GCP components.
- Ensure all dependencies are installed using the `requirements.txt` file.
- Google Cloud SDK must be installed and authenticated for proper GCP interaction.

---

For any further questions or issues, feel free to open an issue on this repository.
