#!/usr/bin/env python
#!/usr/bin/python3
import os
from get_new_files import FileList
from backup_to_drive import backup

if __name__ == '__main__':
    f = FileList()
    current_path = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.join(os.getcwd(), 'BackUpImortantFiles')
    new_files = f.get_list_of_new_files(current_path)

    # print(f'New Files: {new_files}')

    # call the Google Drive v3 API
    if len(new_files):
        backup(current_path)
