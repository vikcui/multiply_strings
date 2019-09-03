# author: YANG CUI
"""
Given two non-negative integers num1 and num2 represented as strings,
return the product of num1 and num2, also represented as a string.
Note:
The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

Code in https://leetcode.com/problems/multiply-strings/discuss/368066/Python-Solution-or-Faster-than-95-or-Place-Values-or-ASCII
was taken for inspiration.
"""


def multiply(num1, num2):
    num1List = [0] * len(num1)
    num2List = [0] * len(num2)
    # convert strings to lists containing the same digits
    for i in range(len(num1)):
        num1List[i] = ord(num1[i])-ord("0")
    for j in range(len(num2)):
        num2List[j] = ord(num2[j])-ord("0")
    # parse lists to ints
    highest_base1 = 10 ** (len(num1List) - 1)
    highest_base2 = 10 ** (len(num2List) - 1)
    value1 = 0
    value2 = 0
    for digit in num1List:
        value1 += highest_base1 * digit
        highest_base1 //= 10
    for digit in num2List:
        value2 += highest_base2 * digit
        highest_base2 //= 10
    return str(value1 * value2)

# print(multiply("111","222"))