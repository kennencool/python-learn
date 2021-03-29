# 序列有两种，tuple 和 list, tuple和list的主要区别在于，一旦建立，tuple的各个元素不可再变更，而list的各个元素可以再变更。
s1 = (2, 1.3, 'hello', True);  # tuple
s2 = [5,'smile',False];  # list
print(s1, type(s1));
print(s2, type(s2))

print(s1[0]);
print(s2[1]);
s2[1] = 50;
print(s2[1]);