#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class MayBePub(Node):
    def __init__(self):
        super().__init__('maybe_pub')
        self.publisher_ = self.create_publisher(String, 'maybe_topic', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = "maybe"
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data}')


def main():
    rclpy.init()
    node = MayBePub()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
