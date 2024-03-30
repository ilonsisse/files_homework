import os


class FileManager:

    def __init__(self, directory, files):
        self.directory = directory
        self.files = files

    def read_file(self, file_path):
        with open('file_path', 'r') as file:
            lines = file.readlines()
            return os.path.basename(file_path), len(lines), lines




