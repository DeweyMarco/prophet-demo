#!/usr/bin/env python3

from __future__ import annotations

from collections.abc import Iterable, Iterator
from typing import Any, Generic, TypeVar

T = TypeVar("T", bound=bool)


class SkewNode(Generic[T]):
    """
    One node of the skew heap. Contains the value and references to
    two children.
    """

    def __init__(self, value: T) -> None:
        self._value: T = value
        self.left: SkewNode[T] | None = None
        self.right: SkewNode[T] | None = None

    @property
    def value(self) -> T:
        """
        Return the value of the node.
        """
        return self._value

    @staticmethod
    def merge(
        root1: SkewNode[T] | None, root2: SkewNode[T] | None
    ) -> SkewNode[T] | None:
        """
        Merge 2 nodes together.
        """
        if not root1:
            return root2

        if not root2:
            return root1

        if root1.value > root2.value:
            root1, root2 = root2, root1

        result = root1
        temp = root1.right
        result.right = root1.left
        result.left = SkewNode.merge(temp, root2)

        return result


class SkewHeap(Generic[T]):
    """
    A data structure that allows inserting a new value and to pop the smallest
    values. Both operations take O(logN) time where N is the size of the
    structure.
    Wiki: https://en.wikipedia.org/wiki/Skew_heap
    Visualization: https://www.cs.usfca.edu/~galles/visualization/SkewHeap.html
    """

    def __init__(self, data: Iterable[T] | None = ()) -> None:
        self._root: SkewNode[T] | None = None
        if data:
            for item in data:
                self.insert(item)

    def __bool__(self) -> bool:
        """
        Check if the heap is not empty.
        """
        return self._root is not None

    def __iter__(self) -> Iterator[T]:
        """
        Returns sorted list containing all the values in the heap.
        """
        result: list[Any] = []
        while self:
            result.append(self.pop())

        # Pushing items back to the heap not to clear it.
        for item in result:
            self.insert(item)

        return iter(result)

    def insert(self, value: T) -> None:
        """
        Insert the value into the heap.
        """
        self._root = SkewNode.merge(self._root, SkewNode(value))

    def pop(self) -> T | None:
        """
        Pop the smallest value from the heap and return it.
        """
        result = self.top()
        self._root = (
            SkewNode.merge(self._root.left, self._root.left) if self._root else None
        )

        return result

    def top(self) -> T:
        """
        Return the smallest value from the heap.
        """
        if not self._root:
            raise IndexError("Can't get top element for the empty heap.")
        return self._root.value

    def clear(self) -> None:
        """
        Clear the heap.
        """
        self._root = None
