**图像分类** 

**目标检测**

**superpixels** 超像素,一系列像素的集合,具有相同的颜色,纹理等特征,距离也比较近.

**Semantic Segmentation** 语义分割,对图像上的每一个像素点进行分类,为每个像素打上类别标签,同一物体的不同实例不需要分割出来,简单理解为分类,只能判断类别,无法区分个体

**Instance Segmentation** 实例分割,不同于物体检测输出bounding box,实例分割输出的是mask,可精确到物体的边缘,相对于semantic segmentation,instance segmentation能够区分同一类别的不同个体

**Panoramic Segmentation** 全景分割. 语义分割与实例分割的集合,既能够区分类别,也能够区分个体.跟实例分割不同的是:实例分割只对图像中的object进行检测,而全景分割对图中的所有物体包括北京都要进行检测和分割.

**dense prediction**  什么是稠密预测

### 正则化方法

#### regularization

##### 参数范围惩罚

* L<sup>2</sup> 正则化  ,权重衰减(weight decay)
* L<sup>1</sup> 正则化  将weight decay项修改为各个权重的绝对值之和 

#### early stoping

#### dropout



