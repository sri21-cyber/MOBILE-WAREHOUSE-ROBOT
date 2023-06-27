# **Rover**

## **Idea**
A rover capable of performing **path planning** using djikstra and A* algorithms.
 
*This package has been created and tested on Ubuntu 22.04 with ROS2 Humble, Gazebo 11.10.2, Rviz2, and Nav2 stack.*

## **How to build**
*Creating a workspace to build the package*
```
mkdir -p ~/rover_ws/src && cd ~/rover_ws/src
```
*Cloning the package*
```
git clone https://github.com/kalashjain23/rover_warehouse
cd ~/rover_ws
```
*Installing the dependencies and building the workspace*
```
rosdep install --from-paths src -y --ignore-src
colcon build
```


## **Path planning**
Run the following commands to setup your system for path planning
```
# source the workspace
cd ~/rover_ws && source ~/rover_ws/install/setup.bash

# Launching Gazebo and controllers
ros2 launch rover_warehouse launch_sim.launch.py world:=./src/rover_warehouse/worlds/warehouse.world

# Path planning using djikstra's algorithm
ros2 launch rover_warehouse djikstra.launch.py

----------------OR---------------------

# Path planning using A* algorithm
ros2 launch rover_warehouse astar.launch.py
```  
*You can now start giving goal poses to the rover through Rviz2.*


https://github.com/kalashjain23/rover/assets/97672680/37563384-b494-4d4c-9429-9d98d0782e38

