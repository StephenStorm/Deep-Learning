### 摘要

* 重复空间池化导致低分辨率特征图
* 多尺度网络结构   multi-scale network structure

### 3 方法

#### 3.1 网络结构

##### 3.1.1稠密特征提取器

 为了合并多尺度信息和重建好分辨率深度图

* stage-wise refinement

* skip connection

* multi-layer deconvolution network

不仅需要额外的计算和内存消耗，还复杂化网络结构和训练过程，所以

移除DCNNs最后的几个下采样算子，在随后的conv层中在过滤器上插入孔，称为膨胀卷积（拓展卷积），以在不减少空间分辨率和增加参数数量的情况下扩大滤波器的视场

##### 3.1.2 场景理解模块

consists three parallel components

**atrous spatial pyramid pooling 多孔空间金字塔池(ASPP) ** 通过膨胀卷积从多个大感知域提取特征，膨胀率分别是6，12，18

**cross-channel leaner** learn complex cross-channel interactions

**full-image encoder** 抓取全局上下文信息

1. 小核平均池化层减少空间维度，
2. f<sub>c</sub>-fashion  fc 层获得维数为 C 的特征向量
3. 将特征向量作为空间维数为1\*1 的特征映射的C通道，并添加一个内核大小为1\*1 的 conv层作为跨通道参数池化结构
4. 沿着空间维度将特征向量复制到F上，使得F的每个位置对整个图像有相同的理解

增加的两个卷积层，第一个用来降低特征维度，学习复杂的跨通道交互。第二个将特征转化为 多通道稠密序列标签

#### 3.2 间隔递增离散化

![image-20200324182335864](C:\Users\ykh\AppData\Roaming\Typora\typora-user-images\image-20200324182335864.png)

#### 3.3 学习和推断

将标准回归问题转化为多分类问题，传统的多分类问题忽略离散标签之间的序列问题，而深度值因为其形成一个有序集而具有很强的序列相关性。





### New Words

**stride**

f<sub>c</sub>-fashion 



