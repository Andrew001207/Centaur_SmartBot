import rospy
import math
import numpy as np
from std_msgs.msg import Float32MultiArray, Vector3

div = 5

def control_func(data):
    resp = Vector3()
    resp.x = 1.0
    resp.y = 1.0
    pub.publish(resp)

if __name__ == '__main__':
    try:
        rospy.loginfo("LidarLogger started!")
        rospy.init_node('las_meas', anonymous=False)
        pub = rospy.Publisher('/cmd_vel', Float32MultiArray, queue_size=10)
        rospy.Subscriber("/scan_d", Float32MultiArray, control_func)
        rate = rospy.Rate(10) # 10hz
        while not rospy.is_shutdown():
            rate.sleep()
    except rospy.ROSInterruptException:
        pass