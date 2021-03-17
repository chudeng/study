import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf

node1 = tf.constant(5.0, tf.float32)
node2 = tf.constant(7.0) # also tf.float32 implicitly
node3 = tf.add(node1, node2)

print('node1 =', node1)
print('node2 =', node2)
print('node3 =', node3)

sess = tf.Session()
print('sess.run(node1, node2) =', sess.run([node1, node2]))
print('sess.run(node3) =', sess.run(node3))

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
addr_node = a + b

print(sess.run(addr_node, feed_dict = {a:2, b:1.5}))
print(sess.run(addr_node, feed_dict = {a:[2,3], b:[1,4]}))