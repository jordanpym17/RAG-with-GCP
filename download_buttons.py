import streamlit as st
from google.cloud import storage
import tempfile

def download_blob(bucket_name, source_blob_name):
    """Downloads a blob from the bucket and returns its content."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    content = blob.download_as_bytes()
    return content

def get_gcs_file_path(gs_url):
    # Assuming gs_url is of the form gs://bucket_name/path/to/file
    parts = gs_url.replace("gs://", "").split("/")
    bucket_name = parts[0]
    blob_name = "/".join(parts[1:])
    return bucket_name, blob_name

@st.experimental_fragment
def make_button(link):
    bucket_name, blob_name = get_gcs_file_path(link)
    file_name = blob_name.split('/')[-1]
    file_content = download_blob(bucket_name, blob_name)
    st.download_button(
    label=file_name,
    data=file_content,
    file_name=file_name,
    mime='application/pdf'
)

    #with st.spinner('Downloading...')

#link = 'gs://general_standards/Engineering standards pdfs/ZA-SES-COR-001.pdf'
#make_button(link)
