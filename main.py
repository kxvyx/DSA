#test cases
from staticlist import StaticList
from dynamiclist import dynamicList
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


    print("--- DYNAMIC LIST TESTING ---")
    dl = dynamicList() # Initial capacity is 5

    print("\n--- Test 1: Filling to Initial Capacity ---")
    for i in range(5):
        dl.append(i * 10)
    print(f"List: {dl.list.list}")
    print(f"Capacity: {dl.list.length}, Count: {dl.list.current_count}")
    # Expected: [0, 10, 20, 30, 40], Cap: 5, Count: 5

    print("\n--- Test 2: Triggering Auto-Resize (Doubling) ---")
    dl.append(50) # This should trigger the resize from 5 to 10
    print(f"List after 6th element: {dl.list.list}")
    print(f"New Capacity: {dl.list.length}") 
    # Expected: [0, 10, 20, 30, 40, 50, None, None, None, None], Cap: 10

    print("\n--- Test 3: Extend with Multiple Elements ---")
    dl.extend([60, 70, 80])
    print(f"List after extend: {dl.list.list}")
    print(f"Current Count: {dl.list.current_count}")
    # Expected: [0, 10, 20, 30, 40, 50, 60, 70, 80, None], Count: 9

    print("\n--- Test 4: Access and Search ---")
    print(f"Value at index 3: {dl.atIndex(3)}") # Expected: 30
    print(f"Find index of 70: {dl.find(70)}")   # Expected: 7
    print(f"Find non-existent: {dl.find(999)}") # Expected: Not found

    print("\n--- Test 5: Summation ---")
    # 0+10+20+30+40+50+60+70+80 = 360
    print(f"Sum of elements: {dl.sum()}") 

    print("\n--- Test 6: Pop and Delete ---")
    popped = dl.pop()
    print(f"Popped value: {popped}") # Expected: 80
    dl.delete(0) # Remove the 0 at the start
    print(f"List after delete index 0 & pop: {dl.list.list}")
    print(f"New Sum: {dl.sum()}") # Expected: 280 (360 - 80 - 0)