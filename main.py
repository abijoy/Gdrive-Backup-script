import os
from get_new_files import FileList

f = FileList()
folder_path = os.path.join(os.getcwd(), 'BackUpImortantFiles')

response = f.get_list_of_new_files(folder_path)
print(response)