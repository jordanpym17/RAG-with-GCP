import os
import win32com.client as win32

def convert_and_delete_docs_single_directory(directory):
    # Create a Word application object
    word = win32.gencache.EnsureDispatch('Word.Application')
    word.Visible = False

    # Iterate through all files in the directory
    for doc in os.listdir(directory):
        if doc.endswith(".doc"):
            doc_path = os.path.join(directory, doc)
            # Open the .doc file
            doc_obj = word.Documents.Open(doc_path)
            # Set the new file path
            docx_path = os.path.join(directory, os.path.splitext(doc)[0] + ".docx")
            # Save as .docx
            doc_obj.SaveAs(docx_path, FileFormat=16)  # FileFormat=16 for .docx
            doc_obj.Close()

            print(f"Converted: {doc} to {os.path.basename(docx_path)}")
            # Delete the original .doc file
            os.remove(doc_path)

    word.Quit()


def convert_and_delete_docs_all_directories(directory):
    # Create a Word application object
    word = win32.gencache.EnsureDispatch('Word.Application')
    word.Visible = False

    # Walk through all directories in the directory tree
    for root, dirs, files in os.walk(directory):
        for doc in files:
            if doc.endswith(".doc"):
                doc_path = os.path.join(root, doc)
                # Open the .doc file
                doc_obj = word.Documents.Open(doc_path)
                # Set the new file path
                docx_path = os.path.join(root, os.path.splitext(doc)[0] + ".docx")
                # Save as .docx
                doc_obj.SaveAs(docx_path, FileFormat=16)  # FileFormat=16 for .docx
                doc_obj.Close()
                # Print the name of the file being converted
                print(f"Converted: {doc} to {os.path.basename(docx_path)}")
                # Delete the original .doc file
                os.remove(doc_path)
            
                

    word.Quit()

    # Specify your directory path here  
#convert_and_delete_docs_all_directories("C:\\Users\\Jordan\\Downloads\\Paper")
#print("done")