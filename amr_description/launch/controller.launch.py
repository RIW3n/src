from launch import LaunchDescription
from launch_ros.actions import Node

import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    controller_ = os.path.join(get_package_share_directory('amr_description'),'config','amr_controller.yaml')
    
    joint_state_broadcaster_spawner = Node(
        package='controller_manager',
        executable='spawner',
        arguments=[
            "joint_state_broadcaster",
            "--controller-manager",
            "/controller_manager",
            ],
    )
    
    planar_drive_spawner = Node(
        package='controller_manager',
        executable='spawner',
        arguments=[
            "planar_drive",
            "--controller-manager",
            "/controller_manager",
            ],
    )
    
    return LaunchDescription([
        joint_state_broadcaster_spawner,
        planar_drive_spawner
    ])