from typing import Union
import re


class CountVectorizer():
    # class for transforming a corpus (a list of strings) into Document-term matrix

    def _prepare_corpus_for_transform(self, corpus: Union[list, str]):
        # function transforms strings to lowercase
        # if input is a str, then transforms into list
        if isinstance(corpus, str):
            return [corpus.lower()]
        if isinstance(corpus, list):
            return [c.lower() for c in corpus]

    def fit_transform(self, corpus: Union[list, str]):
        # function for transforming a corpus (a list of strings) into Document-term matrix
        _corpus = []
        feature_names = []

        # creates _corpus - it is corpus with strings split into words
        # also creates feature_names - a list of feature names
        for c in self._prepare_corpus_for_transform(corpus):
            _corpus.append(re.split(r'[.,;:!? ]+', c))
            for word in _corpus[-1]:
                if word not in feature_names:
                    feature_names.append(word)

        # creates count_matrix
        count_matrix = []
        for c in _corpus:
            dict_feature_names = {word: 0 for word in feature_names}
            for word in c:
                dict_feature_names[word] += 1
            count_matrix.append(list(dict_feature_names.values()))

        self.feature_names = feature_names
        return count_matrix

    def get_feature_names(self):
        # method that returns a list of features in a corpus
        return self.feature_names


if __name__ == '__main__':
    # basic test
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]

    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)

    print(vectorizer.get_feature_names())
    print(count_matrix)

    # test with 1 word
    corpus = 'Crock'
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)

    print(vectorizer.get_feature_names())
    print(count_matrix)

    # test with 1 word
    corpus = ['Crock']
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)

    print(vectorizer.get_feature_names())
    print(count_matrix)

    # test
    corpus = [
        'Crock Pot! Pasta       Never boil pasta again',
        'Pasta Pomodoro;., Fresh ingredients        Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)

    print(vectorizer.get_feature_names())
    print(count_matrix)
