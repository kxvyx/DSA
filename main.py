#test cases
from staticlist import StaticList

if __name__ == "__main__":
    # Initialize a list of length 3
    sl = StaticList(3)

    print("--- Test 1: Basic Addition ---")
    sl.add(0, "A")
    sl.add(1, "B")
    print(f"Count: {sl.current_count}, List: {sl.list}") # Expected: 2, ['A', 'B', None]

    print("\n--- Test 2: Overwriting and Fullness ---")
    sl.add(1, "Z") # Overwrite index 1
    sl.add(2, "C") # Fill the last slot
    print(f"Is Full: {sl.isFull()}") # Expected: True
    print(f"Count: {sl.current_count}, List: {sl.list}") # Expected: 3, ['A', 'Z', 'C']

    print("\n--- Test 3: Handling Errors ---")
    sl.add(0, None)       # Should print: Cannot add None to list
    sl.add("index", 10)   # Should print: Index should be integer only
    sl.add(5, "Out")      # Should do nothing (0 <= index < length check)

    print("\n--- Test 4: Deletion ---")
    sl.delete(1)
    print(f"After delete index 1: {sl.list}, Count: {sl.current_count}") # Expected: ['A', None, 'C'], 2
    sl.delete(1) # Delete already None slot
    print(f"Delete again: {sl.current_count}") # Expected: 2 (should not decrement)

    print("\n--- Test 5: Boundary Addition ---")
    sl.add(2, "New C") # Overwrite index 2
    sl.add(1, "New B") # Fill middle
    print(f"Final State: {sl.list}, Full: {sl.isFull()}")