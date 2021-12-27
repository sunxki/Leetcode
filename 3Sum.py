python = 'https://leetcode.com/problems/3sum/'
nums = [-1,0,1,2,-1,-4]
nums2 = [0,0,0]
num3 = [0]

def threeSum(nums):
    working_matrix = (sorted(nums, reverse=True))
    result = []

    if len(working_matrix) == 0:
        return result
    if len(working_matrix) == 1 and working_matrix[0] == 0:
        return result
    if sum(working_matrix) == 0:
        return result
    if len(working_matrix) >= 3 and sum(working_matrix) == 0:
        return [working_matrix]

    if len(nums) > 3 and sum(working_matrix) != 0:
        for index, i in enumerate(working_matrix):
            if i < 0:
                a = working_matrix[0:index - 1]
                b = working_matrix[index:len(working_matrix)]
                break
        for first in a:
            a_ = a.copy()
            a_.remove(first)
            for second in a_:
                for third in b:
                    if first + second + third == 0:
                        if [first, second, third] not in result:
                            result.append([first, second, third])
        for first in b:
            b_ = b.copy()
            b_.remove(first)
            for second in b_:
                for third in a:
                    if first + second + third == 0:
                        if [first, second, third] not in result:
                            result.append([first, second, third])

        if 0 in working_matrix:
            for i in working_matrix:
                if (i + working_matrix[-1]) != 0:
                    working_matrix.pop()
                if (i + working_matrix[-1] == 0):
                    result.append([+working_matrix[-1], 0, i])
    return result

print(threeSum(nums))
print(threeSum(nums2))
print(threeSum(num3))