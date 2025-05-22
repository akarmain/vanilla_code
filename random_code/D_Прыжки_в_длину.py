def main():
    # n, k = map(int, input().split())
    n, k = 100, 90
    arr = {}
    # arr_input = list(map(int, input().split()))
    arr_input = [727, 878, 803, 905, 290, 438, 141, 756, 940, 446, 36, 273, 130, 783, 523, 845, 698, 369, 802, 48, 886, 485, 247, 983, 255, 865, 904, 402, 221, 432, 934, 108, 314, 760, 905, 839, 322, 240, 784, 913, 510, 219, 789, 356, 713, 154, 90, 673, 850, 576, 624, 128, 757, 443, 859, 510, 490, 105, 533, 268, 356, 171, 590, 256, 211, 465, 785, 417, 170, 356, 112, 969, 524, 789, 391, 80, 335, 354, 80, 107, 150, 781, 449, 391, 705, 27, 967, 311, 88, 637, 966, 447, 781, 632, 439, 338, 279, 205, 266, 874]
    for index, value in enumerate(arr_input):
        arr[index + 1] = value
    if len(set(arr_input)) < k:
        return [-1]
    arr = dict(sorted(arr.items(), key=lambda item: item[1]))
    sorted_dict = list(arr.keys())
    return [sorted_dict[n-k]]+sorted_dict[:n-k]+sorted_dict[n-k+1:]

"""
4 2
templates1.ipynb 2 3 5



"""
if __name__ == '__main__':
    print(*main())
