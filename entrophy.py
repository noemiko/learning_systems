from math import log10


class Entrophy(object):

    def get_entrophy(self, column):
        counted = self._count_values(column)
        probability = self._count_probability(counted)
        return self._count_entrophy(probability)

    def _count_values(self, data):
        classes = dict()
        for item in data:
            if item not in classes:
                classes[item] = 1
            else:
                classes[item] += 1
        return classes

    def _count_probability(self, counted_decisions):
        probabilities = dict()
        all_decisions = sum(counted_decisions.values())
        for k, v in counted_decisions.items():
            probability = v/all_decisions
            probabilities[k] = round(probability,2)
        return probabilities

    def _count_entrophy(self, probability):
        entrophy = 0
        for v in probability.values():
            entrophy += v*log10(v)

        return round(entrophy * -1, 2)
