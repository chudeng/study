import tensorflow as tf
hi = tf.constant('Hello World')
sess = tf.Session()
print(sess.run(hi))

