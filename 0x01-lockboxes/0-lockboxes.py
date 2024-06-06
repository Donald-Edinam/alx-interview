def canUnlockAll(boxes):
    # Set of opened boxes: Box 1 is opened by default
    opened_boxes = set([0])
    # Stack
    stack = [0]

    # algorithm
    while stack:
        current_box = stack.pop()
        print("Current box", current_box)

        # Iteration
        for key in boxes[current_box]:
            if key not in opened_boxes and key < len(boxes):
                opened_boxes.add(key)
                stack.append(key)
    return len(opened_boxes) == len(boxes)


boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))