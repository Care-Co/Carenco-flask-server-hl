import tensorflow as tf

model = tf.keras.Sequential(
    [
        tf.keras.layers.Dense(64, 'relu'),
        tf.keras.layers.LayerNormalization(),
        tf.keras.layers.Dense(64, 'relu'),
        tf.keras.layers.LayerNormalization(),
        tf.keras.layers.Dense(64, 'relu'),
        tf.keras.layers.LayerNormalization(),
        tf.keras.layers.Dense(1)
    ])

optimizer = tf.keras.optimizers.Adam(learning_rate=0.01)
model.compile(optimizer=optimizer, loss='mse', metrics=['mse', 'mae'])

x = [[255, 192], [254, 170], [254, 141], [254, 136], [254, 244]]
y = [[10.2], [69.2], [79.2], [87.1], [56.2]]

model.fit(x, y, epochs=1000)
model.save('./weight_regression.h5')
