#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
import os
import csv

def las_callback(data):
    rospy.loginfo(data.ranges)
    # with open('lidar.csv', mode='w') as csv_file:
    #     csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #     employee_writer.writerow(['John Smith', 'Accounting', 'November'])


if __name__ == '__main__':
    try:
        rospy.init_node('lidar_logger', anonymous=False)
        pub = rospy.Publisher('/ad_scan', LaserScan, queue_size=10)
        rospy.Subscriber("/scan", LaserScan, las_callback)
        rospy.loginfo("INIT")
        rate = rospy.Rate(10) # 10hz
        while not rospy.is_shutdown():
            rate.sleep()
    except rospy.ROSInterruptException:
        pass