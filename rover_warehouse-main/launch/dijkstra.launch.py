import os

from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

from launch_ros.actions import Node

def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    
    rviz_config_file = os.path.join(get_package_share_directory('rover_warehouse'), 'config', 'navigation.rviz')
    rviz2 = Node(
        package='rviz2',
        executable='rviz2',
        output='screen',
        parameters=[{'use_sim_time': use_sim_time}],
        arguments=['-d', rviz_config_file]
    )
    
    slam_toolbox_params_file = os.path.join(get_package_share_directory('rover_warehouse'), 'config', 'mapper_params_online_async.yaml')
    slam_toolbox = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('slam_toolbox'), 'launch', 'online_async_launch.py')
        ]), launch_arguments={'slam_params_file': slam_toolbox_params_file, 'use_sim_time': use_sim_time}.items()
    )
    
    dijkstra_params_file = os.path.join(get_package_share_directory('rover_warehouse'), 'config', 'dijkstra.yaml')
    params_file = LaunchConfiguration('params_file', default=dijkstra_params_file)
    nav_planner = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('nav2_bringup'), 'launch', 'navigation_launch.py')
        ]), launch_arguments={'map': params_file, 'use_sim_time': use_sim_time}.items()
    )

    return LaunchDescription([
        slam_toolbox,
        nav_planner,
        rviz2
    ])
    