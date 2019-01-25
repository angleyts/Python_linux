# 题目描述
# 把只包含因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
# 输入描述:
#
# 整数N
# 输出描述:
# 第N个丑数
# 示例1
# 输入
# 6
# 输出
# 6

n = int(input())
num = [1]
i, j, k = 0, 0, 0
numidx = 1
while numidx < n:
    minNum = min(num[i]*2, num[j]*3, num[k]*5)
    num.append(minNum)
    if minNum == num[i]*2:
        i += 1
    if minNum == num[j]*3:
        j += 1
    if minNum == num[k]*5:
        k += 1
    numidx += 1
print (minNum)