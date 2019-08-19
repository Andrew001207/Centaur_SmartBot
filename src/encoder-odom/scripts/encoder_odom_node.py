#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Vector3, Transform

pos = Transform()

def encoder_callback(data):
    rospy.loginfo(rospy.get_caller_id() + "ACK encoder info", data.data)
    pos.translation.x += data.x
    pos.translation.y += data.y
    pub.publish(pos)


if __name__ == '__main__':
    try:
        rospy.init_node('odometry', anonymous=False)
        pub = rospy.Publisher('/odom', Transform, queue_size=10)
        rospy.Subscriber("/sensors/wheel_encoder", Vector3, encoder_callback)
        rate = rospy.Rate(10) # 10hz
        while not rospy.is_shutdown():
            rate.sleep()
    except rospy.ROSInterruptException:
        pass