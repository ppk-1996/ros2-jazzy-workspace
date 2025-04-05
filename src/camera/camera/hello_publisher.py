#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class HelloPublisher(Node):
    def __init__(self)->None:
        super().__init__('hello_publisher')
        self.publisher_ = self.create_publisher(String, 'hello_topic', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self)->None:
        msg = String()
        msg.data = "Hello"
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data}')

    def get(self)->str:
        s = "string"
        return s
def main()->None:
    rclpy.init()
    node = HelloPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
