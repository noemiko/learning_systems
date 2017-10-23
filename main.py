from data_extractor import DataExtractor
from entrophy import Entrophy


class Analyzer(object):

    def get_analysis(self):
        analyzer = DataExtractor('./zoo.data.txt')
        data = analyzer.get_columns_as_rows()
        algorithm = Entrophy()
        for index, v in enumerate(data):
            entrophy = algorithm.get_entrophy(v)
            print("column number {} has entrophy {}".format(index, entrophy))

if __name__ == "__main__":
    analyzer = Analyzer()
    analyzer.get_analysis()