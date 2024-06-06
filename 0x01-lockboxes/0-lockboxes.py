#!/usr/bin/python3
"""Solves the lock boxes puzzle """

def look_next_opened_box(opened_boxes):
    """Looks for the next opened box
    Args:
        opened_boxes (dict): Dictionary which contains boxes already opened
    Returns:
        int: The index of the next opened box or None if no such box exists
    """
    for index, box in opened_boxes.items():
        if box.get('status') == 'opened':
            box['status'] = 'opened/checked'
            return index
    return None

def canUnlockAll(boxes):
    """Check if all boxes can be opened
    Args:
        boxes (list): List which contain all the boxes with the keys
    Returns:
        bool: True if all boxes can be opened, otherwise, False
    """
    if len(boxes) <= 1 or boxes == [[]]:
        return True

    # Dictionary to manage the boxes' statuses and keys
    aux = {}
    aux[0] = {'status': 'opened', 'keys': boxes[0]}

    while True:
        current_index = look_next_opened_box(aux)
        if current_index is not None:
            keys = aux[current_index]['keys']
            for key in keys:
                if key < len(boxes) and key not in aux:
                    aux[key] = {'status': 'opened', 'keys': boxes[key]}
        else:
            break

    # Check if all boxes have been opened
    return len(aux) == len(boxes)

def main():
    """Entry point"""
    print(canUnlockAll([[]]))

if __name__ == '__main__':
    main()
