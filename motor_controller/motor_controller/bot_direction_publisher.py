import math
from std_msgs.msg import String
from sensor_msgs.msg import Joy
import rclpy
from rclpy.node import Node

def get_angle(strafe_x, strafe_y):
    if strafe_x == 0 and strafe_y == 0: # if all values are 0, stop the bot
            angle = 501
    else:
        angle = math.degrees(math.atan2(strafe_x, strafe_y))  # Swap arguments to adjust direction
        angle = (360 - angle) % 360  # Normalize to 0-360
    return angle

def get_wbz(rotate_x):
    if abs(rotate_x) < 1:
        wbz = 501
    else:
        wbz = rotate_x
    return wbz

class BotDirectionPublisher(Node):
    def __init__(self):
        super().__init__('bot_direction_publisher') # node name
        self.publisher = self.create_publisher(msg_type=String, topic='/bot_direction', qos_profile=10) # data of type string, publish to topic /bot_direction, qos_profile read here https://docs.ros.org/en/rolling/Concepts/Intermediate/About-Quality-of-Service-Settings.html#qos-profiles
        self.subscription = self.create_subscription(msg_type=Joy, topic='/joy', callback=self.joy_callback, qos_profile=10) # subscribe to /Joy node
        self.get_logger().info("Bot Direction Node initialized. listening to joystick input...")

    def joy_callback(self, msg):
        """0, 1, 3 are the index of joy sticks in message published by /joy"""
        strafe_x = msg.axes[0]  
        strafe_y = msg.axes[1]  
        rotate_x = msg.axes[3]
        angle = 501
        wbz = 0

        angle = get_angle(strafe_x, strafe_y)
        wbz = get_wbz(rotate_x)
        
        message_to_be_published = f"{angle:.2f},{wbz}"
        self.publish_message(message_to_be_published) # angle will be from 0 to 360, or 501

    def publish_message(self, msg):
        message = String()
        message.data = msg
        self.publisher.publish(message)
        self.get_logger().info(f"Published: {message.data}") # log message to console


def main(args=None):
    rclpy.init(args=args)
    node = BotDirectionPublisher()
    try:
        rclpy.spin(node=node) # keep node running
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()