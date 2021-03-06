import tensorflow as tf


x_data = [[1, 0, 3, 0, 5], [0, 2, 0, 4, 0]]
y_data = [1, 2, 3, 4, 5]

W = tf.Variable(tf.random_uniform([1, 2], -10.0, 10.0))
b = tf.Variable(tf.random_uniform([1], -10.0, 10.0))

x = tf.placeholder(tf.float32)

y = tf.placeholder(tf.float32)

hypothesis = tf.matmul(W, x) + b

cost = tf.reduce_mean(tf.square(hypothesis - y))

a = tf.Variable(0.1)
optimizer = tf.train.GradientDescentOptimizer(a)
train = optimizer.minimize(cost)

init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)

for step in range(2001):
    sess.run(train, feed_dict={x:x_data, y:y_data})
    if step % 20 == 0:
        print(step, sess.run(cost, feed_dict={x:x_data, y:y_data}), sess.run(W), sess.run(b))
