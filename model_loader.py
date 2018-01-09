import os
import gensim


def load(filename):
    root_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(root_dir, filename)
    print 'word2vec english model: loading...'
    model = gensim.models.KeyedVectors.load_word2vec_format(os.path.abspath(model_path), binary=True)
    print 'done'
    return model
