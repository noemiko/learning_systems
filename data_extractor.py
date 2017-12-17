from io import  open
from sys import exit


class DataExtractor(object):

    labels = []
    data_rows = []

    def __init__(self, path_to_file, is_first_row_as_label):
        raw_data = self.extract_data_from_file(path_to_file)
        self.labels, self.data_rows = self.extract_label_and_data(raw_data, is_first_row_as_label)

    def extract_data_from_file(self, path):
        """Get file path and get table from file."""
        try:
            with open(path, 'r') as file:
                for row in file:
                    row = row.replace('\n','')
                    row = row.split(',')
                    yield row
        except EOFError as err:
            exit(err)

    def extract_label_and_data(self, raw_data, is_first_row_as_label):
        """
        :param raw_data: table with tables with rows
        :param is_first_row_as_label:
        :return: two tables, first is label,
         second is table with tables with rows
        """
        raw_data = list(raw_data)
        if is_first_row_as_label is True:
            labels = raw_data.pop(0)
        else:
            labels = self.generate_labels(len(raw_data[0]))
        return labels, raw_data

    def generate_labels(self, number_of_columns):
        labels = []
        for i in range(0, number_of_columns-1):
            labels.append("column {}".format(i))
        labels.append("class")
        return labels

    def create_nested_rows(self, rows):
        """
        :return: dict with column name and list of cases
        example:
        {'class': ["Don'tPlay", "Don'tPlay", 'Play', (...)]}
        """
        rows_with_labels = dict()
        for index, row in enumerate(rows):
            label = self.labels[index]
            rows_with_labels.update({label:list(row)})
        return rows_with_labels

    def assign_classes_to_column_cases(self, rows_with_labels, classification_column):
        attribute_classes = dict()
        for column_name, list_od_cases in rows_with_labels.items():
            attribute_classes[column_name] = dict()
            for index, item in enumerate(list_od_cases):
                if item not in attribute_classes[column_name]:
                    attribute_classes[column_name][item] = []
                    attribute_classes[column_name][item].append(classification_column[index])
                else:
                    attribute_classes[column_name][item].append(classification_column[index])
        return attribute_classes

    # def make_format_data(self, raw_data):
    #     formatted_data = []
    #     for row in raw_data:
    #         formatted_line = self.get_formatted_line(row)
    #         formatted_data.append(formatted_line)
    #     return formatted_data
    #
    # def get_formatted_line(self, line):
    #     return line
    #
    # def make_type_by_index_rules(self, index, line):
    #     if index in range(0, 12) or index in range(13, 16):
    #         return bool(line[index])
    #     elif index is 12 or index is 16:
    #         return int(line[index])
    #     else:
    #         msg = "not all data has rules, add rule for {}".format(index)
    #         exit(msg)
    #
    def get_columns_as_rows(self, rows):
        columns = len(rows[0])
        for column_index in range(0, columns):
            yield map(lambda x: x[column_index], rows)

    def get_specyfic_group_rows_with_attribute(self, group_name, attribute):
        group_index = self.labels.index(group_name)
        for row in self.data_rows:
            if row[group_index] == attribute:
                yield row


if __name__ == "__main__":

    analyzer = DataExtractor('./zoo.data.txt', True)
    rows = analyzer.get_specyfic_group_rows_with_attribute('outlook', 'sunny')
    print(list(rows))
    # print(analyzer.labels)
    # print(analyzer.data_rows)
    # for index, column in enumerate(analyzer.get_columns_as_rows()):
    #     print("Column name: {}".format(analyzer.labels[index]))
    #     print(list(column))
