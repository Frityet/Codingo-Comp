# Uncomment the code below and fix the bug as described in the question.
# Underneath the fixed code, describe what the initial issue was and how
# you fixed it.


CONVERSION_RATE = 0.393701


def height_conversion(heights):
    heights_in_inches = []
    for i in range(0, len(heights)):
        heights_in_inches.append(heights[i] * CONVERSION_RATE)
    return heights_in_inches

l = [ 10, 7, 8 ]

print(height_conversion(l))
