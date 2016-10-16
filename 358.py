#!/usr/bin/python
# -*- coding: utf-8

# 142857 × 6 = 999999
# 0588235294117647 × 17 = 9999999999999999

def digit_sum(a):
    s = 0
    while a > 0:
        s += a % 10
        a /= 10

    return s

def find_rem(k, x, rem):
    # x * value ends by rem

    ret = 0
    idx = 1

    while k > 0:
        k -= 1
        idx *= 10

        for i in range(10):
            if ( x % idx ) * ( i * idx / 10 + ret ) % idx == rem % idx:
                ret = i*idx/10 + ret
                break

    return ret

print [ find_rem(5, 56789, rem) for rem in (1,13,137,90000,67890, 78900, 89000) ]
print find_rem(4,8789,5678)
lst = find_rem(5, 56789, 10**5-1)
print lst

sums = [ digit_sum(a) for a in range(0,10**5) ]
total = sum(sums[56789 * a % 10**5] for a in range(1,9891+10**5))
print total/5

# n = 100009891
# for i in range(1,10**5):
#     rem = 56789 * i % 100000
#     cnt = ((n-rem) / 10**5)
#     if cnt < 1:
#         print i
        
#     total += sums[rem] * cnt
# print total


i = 9891
while True:
    i += 10**5
    if 10**


"""
maximal result
00000000137...56789 x ...2902 =
900000000137...5678

cycle gives number of digits
00000000137...56789 x ...9891 =
99999999999...99999

(10**n - 1) mod (n+1) = 0
or 10**n mod (n+1) = 1
where n=...9890
"""
