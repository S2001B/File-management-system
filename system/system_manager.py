import os
import shutil
from typing import Optional, Tuple, List

class FileSystem:

    def __init__(self, file_name: Optional[str]) -> None:
        if file_name is None or "." not in file_name:
            self.file_name, self.extension = None, None
        else:
            self.file_name, self.extension = file_name.split(".")

        self.destination_directory = "..\\FileManagementSystemLibreOffice\\SavedFiles\\FileExtentions"
        self.final_directory = self.destination_directory if self.extension == None else os.path.join(self.destination_directory, self.extension) 


    def return_var_name(self) -> str:
        full_file = ".".join([self.file_name, self.extension])
        return full_file
    

    def move(self) -> None:
        try:
            full_file = self.return_var_name()

            if self.check_file_exists(full_file):
                raise FileExistsError
            
            shutil.move(full_file, self.final_directory)

            print(f"\n{self.file_name} with {self.extension} saved in:")
            print(self.final_directory,"\n")

        except FileNotFoundError:
            print(f"File {full_file} could not be found, or does not exist")
        return


    def check_file_exists(self, full_file) -> bool:
        self.check: bool = False
        list_dir = os.listdir(self.final_directory)

        if full_file in list_dir:
            self.check = True
            print(f"File {full_file} already exists in the directory {self.extension}")
        return self.check
    
    
    def copy(self) -> None:
        full_file = self.return_var_name()
        shutil.copy(full_file, self.final_directory)
        
        self.check_file_exists(full_file)
        return


    def sort_files(self) -> Optional[List[str]]:
        self.system_directory = "..\\FileManagementSystemLibreOffice"
        system_contents = os.listdir(self.system_directory)
        save_directory = os.listdir(self.destination_directory)
        files_list = list()

        for file in system_contents:
            try:
                file_name, file_extension = self.split_file(file)
                if self.validate_file_existence(file_name, file_extension) == (None, None):
                    continue

                if file_extension in save_directory:
                        self.check_file_exists(file)
                        file_old_location = os.path.join(self.system_directory, file)
                        file_new_location = os.path.join(self.destination_directory, file_extension)
                        shutil.move(file_old_location, file_new_location)
                        print(f"File [< {file_name} >] moved succesfully to [< {file_extension} >]")

                        files_list.append(file)
            except:
                if file.endswith(".py") or self.validate_file_existence is None:
                    print(f"File [< {file} >] unable to be sorted because the file type does not match")
                    continue

        if files_list == []:
            print("All files are sorted")

        return files_list
        
    # used in sort_files
    def validate_file_existence(self, file_name: Optional[str], file_extension: Optional[str]) -> Optional[Tuple[str, str]]:
        if file_name is None or file_extension is None:
            return None, None
        return file_name, file_extension
    
    # used in sort_files
    def split_file(self, file: Optional[str]) -> Optional[Tuple[str, str]]:
        try:
            file_name, file_extension = file.split(".")
            return file_name, file_extension
        except (UnboundLocalError, TypeError):
            return None, None
    

    
    
            
