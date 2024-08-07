#!/usr/bin/env python
# coding: utf-8

# # Hypothesis Testing in a Real-World Industry Example
# 
# ## Hypothesis Testing
# 
# Hypothesis testing is a statistical method used to make inferences or draw conclusions about a population based on sample data. It involves the following steps:
# 1. **Formulate Hypotheses**: Define the null hypothesis (H0) and the alternative hypothesis (H1). 
#    - The null hypothesis represents the status quo or a statement of no effect, 
#    - while the alternative hypothesis represents what you want to test.
# 
# 2. **Choose Significance Level**: Determine the significance level (alpha), typically 0.05, which is the probability of rejecting the null hypothesis when it is actually true.
# 
# 3. **Collect Data**: Obtain a random sample from the population and calculate relevant statistics.
# 
# 4. **Perform Test**: Use an appropriate statistical test to calculate the test statistic and p-value.
# 
# 5. **Make Decision**: Compare the p-value to the significance level. If the p-value is less than alpha, reject the null hypothesis; otherwise, fail to reject the null hypothesis.

# ### Real-World Industry Example
# 
# Suppose a company wants to test if the average daily sales are equal to a specified target value, say $500. We can set up our hypotheses as follows:
# 
# 
# - H0: The average daily sales are equal to $500.
# 
# - H1: The average daily sales are different from $500.
# 
# We'll use a dataset of daily sales figures to perform our hypothesis test.
# 
# ## Hypothesis Testing Example in Python

# ## In the Context of the Example:
# 
# - Population Data: The total set of all possible daily sales figures for the company.
# 
# - Sample Data: A subset of daily sales figures collected over a specific period (e.g., 100 days in our example).
# 
# #### Explanation:
# - Population: All daily sales figures the company could possibly record. If the company operates every day for a year, the population could consist of 365 daily sales figures for that year. For multiple years, this number grows accordingly.
# 
# - Sample: A smaller, manageable number of daily sales figures drawn from the population. In our example, we used a sample of 100 daily sales figures to perform our hypothesis test.
# 
# - Inference: The goal is to make inferences about the population based on the sample. We use statistical tests to determine if the observed sample provides enough evidence to draw conclusions about the population mean.

# #### Population?
# - In statistics, a population refers to the entire group of individuals, items, or events about which you want to draw conclusions. This group is often large and can be difficult or impractical to measure or observe in its entirety. The population typically represents the broader group to which you want to generalize your findings.
# 
# #### Sample?
# - On the other hand, a sample is a subset of the population that is selected for observation or analysis. It is a smaller, manageable portion of the population that is chosen to represent the whole. The purpose of taking a sample is to draw inferences or make conclusions about the population without having to measure or observe every single member of the population.

# In[1]:


# Importing necessary libraries
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

# Display settings
sns.set(style="whitegrid")


# In[2]:


# Simulated data for daily sales (in dollars)
np.random.seed(42)
daily_sales = np.random.normal(520, 50, 100)  # mean = 520, std = 50, n = 100


# In[3]:


# Create a DataFrame
data = pd.DataFrame({'Daily Sales': daily_sales})
data


# In[5]:


# Calculate the sample mean and standard deviation
sample_mean = np.mean(daily_sales)
sample_std = np.std(daily_sales, ddof=1)
n = len(daily_sales)


# Q) **Why sample mean and sample std is important?**
# 
# The sample mean and sample standard deviation are related to the population:
# 
# - Sample Mean: In this example, the sample mean represents the average daily sales observed in the sample data collected over a specific period. It gives us an estimate of the average daily sales for the subset of days included in the sample.
# 
# - Sample Standard Deviation: The sample standard deviation measures the variability or spread of the observed daily sales figures around the sample mean. It quantifies how much the individual daily sales values deviate from the average daily sales observed in the sample
# 
# Q) **What relationship it have with population?**
# - Population Mean: The population mean represents the average daily sales of the entire company over all possible days. It is the true average daily sales value for the entire population of days.
# 
# - Population Standard Deviation: The population standard deviation measures the variability or spread of the daily sales figures around the population mean. It quantifies how much the individual daily sales values deviate from the true average daily sales value for the entire population.
# 
# #### How They Relate:
# - Estimation: The sample mean and sample standard deviation are used to estimate the population mean and population standard deviation, respectively. They provide estimates of the true population parameters based on the observed sample data.
# 
# - Inference: In hypothesis testing, we use the sample mean and sample standard deviation to test hypotheses about the population mean. We make inferences about the population based on the characteristics of the sample.
# 
# - Generalization: The goal is to generalize the findings from the sample to the entire population. The sample statistics (mean and standard deviation) help us draw conclusions about the population parameters (mean and standard deviation) based on the observed sample data.

# In[6]:


# Set the target average sales
target_mean = 500


# - The "target mean" refers to a specific value that you want to test your sample data against in hypothesis testing. In the context of the example provided, it is the value you expect or want to compare the sample mean to. This target value is usually based on a theoretical expectation, business goal, or industry standard.
# 
# - In the given example, the company wants to test whether their average daily sales are equal to $500. Here, $500 is the target mean. The hypotheses are set up to determine whether the observed sample mean (the average of the collected daily sales data) is statistically significantly different from this target mean of $500.

# In[7]:


# Perform a one-sample t-test
t_stat, p_value = stats.ttest_1samp(daily_sales, target_mean)


# **T-Test:**
# 
# A t-test is a type of inferential statistic used to determine if there is a significant difference between the means of two groups, which may be related in certain features. It is commonly used when the sample size is small, and the population standard deviation is unknown.
# 
# There are several types of t-tests, but in the context of the example provided, we are using a **one-sample t-test.**
# 
# 
# **One-Sample T-Test:**
# 
# A one-sample t-test compares the mean of a single sample to a known value (often a population mean or target value).
# 
# **P-Value:**
# 
# The p-value is a measure of the probability that an observed difference could have occurred just by random chance. It is used to determine the statistical significance of the results.
# 
# 
# 
# ### How They Work Together:
# 
# #### Formulate Hypotheses:
# 
#  - Null Hypothesis (H0): The sample mean is equal to the target value (e.g., average daily sales are $500).
# 
#  - Alternative Hypothesis (H1): The sample mean is not equal to the target value (e.g., average daily sales are different from $500).
# 
# #### Calculate the T-Statistic:
# Calculate the T-Statistic:
# The t-statistic measures how far the sample mean is from the target value in terms of the standard error of the mean.
# 
# t = (x̄ - μ₀) / (s / √n)
# 
# where:
# 
# * `x̄` (sample mean)
# * `μ₀` (target value (population mean under the null hypothesis)
# * `s` (sample standard deviation)
# * `n` (sample size)
# 
# 
# #### Determine the P-Value:
# 
# The p-value is derived from the t-statistic and indicates the probability of obtaining a test statistic at least as extreme as the one observed, assuming the null hypothesis is true.
# 
# #### Compare P-Value to Significance Level (α):
# 
# - If 
# p≤α: Reject the null hypothesis (e.g., there is a significant difference from the target value).
# 
# - If 
# p>α: Fail to reject the null hypothesis (e.g., there is no significant difference from the target value).
# 

# In[8]:


print(f"Sample Mean: {sample_mean:.2f}")
print(f"Sample Standard Deviation: {sample_std:.2f}")
print(f"T-statistic: {t_stat:.2f}")
print(f"P-value: {p_value:.4f}")


# In[13]:


# Visualize the distribution of daily sales
plt.figure(figsize=(8, 5))
sns.histplot(daily_sales, kde=True)
plt.axvline(target_mean, color='red', linestyle='dashed', linewidth=2)
plt.title('Distribution of Daily Sales')
plt.xlabel('Daily Sales ($)')
plt.ylabel('Frequency')
plt.show()


# ***The histogram with the KDE (Kernel Density Estimate) and the target mean line provides insights into the sample data's distribution and its comparison to the target value. Here's a detailed explanation of the visual:***
# 
# #### Visualization Breakdown:
# 
# - Histogram:
#     - The histogram displays the frequency distribution of daily sales in the sample.
#     - The x-axis represents daily sales amounts in dollars.
#     - The y-axis represents the frequency of these sales amounts in the sample.
# 
# 
# - Kernel Density Estimate (KDE):
#     - The blue line overlaid on the histogram is the KDE, which provides a smoothed estimate of the data distribution.
#     - It helps visualize the distribution shape more clearly than the histogram alone.
# 
# - Target Mean Line:
#     - The vertical red dashed line represents the target mean of $500.
#     
#     - This line allows us to visually compare the sample data's distribution to the target value.
# 
# #### Interpretation:
# 
# - Central Tendency:
#     - The highest bar in the histogram and the peak of the KDE line are around the target mean of $500.
#     
#     - This suggests that the most frequent daily sales amounts are close to $500.
#     
# 
# - Spread and Variability:
#     - The histogram bars and the KDE line indicate the spread of the data around the mean.
#     
#     - There is a noticeable spread on both sides of the $500 mark, indicating variability in daily sales.
#     
#     - Sales values range approximately from $400   to   $600.
# 
# - Comparison to Target Mean:
#     - The sample mean appears to be close to the target mean of $500, as indicated by the concentration of data around this value.
#     
#     - The bulk of the data is centered around the $500 mark, with some spread to both lower and higher values.
#     
#     - This visual closeness suggests that the sample mean might not be significantly different from the target mean.
# 
# #### Statistical Significance:
# 
# - To confirm the visual interpretation, we look at the results of the one-sample t-test:
# 
#     - T-Statistic: Measures how far the sample mean is from the target mean in terms of standard errors.
# 
#     - P-Value: Indicates the probability of obtaining a test statistic as extreme as the observed one, assuming the null hypothesis is true.
# 
# #### Decision:
# If the p-value is less than or equal to the significance level (typically 0.05), we reject the null hypothesis, concluding that there is a significant difference between the sample mean and the target mean.
# If the p-value is greater than the significance level, we fail to reject the null hypothesis, concluding that there is no significant difference between the sample mean and the target mean.
# Given the visual indication that the sample mean is close to the target mean and assuming the p-value is not significantly low, we might fail to reject the null hypothesis, suggesting that the average daily sales are not significantly different from $500.

# In[10]:


# Decision based on p-value
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: The average daily sales are significantly different from $500.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference from $500.")


# In[ ]:


# Hypothesis Testing in a Real-World Industry Example

## Hypothesis Testing

Hypothesis testing is a statistical method used to make inferences or draw conclusions about a population based on sample data. It involves the following steps:
1. **Formulate Hypotheses**: Define the null hypothesis (H0) and the alternative hypothesis (H1). 
   - The null hypothesis represents the status quo or a statement of no effect, 
   - while the alternative hypothesis represents what you want to test.

2. **Choose Significance Level**: Determine the significance level (alpha), typically 0.05, which is the probability of rejecting the null hypothesis when it is actually true.

3. **Collect Data**: Obtain a random sample from the population and calculate relevant statistics.

4. **Perform Test**: Use an appropriate statistical test to calculate the test statistic and p-value.

5. **Make Decision**: Compare the p-value to the significance level. If the p-value is less than alpha, reject the null hypothesis; otherwise, fail to reject the null hypothesis.

### Real-World Industry Example

Suppose a company wants to test if the average daily sales are equal to a specified target value, say $500. We can set up our hypotheses as follows:


- H0: The average daily sales are equal to $500.

- H1: The average daily sales are different from $500.

We'll use a dataset of daily sales figures to perform our hypothesis test.

## Hypothesis Testing Example in Python

## In the Context of the Example:

- Population Data: The total set of all possible daily sales figures for the company.

- Sample Data: A subset of daily sales figures collected over a specific period (e.g., 100 days in our example).

#### Explanation:
- Population: All daily sales figures the company could possibly record. If the company operates every day for a year, the population could consist of 365 daily sales figures for that year. For multiple years, this number grows accordingly.

- Sample: A smaller, manageable number of daily sales figures drawn from the population. In our example, we used a sample of 100 daily sales figures to perform our hypothesis test.

- Inference: The goal is to make inferences about the population based on the sample. We use statistical tests to determine if the observed sample provides enough evidence to draw conclusions about the population mean.

#### Population?
- In statistics, a population refers to the entire group of individuals, items, or events about which you want to draw conclusions. This group is often large and can be difficult or impractical to measure or observe in its entirety. The population typically represents the broader group to which you want to generalize your findings.

#### Sample?
- On the other hand, a sample is a subset of the population that is selected for observation or analysis. It is a smaller, manageable portion of the population that is chosen to represent the whole. The purpose of taking a sample is to draw inferences or make conclusions about the population without having to measure or observe every single member of the population.

# Importing necessary libraries
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

# Display settings
sns.set(style="whitegrid")

# Simulated data for daily sales (in dollars)
np.random.seed(42)
daily_sales = np.random.normal(520, 50, 100)  # mean = 520, std = 50, n = 100


# Create a DataFrame
data = pd.DataFrame({'Daily Sales': daily_sales})
data

# Calculate the sample mean and standard deviation
sample_mean = np.mean(daily_sales)
sample_std = np.std(daily_sales, ddof=1)
n = len(daily_sales)

Q) **Why sample mean and sample std is important?**

The sample mean and sample standard deviation are related to the population:

- Sample Mean: In this example, the sample mean represents the average daily sales observed in the sample data collected over a specific period. It gives us an estimate of the average daily sales for the subset of days included in the sample.

- Sample Standard Deviation: The sample standard deviation measures the variability or spread of the observed daily sales figures around the sample mean. It quantifies how much the individual daily sales values deviate from the average daily sales observed in the sample

Q) **What relationship it have with population?**
- Population Mean: The population mean represents the average daily sales of the entire company over all possible days. It is the true average daily sales value for the entire population of days.

- Population Standard Deviation: The population standard deviation measures the variability or spread of the daily sales figures around the population mean. It quantifies how much the individual daily sales values deviate from the true average daily sales value for the entire population.

#### How They Relate:
- Estimation: The sample mean and sample standard deviation are used to estimate the population mean and population standard deviation, respectively. They provide estimates of the true population parameters based on the observed sample data.

- Inference: In hypothesis testing, we use the sample mean and sample standard deviation to test hypotheses about the population mean. We make inferences about the population based on the characteristics of the sample.

- Generalization: The goal is to generalize the findings from the sample to the entire population. The sample statistics (mean and standard deviation) help us draw conclusions about the population parameters (mean and standard deviation) based on the observed sample data.

# Set the target average sales
target_mean = 500


- The "target mean" refers to a specific value that you want to test your sample data against in hypothesis testing. In the context of the example provided, it is the value you expect or want to compare the sample mean to. This target value is usually based on a theoretical expectation, business goal, or industry standard.

- In the given example, the company wants to test whether their average daily sales are equal to $500. Here, $500 is the target mean. The hypotheses are set up to determine whether the observed sample mean (the average of the collected daily sales data) is statistically significantly different from this target mean of $500.

# Perform a one-sample t-test
t_stat, p_value = stats.ttest_1samp(daily_sales, target_mean)

**T-Test:**

A t-test is a type of inferential statistic used to determine if there is a significant difference between the means of two groups, which may be related in certain features. It is commonly used when the sample size is small, and the population standard deviation is unknown.

There are several types of t-tests, but in the context of the example provided, we are using a **one-sample t-test.**


**One-Sample T-Test:**

A one-sample t-test compares the mean of a single sample to a known value (often a population mean or target value).

**P-Value:**

The p-value is a measure of the probability that an observed difference could have occurred just by random chance. It is used to determine the statistical significance of the results.



### How They Work Together:

#### Formulate Hypotheses:

 - Null Hypothesis (H0): The sample mean is equal to the target value (e.g., average daily sales are $500).

 - Alternative Hypothesis (H1): The sample mean is not equal to the target value (e.g., average daily sales are different from $500).

#### Calculate the T-Statistic:
Calculate the T-Statistic:
The t-statistic measures how far the sample mean is from the target value in terms of the standard error of the mean.

t = (x̄ - μ₀) / (s / √n)

where:

* `x̄` (sample mean)
* `μ₀` (target value (population mean under the null hypothesis)
* `s` (sample standard deviation)
* `n` (sample size)


#### Determine the P-Value:

The p-value is derived from the t-statistic and indicates the probability of obtaining a test statistic at least as extreme as the one observed, assuming the null hypothesis is true.

#### Compare P-Value to Significance Level (α):

- If 
p≤α: Reject the null hypothesis (e.g., there is a significant difference from the target value).

- If 
p>α: Fail to reject the null hypothesis (e.g., there is no significant difference from the target value).


print(f"Sample Mean: {sample_mean:.2f}")
print(f"Sample Standard Deviation: {sample_std:.2f}")
print(f"T-statistic: {t_stat:.2f}")
print(f"P-value: {p_value:.4f}")

# Visualize the distribution of daily sales
plt.figure(figsize=(8, 5))
sns.histplot(daily_sales, kde=True)
plt.axvline(target_mean, color='red', linestyle='dashed', linewidth=2)
plt.title('Distribution of Daily Sales')
plt.xlabel('Daily Sales ($)')
plt.ylabel('Frequency')
plt.show()

***The histogram with the KDE (Kernel Density Estimate) and the target mean line provides insights into the sample data's distribution and its comparison to the target value. Here's a detailed explanation of the visual:***

#### Visualization Breakdown:

- Histogram:
    - The histogram displays the frequency distribution of daily sales in the sample.
    - The x-axis represents daily sales amounts in dollars.
    - The y-axis represents the frequency of these sales amounts in the sample.


- Kernel Density Estimate (KDE):
    - The blue line overlaid on the histogram is the KDE, which provides a smoothed estimate of the data distribution.
    - It helps visualize the distribution shape more clearly than the histogram alone.

- Target Mean Line:
    - The vertical red dashed line represents the target mean of $500.
    
    - This line allows us to visually compare the sample data's distribution to the target value.

#### Interpretation:

- Central Tendency:
    - The highest bar in the histogram and the peak of the KDE line are around the target mean of $500.
    
    - This suggests that the most frequent daily sales amounts are close to $500.
    

- Spread and Variability:
    - The histogram bars and the KDE line indicate the spread of the data around the mean.
    
    - There is a noticeable spread on both sides of the $500 mark, indicating variability in daily sales.
    
    - Sales values range approximately from $400   to   $600.

- Comparison to Target Mean:
    - The sample mean appears to be close to the target mean of $500, as indicated by the concentration of data around this value.
    
    - The bulk of the data is centered around the $500 mark, with some spread to both lower and higher values.
    
    - This visual closeness suggests that the sample mean might not be significantly different from the target mean.

#### Statistical Significance:

- To confirm the visual interpretation, we look at the results of the one-sample t-test:

    - T-Statistic: Measures how far the sample mean is from the target mean in terms of standard errors.

    - P-Value: Indicates the probability of obtaining a test statistic as extreme as the observed one, assuming the null hypothesis is true.

#### Decision:
If the p-value is less than or equal to the significance level (typically 0.05), we reject the null hypothesis, concluding that there is a significant difference between the sample mean and the target mean.
If the p-value is greater than the significance level, we fail to reject the null hypothesis, concluding that there is no significant difference between the sample mean and the target mean.
Given the visual indication that the sample mean is close to the target mean and assuming the p-value is not significantly low, we might fail to reject the null hypothesis, suggesting that the average daily sales are not significantly different from $500.

# Decision based on p-value
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: The average daily sales are significantly different from $500.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference from $500.")

