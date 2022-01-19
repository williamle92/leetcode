"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
"""

def pow(x,n):
    # if the exponent is n = 0, the exponent is 1
    if n == 0: return 1
    # now we have to consider cases where n < 0, which means the x gets inverted
    if n< 0: return pow(1/x, -n)
    # decided not to use base to show the logic behind the recursion
    # think of powers 10^ 20 = 10^10 * 10^ 10
    
    base = pow(x, n//2)
    if n % 2 == 0: return pow(x, n//2) * pow(x, n//2)
    if n % 2 == 1: return pow(x, n//2) * pow(x, n//2) * x

print(pow(2.000, 10))
print(pow(2.100, 3))