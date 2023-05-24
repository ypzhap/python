# -*- coding: utf-8 -*-
"""
Created on Sat May  6 11:35:21 2023

@author: ypzhao
"""

import pandas as pd
import numpy as np
import xlsxwriter as xw
import matplotlib.pyplot as plt
from PIL import Image

excel = pd.read_excel("C:/Users/ypzhao/Desktop/毕设数据/电机数据/电机参数.xlsx")
data = pd.DataFrame(excel)

t = data['时间']
T1 = data['转矩1']
S1 = data['转速1']
P1 = data['功率1']

T2 = data['转矩2']
S2 = data['转速2']
P2 = data['功率2']

font = {'family': 'Times New Roman','size': 15}
font_1 = {'family': 'Times New Roman','size': 19}


# 画第1个图：折线图
fig, ax1 = plt.subplots(figsize=(12, 8),dpi=1200)


ax1=fig.add_subplot(3,1,1)
# fig.tight_layout()
ax1.plot(t,T1,marker = "",markersize=1,alpha=.8,color='y',
          linewidth=1,label='Control',markeredgecolor='green',)
ax1.plot(t,T2,marker = "",markersize=1,alpha=.7,
          linewidth=1,label='Uncontrol',markeredgecolor='blue',)
ax1.axis([0, 2100, -250, 750])   #X、Y轴区间

plt.tick_params(labelsize=16)
labels = ax1.get_xticklabels() + ax1.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]
plt.rcParams["font.family"] = "Times New Roman"  #全图字号新罗马字体
plt.legend(ncol=2,frameon=False,prop=font)
# 设置右和上边框是否可见
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
plt.xlabel('Times/s',font_1)
plt.ylabel('Torque/N·m',font_1)


# 画第2个图：转速与时间的关系图
ax2=fig.add_subplot(3,1,2)
fig.tight_layout()
ax2.plot(t,S1,marker = "",markersize=1,alpha=.8,
          linewidth=1,label='Control',markeredgecolor='lightgary',)
ax2.plot(t,S2,marker = "",markersize=1,alpha=.4,color='g',
          linewidth=1,label='Uncontrol',markeredgecolor='maroon',)
plt.tick_params(labelsize=16)
labels = ax2.get_xticklabels() + ax2.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]
plt.rcParams["font.family"] = "Times New Roman"  #全图字号新罗马字体
plt.legend(ncol=2,frameon=False,prop=font)
# 设置右和上边框是否可见
ax2.axis([0, 2100, 0, 3700])   #X、Y轴区间

ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
plt.xlabel('Times/s',font_1)
plt.ylabel('r/min',font_1)


# 画第3个图：饼图
ax3=fig.add_subplot(3,1,3)
ax3 = plt.subplot(3,1,3)
ax3.plot(t,P1,marker = "",markersize=1,alpha=.8,
          linewidth=1,label='Control',markeredgecolor='green',)
ax3.plot(t,P2,marker = "",markersize=1,alpha=.8,
          linewidth=1,label='Uncontrol',markeredgecolor='blue',)
ax3.axis([0, 2100, -50, 105])   #X、Y轴区间

plt.tick_params(labelsize=16)
labels = ax3.get_xticklabels() + ax3.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]
plt.rcParams["font.family"] = "Times New Roman"  #全图字号新罗马字体
plt.legend(ncol=2,frameon=False,prop=font)
# 设置右和上边框是否可见
ax3.spines['right'].set_visible(False)
ax3.spines['top'].set_visible(False)
plt.xlabel('Times/s',font_1)
plt.ylabel('Power/kW',font_1)


plt.savefig('电机数据.jpg',dpi=1200) #保存为图片png格式
# plt.savefig('电机数据.png',dpi=1200) #保存为图片png格式
# plt.savefig('电机数据.tif',dpi=1200) #保存为图片png格式
# plt.savefig('电机数据.eps',dpi=1200) #保存为图片png格式
# plt.savefig('电机数据.pdf',dpi=1200) #保存为图片png格式

# file_path ='电机数据.jpg'
# # 获取图片大小
# img = Image.open(file_path)
# imgSize = img.size  #大小/尺寸
# w = img.width       #图片的宽
# h = img.height      #图片的高
# f = img.format      #图像格式
# img.close
# print(imgSize)
# print(w, h, f)
