key words

objective function 目标函数

cost function , loss function, penaty function or objective function   are same things

softmax regression  多分类逻辑回归

activation function  激活函数

sigmoid  s形激活函数

intercept term( 截距项) or bias unit(偏置项),表示函数的截距 y = wx + b b表示函数在y轴上的截距,控制函数偏离原点的距离,神经网络中的偏置项类似  没有输入项

W<sub>i,j</sub><sup>(l)</sup>  表示 l层的unit j  和  l+1层的 unit i 之间的权重

每层神经元的个数不包括偏置项

average sum-of-squares error   平均平方和误差



![1584944236390](/home/ykh/.config/Typora/typora-user-images/1584944236390.png)

![1584944283011](/home/ykh/.config/Typora/typora-user-images/1584944283011.png)

**weight decay** 权重衰减, L2正则化

**L2正则化** 就是在原始代价函数后边机上所有参数w的平方的和除以训练集的样本大小n,lamda是正则项系数,权衡正则项与C0的比重 , 1/2是为了求导的方便

 **symmetry breaking** 对称破坏

**Fully Connected Networks** fully  connect  all the hidden units to all the input units

**Locally Connected Networks** each hidden units to connect only a small subset of the input units  Specifically, each hidden unit will connect to only a small contiguous region of pixels in the input.

**stationary** images have the "stationary" property

**stochastic gradient descent**  随机梯度下降



**Autoencoder**  给数据压缩和降维,高维的原始数据用低维的向量表示

目标是让输出值等于输入值,输入层的神经元数量和输出层数量相等

输入层到中间层是编码的过程,中间层到输出层是解码的过程

**whitening  or  sphering**   when process images,to make the input less redundant

**Sparse Coding** 找到基向量已能够线性表示所有输入x,即x可以用坐标表示?

**residual** 残差