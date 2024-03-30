import os


class FileManager:

    def __init__(self, directory, files):
        self.directory = directory
        self.files = files

    def read_file(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return os.path.basename(file_path), len(lines), lines

    def process_files(self):
        file_contents = [self.read_file(filename) for filename in self.files]
        file_contents.sort(key=lambda x: x[1])
        return file_contents

    def write_to_result_file(self, file_contents):
        with open('result.txt', 'w') as result_file:
            for filename, num_lines, lines in file_contents:
                result_file.write(f'{filename}\n{num_lines}\n')
                result_file.writelines(lines)
                result_file.write('\n')


curr_dir = os.getcwd()
files = ['1.txt', '2.txt', '3.txt']

file_manager = FileManager(curr_dir, files)
file_contents = file_manager.process_files()
file_manager.write_to_result_file(file_contents)
