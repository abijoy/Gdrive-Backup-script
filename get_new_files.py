import os

class FileList:
    def __init__(self) -> None:
        pass 

    def get_list_of_new_files(self, current_path):
        folder_path = os.path.join(current_path, 'BackUpImortantFiles')
        existing_files_filename = os.path.join(current_path, 'existing_files.txt')
        new_files_filename = os.path.join(current_path, 'new_files.txt')

        # get the existing files in a set
        with open(existing_files_filename, 'r') as file_list:
            existing_files = set(file for file in file_list)
        
        # get all files in a set
        all_files = set(os.path.join(folder_path, f+'\n') for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)))
        # print(f'ALL FILES: {all_files}')

        # get the new files in a set
        new_files = all_files - existing_files

        # create a new file containing the newly added files.
        with open(new_files_filename, 'w') as file_list:
            for file in new_files:
                file_list.write(file)

        # update the existing file list
        with open(existing_files_filename, 'a') as file_list:
            for file in new_files:
                file_list.write(file)
        
        return new_files

