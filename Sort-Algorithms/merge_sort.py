def merge_sort(items):
  if len(items) <= 1:
    return items
    # Split the list in half
  middle_index = len(items) // 2
  left_split = items[:middle_index]
  right_split = items[middle_index:]
    # split the list into smaller list, eventually will be only item with recursive function
  left_sorted = merge_sort(left_split)
  right_sorted = merge_sort(right_split)

  return merge(left_sorted, right_sorted)

def merge(left, right):
  result = []
    # Checking which number is lower then will add to the new ordered list
    # The loop will stop when one of the list is empty
  while (left and right):
    if left[0] < right[0]:
      result.append(left.pop(0))
    else:
      result.append(right.pop(0))
    # What ever has left in the list, either left or right (which is already sorted), will add 
  if left:
    result += left
  if right:
    result += right

  return result

