# 《机器学习》第四章决策树代码实现

首先将表 4.1 西瓜数据集2.0 的数据转换存储在dataSet中。
此代码包含两个**模块**：WaterlemonData.py和treePlotter.py。WaterlemonData模块的主要功能是：计算信息熵，计算信息增益，根据信息增益最大的特征来划分从而得出决策树。
在treePlotter模块的功能是决策树的可视化。
结果如图所示（有个bug：色泽浅白叶子节点没显示出来）：![image](https://github.com/MingQuanXu/MachineLearning/blob/master/WatermelonData/tree.png)


可以使用其他数据集来测试此代码，但保证：1.数据必须是一种由列表元素组成的列表，而且所有的列表元素都要具有相同的数据长度；2.数据的最后一列或者每个实例的最后一个元素
是当前实例的类标签。