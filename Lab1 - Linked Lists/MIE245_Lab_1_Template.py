class Node:
    def __init__(self, value):
        """ Node class.  This does not need to be modified. """
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        """ Initialize head/tail to none (be sure to update these when appropriate). """
        self.head = None  
        self.tail = None 

    def insert_start(self, value):
        """ Inserts a Node with Value to the start of the LinkedList. """
        start = Node(value)
        # If no nodes in list: start = head = tail
        if self.head is None:
            self.head = start
            self.tail = start
            return
        # If >= 1 nodes in list: start -> head
        else:
            start.next = self.head
            self.head = start
        return

    def insert_end(self, value):
        """ inserts a Node with Value to the end of the LinkedList. """
        end = Node(value)
        # If no nodes in list: end = head = tail
        if self.head is None:
            self.head = end
            self.tail = end
        # If >= 1 nodes in list: tail -> end
        else:
            self.tail.next = end
            self.tail = end
        return

    def search_for_node_by_value(self, value):
        """ Searches for a Node with Value in the LinkedList. """
        check = self.head
        # If no nodes (left) in list: return check = None
        while check is not None:
            if check.value == value:
                return check
            check = check.next 
        return check

    def delete_node_by_value(self, value):
        """ Deletes a Node with Value in the LinkedList. 
            If the node does not exist, then does nothing.
        """
        prev = None
        check = self.head

        # # V1: Use check.value == value at the start
        # # If no nodes (left) in list: return
        # while check is not None:
        #     if check.value == value:
        #         # If check is head
        #         if prev is None:
        #             self.head = check.next
        #             # If check is head and tail
        #             if check == self.tail:
        #                 self.tail = self.head
        #         else:
        #             # If check is in middle
        #             prev.next = check.next
        #             # If check is tail
        #             if check == self.tail:
        #                 self.tail = prev
        #         return
        #     prev = check
        #     check = check.next
                
        # V2: Use check.value != value at the start + continue
        # If no nodes (left) in list: return
        while check is not None:
            if check.value != value:
                prev = check
                check = check.next
                continue
            # If check is head and tail
            if (check == self.head) and (check == self.tail):
                self.head = None
                self.tail = None
            # If check is head
            elif check == self.head:
                self.head = check.next
            # If check is tail
            elif check == self.tail:
                self.tail = prev
                prev.next = None
            # If check is in middle
            else:
                prev.next = check.next
            return
        return
    
# def get_candidate_order(linked_list):
#     current = linked_list.head
#     candidate_order = []
#     while current:
#         candidate_order.append(int(current.value))
#         current = current.next
#     return candidate_order

# list = LinkedList()
# list.insert_start(1)
# list.insert_start(2)
# list.insert_end(3)
# list.insert_end(4)
# list.delete_node_by_value(4)
# print(get_candidate_order(list)) 
