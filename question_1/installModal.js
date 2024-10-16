import tensorflow as tf

model = tf.keras.applications.MobileNetV2(weights='imagenet')

model.save('mobilenet_v2.h5')

print("Model saved as mobilenet_v2.h5")