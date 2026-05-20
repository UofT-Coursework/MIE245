import random
import time
import matplotlib.pyplot as plt

RED = 1
BLACK = 0

class RedBlackNode:
    def __init__(self, data, left=None, right=None, color=RED, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.color = color
        self.parent = parent


class RedBlackTree:
    def __init__(self):
        self.NIL = RedBlackNode(None, color=BLACK)
        self.root = self.NIL

    def insert(self, data):
        
        # Create new node
        node = RedBlackNode(data, left=self.NIL, right=self.NIL, color=RED, parent=self.NIL)
        current = self.root # start at root
        parent = self.NIL # track parent of current node - self.NIL if current is root

        # While not leaf, keep traversing 
        while current is not self.NIL:
            parent = current
            if data < current.data:
                current = current.left
            else:
                current = current.right
        # Set parent of new node to last non-leaf
        node.parent = parent

        # If tree empty, node is root, else set as left/right child
        if parent is self.NIL:
            self.root = node
        elif data < parent.data:
            parent.left = node
        else:
            parent.right = node

        # fixup tree properties
        self.insert_fixup(node)
        return

    def traverse_inorder(self, node):
        if node != self.NIL:
            self.traverse_inorder(node.left)
            print(f"{node.data}-{node.color}", end=" ")
            self.traverse_inorder(node.right)

    def rotate_left(self, node):
        x, y = node, node.right

        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def rotate_right(self, node):
        y, x = node, node.left

        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y

        x.parent = y.parent
        if y.parent == self.NIL:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x

        x.right = y
        y.parent = x

    def insert_fixup(self, node):
        while node.parent.color == RED:
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right

                if uncle.color == RED:
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.rotate_left(node)

                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self.rotate_right(node.parent.parent)

            else:
                uncle = node.parent.parent.left

                if uncle.color == RED:
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.rotate_right(node)
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self.rotate_left(node.parent.parent)

        self.root.color = BLACK

    def search(self, data):
        curr_node = self.root

        while curr_node != self.NIL and curr_node.data != data:
            if data < curr_node.data:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right

        return curr_node

    def search_inorder_successor(self, node):
        curr_node = node.right
        if node.right == self.NIL:
            return curr_node

        while curr_node.left != self.NIL:
            curr_node = curr_node.left

        return curr_node

    def transplant(self, u, v):
        if u.parent == self.NIL:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

        v.parent = u.parent

    def delete_fixup(self, x):
        while x != self.root and x.color == BLACK:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self.rotate_left(x.parent)
                    w = x.parent.right
                if w.left.color == BLACK and w.right.color == BLACK:
                    w.color = RED
                    x = x.parent
                else:
                    if w.right.color == BLACK:
                        w.left.color = BLACK
                        w.color = RED
                        self.rotate_right(w)
                        w = w.parent.right

                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.right.color = BLACK
                    self.rotate_left(x.parent)
                    x = self.root

            else:
                w = x.parent.left
                if w.color == RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self.rotate_right(x.parent)
                    w = x.parent.left
                if w.right.color == BLACK and w.left.color == BLACK:
                    w.color = RED
                    x = x.parent
                else:
                    if w.left.color == BLACK:
                        w.right.color = BLACK
                        w.color = RED
                        self.rotate_left(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.left.color = BLACK
                    self.rotate_right(x.parent)
                    x = self.root

        x.color = BLACK

    def delete(self, data):
        node = self.search(data)
        if node == self.NIL:
            return

        y = node
        y_original_color = y.color
        if node.left == self.NIL:
            x = node.right
            self.transplant(node, node.right)
        elif node.right == self.NIL:
            x = node.left
            self.transplant(node, node.left)
        else:
            y = self.search_inorder_successor(node)
            y_original_color = y.color
            x = y.right
            if y != node.right:
                self.transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            else:
                x.parent = y
            self.transplant(node, y)
            y.left = node.left
            y.left.parent = y
            y.color = node.color

        if y_original_color == BLACK:
            self.delete_fixup(x)

class SkipNode:
    def __init__(self, height=0, elem=None):
        self.elem = elem
        self.next = [None] * height # list of next pointers for each level

class SkipList:
    def __init__(self):
        self.head = SkipNode() # head node, None elem and empty next list
        self.maxHeight = 1

    def randomHeight(self):
        height = 1
        while random.random() < 0.5:
            height += 1
        return height

    def find(self, elem):
        node = self.head
        # Iterate from top level down, at each level traverse right while next node is less than elem
        for level in reversed(range(len(self.head.next))):
            while node.next[level] and node.next[level].elem < elem:
                node = node.next[level]
        # Return next node at level 0 if it exists and matches elem, else None
        return node.next[0] if node.next and node.next[0] and node.next[0].elem == elem else None

    def insert(self, elem):
        
        # node is current node at each level, start at head
        node = self.head
        # keep track of last node at each level before elem
        update = [None] * len(self.head.next)

        # traverse down levels, reverse to start from top level
        for level in reversed(range(len(self.head.next))):
            # while next node exists and is less, traverse right 
            while node.next[level] and node.next[level].elem < elem:
                # point to next node at this level
                node = node.next[level] 
            update[level] = node # last node before elem at this level is current node

        height = self.randomHeight() # generate height

        # In case height exceeds current max
        while len(self.head.next) < height:
            self.head.next.append(None) # add new level slot
            update.append(self.head) # head is predecessor for new level
        self.maxHeight = max(self.maxHeight, height) # update max height if needed

        # create new node and splice into each level
        newNode = SkipNode(height, elem)

        # for each level of new node, update pointers (update[level] is predecessor)
        for level in range(height):
            newNode.next[level] = update[level].next[level] # new node points to next node at this level
            update[level].next[level] = newNode # update node points to new node at this level

        return

    def delete(self, elem):
        update = [None] * len(self.head.next)
        node = self.head
        for level in reversed(range(len(self.head.next))):
            while node.next[level] and node.next[level].elem < elem:
                node = node.next[level]
            update[level] = node

        target = node.next[0] if node.next else None
        if target and target.elem == elem:
            for level in range(len(target.next)):
                update[level].next[level] = target.next[level]


class Experiment:
    def __init__(self, data):
        self.data = data
        self.insert_plot = None
        self.delete_plot = None

    def get_insert_times(self, data_structure):
        runtimes = []

        for elem in self.data:
            start = time.perf_counter()
            data_structure.insert(elem)
            end = time.perf_counter()
            runtimes.append(end-start)

        return runtimes

    def get_delete_times(self, data_structure):
        runtimes = []

        for elem in self.data:
            start = time.perf_counter()
            data_structure.delete(elem)
            end = time.perf_counter()
            runtimes.append(end-start)

        return runtimes

    def plot_insert_times(self, insert_times_RBT, insert_times_SL):
        fig, ax = plt.subplots()
        self.insert_plot = fig

        ax.plot(self.data, insert_times_RBT, label="Red-Black Tree")
        ax.plot(self.data, insert_times_SL, label="Skip List")
        ax.set_ylabel("Runtime (s)")
        ax.set_xlabel("Inserted Elem")
        ax.legend()

        ax.set_xticks(self.data)
        ax.set_xticklabels(self.data)
        ax.set_title("Insert Runtimes for RBT vs SL")

        plt.show()

    def plot_delete_times(self, delete_times_RBT, delete_times_SL):
        fig, ax = plt.subplots()
        self.delete_plot = fig

        ax.plot(self.data, delete_times_RBT, label="Red-Black Tree")
        ax.plot(self.data, delete_times_SL, label="Skip List")
        ax.set_ylabel("Runtime (s)")
        ax.set_xlabel("Deleted Elem")
        ax.legend()

        ax.set_xticks(self.data)
        ax.set_xticklabels(self.data)
        ax.set_title("Delete Runtimes for RBT vs SL")

        plt.show()