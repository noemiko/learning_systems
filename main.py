from data_extractor import DataExtractor
from entrophy import Entrophy
from information_gain import get_information_gain

class Analyzer(object):

    def calculate_C4(self):
        extractor = DataExtractor('./zoo.data.txt', True)
        columns = extractor.get_columns_as_rows()
        #column name with cases
        rows_with_labels = extractor.create_nested_rows(columns)

        classification_column = rows_with_labels.pop(extractor.labels[-1])
        attribute_classes = extractor.assign_classes_to_column_cases(
            rows_with_labels,
            classification_column)
        #entrophy
        calculate = Entrophy()
        entrophy_values = calculate.get_entrophy_for_dict(attribute_classes)
        class_entrophy = calculate.get_entrophy_for_row(classification_column)

        #info
        gain = get_information_gain(entrophy_values, class_entrophy)

        root = max(gain, key=gain.get)
        rules = ""
        node = entrophy_values[root]


if __name__ == "__main__":
    analyzer = Analyzer()
    analyzer.calculate_C4()
