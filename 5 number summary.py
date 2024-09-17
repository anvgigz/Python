import numpy as np
import matplotlib.pyplot as plt

li = [10, 9, 11, 8, 13, 11, 17, 10, 14, 10, 11]

li_sorted = sorted(li)

print(li_sorted)

# The if/else statements both divide the data into two subsets, low_subset and high_subset then dividing them by 2 to get both the Q1 and Q3 values
# the Q3 (high_subset) is recomended to add a 1 in order to keep the start point off the median
if len(li) % 2 ==0:
    low_subset = li_sorted[:len(li_sorted)//2] #q1 if len is even
    high_subset = li_sorted[len(li) // 2:] #q3 if len is even
else:
    low_subset = li_sorted[:len(li) //2] #q1 if len is odd
    high_subset = li_sorted[(len(li) //2)+1] #q3 if len is odd


min_ = min(li_sorted)
q1 = np.median(low_subset) #this is the 25% (percentile)
median = np.median(li_sorted) # 50% (percentile) or Q2
q3 = np.median(high_subset) # 75% (percentile)
max_ = max(li_sorted)
iqr = q3 - q1 # used for calculating oultiers (data points that may mess up the veiwing of the metrics)
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
