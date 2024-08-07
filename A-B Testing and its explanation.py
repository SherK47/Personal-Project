#!/usr/bin/env python
# coding: utf-8

# # A/B Testing 
# 
# ## Introduction to A/B Testing
# 
# A/B testing, also known as split testing, is a method of comparing two versions of a webpage, product feature, or other user experience to determine which one performs better. By randomly assigning users to either the control group (A) or the treatment group (B), we can measure the effect of a single variable while controlling for other factors.
# 

# ### Key Concepts:
# 
# 1. **Hypothesis**: A statement that we want to test. Example: "Changing the color of the call-to-action button from green to red will increase the click-through rate (CTR)."
# 2. **Control Group**: The group that sees the existing version (A).
# 3. **Treatment Group**: The group that sees the new version (B).
# 4. **Metric**: The measure of user behavior that we are interested in, such as CTR, conversion rate, etc.
# 5. **Significance Level**: The threshold at which we determine whether the observed effect is statistically significant. Commonly set at 0.05.
# 6. **P-Value**: The probability of observing the effect, or something more extreme, if the null hypothesis is true.
# 7. **Confidence Interval**: A range of values that is likely to contain the true effect size.

# 
# ### Steps to Conduct A/B Testing
# 
# 1. **Define the Objective**
#    - Identify the goal of the A/B test, such as increasing user engagement, conversion rates, or any other key metric.
# 
# 2. **Formulate the Hypothesis**
#    - Create a clear, testable hypothesis. For example, "Adding a new feature will increase the average time users spend on the product."
# 
# 3. **Identify Key Metrics**
#    - Determine the primary metric that will measure the success of the test. This could be engagement time, conversion rate, click-through rate, etc.
# 
# 4. **Segment the Audience**
#    - Randomly split your audience into two groups: Control Group (A) and Treatment Group (B).
# 
# 5. **Ensure Randomization**
#    - Make sure the random assignment is truly random and that both groups are similar in composition.
# 
# 6. **Design the Experiment**
#    - **Control Group (A)**: This group will experience the existing version without any changes.
#    - **Treatment Group (B)**: This group will experience the new version with the changes or new feature.
# 
# 7. **Collect Data**
#    - Run the experiment for a sufficient duration to gather enough data. The duration depends on the sample size and the expected effect size.
# 
# 8. **Analyze the Results**
#    - Calculate the mean of the key metric for both groups.
#    - Perform statistical tests (e.g., t-test) to determine if there is a significant difference between the groups.
#    - Check the p-value against the significance level (commonly 0.05).
# 
# 9. **Interpret the Results**
#    - **P-Value**: If the p-value is less than the significance level, reject the null hypothesis. This indicates that the difference between the groups is statistically significant.
#    - **Confidence Interval**: Provide a range in which the true effect size lies with a certain level of confidence (usually 95%).
# 
# 10. **Make a Decision**
#     - Based on the analysis, decide whether to implement the change permanently, run another test, or discard the change.
# 
# 11. **Document the Findings**
#     - Record the methodology, data, statistical analysis, and conclusions for future reference and to share with stakeholders.
# 
# 12. **Monitor the Long-term Impact**
#     - Even after making the change, continue to monitor the key metrics to ensure that the observed improvements are sustained over time.
# 
# 
# 

# ### Example Scenario: Product Analysis
# 
# **Objective**: Increase user engagement with a new feature.
# 
# **Hypothesis**: Adding the new feature will increase the average time users spend on the product.
# 
# **Metric**: Average time spent on the product per session.
# 
# **Experiment Design**:
# - **Control Group (A)**: Uses the product without the new feature.
# - **Treatment Group (B)**: Uses the product with the new feature.
# 
# ### Simulating the A/B Test
# 

# # Importing necessary libraries
# 

# In[1]:


import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns


# #### Set random seed for reproducibility
# 

# In[2]:


np.random.seed(42)


# #### Step 1: Define the Objective
# 

# In[3]:


objective = "Increase user engagement with a new feature"


# #### Step 2: Formulate the Hypothesis
# 

# In[4]:


hypothesis = "Adding the new feature will increase the average time users spend on the product"


# #### Step 3: Identify Key Metrics
# 

# In[5]:


metric = "Average time spent on the product per session"


# #### Step 4: Segment the Audience
# #### Sample size for each group
# 

# In[6]:


n_A = n_B = 1000


# #### Step 5: Ensure Randomization
# #### Randomly split the audience into two groups: Control Group (A) and Treatment Group (B)
# #### No further action needed as we use numpy's random functions which already provide randomization
# 

# 
# #### Step 6: Design the Experiment
# #### Control Group (A): Uses the product without the new feature
# #### Treatment Group (B): Uses the product with the new feature
# 

# #### Step 7: Collect Data
# #### Simulate user engagement time (in minutes) for both groups
# #### Control group (A) average engagement time: 10 minutes, standard deviation: 2 minutes
# #### Treatment group (B) average engagement time: 12 minutes, standard deviation: 2.5 minutes
# 

# In[7]:


engagement_time_A = np.random.normal(10, 2, n_A)
engagement_time_B = np.random.normal(12, 2.5, n_B)


# #### Step 8: Analyze the Results
# #### Calculate the mean engagement times
# 

# In[8]:


mean_engagement_A = engagement_time_A.mean()
mean_engagement_B = engagement_time_B.mean()


# In[9]:


print(f"Mean engagement time for Control Group (A): {mean_engagement_A:.2f} minutes")
print(f"Mean engagement time for Treatment Group (B): {mean_engagement_B:.2f} minutes")


# #### Perform a t-test to compare the means
# 

# - A t-test is a statistical test used to determine if there is a significant difference between the means of two groups. It is commonly used in A/B testing scenarios to compare the performance of a control group (A) against a treatment group (B). The t-test calculates a statistic called the t-statistic, which measures the difference between the means of the two groups relative to the variation within the groups.
# 
# - The p-value, on the other hand, is a probability value that helps assess the strength of evidence against the null hypothesis. In the context of an A/B test, the null hypothesis usually states that there is no difference between the groups (i.e., the treatment has no effect). The p-value indicates the probability of observing the effect (or something more extreme) if the null hypothesis is true. A low p-value (typically below a predefined significance level, often 0.05) suggests that the observed difference between the groups is unlikely to occur by random chance alone, leading to the rejection of the null hypothesis.
# 
# - We use a t-test in A/B testing because it is appropriate for comparing the means of two groups, especially when the sample sizes are relatively small (less than 30) and the population standard deviations are unknown. The t-test accounts for the variability within each group and provides a reliable measure of whether the observed difference in means is statistically significant. This helps us determine whether the difference is likely due to the treatment or simply due to chance.

# In[10]:


t_stat, p_value = stats.ttest_ind(engagement_time_A, engagement_time_B)


# In[11]:


print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_value:.4f}")


# - A t-statistic of -21.3271 indicates a significant difference between the means of the two groups being compared. The negative sign simply indicates that the mean of the first group (Control Group A) is lower than the mean of the second group (Treatment Group B), which is expected given the context of the experiment.
# 
# - The p-value of 0.0000 means that the probability of observing such an extreme difference in means (or more extreme) if there were truly no difference between the groups is essentially zero. In other words, it is highly unlikely to observe such a large difference in means purely by chance.
# 
# - In practical terms, this result suggests strong evidence against the null hypothesis, which typically states that there is no difference between the groups or that the treatment has no effect. With such a low p-value, we reject the null hypothesis and conclude that there is a statistically significant difference between the two groups in terms of the metric being measured (in this case, user engagement time).

# #### Check if the result is statistically significant
# 

# In[12]:


alpha = 0.05
if p_value < alpha:
    print("We reject the null hypothesis. The difference in engagement times is statistically significant.")
else:
    print("We fail to reject the null hypothesis. The difference in engagement times is not statistically significant.")


# #### Step 9: Interpret the Results
# #### Visualize the distributions
# 

# In[13]:


plt.figure(figsize=(12, 6))
sns.histplot(engagement_time_A, kde=True, color='blue', label='Control Group (A)', bins=30)
sns.histplot(engagement_time_B, kde=True, color='green', label='Treatment Group (B)', bins=30)
plt.xlabel('Engagement Time (minutes)')
plt.ylabel('Frequency')
plt.title('Distribution of User Engagement Time')
plt.legend()
plt.show()


# ## Why A/B testing is important?

# A/B testing is important for several reasons:
# 
# 1. **Data-Driven Decision Making**: A/B testing allows organizations to make decisions based on data rather than assumptions or opinions. By testing different versions of a product or feature, companies can objectively determine which version performs better with their audience.
# 
# 2. **Optimizing User Experience**: A/B testing helps optimize user experience by identifying changes that lead to improved metrics such as engagement, conversion rates, or user satisfaction. This iterative process allows companies to continuously refine their products and services to better meet user needs.
# 
# 3. **Mitigating Risk**: A/B testing reduces the risk associated with making significant changes to a product or website. Instead of implementing changes across the entire user base and potentially causing negative impacts, A/B testing allows changes to be tested on a smaller subset of users before full rollout.
# 
# 4. **Maximizing ROI**: A/B testing helps maximize return on investment (ROI) by ensuring that resources are allocated to changes that have the greatest positive impact. By focusing on changes that lead to measurable improvements, companies can optimize their resources and achieve better outcomes.
# 
# 5. **Understanding User Behavior**: A/B testing provides insights into user behavior and preferences. By analyzing how users respond to different variations, companies gain a deeper understanding of what resonates with their audience and can tailor their offerings accordingly.
# 
# 6. **Continuous Improvement**: A/B testing fosters a culture of continuous improvement within organizations. By constantly testing and iterating, companies can stay competitive in a rapidly evolving market and maintain a high level of customer satisfaction.
# 
# Overall, A/B testing is a powerful tool for optimizing products, increasing conversion rates, and driving business growth. It allows companies to make informed decisions, mitigate risks, and stay ahead of the competition in today's data-driven world.

# In[ ]:




