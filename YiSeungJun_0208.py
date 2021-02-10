import tensorflow as tf

# 실행시 값을 입력받아 해당 구구단을 출력하세요
with tf.Session() as sess:
    i = 1
    j = 1
    fdan = tf.Variable(i)
    bdan = tf.Variable(j)
    r = tf.multiply(fdan, bdan)
    sess.run(tf.global_variables_initializer())
    for i in range(1,10):
        sess.run(tf.assign(fdan, i))
        print('\n{} 단'.format(i))
        for j in range(1,10):
            sess.run(tf.assign(bdan, j))
            print('{} * {} = {}'.format(sess.run(fdan), sess.run(bdan), sess.run(r)))
