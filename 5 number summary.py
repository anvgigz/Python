import numpy as np
import matplotlib.pyplot as plt

li = [10, 9, 11, 8, 13, 11, 17, 10, 14, 10, 11]

li_sorted = sorted(li)

print(li_sorted)

if len(li) % 2 ==0:
    low_subset = li_sorted[:len(li_sorted)//2]
    high_subset = li_sorted[len(li) // 2:]
else:
    low_subset = li_sorted[:len(li) //2]
    high_subset = li_sorted[(len(li) //2)+1]


min_ = min(li)
q1 = np.median(low_subset)
median = np.median(li)
q3 = np.median(high_subset)
max_ = max(li)
iqr = q3 - q1
low_fence = q1 - 1.5 * iqr
high_fence = q3 + 1.5 * iqr
outliers = [x for x in li if x < low_fence or x > high_fence]


print(f'min: {min_},\t q1: {q1},\t median: {median},\t q3: {q3},\t max: {max_},\t iqr: {iqr},\n low_fence: {low_fence},\t high_fence: {high_fence}')
print(f"Outliers: {outliers}")

#below I am showing work for using the percent function rather than numpy
# The below code is explicitly used on the w3school website to calculate percentile --https://www.w3schools.com/python/python_ml_percentile.asp
print("Next code output\n Using Numpy Percentile function\n")

li = [10, 9, 11, 8, 13, 11, 17, 10, 14, 10, 11]

li_sorted = sorted(li)

min_ = min(li)
q1 = np.percentile(li, 25)
median = np.percentile(li, 50)
q3 = np.percentile(li, 75)
max_ = max(li)
iqr = q3 - q1
low_fence = q1 - 1.5 * iqr
high_fence = q3 + 1.5 * iqr
outliers = [x for x in li if x < low_fence or x > high_fence]

print(f'min: {min_},\t q1: {q1},\t median: {median},\t q3: {q3},\t max: {max_},\t iqr: {iqr},\n low_fence: {low_fence},\t high_fence: {high_fence}')
print(f"Outliers: {outliers}")



plt.boxplot(li, vert=False)
plt.xlabel('Cholesterol Level')
plt.title('Boxplot of Cholesterol Levels')
plt.show()

#heres my output
'''[8, 9, 10, 10, 10, 11, 11, 11, 13, 14, 17]
min: 8, q1: 10.0, median: 11.0, q3: 11.0, max: 17, iqr: 1.0, low_fence: 8.5, high_fence: 12.5
Outliers: [8, 13, 17, 14]'''

'''the following are incorrect
q3 should be 13
iqr should be 3
low_fence shoulw be .55
high_fence should be 17.5
I should have no Outliers


If i try using percentiles i get the same answers

min_, q1, median, q3, max_ = np.percentile(li, [0, 25, 50, 75, 100])

print(f'min: {min_}, q1: {q1}, median: {median}, q3: {q3}, max: {max_}')'''
