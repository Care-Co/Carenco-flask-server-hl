import tensorflow as tf

model = tf.keras.models.load_model('./weight_regression.h5')



print(model.predict([[254, 170]])[0][0])