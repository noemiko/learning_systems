from math import log2


class Entrophy(object):

    def get_entrophy_for_dict(self, attribute_classes):
        entrophy_values = dict()
        for k, v in attribute_classes.items():
            entrophy_values.update({k: {}})
            number_of_rows = 0
            for attribute, list_of_class in v.items():
                count_attributes = len(list_of_class)
                calculator = self.get_entrophy_for_row(list_of_class)
                entrophy_values[k].update({attribute:calculator})
                entrophy_values[k][attribute].update({'count': count_attributes})
                number_of_rows+=count_attributes
            entrophy_values[k].update({'count': number_of_rows})
        return entrophy_values

    def get_entrophy_for_row(self, column):
        counted = self._count_values(column)
        probability = self._count_fraction(counted)
        probability["entrophy"] = self._count_entrophy(probability)
        return probability

    def _count_values(self, data):
        classes = dict()
        for item in data:
            if item not in classes:
                classes[item] = 1
            else:
                classes[item] += 1
        return classes

    def _count_fraction(self, counted_decisions):
        fractions = dict()
        all_decisions = sum(counted_decisions.values())
        for k, v in counted_decisions.items():
            fraction = v/all_decisions
            fractions[k] = round(fraction,2)
        return fractions

    def _count_entrophy(self, fraction):
        entrophy = 0
        for v in fraction.values():
            entrophy += v*log2(v)

        return round(entrophy * -1, 3)
