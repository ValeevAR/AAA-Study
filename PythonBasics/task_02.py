from typing import Union
import re


class CountVectorizer():
    # class for transforming a corpus (a list of strings) into Document-term matrix
    def __init__(self):
        self.feature_names = []

    def _prepare_corpus_for_transform(self, corpus: Union[list, str]):
        # function transforms strings to lowercase
        # if input is a str, then transforms into list
        if isinstance(corpus, str):
            return [corpus.lower()]
        if isinstance(corpus, list):
            return [c.lower() for c in corpus]

    def fit_transform(self, corpus: Union[list, str]):
        # function for transforming a corpus (a list of strings) into Document-term matrix
        count_matrix = []
        feature_names = []
        for c in self._prepare_corpus_for_transform(corpus):
            cleaned_corpus = re.split(r'[.,;:!? ]+', c)

            # reset "dict_feature_names" for current "cleaned_corpus"
            dict_feature_names = {word: 0 for word in feature_names}

            # if a feature is met for a first time - add corresponding key to the dictionary "dict_feature_names"
            # if a feature is already known - increase number of the feature in the dictionary "dict_feature_names"
            for word in cleaned_corpus:
                dict_feature_names.setdefault(word, 0)
                dict_feature_names[word] += 1

            feature_names = list(dict_feature_names)
            count_matrix.append(list(dict_feature_names.values()))

        # the first few rows has less length. We fill them by zeros until the length is sufficient
        n_feature_names = len(feature_names)
        for row in count_matrix:
            row += [0] * (n_feature_names - len(row))

        self.feature_names = feature_names
        return count_matrix

    def get_feature_names(self):
        # method that returns a list of features in a corpus
        return self.feature_names


def test_1():
    # basic test
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]

    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)

    assert vectorizer.get_feature_names() == ['crock', 'pot', 'pasta', 'never', 'boil', 'again', 'pomodoro', 'fresh',
                                              'ingredients', 'parmesan', 'to', 'taste']
    assert count_matrix == [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                            [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]


def test_2():
    # test with 1 word
    corpus = 'Crock'
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)

    assert vectorizer.get_feature_names() == ['crock']
    assert count_matrix == [[1]]


def test_3():
    # test with split sentences
    corpus = [
        'Crock Pot! Pasta       Never boil pasta again',
        'Pasta Pomodoro;., Fresh ingredients        Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)

    assert vectorizer.get_feature_names() == ['crock', 'pot', 'pasta', 'never', 'boil', 'again', 'pomodoro', 'fresh',
                                              'ingredients', 'parmesan', 'to', 'taste']
    assert count_matrix == [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                            [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
