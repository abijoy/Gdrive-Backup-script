import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload


def backup(current_path):
    SCOPES = ["https://www.googleapis.com/auth/drive"]

    creds = None
    token_file = os.path.join(current_path, 'token.json')
    credentials_file = os.path.join(current_path, 'credentials.json')
    new_files_filename = os.path.join(current_path, 'new_files.txt')

    if os.path.exists(token_file):
        creds = Credentials.from_authorized_user_file(token_file, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                credentials_file, SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open(token_file, 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('drive', 'v3', credentials=creds)
        response = service.files().list(
            q="name='BackUpImortantFiles' and mimeType='application/vnd.google-apps.folder'",
            spaces='drive'
        ).execute()

        if not response ['files']:
            file_metadata = {
                'name': 'BackUpImortantFiles',
                'mimeType': 'application/vnd.google-apps.folder'
            }

            file = service.files().create(body=file_metadata, fields='id').execute()

            folder_id = file.get('id')
        else:
            folder_id = response['files'][0]['id']

        with open(new_files_filename, 'r') as file_list:
            for file in file_list:
                file = file[:-1]
                file_name = file.split('/')[-1]
                file_metadata = {
                    'name': file_name,
                    'parents': [folder_id]
                }
                media = MediaFileUpload(f'{file}')
                upload_file = service.files().create(
                    body=file_metadata,
                    media_body=media,
                    fields='id'
                ).execute()

                print(f'Backed up file: {file}')
    except HttpError as error:
        print(f'Error Happend: {error}')


if __name__ == '__main__':
    pass