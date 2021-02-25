#!/usr/bin/env python

import rospy

rospy.init_node('hello_world', anonymous = True)
freq = rospy.get_param('freq', 20)
text = rospy.get_param('text', "Hello World from Program")
rate = rospy.Rate(freq)

while not rospy.is_shutdown():
    full_string = text + "%s" %rospy.get_time()
    print full_string
    rate.sleep()
