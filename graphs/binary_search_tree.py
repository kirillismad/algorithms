from collections import deque
from typing import Tuple, TypeVar, Optional

NodeType = TypeVar('NodeType', bound='Node')


class Node:
    def __init__(self, data):
        self.data = data
        self.left: Optional[NodeType] = None
        self.right: Optional[NodeType] = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        left = 'None' if self.left is None else self.left.mini_repr()
        right = 'None' if self.right is None else self.right.mini_repr()
        return 'Node(data={data!r}, left={left}, right={right})'.format(
            data=self.data,
            left=left,
            right=right,
        )

    def mini_repr(self):
        return f'Node(data={self.data!r})'

    def printable(self):
        return f'({self.data})'

    @property
    def is_leaf(self):
        return all(child is not None for child in (self.right, self.left))

    @property
    def has_single_child(self):
        return (self.left is not None and self.right is None) or (self.left is None and self.right is not None)

    def get_single_child(self):
        return self.left or self.right



class BinaryTree:
    def __init__(self):
        self.root = None
        self.count = 0

    def __str__(self):
        return str(self.root)

    def __repr__(self):
        pass

    def _add(self, node, data):
        if data >= node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                self._add(node.right, data)
        else:
            if node.left is None:
                node.left = Node(data)
            else:
                self._add(node.left, data)

    def add(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._add(self.root, data)

        self.count += 1

    def remove(self, data):
        r = self.find(data)
        if r is None:
            return False

        current, parent = r

        if current.is_leaf:
            if current.data < parent.data:
                parent.left = None
            elif current.data > parent.data:
                parent.right = None

        elif current.has_single_child:
            if current.data < parent.data:
                parent.left = current.get_single_child()
            elif current.data > parent.data:
                parent.right = current.get_single_child()

    def remove2(self, data):
        pass

        # # у удаляемого узла нет правого ребенка
        # if current.right is None:
        #     # удаляемый элемент это корень
        #     if parent is None:
        #         self.root = current.left
        #
        #     else:
        #         # удаляемый узел стоял слева
        #         if current.data < parent.data:
        #             parent.left = current.left
        #         # удаляемый узел стоял справа
        #         elif current.data > parent.data:
        #             parent.right = current.left

    def find(self, data) -> Optional[Tuple[NodeType, NodeType]]:
        current = self.root
        parent = None

        while current is not None:
            if data == current.data:
                return current, parent

            elif data > current.data:
                parent = current
                current = current.right
            else:
                parent = current
                current = current.left

    def __contains__(self, data):
        return self.find(data) is not None

    def print(self):
        result = []
        dq = deque([(0, self.root)])
        while dq:
            lvl, node = dq.popleft()

            try:
                result[lvl].append(node)
            except IndexError:
                result.append([])
                result[lvl].append(node)

            if node.left is not None:
                dq.append((lvl + 1, node.left))

            if node.right is not None:
                dq.append((lvl + 1, node.right))

        for lvl, item in enumerate(result):
            print(f'lvl {lvl}: ', [str(n) for n in item])


def main():
    lst = [4, 2, 6, 1, 3, 5, 7]

    tree = BinaryTree()

    for i in lst:
        tree.add(i)

    tree.print()


if __name__ == '__main__':
    main()
