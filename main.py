from data_extractor import DataExtractor
from entrophy import Entrophy
from information_gain import get_information_gain


class TreeGenerator(object):

    def calculate_C4(self, group, attribute, extractor, loop_index):
        if group is None or attribute is None:
            rows = extractor.data_rows
        else:
            rows = extractor.get_specyfic_group_rows_with_attribute(group, attribute)
        rows_with_labels = extractor.create_nested_rows(list(rows))

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

        next_node_name = max(gain, key=gain.get)
        self.build_tree(next_node_name, entrophy_values, extractor, loop_index)
        loop_index += 1

    def build_tree(self, next_node_name, entrophy_values, extractor, loop_index):
        node_cases = entrophy_values[next_node_name]
        level_lines = "-----"*loop_index
        empty_place = "      "*loop_index
        print("{} {}".format(level_lines, next_node_name))
        print("{}|".format(empty_place))
        for attribute, atribute_details in node_cases.items():
            if atribute_details['entrophy'] == 0.0:
                result = self.get_leaf(atribute_details)
                print("{} when is {} then {}".format(level_lines, attribute, result))
            else:
                print("{} {} is divided by ".format(level_lines, attribute))
                loop_index += 1
                self.calculate_C4(next_node_name, attribute, extractor, loop_index)

    def get_leaf(self, values):
        values.pop("count")
        values.pop("entrophy")
        return list(values.keys())[0]


if __name__ == "__main__":
    extractor = DataExtractor('./zoo.data.txt', False)
    analyzer = TreeGenerator()
    try:
        analyzer.calculate_C4(None, None, extractor, 1)
    except RecursionError as err:
        print("There is no optimal solution.")
        print(err)
