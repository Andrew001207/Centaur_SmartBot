#!/usr/bin/env python

import rospy
import math
import numpy as np
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Vector3

def interpolate_arr(frm):
    enum_frame = enumerate(frm)
    enum_frame = list(filter(lambda x: x[1] > 0, enum_frame))
    xp = [x[0] for x in enum_frame]
    fp = [x[1] for x in enum_frame]
    return [np.interp(i , xp, fp,period=360) for i in range(360)]

def encoder_callback(data):
    data.ranges = interpolate_arr(data.ranges)
    pub.publish(data)

if __name__ == '__main__':
    try:
        rospy.loginfo("LidarLogger started!")
        rospy.init_node('las_interpolator', anonymous=False)
        pub = rospy.Publisher('/scan_interp', LaserScan, queue_size=10)
        rospy.Subscriber("/scan", LaserScan, encoder_callback)
        rate = rospy.Rate(10) # 10hz
        while not rospy.is_shutdown():
            rate.sleep()
    except rospy.ROSInterruptException:
        pass