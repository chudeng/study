import tensorflow as tf

a = tf.placeholder(tf.int32, [None])
print(a)

b = tf.constant(10)
print(b)
x10_op = a * b
print(x10_op)

float_tensor = tf.cast(tf.constant([1, 2, 3]), dtype = tf.float32)
print(float_tensor)

sess = tf.Session()
r1 = sess.run(x10_op, feed_dict = {a: [1, 2, 3, 4, 5]})
r2 = sess.run(x10_op, feed_dict = {a: [10, 20]})
print(r1)
print(r2)