def binary_search(arr: list[int], val: int):
    left, right = 0, len(arr) - 1
    print(f"left: {left}")
    print(f"right: {right}")
    while left <= right:
        mid = (left + right) // 2
        print(f"mid: {arr[mid]}")
        if val == arr[mid]:
            return mid
        elif val < arr[mid]:
            left = mid + 1
            print(f"the remaining arr: {arr[left:right]}")
        elif val > arr[mid]:
            right = mid - 1
            print(f"the remaining arr: {arr[left:right]}")
        else:
            print("idk what happened")
    return left


if __name__ == "__main__":
    result =     binary_search([100, 90, 90, 80, 75, 60], 65)
    print(result)
