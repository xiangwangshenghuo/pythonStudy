import torch
# 第一种用法
"""
torch.min()方法是一个在PyTorch库中提供的用于求解张量最小值的函数。

此函数可以有两种用法：

torch.min(input) → Tensor：返回输入张量input的所有元素的最小值。

torch.min(input, dim, keepdim=False, out=None) -> (Tensor, LongTensor)：返回输入张量input在指定轴dim上的最小值，并同时返回这个最小值所在的位置。

参数解释：

input(Tensor)：输入的张量。

dim(int)：要减少的尺寸。

keepdim(bool)：输出张量的维数是否保持与原输入张量相同，True则保持，False（默认）则不保持。

out(tuple, optional)：一个可选参数，用于指定输出张量。

返回值：

如果指定了dim则返回一个元组（values, indices），其中values是最小值，indices是最小值的索引，否则返回一个张量。
"""

x = torch.rand(2,64)
print(x)
print(torch.min(x)) # 返回所有元素的最小值

y, index = torch.min(x, dim=0)
print(y)
print(index)
# 则呢么

# 第三种用法
"""

orch.min()函数还有另一种形式：

torch.min(input, other, out=None) -> Tensor

这种形式是对输入张量 input 和 other 进行按元素比较，并返回一个新的张量，包含每个位置上 input 和 other 中较小的元素。

参数解释：

input (Tensor)：输入的张量。

other (Tensor)：要进行比较的另一个张量。

out (Tensor, optional)：标量或元组（可选） 的输出张量。"""
a = torch.randn([2,3])
b = 1/ a
print(a)
print(b)
x = torch.min(a,b)
print(x)