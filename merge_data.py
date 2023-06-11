# import pandas as pd
# import numpy as np
# from scipy.fft import fft, fftfreq
# import matplotlib.pyplot as plt
# import os
# import pandas as pd
# from scipy.signal import correlate
# import openpyxl
#
# # 输入和输出目录
# input_dir = 'merge_datas'
# output_dir = 'merge_data'
#
# # 获取输入目录下的子文件夹列表
# subfolders = os.listdir(input_dir)
#
# # 循环遍历每个子文件夹
# for subfolder in subfolders:
#     # 构建输入和输出子文件夹路径
#     input_subfolder = os.path.join(input_dir, subfolder)
#
#     print('input_subfolder: ' + input_subfolder)
#
#     # 获取输入子文件夹中的文件列表
#     files = [file for file in os.listdir(input_subfolder) if file.endswith('.xlsx')]
#
#     # 循环遍历每个文件
#     for file in files:
#         # 构建输入和输出文件路径
#         input_file = os.path.join(input_subfolder, file)
#
#         print('input_file: '+input_file)
#
#         # 读取Excel数据
#         df = pd.read_excel(input_file, header=None)
#
#         # 遍历每一行数据
#         for index, row in df.iterrows():
#             data = row.values  # 获取一行数据
#
#
#
#
#
#
#
#
#

import pandas as pd
import os

# 输入和输出目录
input_dir = 'merge_datas2'
output_dir = 'merge_data'

# 创建输出目录
os.makedirs(output_dir, exist_ok=True)

# 创建一个空的DataFrame用于存储合并的数据
merged_data = pd.DataFrame()

# 获取输入目录下的子文件夹列表
subfolders = os.listdir(input_dir)

# 读取第一个子文件夹中的第一个文件的标题
first_subfolder = subfolders[0]
first_folder_path = os.path.join(input_dir, first_subfolder)
first_file = os.listdir(first_folder_path)[0]
first_file_path = os.path.join(first_folder_path, first_file)
df = pd.read_excel(first_file_path, header=None)
header = df.iloc[0].tolist()

# 循环遍历每个子文件夹
for subfolder in subfolders:
    # 构建输入子文件夹路径
    input_subfolder = os.path.join(input_dir, subfolder)

    # 获取输入子文件夹中的文件列表
    files = [file for file in os.listdir(input_subfolder) if file.endswith('.xlsx')]

    # 循环遍历每个文件
    for file in files:
        # 构建输入文件路径
        input_file = os.path.join(input_subfolder, file)

        # 读取Excel数据，跳过标题行
        df = pd.read_excel(input_file, skiprows=1, header=None)
        df.columns = header  # 设置标题

        # 将数据添加到合并的DataFrame中
        merged_data = merged_data.append(df, ignore_index=True)

# 构建输出文件路径
output_file = os.path.join(output_dir, 'merged_data_8.xlsx')

# 保存合并的数据到Excel文件
merged_data.to_excel(output_file, index=False)

