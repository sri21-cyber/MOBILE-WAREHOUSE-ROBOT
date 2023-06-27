# MOBILE-WAREHOUSE-ROBOT

A rover capable of performing **path planning** using djikstra and A* algorithms.

Creating a workspace to build the package
mkdir -p ~/rover_ws/src && cd ~/rover_ws/src

Installing the dependencies and building the workspace
rosdep install --from-paths src -y --ignore-src
colcon build

For path planning use
cd ~/rover_ws && source ~/rover_ws/install/setup.basH

# Launching Gazebo and controllers
ros2 launch rover_warehouse launch_sim.launch.py world:=./src/rover_warehouse/worlds/warehouse.world

# Path planning using djikstra's algorithm
ros2 launch rover_warehouse djikstra.launch.py
