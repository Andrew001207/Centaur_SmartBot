#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Vector3, Transform

def encoder_callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)


if __name__ == '__main__':
    try:
        rospy.init_node('/odometry', anonymous=False)
        pub = rospy.Publisher('/odom', Transform, queue_size=10)
        rospy.Subscriber("/sensors/encoder", String, encoder_callback)
        rate = rospy.Rate(10) # 10hz
        while not rospy.is_shutdown():
            hello_str = "hello world %s" % rospy.get_time()
            rospy.loginfo(hello_str)
            pub.publish(hello_str)
            rate.sleep()
    except rospy.ROSInterruptException:
        pass