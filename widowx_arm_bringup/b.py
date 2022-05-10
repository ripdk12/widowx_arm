#!/usr/bin/env python
import rospy
import sys
import tf
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list
from geometry_msgs.msg import Pose

from std_msgs.msg import Int32 # Messages used in the node must be imported.
'''
"my_callback" is the callback method of the subscriber. Argument "msg" contains the published data.
'''

def my_callback(msg):
	#rospy.loginfo("received data from x: %f, y: %f, z: %f",msg.position.x,msg.position.y,msg.position.z)
	#group.set_position_target([msg.position.x,msg.position.y,msg.position.z])
	
	rospy.loginfo("received position from x: %f, y: %f, z: %f\nreceived orientation from x: %f, y: %f, z: %f, w: %f",msg.position.x,msg.position.y,msg.position.z,msg.orientation.x,msg.orientation.y,msg.orientation.z,msg.orientation.w)
	group.set_position_target([msg.position.x,msg.position.y,msg.position.z])
	group.set_orientation_target([msg.orientation.x,msg.orientation.y,msg.orientation.z,msg.orientation.w])
	
	plan = group.go(wait=True)
	group.stop()
	group.clear_pose_targets()


rospy.init_node('subscriber_py') #initialzing the node with name "subscriber_py"
# moveit start

moveit_commander.roscpp_initialize(sys.argv)
robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group_name = "widowx_arm"#"arm"
group = moveit_commander.MoveGroupCommander(group_name)

listener=tf.TransformListener()
listener.waitForTransform('/wrist_2_link','/arm_base_link',rospy.Time(), rospy.Duration(1.0))
print listener.frameExists('arm_base_link')
print listener.frameExists('wrist_2_link')
(trans,rot)=listener.lookupTransform('arm_base_link','wrist_2_link',rospy.Time())
print trans,rot


rospy.Subscriber("follow_blob", Pose, my_callback, queue_size=10) 

rospy.loginfo("subscriber_py node started and subscribed to topic_py") #debug statement

rospy.spin()
