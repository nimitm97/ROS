#!/usr/bin/env python

###################### import ############################
import rospy
from sensor_msgs.msg import Joy		# joystick message type
from geometry_msgs.msg import Twist	# turtlebot message type
from sensor_msgs.msg import Range	# range sensor data
##################### instantiation of objects ###################
distance = Twist()

##################### node initialization ########################
rospy.init_node('teleop', anonymous=True)

##### initialize values #####
distance.linear.x = 0
distance.angular.z = 0
flag = True
obstacle = True

#################### definitions of functions ######################
def callback_drive(data):
	global distance
	global flag
	check = data.buttons[0]
	if check == 1:
		flag = True
	else:
		flag = False

	distance.linear.x = data.axes[1]
	distance.angular.z = data.axes[2]

def callback_obstacle(data):
	global obstacle
	dist = data.range
	if dist <= 0.5:			# standoff distance = 0.5 m
		obstacle = True
	else:
		obstacle = False
################### definition of publisher/subscriber and services #################
rospy.Subscriber("joy", Joy, callback_drive)
rospy.Subscriber("range", Range, callback_obstacle)
pub = rospy.Publisher('cmd_vel', Twist, queue_size = 10)


########## main program #############
rate = rospy.Rate(10)

#------------------------endless loop till shutdown -----------------------#
while not rospy.is_shutdown():

	if flag == True:
		distance.linear.x = 0
		distance.angular.z = 0

	pub.publish(distance)
	rate.sleep()
