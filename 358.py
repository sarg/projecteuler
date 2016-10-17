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

# print [ find_rem(5, 56789, rem) for rem in (1,13,137,90000,67890, 78900, 89000) ]
# print find_rem(4,8789,5678)
# lst = find_rem(5, 56789, 10**5-1)
# print lst

n = 729809890
# more 

last_digit = 9
total = 0
for rem in xrange(0,10):
    i = find_rem(1, last_digit, rem)
    if i > n:
        continue
    cnt = int(((n-i) / 10)) + 1
    total += rem * cnt
print total


"""
maximal result
00000000137...56789 x ...2902 =
900000000137...5678

00000000137...56789 x ... =
99999000000...

minimal cycle is greater than
90000000013/138 = 652173913

cycle gives number of digits
00000000137...56789 x ...9891 =
99999999999...99999

(10**n - 1) mod (n+1) = 0
or 10**n mod (n+1) = 1
where n=...9890

because there is minimal cycle then 9891 is not it
and in fact the cycle ends with 09891

let's check
652109891

for i: 724609890 thru 730000000 step 10^5 do if power_mod(10,i,i+1)=1 then print(i);
"""
