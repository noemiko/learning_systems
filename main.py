from data_extractor import DataExtractor
from entrophy import Entrophy
from information_gain import get_information_gain
import pprint
class Analyzer(object):

    def calculate_C4(self, group, attribute):
        extractor = DataExtractor('./zoo.data.txt', True)
        if group is None or attribute is None:
            rows = extractor.data_rows
        else:
            rows = extractor.get_specyfic_group_rows_with_attribute(group, attribute)
        columns = extractor.get_columns_as_rows(list(rows))
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

        root_name = max(gain, key=gain.get)
        rules = ""
        node = entrophy_values[root_name]
        self.build_tree(gain, entrophy_values)

    def build_tree(self, gain, entrophy_values):
        next_node_name = max(gain, key=gain.get)
        gain.pop(next_node_name, '')
        node_cases = entrophy_values[next_node_name]
        print("column {} ".format(next_node_name))
        for case, values in node_cases.items():
            if values['entrophy'] == 0.0:
                values.pop("count")
                values.pop("entrophy")
                result = list(values.keys())[0]
                print("column {} attribute: {} is always {} ".format(next_node_name, case, result))
                print("----------------")
            else:
                print("column {} attribute: {}".format(next_node_name, case))
                print('was divided by:')
                self.calculate_C4(next_node_name, case)






if __name__ == "__main__":
    analyzer = Analyzer()
    analyzer.calculate_C4(None, None)
