#!/usr/bin/env python

import rospy
from math import sin, cos, tan, atan
from std_msgs.msg import String
from geometry_msgs.msg import Vector3
import tf

L = 0.185
R = 0.029
steps_per_m=1/(0.182/80)


pos = Vector3(0,0,0)

def encoder_callback(data):
    Dl=data.x/steps_per_m
    Dr=data.y/steps_per_m
    Dc=(Dl+Dr)/2
    pos.x += Dc*cos(pos.z)
    pos.y += Dc*sin(pos.z)
    pos.z += (Dr-Dl)/L
    pub.publish(pos)


if __name__ == '__main__':
    try:
        rospy.init_node('odometry', anonymous=False)
        pub = rospy.Publisher('/odom', Vector3, queue_size=10)
        rospy.Subscriber("/sensors/wheel_encoder", Vector3, encoder_callback)
        rate = rospy.Rate(10) # 10hz
        while not rospy.is_shutdown():
            rate.sleep()
    except rospy.ROSInterruptException:
        pass