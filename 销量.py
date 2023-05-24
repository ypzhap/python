# -*- coding: utf-8 -*-
"""
Created on Sat May 20 17:55:37 2023

@author: ypzhao
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
from matplotlib.font_manager import FontProperties

excel = pd.read_excel("C:/Users/ypzhao/Desktop/毕业论文数据/销量图/新能源汽车数据.xlsx")
data = pd.DataFrame(excel)

# 生成随机数据
x = data['年份']
y1 = data['销量']
y2 = data['增长率']

# 设置字体和字号
matplotlib.rcParams['font.family'] = 'Times New Roman'
matplotlib.rcParams['font.size'] = 24

font = {'family':'Times New Roman','size':28}
# 创建画布和子图
fig, ax1 = plt.subplots(figsize=(11,6))
ax2 = ax1.twinx()



# 准备颜色渐变
n_groups = 6
cmap = plt.get_cmap('coolwarm')
colors_1 = [cmap(i) for i in np.linspace(0, 0.8, n_groups)]

# 绘制图
bar_plot=ax1.bar(x, y1, color=colors_1,label='销量')
# 调整字体颜色、柱子宽度等其他参数

ax2.plot(x, y2, color='green',marker='*',markersize=10,label='增长率')


# 设置坐标轴标签和标题
ax1.set_xlabel('年份',fontname='SimSun')
ax2.set_ylabel('增长率/%', color='#3F7F4C',fontname='SimSun')
ax1.set_ylabel('销量/万辆', color='#6D8F18',fontname='SimSun')


# 设置坐标轴字体和字号
for ax in [ax1, ax2]:
    ax.tick_params(axis='both', which='major', labelsize=16)
    for tick in ax.get_xticklabels() + ax.get_yticklabels():
        tick.set_fontname('Times New Roman')

# 设置网格线不可见
ax1.grid(visible=False)
ax2.grid(visible=False)
ax2.set_ylim(-45,490)
ax1.set_ylim(0,830)

# 设置双坐标轴的颜色不一致
ax1.spines['left'].set_color('#6D8F18')
ax1.spines['right'].set_color('#3F7F4C')
ax1.tick_params(axis='y', colors='#6D8F18')
ax2.tick_params(axis='y', colors='#3F7F4C')

# 给折线图增添数据
for i, j in zip(x, y2):
    ax.annotate('{:.2f}'.format(j), xy=(i, j), xytext=(-10, 10),
                textcoords='offset points', fontsize=16)
    

# 调柱状图增加数据
for rect in bar_plot:
    height = rect.get_height()
    ax1.text(rect.get_x() + rect.get_width()/2., height+1, '%.1f' % (height),
            ha='center', va='bottom', fontsize=16, color='blue',fontname='Times New Roman')  # 字体颜色蓝色
# 自动调整布局

font = FontProperties(fname=r'C:\Windows\Fonts\simsun.ttc', size=14)

plt.tight_layout()
plt.legend(ncol=2,loc=1,prop=font)

plt.savefig("sells.jpg",dpi=1200)
