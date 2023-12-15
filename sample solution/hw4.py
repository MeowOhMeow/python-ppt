# set & set 是取交集的意思，再扣除需要排除的元素
# 之後轉成list，再用sorted()排序
print(sorted(list(set(input()) & set(input()) - {'，', '。', '？'})), end='')
