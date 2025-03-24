# 此區為程式測試區，可以於此測試程式
# 從虛線下開始使用
# ------------------------------------------------------------------------------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager
matplotlib.rc("font", family = "Microsoft JhengHei")
from scipy import stats
from statsmodels.formula.api import ols
import statsmodels.api as sm
import scikit_posthocs as sp
import numpy as np
import statsmodels.api as sm
from statsmodels.stats.multicomp import pairwise_tukeyhsd


# Data pre-processing
data = pd.read_csv("統計資料分析期末報告.csv")
data = data.dropna(how = "any")
data = data[data["對於使用社交軟體之感受程度 [此題請填4，否則問卷無效]"] == 4]
data = data.drop("對於使用社交軟體之感受程度 [此題請填4，否則問卷無效]", axis = 1)
data["平均每日社群軟體使用時間"] += 1

data["人際交流選擇"] = data["人際交流選擇"] + data["交流"] 
test = ["分享慾", "人際交流選擇", "認同度", "社交軟體綁架程度", "孤獨感", "滿意度"]


# Show the amount of every age

# age = data.groupby("年紀").count()
# age.plot(kind = "bar", y = age.iloc[0])
# plt.legend("")
# plt.show()


# 1. Pie chart of social media preference

# message = data.groupby("我更偏好使用什麼軟體「訊息他人」？").count()
# message.plot.pie(y=message.columns[0], autopct = "%1.1f%%")
# plt.title("Social Media Preference")
# plt.axis("off")
# plt.show()


# 5. Sex would affect the the favorite SM

# favorite = data[["生理性別", "綜合來說我最喜歡什麼社交軟體？"]]
# male = favorite[favorite["生理性別"] == "男性"]
# female = favorite[favorite["生理性別"] == "女性"]
# male = male.groupby("綜合來說我最喜歡什麼社交軟體？").count()
# female = female.groupby("綜合來說我最喜歡什麼社交軟體？").count()
# # female.apply(print)
# new = pd.merge(male, female, on = "綜合來說我最喜歡什麼社交軟體？", how = "outer")
# p_value = chi2_contingency(new)[1]
# print(p_value)

# print("----------------------------------------------")

# for i in range(len(male)):
#     print(f"{male.index[i]:<30}{chisquare([male.iloc[i], female.iloc[i]])[1][0]:>10.5f}")

     






# 6. Favorite SM rate from year 19 ~ 22

age = data.groupby("年紀")[["年紀", "綜合來說我最喜歡什麼社交軟體？"]]
age18 = age.get_group(18).groupby("綜合來說我最喜歡什麼社交軟體？").count()
age19 = age.get_group(19).groupby("綜合來說我最喜歡什麼社交軟體？").count()
age20 = age.get_group(20).groupby("綜合來說我最喜歡什麼社交軟體？").count()
age21 = age.get_group(21).groupby("綜合來說我最喜歡什麼社交軟體？").count()
age22 = age.get_group(22).groupby("綜合來說我最喜歡什麼社交軟體？").count()
age23 = age.get_group(23).groupby("綜合來說我最喜歡什麼社交軟體？").count()
age24 = age.get_group(24).groupby("綜合來說我最喜歡什麼社交軟體？").count()
ages = [age19, age20, age21, age22, age23]
check = np.eye(7, dtype = "int")
for i in range(19, 24):
    for j in range(19, 24):
        if check[i - 19][j - 19] ==0:
                print("\n---------------------------------------------------------------------")
                new = pd.merge(ages[i - 19], ages[j - 19], on = "綜合來說我最喜歡什麼社交軟體？", how = "inner")
                p_value = stats.chi2_contingency(new)[1]
                print(f"p value: {p_value}")
                print(f"\nAge {i}:")
                ages[i - 19].apply(print)
                print(f"\nAge {j}:")
                ages[j - 19].apply(print)
                check[i - 19][j - 19] += 1
                check[j - 19][i - 19] += 1
                print("\n---------------------------------------------------------------------\n")


# Redo of 5.
##new

# for i in test:
#     target = data[[i, "平均每日社群軟體使用時間"]]
#     average = data[i].mean()
#     positive = target[target[i] > average]
#     negative = target[target[i] <= average]
#     positive = positive.groupby("平均每日社群軟體使用時間").count()
#     negative = negative.groupby("平均每日社群軟體使用時間").count()
#     new = pd.merge(positive, negative, on = "平均每日社群軟體使用時間", how = "outer")
#     print(new)
#     p_value = stats.chi2_contingency(new)[1]
#     print(f"------------------------------------------------\nChi-square Test of {i}\np value: {p_value}\n------------------------------------------------\n")


# Linear Regression of data in test
##new

# check = np.eye(len(test), dtype = "int")
# for i in range(len(test)):
#     for j in range(len(test)):
#         if check[i][j] == 0:
#             var = stats.levene(data[test[i]], data[test[j]])[1]
#             p_value = stats.ttest_ind(data[test[i]], data[test[j]], equal_var = (var < 0.05), alternative = "two-sided")[1]
#             if p_value < 0.05:
#                 print(f"--------------------------------------------------\nIndependent T Test p value: {p_value}")
#                 model = ols(f"{test[j]} ~ {test[i]}", data = data).fit()
#                 print(model.summary())
#                 plt.scatter(data[test[i]], data[test[j]], color="black")
#                 plt.plot(data[test[i]], model.fittedvalues, color="red", linewidth=2)
#                 plt.xlabel(test[i])
#                 plt.ylabel(test[j])
#                 plt.show()
#         check[i][j] += 1



# Remake of 1.
##new

# age = data[["年紀", "平均每日社群軟體使用時間"]]
# age19 = age[age["年紀"] == 19].groupby("平均每日社群軟體使用時間")["年紀"].count().rename("19歲")
# age20 = age[age["年紀"] == 20].groupby("平均每日社群軟體使用時間")["年紀"].count().rename("20歲")
# age21 = age[age["年紀"] == 21].groupby("平均每日社群軟體使用時間")["年紀"].count().rename("21歲")
# age22 = age[age["年紀"] == 22].groupby("平均每日社群軟體使用時間")["年紀"].count().rename("22歲")
# age23 = age[age["年紀"] == 23].groupby("平均每日社群軟體使用時間")["年紀"].count().rename("23歲")

# new = pd.merge(age19, age20, on="平均每日社群軟體使用時間", how="outer", suffixes=('', '_20'))
# new = pd.merge(new, age21, on="平均每日社群軟體使用時間", how="outer", suffixes=('', '_21'))
# new = pd.merge(new, age22, on="平均每日社群軟體使用時間", how="outer", suffixes=('', '_22'))
# new = pd.merge(new, age23, on="平均每日社群軟體使用時間", how="outer", suffixes=('', '_23'))
# print(new)
# print("\np value: ", end = "")
# print(stats.chi2_contingency(new)[1])
# print()

# check = np.eye(len(new.index), dtype = "int")
# for i in range(len(new.index)):
#     for j in range(len(new.index)):
#         if check[i][j] == 0:
#             print(f"-----------------------------------------\nChi-squared Test of {new.index[i]} and {new.index[j]}\np value: {stats.chisquare([new.iloc[i], new.iloc[j]])[1]}\n-----------------------------------------\n")
#         check[i][j] += 1
#         check[j][i] += 1


#check
# 构造观测频数表
# observed = np.array([
#     [6, 5, 1, 4, 1],
#     [36, 27, 11, 11, 5],
#     [27, 40, 17, 12, 5],
#     [7, 15, 6, 3, 2],
#     [4, 6, 1, 2, 2]
# ])

# # 进行卡方检定
# chi2, p, dof, expected = stats.chi2_contingency(observed)

# # 检查期望频数
# print("期望频数:\n", expected)

# # 检查期望频数是否有小于5的情况
# if np.any(expected < 5):
#     print("警告: 有期望频数小于5的单元格。")
#     print("这些期望频数小于5的单元格:")
#     print(expected[expected < 5])
# else:
#     print("所有单元格的期望频数都大于或等于5。")

# print("卡方统计量:", chi2)
# print("P值:", p)

# Redo of 2.

# average = data[["平均每日社群軟體使用時間", "生理性別"]]
# male = average[average["生理性別"] == "男性"].groupby("平均每日社群軟體使用時間")["生理性別"].count().rename("Male")
# female = average[average["生理性別"] == "女性"].groupby("平均每日社群軟體使用時間")["生理性別"].count().rename("Female")
# new = pd.merge(male, female, on = "平均每日社群軟體使用時間", how = "outer").transpose()
# print(new)
# print(stats.chi2_contingency(new)[1])


# The extra of extra

# a = ["平均每日社群軟體使用時間", "綜合來說我最喜歡什麼社交軟體？"]
# b = ["年紀", "生理性別"]
# data1 = {'平均每日社群軟體使用時間' , "滿意度"}
# abc = pd.DataFrame(data1)
# abc
# for i in a:
#     for j in b:
#         df = data[[i, j]]
#         df = pd.crosstab(df[j], df[i])
#         chi_stat, p_value, dof, expect = stats.chi2_contingency(df)
#         print(f"\n---------------------------------------------------\nChi-squared Test of {j} and {i}\nChi-square Statistic: {chi_stat}\np value: {p_value}\nDegrees of Freedom: {dof}\n---------------------------------------------------\n")

# for i in a:
#     df = data[[i, "滿意度"]]
#     groups = [df[df[i] == group]['滿意度'] for group in df[i].unique()]
#     statistic, p_value = stats.f_oneway(*groups)
#     print(f"\n---------------------------------------------------\nF: {statistic}\np value: {p_value}")
#     if p_value < 0.05:
#         model = ols(f'滿意度 ~ C({i})', data=df).fit()
#         anova_table = sm.stats.anova_lm(model, typ=2)
#         tukey = pairwise_tukeyhsd(df['滿意度'], df[i], alpha=0.05)
#         print()
#         print(tukey)
#     print("---------------------------------------------------\n")