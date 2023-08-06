import keras 
class dualEncoder(keras.Model):
    def __init__(self, imageEncoder, textEncoder, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.imageEncoder=imageEncoder
        self.textEncoder=textEncoder
    def call(self, inputs, training=None, mask=None):
        pass
    def train_step(self, data):
        pass
    def loss(self):
        pass
    def metrics(self):
        pass