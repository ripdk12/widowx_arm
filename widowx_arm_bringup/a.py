#!/usr/bin/env python
import time
import rospy
from std_msgs.msg import Int32 # Messages used in the node must be imported.
from geometry_msgs.msg import Pose

import sys

import numpy as np


rospy.init_node("track_blob")

pub = rospy.Publisher('follow_blob', Pose, queue_size=1)

target_pose=Pose() # declaring a message variable of type Int32


x_d=10.0
y_d=12.0
z_d=40.0
x_d_p=0.0
y_d_p=0.0

while not rospy.is_shutdown():
	time.sleep(1)
	rospy.loginfo("PEW! :D")

	#x_d= (((2*y+h)/2)-68) * 0.06
	#y_d= (((2*x+w)/2)-260) * 0.075

	target_pose.position.x=x_d*0.01
	target_pose.position.y=y_d*0.01
	target_pose.position.z=z_d*0.01
	target_pose.orientation.x=0
	target_pose.orientation.y=0
	target_pose.orientation.z=0
	target_pose.orientation.w=1
	pub.publish(target_pose)

	x_d_p=x_d
	y_d_p=y_d
			
		
