import os

class FileList:
    def __init__(self) -> None:
        # self.existing = set()
        # self.new = set()
        pass 

    def get_list_of_new_files(self, folder_path):
        # get the existing files in a set
        with open('existing_files.txt', 'r') as file_list:
            existing_files = set(file for file in file_list)
        
        print(f'EXISTING FILES: {existing_files}')
        # get all files in a set
        all_files = set(os.path.join(folder_path, f+'\n') for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)))
        print(f'ALL FILES: {all_files}')

        # get new files in a set
        new_files = all_files - existing_files
        print(f'NEW FILES: {new_files}')

        # create a new file containing the newly added files.
        with open('new_files.txt', 'w') as file_list:
            for file in new_files:
                file_list.write(file)

        # update the existing file list
        with open('existing_files.txt', 'a') as file_list:
            for file in new_files:
                file_list.write(file)
        
        return new_files

