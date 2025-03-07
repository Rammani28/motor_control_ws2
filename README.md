# Description
This repo contains all the codes required for VEKTOR bot. VEKTOR bot is a six wheeled omnidirectional robot, which uses three omniwheels to drive the bot, while other three wheels to implement odometry. We have used linear odometry due to its simplicity.

# How to use 
* you might need to contact me to actually use this code, as this is an implementation of our custom hardware project.

* git clone this repo on pi
* note that motor_controller is for testing only. The whole bot's code is in vektor/ and custom interfaces are defined in wheel_sensors_interface/

* On pi machine, run the following
```
git clone https://github.com/Rammani28/motor_control_ws2.git
# rosdep init # or similar command to install/manage dependencies
cd ~/ros_ws # your ros workspace
colcon build --symlink-install
source install/setup.bash
ros2 launch vektor vektor_launch.py
```
### Note:
Pressing r2 button of joystick is compulsory for the bot to move. 
gpio pins used for motors are defined in motor_ccontrol.py
pins used for sensors are defined in main.py which lies in pico_code_dump/ .
uart is used as communication standard between pi and pico, at baudrate 192500.
