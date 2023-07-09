#!/usr/bin/env python
# coding: utf-8

# ## Calculate the mean, median, mode and standard deviation for the problem
# ## statements 1& 2.

# # Problem Statement 1:

# The marks awarded for an assignment set for a Year 8 class of 20 students were as
# follows:
# 6 7 5 7 7 8 7 6 9 7 4 10 6 8 8 9 5 6 4 8

# In[4]:


import numpy as np
from scipy import stats
import statistics
#problem statement 1
a = [6,7,5,7,7,8,7,6,9,7,4,10,6,8,8,9,5,6,4,8]
mean = np.mean(a)
median = np.median(a)
mode = stats.mode(a)
std_d = statistics.stdev(a)
print('mean is', mean)
print('median is', median)
print('mode is ', mode)
print('standard Deviation is',std_d)


# # Problem Statement 2:

# The number of calls from motorists per day for roadside service was recorded for a
# particular month:
# 28, 122, 217, 130, 120, 86, 80, 90, 140, 120, 70, 40, 145, 113, 90, 68, 174, 194, 170,
# 100, 75, 104, 97, 75,
# 123, 100, 75, 104, 97, 75, 123, 100, 89, 120, 109

# In[5]:


#problem statement 2
b = [28, 122, 217, 130, 120, 86, 80, 90, 140, 120, 70, 40, 145, 113, 90, 68, 174, 194, 170, 100, 75, 104, 97, 75, 123, 100, 75, 104, 97, 75, 123, 100, 89, 120, 109]
mean = np.mean(b)
median = np.median(b)
mode = stats.mode(b)
std_d = statistics.stdev(b)
print('mean is ', mean)
print('median is' , median)
print('mode is ',mode)
print('standard Deviation is',std_d)




# # Problem Statement 3:
# The number of times I go to the gym in weekdays, are given below along with its
# associated probability:
# x = 0, 1, 2, 3, 4, 5
# f(x) = 0.09, 0.15, 0.40, 0.25, 0.10, 0.01
# Calculate the mean no. of workouts in a week. Also evaluate the variance involved in
# it.

# In[6]:


# problem statement 3
x = [0, 1, 2, 3, 4, 5]
fx = [0.09, 0.15, 0.40, 0.25, 0.10, 0.01]
mean = sum([float(x[i])*fx[i] for i in range(len(x))])
variance = (sum([float(x[i]**2)*fx[i] for i in range(len(x))])-mean)
print('mean is',mean)
print('Variance is', variance)


# # Problem Statement 4:
# Let the continuous random variable D denote the diameter of the hole drilled in an
# aluminum sheet. The target diameter to be achieved is 12.5mm. Random
# disturbances in the process often result in inaccuracy.
# Historical data shows that the distribution of D can be modelled by the PDF (d) =
# 20e−20(d−12.5), d ≥ 12.5. If a part with diameter > 12.6 mm needs to be scrapped,
# what is the proportion of those parts? What is the CDF when the diameter is of 11
# mm? What is your conclusion regarding the proportion of scraps?

# # Problem Statement 5:
# 
# A company manufactures LED bulbs with a faulty rate of 30%. If I randomly select 6
# chosen LEDs, what is the probability of having 2 faulty LEDs in my sample?
# Calculate the average value of this process. Also evaluate the standard deviation
# associated with it.

# In[7]:


#problem statement 5
from scipy.stats import binom
add = sum(np.random.binomial(6, 0.3, 50000) == 2)/50000
print(add)
n = 6
p = 0.3
mean , var = binom.stats(n, p)
std = var**0.5
print('Mean is',mean)
print('Standard deviation for this process is',std)


# # Problem Statement 6:
# Gaurav and Barakha are both preparing for entrance exams. Gaurav attempts to solve 8 questions per day with a correction rate of 75%, while Barakha averages around 12 questions per day with a correction rate of 45%. What is the probability that each of them will solve 5 questions correctly? What happens in cases of 4 and 6 correct solutions? What do you infer from it? What are the two main governing factors affecting their ability to solve questions correctly? Give a pictorial representation of the same to validate your answer.

# In[8]:


from scipy.stats import binom 
import matplotlib.pyplot as plt 
# setting the values of n and p  
n_Gaurav = 8
p_Gaurav = 0.75
n_Barkha = 12
p_Barkha = 0.45
# defining list of r values 
r_values_Gaurav = list(range(n_Gaurav + 1)) 
r_values_Barkha = list(range(n_Barkha + 1)) 
# list of pmf values 
dist_Gaurav = [binom.pmf(r, n_Gaurav, p_Gaurav) for r in r_values_Gaurav]
dist_Barkha = [binom.pmf(r, n_Barkha, p_Barkha) for r in r_values_Barkha ]
# plotting the graph  
fig = plt.figure(figsize=(18,8))
plt.subplot(1, 2, 1)
plt.title('Gaurav\'s probability distribution')
plt.xlabel('Number of questions solved correctly')
plt.ylabel('Probability of solving')
plt.bar(r_values_Gaurav, dist_Gaurav)
plt.subplot(1, 2, 2)
plt.title('Barkha\'s probability distribution')
plt.xlabel('Number of questions solved correctly')
plt.ylabel('Probability of solving')
plt.bar(r_values_Barkha, dist_Barkha) 
plt.show()


# In[9]:


print('Probability to solve',r_values_Barkha[4],'correctly for Barkha is', dist_Barkha[4])
print('Probability to solve',r_values_Gaurav[4],'correctly for Gaurav is', dist_Gaurav[4])
print('Probability to solve',r_values_Barkha[6],'correctly for Barkha is', dist_Barkha[6])
print('Probability to solve',r_values_Gaurav[6],'correctly for Gaurav is', dist_Gaurav[6])


# The two main factors affecting the ability to solve questions correctly are:
# 
# Correction rate
# Number of questions solved per day
# As the correction rate increases the chances of the distribution to be left skewed increases. Since Barkha's correction rate is close to 0.5 so highest probability of solving questions is found at around 50% of the total number of questions.
# 
# Increasing the number of questions solved daily reduces skewness as well.As the number of questions increases the distribution skewness decreases

# # Problem Statement 7:
# 
# Customers arrive at a rate of 72 per hour to my shop. What is the probability of k
# customers arriving in 4 minutes? a) 5 customers, b) not more than 3 customers, c)
# more than 3 customers. Give a pictorial representation of the same to validate your
# answer.

# In[11]:


from scipy.stats import poisson
import seaborn as sb
data_binom = poisson.rvs(mu=4.8, size=200)

ax = sb.distplot(data_binom)
ax.set(xlabel='Customers per 4 minutes', ylabel='Frequency')
plt.title('Poisson distribution')
plt.show()


# In[12]:


import numpy as np
x = np.arange(0,25)
prob = poisson.cdf(x, 4.8)
y = prob[3]
print('Probability of not more than 3 customers is',round(y,3))
print('Probability of more than 3 customers is',round((1 - y),3))
plt.plot(prob)
plt.plot((3,3),(0,1))
plt.scatter(3,prob[3])
plt.text(3,prob[3],'({}, {})'.format(3, round(prob[3],3)))
plt.title('CDF of poisson distribution')
plt.show()


# # Problem Statement 8:
# 
# I work as a data analyst in Aeon Learning Pvt. Ltd. After analyzing data, I make
# reports, where I have the efficiency of entering 77 words per minute with 6 errors per
# hour. What is the probability that I will commit 2 errors in a 455-word financial report?
# What happens when the no. of words increases/decreases (in case of 1000 words,
# 255 words)?
# How is the λ affected?
# How does it influence the PMF?
# Give a pictorial representation of the same to validate your answer.

# In[13]:


fig = plt.figure(figsize=(18, 8))
x = np.arange(0,10)
mu_1 = 0.59
mu_2 = 1.299
mu_3 = 0.33
plt.subplot(1,2,1)
plt.plot(x, poisson.pmf(x, mu_1), 'b-', label='λ: 0.59')
plt.plot(x, poisson.pmf(x, mu_2), 'g-', label='λ: 1.299')
plt.plot(x, poisson.pmf(x, mu_3), 'r-', label='λ: 0.33')
plt.legend()
plt.title('PDF for different lambda')
plt.subplot(1, 2, 2)
x = np.arange(0,10)
mu_1 = 0.59
mu_2 = 1.299
mu_3 = 0.33
plt.plot(x, poisson.cdf(x, mu_1), 'b-',label='λ: 0.59')
plt.plot(x, poisson.cdf(x, mu_2), 'g-', label='λ: 1.299')
plt.plot(x, poisson.cdf(x, mu_3), 'r-', label='λ: 0.33')
plt.legend()
plt.title('CDF for different lambda')
plt.show()


# # Problem Statement 9:
# 
# Let the continuous random variable D denote the diameter of the hole drilled in an
# aluminum sheet. The target diameter to be achieved is 12.5mm. Random
# disturbances in the process often result in inaccuracy.
# Historical data shows that the distribution of D can be modelled by the PDF, f(d) =
# 20e−20(d−12.5), d ≥ 12.5. If a part with diameter > 12.6 mm needs to be scrapped,
# what is the proportion of those parts? What is the CDF when the diameter is of 11
# mm?
# What is the conclusion of this experiment?

# In[ ]:




