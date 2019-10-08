#!/usr/bin/env python

import rospy
import math
import numpy as np
from std_msgs.msg import Float32MultiArray
from geometry_msgs.msg import Vector3

def control_func(data):
    resp = Vector3()
    if data.data[2] < 1.0:
        resp.x = -1.0
        resp.y = -1.0
    else:
        resp.x = 0
        resp.y = 0
    pub.publish(resp)

if __name__ == '__main__':
    try:
        rospy.loginfo("LidarLogger started!")
        rospy.init_node('algorithm', anonymous=False)
        pub = rospy.Publisher('/cmd_vel', Vector3, queue_size=10)
        rospy.Subscriber("/scan_d", Float32MultiArray, control_func)
        rate = rospy.Rate(10) # 10hz
        while not rospy.is_shutdown():
            rate.sleep()
    except rospy.ROSInterruptException:
        pass