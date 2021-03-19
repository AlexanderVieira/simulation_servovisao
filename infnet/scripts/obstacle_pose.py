#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Pose2D

pose_goal = Pose2D()

def callback_pose_goal(msg):
    global pose_goal
    pose_goal.x = msg.x
    pose_goal.y = msg.y
    rospy.loginfo("position x = {}".format(pose_goal.x))
    rospy.loginfo("position y = {}".format(pose_goal.y))

def main_control():
        
    rospy.init_node('obstacle_pose', anonymous=True)    # node name    
    robot_goal = rospy.Subscriber('goal',Pose2D,callback_pose_goal)    
    rate = rospy.spin()        

############### Main code ################
if __name__ == '__main__':
    main_control()
