class Sorter:    
    def insertion_sort(self, input_list):
        """
        Sorts a list of integers using the Insertion Sort algorithm.
        
        Args:
            input_list (list): A list of integers (e.g., [4, 2, 7, 1])
            
        Returns:
            list: The sorted list in ascending order.
        """
        # TODO: Implement Insertion Sort
        for i in range(1, len(input_list)):
            num = input_list[i] # set current number num
            j = i # set position to num 
            while num < input_list[j - 1] and j > 0: # while num < previous number and j-1 >= 0
                input_list[j] = input_list[j - 1] # replace current position with previous number
                j -= 1 # shift position to left 
            input_list[j] = num # insert num at correct position
        return input_list

    # def merge(array, tmp, lo, mid, hi):
    #     i = lo
    #     j = mid + 1
    #     for k in range(lo, hi + 1): 
    #         if j > hi or (i <= mid and array[i] <= array[j]):
    #             tmp[k] = array[i]
    #             i += 1
    #         else:
    #             tmp[k] = array[j]
    #             j += 1
    #     for k in range(lo, hi + 1):  # k = lo,...,hi
    #         array[k] = tmp[k]

    def merge_sort(self, input_list):
        """
        Sorts a list of integers using the Merge Sort algorithm.
        
        Args:
            input_list (list): A list of integers (e.g., [4, 2, 7, 1])
            
        Returns:
            list: The sorted list in ascending order.
        """
        # TODO: Implement Merge Sort
        if len(input_list) <= 1: # initial list could be 0, fully broken down lists will be == 1
            return input_list
        
        mid = len(input_list) // 2 # floor in case of odd length

        sorted_left = self.merge_sort(input_list[:mid]) # left half of input - recursive
        sorted_right = self.merge_sort(input_list[mid:]) # right half of input - recursive
        return self.merge(sorted_left, sorted_right) # starting from len=1 lists, merge back up

    def merge(self, left, right):
        sorted = [] # empty list to store sorted elements
        i = j = 0
        # Say all values in left are smaller than all values in right, 
        # then we want to add all values in left first before adding any from right.
        # However, after the last iteration, i will be equal to len(left) and the loop breaks
        # so we need to add the remaining values in right to sorted.
        # The same logic applies if all values in right are smaller than all values in left.
        # 
        # The reason this works is because the merge function is only called with sorted lists, 
        # so we can guarantee that all remaining values in whichever list are in order.
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                sorted.append(left[i])
                i += 1
            else:
                sorted.append(right[j])
                j += 1
        sorted.extend(left[i:])
        sorted.extend(right[j:])
        return sorted
    

# def test_case_insertion():
#     """ Tests the insertion_sort function inside Sorter class """
#     try:
#         # 1. Ground truth
#         input_data = [38, 27, 27, 43, 3, 9, 9, 9, 10, 82, 10]
#         ground_truth = sorted(input_data.copy())
#         # 2. Instantiate Student Class
#         sorter = Sorter()
#         # 3. Get candidate result
#         # Passing a copy to ensure the student function doesn't modify original for comparison
#         candidate_result = sorter.insertion_sort(input_data.copy())
#         # 4. Compare
#         if candidate_result == ground_truth:
#             return 1
#         return 0
#     except Exception as e:
#         # print(f"Debug - Insertion Sort Error: {e}") # Uncomment for debugging
#         return 0

# def test_case_merge():
#     """ Tests the merge_sort function inside Sorter class """
#     try:
#         # 1. Ground truth
#         input_data = [38, 27, 27, 43, 3, 9, 9, 9, 10, 82, 10]
#         ground_truth = sorted(input_data.copy())
#         # 2. Instantiate Student Class
#         sorter = Sorter()
#         # 3. Get candidate result
#         candidate_result = sorter.merge_sort(input_data.copy())
#         # 4. Compare
#         if candidate_result == ground_truth:
#             return 1
#         return 0
#     except Exception as e:
#         # print(f"Debug - Merge Sort Error: {e}") # Uncomment for debugging
#         return 0
    
# print(test_case_insertion())
# print(test_case_insertion())