"""
Given the root of a binary tree, mirror the tree, and return its root.

Leetcode problem reference: https://leetcode.com/problems/mirror-binary-tree/
"""

from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass


@dataclass
class Node:
    """
    A Node has value variable and pointers to Nodes to its left and right.
    """

    value: int
    left: Node | None = None
    right: Node | None = None

    def __iter__(self) -> Iterator[int]:
        if self.left:
            yield from self.left
        yield self.value
        if self.right:
            yield from self.right

    def __len__(self) -> int:
        return sum(1 for _ in self)

    def mirror(self) -> Node:
        """
        Mirror the binary tree rooted at this node by swapping left and right children.
        """
        self.left, self.right = self.right, self.left
        if self.left:
            self.left.mirror()
        if self.right:
            self.right.mirror()
        return self
