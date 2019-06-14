# -*- coding: utf-8 -*-
"""
@author: shirasak
"""
import tensorflow as tf


a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0],
                shape=[2, 3],
                name='a')
b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0],
                 shape=[3, 2],
                 name='b')
c = tf.matmul(a, b)

with tf.Session(config=tf.ConfigProto(log_device_placement=True)) as sess:
    print(sess.run(c))
