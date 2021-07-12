import tensorflow as tf
import tensorflow_datasets as tfds

imdb , info= tfds.load("imdb_reviews", with_info=True, as_supervised=True)

train_data, test_data = imdb['train'], imdb['test']
