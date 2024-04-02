import rclpy
from first_pkg.advanced_node_interface import AdvancedNode

def main(args=None):
    # initialize ROS client library for Python
    # initialize ROS communications
    rclpy.init(args=args)
    # instantiate a node
    node = AdvancedNode("advanced_node")
    # print message in the terminal
    node.get_logger().info("Hello World")
    # clean up
    rclpy.shutdown()