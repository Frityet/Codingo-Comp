"""
This function takes in a list of numbers and returns the 
average of all the numbers rounded down.

Arguments:
    list_of_nums (List[int] Array of integers): A list of the numbers
Returns:
    the average of all the numbers rounded down
Examples:
    [1,2,3,4] => 2
    [100] => 100
Notes:
    - You can assume that the list is not empty
"""


def average_of_list(list_of_nums):
    if len(list_of_nums) == 0:
        return 0
    sum = 0
    for i in list_of_nums:
        sum += i
    return sum / len(list_of_nums)


