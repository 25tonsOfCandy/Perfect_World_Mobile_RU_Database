class FileWriter():
    def __init__(self, file_name):
        self.file_name = file_name
        self.file = open(self.file_name, 'w', encoding='UTF-8')

    def _close_file(self):
        self.file.close()

    def write(self, string: str):
        self.file.write(string)
        self._close_file()
        
    def write_list(self, data_list: list):
        for data in data_list:
            self.file.write(str(data))
            self._close_file()


