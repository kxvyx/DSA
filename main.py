#test cases
from staticlist import StaticList
from dynamiclist import dynamicList
from doublylinkedlist import DoublyLinkedList
from doublylinkedlist import DoublyNode
from stack import Stack
from queue import Queue
from tree import TreeNode, BinaryTree
if __name__ == "__main__":
    # # Initialize a list of length 3
    # sl = StaticList(3)

    # print("--- Test 1: Basic Addition ---")
    # sl.add(0, "A")
    # sl.add(1, "B")
    # print(f"Count: {sl.current_count}, List: {sl.list}") # Expected: 2, ['A', 'B', None]

    # print("\n--- Test 2: Overwriting and Fullness ---")
    # sl.add(1, "Z") # Overwrite index 1
    # sl.add(2, "C") # Fill the last slot
    # print(f"Is Full: {sl.isFull()}") # Expected: True
    # print(f"Count: {sl.current_count}, List: {sl.list}") # Expected: 3, ['A', 'Z', 'C']

    # print("\n--- Test 3: Handling Errors ---")
    # sl.add(0, None)       # Should print: Cannot add None to list
    # sl.add("index", 10)   # Should print: Index should be integer only
    # sl.add(5, "Out")      # Should do nothing (0 <= index < length check)

    # print("\n--- Test 4: Deletion ---")
    # sl.delete(1)
    # print(f"After delete index 1: {sl.list}, Count: {sl.current_count}") # Expected: ['A', None, 'C'], 2
    # sl.delete(1) # Delete already None slot
    # print(f"Delete again: {sl.current_count}") # Expected: 2 (should not decrement)

    # print("\n--- Test 5: Boundary Addition ---")
    # sl.add(2, "New C") # Overwrite index 2
    # sl.add(1, "New B") # Fill middle
    # print(f"Final State: {sl.list}, Full: {sl.isFull()}")


    # print("--- DYNAMIC LIST TESTING ---")
    # dl = dynamicList() # Initial capacity is 5

    # print("\n--- Test 1: Filling to Initial Capacity ---")
    # for i in range(5):
    #     dl.append(i * 10)
    # print(f"List: {dl.list.list}")
    # print(f"Capacity: {dl.list.length}, Count: {dl.list.current_count}")
    # # Expected: [0, 10, 20, 30, 40], Cap: 5, Count: 5

    # print("\n--- Test 2: Triggering Auto-Resize (Doubling) ---")
    # dl.append(50) # This should trigger the resize from 5 to 10
    # print(f"List after 6th element: {dl.list.list}")
    # print(f"New Capacity: {dl.list.length}") 
    # # Expected: [0, 10, 20, 30, 40, 50, None, None, None, None], Cap: 10

    # print("\n--- Test 3: Extend with Multiple Elements ---")
    # dl.extend([60, 70, 80])
    # print(f"List after extend: {dl.list.list}")
    # print(f"Current Count: {dl.list.current_count}")
    # # Expected: [0, 10, 20, 30, 40, 50, 60, 70, 80, None], Count: 9

    # print("\n--- Test 4: Access and Search ---")
    # print(f"Value at index 3: {dl.atIndex(3)}") # Expected: 30
    # print(f"Find index of 70: {dl.find(70)}")   # Expected: 7
    # print(f"Find non-existent: {dl.find(999)}") # Expected: Not found

    # print("\n--- Test 5: Summation ---")
    # # 0+10+20+30+40+50+60+70+80 = 360
    # print(f"Sum of elements: {dl.sum()}") 

    # print("\n--- Test 6: Pop and Delete ---")
    # popped = dl.pop()
    # print(f"Popped value: {popped}") # Expected: 80
    # dl.delete(0) # Remove the 0 at the start
    # print(f"List after delete index 0 & pop: {dl.list.list}")
    # print(f"New Sum: {dl.sum()}") # Expected: 280 (360 - 80 - 0)

    # DLL = DoublyLinkedList()

    # print("--- Test 1: Empty List Operations ---")
    # DLL.traverse() # Should print nothing or just None
    # DLL.delete_last_node() # Should print: list is empty
    # DLL.delete_at_position(1) # Should print: position not in range

    # print("\n--- Test 2: Basic Appends ---")
    # DLL.insert_at_end(DoublyNode(10))
    # DLL.insert_at_end(DoublyNode(20))
    # DLL.insert_at_end(DoublyNode(30))
    # print("Forward: ", end=""); DLL.traverse(); print("None")
    # print("Reverse: ", end=""); DLL.reverseTraverse(); print("None")
    # # Expected Forward: 10 -> 20 -> 30 -> None
    # # Expected Reverse: 30 -> 20 -> 10 -> None

    # print("\n--- Test 3: Insert at Boundaries (Start and End) ---")
    # DLL.insert_at_position(1, DoublyNode(5))  # New head
    # DLL.insert_at_position(DLL.size + 1, DoublyNode(40)) # New tail
    # print("After boundary inserts: ", end=""); DLL.traverse(); print("None")
    # # Expected: 5 -> 10 -> 20 -> 30 -> 40 -> None

    # print("\n--- Test 4: Insert in Middle ---")
    # DLL.insert_at_position(3, DoublyNode(15)) # Between 10 and 20
    # print("After middle insert: ", end=""); DLL.traverse(); print("None")
    # # Expected: 5 -> 10 -> 15 -> 20 -> 30 -> 40 -> None

    # print("\n--- Test 5: Modify and Delete ---")
    # DLL.modify_val_at_position(3, 99) # Change 15 to 99
    # DLL.delete_at_position(1) # Delete head (5)
    # DLL.delete_at_position(DLL.size) # Delete tail (40)
    # print("After modify and deletes: ", end=""); DLL.traverse(); print("None")
    # # Expected: 10 -> 99 -> 20 -> 30 -> None

    # print("\n--- Test 6: Final Bidirectional Check ---")
    # print("Final Forward: ", end=""); DLL.traverse(); print("None")
    # print("Final Reverse: ", end=""); DLL.reverseTraverse(); print("None")

    # stack = Stack()

    # # 1. Test Empty Stack
    # print("Testing Empty Pop:", stack.pop()) # Should be None
    # print("Is Empty?", stack.isEmpty())     # Should be True

    # # 2. Test Sequential Pushes
    # for i in range(1, 6):
    #     stack.push(i * 10)
    # print("Stack after 5 pushes:", end=" ")
    # stack.display() # Expected: 10 20 30 40 50
    # print("Size:", stack.size) # Expected: 5

    # # 3. Test Peek (Peak)
    # print("Current Peak:", stack.peak()) # Expected: 50

    # # 4. Test Multi-Pop
    # print("Popped:", stack.pop()) # 50
    # print("Popped:", stack.pop()) # 40
    # print("Size now:", stack.size) # Expected: 3
    # print("New Peak:", stack.peak()) # Expected: 30

    # # 5. Clear the stack
    # while not stack.isEmpty():
    #     stack.pop()
    # print("Size after clearing:", stack.size) # Expected: 0

    # q = Queue()

    # # --- Test 1: Empty Queue Behavior ---
    # print("--- Test 1: Initial State ---")
    # print(f"Is empty? {q.isEmpty()}")      # Expected: True
    # print(f"Peek on empty: {q.peek()}")    # Expected: Message + None
    # print(f"Dequeue on empty: {q.dequeue()}") # Expected: Message + None

    # # --- Test 2: Enqueue Operations ---
    # print("\n--- Test 2: Enqueueing Elements ---")
    # for item in ["Apple", "Banana", "Cherry"]:
    #     q.enqueue(item)
    #     print(f"Enqueued: {item}")
    
    # print("Current Queue: ", end="")
    # print(q.display())                            # Expected: Apple -> Banana -> Cherry ->
    # print(f"Size: {q.size}")               # Expected: 3

    # # --- Test 3: Peek and Dequeue (FIFO Logic) ---
    # print("\n--- Test 3: Dequeueing (FIFO) ---")
    # print(f"Front item (Peek): {q.peek()}")# Expected: Apple
    
    # removed = q.dequeue()
    # print(f"Removed element: {removed}")   # Expected: Apple
    # print("Queue after dequeue: ", end="")
    # print(q.display())                            # Expected: Banana -> Cherry ->
    # print(f"New Size: {q.size}")           # Expected: 2

    # # --- Test 4: Drain to Empty and Re-fill ---
    # print("\n--- Test 4: Emptying and Refilling ---")
    # q.dequeue() # Removes Banana
    # q.dequeue() # Removes Cherry
    # print(f"Is empty after draining? {q.isEmpty()}") # Expected: True
    
    # q.enqueue("Date")
    # print("Queue after refill: ", end="")
    # print(q.display())                            # Expected: Date ->
    # print(f"Peek: {q.peek()}")             # Expected: Date

    BST = BinaryTree()
    for val in [10, 5, 15, 3, 7, 12, 18]:
        BST.insert_node(TreeNode(val))

    print("Original Tree (Inorder - should be sorted):", BST.inorder(BST.root))
    print("Original Tree (Preorder):", BST.preorder(BST.root))
    print("-" * 30)

    # TEST CASE 1: Delete a Leaf Node (e.g., 18)
    # Descent: 10 -> 15 -> 18. Ascent: 18 returns None to 15.
    print("Deleting leaf node 18...")
    BST.delete_node(18, BST.root)
    print("After deleting 18 (Inorder):", BST.inorder(BST.root))
    print("-" * 30)

    # TEST CASE 2: Delete a Node with One Child (e.g., 3)
    # If we add a child to 3 first
    BST.insert_node(TreeNode(2)) 
    print("Deleting node 3 (which now has child 2)...")
    # Descent: 10 -> 5 -> 3. Ascent: 3 returns its left child (2) to node 5.
    BST.delete_node(3, BST.root)
    print("After deleting 3 (Inorder):", BST.inorder(BST.root))
    print("-" * 30)

    # TEST CASE 3: Delete the Root Node with Two Children (10)
    # Descent: Finds 10. Find Predecessor: 7. 
    # Swap: Root becomes 7. Cleanup: Delete duplicate 7 from left branch.
    print("Deleting root node 10...")
    # Capture the return value in case the root object itself changes
    BST.root = BST.delete_node(10, BST.root) 
    print("After deleting root 10 (Inorder):", BST.inorder(BST.root))
    print("New Preorder (Root should be 7):", BST.preorder(BST.root))
    print("-" * 30)

    # TEST CASE 4: Search verification
    print("Searching for deleted 10:", BST.search(10, BST.root))
    print("Searching for existing 7:", BST.search(7, BST.root))