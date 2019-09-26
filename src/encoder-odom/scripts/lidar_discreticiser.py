#!/usr/bin/env python

import rospy
import math
import numpy as np
from std_msgs.msg import Float32MultiArray
from sensor_msgs.msg import LaserScan

div = 5

def encoder_callback(data):
    frame = data.ranges[:180]
    resp = Float32MultiArray()
    for i in range(div):
        resp.data.append(np.mean(frame[(i * len(frame)/5) : ((i+1) * len(frame)/5)]))
    pub.publish(resp)

if __name__ == '__main__':
    try:
        rospy.loginfo("LidarLogger started!")
        rospy.init_node('las_meas', anonymous=False)
        pub = rospy.Publisher('/scan_d', Float32MultiArray, queue_size=10)
        rospy.Subscriber("/scan", LaserScan, encoder_callback)
        rate = rospy.Rate(10) # 10hz
        while not rospy.is_shutdown():
            rate.sleep()
    except rospy.ROSInterruptException:
        pass