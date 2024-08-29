import tensorflow as tf

def load_model():
    model = tf.keras.models.load_model('path/to/your/model')
    return model

def make_prediction(token_pairs, amounts_in):
    model = load_model()
    # Preprocess data and make predictions
    prediction = model.predict([token_pairs, amounts_in])
    return prediction
