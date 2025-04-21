from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
import io
import time
import os

# === Setup ===
INPUT_FILE = r"D:\NLP Project\Pipeline\input_files\story1.txt"
INPUT_FOLDER_ID = "18upUlGhsEpiQC1hOsB0-o9-4Eek6FhJ-"
OUTPUT_FOLDER_ID = "10kXwXOcPVNNYhrm47UWS1CxJICzyhrIy"
CREDENTIALS_JSON = "booknlp-8f5461635c8d.json"
OUTPUT_FILE = "story1.book"

def get_drive_service():
    creds = service_account.Credentials.from_service_account_file(CREDENTIALS_JSON, scopes=["https://www.googleapis.com/auth/drive"])
    return build("drive", "v3", credentials=creds)

def upload_file(service):
    file_metadata = {
        "name": os.path.basename(INPUT_FILE),
        "parents": [INPUT_FOLDER_ID]
    }
    media = MediaFileUpload(INPUT_FILE, resumable=True)
    uploaded_file = service.files().create(body=file_metadata, media_body=media, fields="id").execute()
    print("✅ Uploaded:", uploaded_file["id"])

def wait_for_output(service, timeout=300):
    print("⏳ Waiting for output...")
    start = time.time()
    while time.time() - start < timeout:
        results = service.files().list(q=f"'{OUTPUT_FOLDER_ID}' in parents and name = '{OUTPUT_FILE}'",
                                       fields="files(id, name)").execute()
        files = results.get("files", [])
        if files:
            print("✅ Output found!")
            return files[0]["id"]
        time.sleep(10)
    raise TimeoutError("❌ Output not found within time limit")

def download_file(service, file_id, destination):
    request = service.files().get_media(fileId=file_id)
    fh = io.FileIO(destination, "wb")
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while not done:
        status, done = downloader.next_chunk()
    print("✅ Download complete:", destination)

# === Main ===
if __name__ == "__main__":
    service = get_drive_service()
    upload_file(service)
    output_id = wait_for_output(service)
    download_file(service, output_id, "story1.book")