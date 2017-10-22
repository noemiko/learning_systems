from io import  open
from sys import exit


class DataExtractor(object):

    zoo_data = []

    def __init__(self, path_to_file):
        raw_data = self.extract_data_from_file(path_to_file)
        self.zoo_data = self.make_format_data(raw_data)

    def extract_data_from_file(self, path):
        """Get file path and get table from file."""
        try:
            with open(path, 'r') as file:
                raw_data = [line.split(',') for line in file]
        except EOFError as err :
            exit(err)
        else:
            return raw_data

    def make_format_data(self, raw_data):
        formatted_data = []
        for row in raw_data:
            formatted_line = self.get_formatted_line(row)
            formatted_data.append(formatted_line)
        return formatted_data

    def get_formatted_line(self, line):
        formated_line = []

        formated_line.append(line.pop(0))
        line = list(map(int, line))
        for index in range(len(line)):
            index = int(index)
            item = self.make_type_by_index_rules(index, line)
            formated_line.append(item)
        return formated_line

    def make_type_by_index_rules(self, index, line):
        if index in range(0, 12) or index in range(13, 16):
            return bool(line[index])
        elif index is 12 or index is 16:
            return int(line[index])
        else:
            msg = "not all data has rules, add rule for {}".format(index)
            exit(msg)

    def get_data_without_name_column(self):
        data = self.zoo_data.copy()
        [line.remove(line[0]) for line in data]
        return data

if __name__ == "__main__":

    analyzer = DataExtractor('./zoo.data.txt')

    print(analyzer.get_data_without_name_column())
