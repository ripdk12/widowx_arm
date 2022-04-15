# widowx_arm_dev

## Quick Start:

mkdir -p ~/widowx_arm/src

$ cd ~/widowx_arm/src

$ git clone https://github.com/ripdk12/widowx_arm.git .

$ git clone https://github.com/ripdk12/arbotix_ros.git -b parallel_gripper

$ cd ~/widowx_arm

$ catkin_make

## Rviz simulation

$ source devel/setup.bash

$ roslaunch widowx_arm_bringup arm_moveit.launch sr300:=false

## Widowx arm

$ source devel/setup.bash

$ roslaunch widowx_arm_bringup arm_moveit.launch sim:=false sr300:=false

you might need to give permission to access ttyUSB0:

$ sudo chmod 777 /dev/ttyUSB0

## Object manipluation:

@ roslaunch widowx_arm_bringup arm_moveit.launch sim:=false sr300:=true

@ roslaunch widowx_block_manipulation block_sorting_demo.launch
