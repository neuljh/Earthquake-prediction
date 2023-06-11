
import pandas as pd
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score,mean_absolute_percentage_error,median_absolute_error
import matplotlib.pyplot as plt
import seaborn as sns
import math

# 读取数据
data = pd.read_excel('data/app10/10.xls')  # 替换为实际的数据文件路径

# 分割自变量和因变量
X = data[['reservoir_depth', 'reservoir_capacity', 'rock_fault_type', 'Tectonic_activity/basic_intensity', 'lithology']]
y = data['magnitude']

# 添加截距项
X = sm.add_constant(X)

# 拟合多元线性回归模型
model = sm.OLS(y, X)
results = model.fit()

# 输出回归结果摘要
print(results.summary())

# 打印回归方程
print("回归方程：")
print("magnitude = {:.4f}".format(results.params[0]), end=" ")
for i in range(1, len(results.params)):
    print("+ {:.4f} * {}".format(results.params[i], X.columns[i]), end=" ")
print()

# 设置图像大小
plt.figure(figsize=(25, 25))

# 检查线性关系
sns.pairplot(data)  # 可视化自变量与因变量的关系，使用seaborn库
plt.show()

# 检查多重共线性
corr_matrix = data[['reservoir_depth', 'reservoir_capacity', 'rock_fault_type', 'Tectonic_activity/basic_intensity', 'lithology']].corr()
sns.heatmap(corr_matrix, annot=True)  # 可视化自变量之间的相关性，使用seaborn库
plt.show()

# 检查误差项独立性和正态性（假设检验）
residuals = results.resid
sm.stats.diagnostic.acorr_breusch_godfrey(results)  # 检验误差项的自相关性
sm.stats.diagnostic.normal_ad(residuals)  # 检验误差项的正态性

# 交叉验证
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model_cv = sm.OLS(y_train, X_train)
results_cv = model_cv.fit()
y_pred = results_cv.predict(X_test)

# 模型评估
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
mae = median_absolute_error(y_test, y_pred)
mape = mean_absolute_percentage_error(y_test, y_pred)
print('Mean Squared Error:', mse)
print('Root Mean Square Error:', math.sqrt(mse))
print('median_absolute_error:', mae)
print('ean_absolute_percentage_error:', mape)
print('R^2 Score:', r2)

# 残差分析
residuals = y_test - y_pred
sns.scatterplot(x=y_pred, y=residuals)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.show()

