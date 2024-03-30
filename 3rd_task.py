import os


class FileManager:
    """ Manages files for its processing and writing result.
     Methods: process_files, write_to_result_file.

     """

    def __init__(self, directory, files):
        """Creates FileManager instance.
         directory: gets files directory
         files: gets list of file names.

         """
        self.directory = directory
        self.files = files

    def process_files(self):
        """Returns list of tuples with each file information."""
        file_contents = []
        for filename in self.files:
            file_path = os.path.join(self.directory, filename)
            with open(file_path, 'r') as file:
                lines = file.readlines()
                file_contents.append((filename, len(lines), lines))
        file_contents.sort(key=lambda x: x[1])
        return file_contents

    def write_to_result_file(self, file_contents):
        """Gets list of tuples with each file information and writes down its information to result.txt in current
        directory.

        """
        with open('result.txt', 'w') as result_file:
            for filename, num_lines, lines in file_contents:
                result_file.write(f'{filename}\n{num_lines}\n')
                result_file.writelines(lines)
                result_file.write('\n')


files_dir = os.path.join(os.getcwd(),'files')
files = ['1.txt', '2.txt', '3.txt']

file_manager = FileManager(files_dir, files)
file_contents = file_manager.process_files()
file_manager.write_to_result_file(file_contents)
