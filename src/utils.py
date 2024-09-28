import tensorflow as tf

def load_data():
    mnist = tf.keras.datasets.mnist
    return mnist.load_data()
