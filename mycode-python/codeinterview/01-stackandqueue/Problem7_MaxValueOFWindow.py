class MaxValueOFWindow:
    @classmethod
    def get_max_values(cls, arr, window):
        if len(arr) == 0 or window < 1 or len(arr) < window:
            return None

        index = 0
        deque = list()
        max_values = list()     # len(max_values) = len(arr) - window + 1

        while index < len(arr):
            while len(deque) > 0 and arr[index] >= arr[deque[-1]]:
                deque.pop()
            deque.append(index)

            if deque[-1] - deque[0] == window:
                deque.pop(0)

            if index >= window - 1:
                max_values.append(arr[deque[0]])

            index += 1

        return max_values

if __name__ == '__main__':
    # res = MaxValueOFWindow.get_max_values([4, 3, 5, 4, 3, 3, 6, 7], 3)
    res = MaxValueOFWindow.get_max_values([5,4,3,2,1,6], 6)
    print(res)
