# Set random seed for reproducibility
set.seed(16)
         
# Number of ACT Tests to simulate
B <- 10000

# simulate normal distribution of 10000 ACT tests with a mean of 20.9 and standard deviation of 5.7.
act_scores <- rnorm(B, mean = 20.9, sd = 5.7)

# mean of ACT scores
mean_scores <- mean(act_scores)

# sd of ACT scores
sd_scores <- sd(act_scores)

# num scores greater than or equal to 36
perfect_scores <- sum(act_scores >= 36)

#In act_scores, what is the probability of an ACT score greater than 30?
scores_less_than_or30 <- sum(act_scores <= 30)
prob_greater_than_30 <- (B - scores_less_than_or30) / B

#In act_scores, what is the probability of an ACT score less than or equal to 10?
scores_less_than_or10 <- sum(act_scores <= 10)
scores_less_than_or10 <- (scores_less_than_or10) / B
scores_less_than_or10

#Set x equal to the sequence of integers 1 to 36. Use dnorm to determine 
# the value of the probability density function over x given a mean of 20.9 
# and standard deviation of 5.7; save the result as f_x. Plot x against f_x.
x <- 1:36
f_x <- dnorm(x, 20.9, 5.7)
#plot(x, f_x)

# Convert act_scores to Z-scores. Recall that to standardize values 
# (convert values into Z-scores, that is, values distributed with a mean of 0 
# and standard deviation of 1), you must subtract the mean and then divide by 
# the standard deviation. Use the mean and standard deviation of act_scores, not 
# the original values used to generate random test scores.
mean_act_scores <- mean(act_scores)
sd_act_scores <- sd(act_scores)
z_scores <- (act_scores - mean_act_scores) / sd_act_scores

# What is the probability of a Z-score greater than 2 (2 standard deviations above the mean)?
z_scores_greater_than2 <- sum(z_scores > 2)
prob_z_scores_greater_than2 <- z_scores_greater_than2 / B

# What ACT score value corresponds to 2 standard deviations above the mean (Z = 2)?
z_score_2sd_above_mean <- mean_act_scores + 2*(sd_act_scores)
z_score_2sd_above_mean

# A Z-score of 2 corresponds roughly to the 97.5th percentile. Use qnorm() to determine 
# the 97.5th percentile of normally distributed data with the mean and standard deviation 
# observed in act_scores. What is the 97.5th percentile of act_scores?
percentile97.5 <- qnorm(0.975, mean_act_scores, sd_act_scores)

# What is the minimum integer score such that the probability of that score or lower is at least .95?
# Your answer should be an integer 1-36.
ceiled_percentile95 <- ceiling(qnorm(0.95, mean_act_scores, sd_act_scores))

# Use qnorm() to determine the expected 95th percentile, the value for which the probability 
#of receiving that score or lower is 0.95, given a mean score of 20.9 and standard deviation of 5.7.
#What is the expected 95th percentile of ACT scores?

percentile95 <- qnorm(0.95, 20.9, 5.7)

# We can use quantile() to determine sample quantiles from the data. Make a vector containing 
# the quantiles for p <- seq(0.01, 0.99, 0.01), the 1st through 99th percentiles of the act_scores data. 
# Save these as sample_quantiles. In what percentile is a score of 26? Your answer should be an 
# integer (i.e. 60), not a percent or fraction. Note that a score between the 98th and 99th percentile 
# should be considered the 98th percentile, for example, and that quantile numbers are used as 
# names for the vector sample_quantiles.
p <- seq(0.01, 0.99, 0.01)
sample_quantiles <- quantile(act_scores, p)
#which(sample_quantiles > 26)[1] - 1  # Integer percentile, as requested

# Make a corresponding set of theoretical quantiles using qnorm() over the interval 
# p <- seq(0.01, 0.99, 0.01) with mean 20.9 and standard deviation 5.7. Save these 
# as theoretical_quantiles. Make a QQ-plot graphing sample_quantiles on the y-axis versus 
# theoretical_quantiles on the x-axis.
theoretical_quantiles <- qnorm(p, mean = 20.9, sd = 5.7)
qqplot(theoretical_quantiles, sample_quantiles)
