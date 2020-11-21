"""

Given the root to a binary tree, implement serialize(root), which 
serializes the tree into a string, and deserialize(s), which 
deserializes the string back into the tree.

For example, given the following Node class
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'


"""
import re

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root: Node) -> str:
    if root is None:
        return ""
    return f"({root.val},{serialize(root.left)},{serialize(root.right)})"


def deserialize(serialized: str) -> Node:
    if serialized is None:
        return None
    match = re.search(r"\(([\w\.]+),(\(.*\))?,(\(.*\))?\)", serialized)
    if match:
        val, left, right = match.groups()
        return Node(val=val, left=deserialize(left), right=deserialize(right))


node = Node("root", Node("left", Node("left.left")), Node("right"))
assert deserialize(serialize(node)).left.left.val == "left.left"