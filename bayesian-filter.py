# 観測が正しい確立 p
p = 0.5
# 正しく移動 q
q = 1


def print_ans(i, f):
    print("{}: ".format(i), end='')
    print(list(map(lambda x: round(x, 3), ans)))


def move(ans):
    temp = []
    for i in range(8):
        if i == 0:
            temp.append(ans[i] * (1-q))
        elif i == 7:
            temp.append((ans[i-1] * q) + (ans[i] * 1))
        else:
            temp.append((ans[i-1] * q) + (ans[i] * (1-q)))
    return temp


def normaralize(ans):
    sum_num = sum(ans)
    return list(map(lambda x: x/sum_num, ans))


mase_kuro = [1-p, p, 1-p, p, 1-p, 1-p, p, p]
mase_shiro = [p, 1-p, p, 1-p, p, p, 1-p, 1-p]

# 移動
ans = [0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125]

# 黒と報告
for i in range(8):
    ans[i] = ans[i] * mase_kuro[i]
ans = normaralize(ans)
print_ans(1, ans)

# 横に移動
ans = move(ans)
print_ans(2, ans)

# 白と報告
for i in range(8):
    ans[i] = ans[i] * mase_shiro[i]
ans = normaralize(ans)
print_ans(3, ans)

# 横に移動
ans = move(ans)
print_ans(4, ans)

# 黒と報告
for i in range(8):
    ans[i] = ans[i] * mase_kuro[i]
ans = normaralize(ans)
print_ans(5, ans)
