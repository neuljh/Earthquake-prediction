# import pandas as pd
#
# # 读取txt文件
# with open('data/app1/1.txt', 'r') as file:
#     data = file.read().split()
#
# n = 64  # 假设你知道n的值
# m = len(data) // n  # 计算m的值
#
# # 创建DataFrame
# df = pd.DataFrame([data[i:i+n] for i in range(0, len(data), n)])
#
# # 将DataFrame保存为Excel文件
# df.to_excel('data1.xlsx', index=False, header=False)
#
#
#

import os
import pandas as pd

# 输入和输出目录
input_dir = 'data'
output_dir = 'outputdata'

# 获取输入目录下的子文件夹列表
subfolders = os.listdir(input_dir)

# 循环遍历每个子文件夹
for subfolder in subfolders:
    # 构建输入和输出子文件夹路径
    input_subfolder = os.path.join(input_dir, subfolder)
    output_subfolder = os.path.join(output_dir, subfolder)

    # 创建输出子文件夹
    os.makedirs(output_subfolder, exist_ok=True)

    # 获取输入子文件夹中的txt文件列表
    txt_files = [file for file in os.listdir(input_subfolder) if file.endswith('.txt')]

    # 循环遍历每个txt文件
    for txt_file in txt_files:
        # 构建输入和输出文件路径
        input_file = os.path.join(input_subfolder, txt_file)
        output_file = os.path.join(output_subfolder, txt_file.replace('.txt', '.xlsx'))

        # 读取txt文件
        with open(input_file, 'r') as file:
            data = file.read().split()

        n = 64  # 假设你知道n的值
        m = len(data) // n  # 计算m的值

        # 创建DataFrame
        df = pd.DataFrame([data[i:i+n] for i in range(0, len(data), n)])

        # 将DataFrame保存为Excel文件
        df.to_excel(output_file, index=False, header=False)


