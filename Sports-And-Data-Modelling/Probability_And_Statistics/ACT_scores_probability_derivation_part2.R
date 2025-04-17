# The SAT is a standardized college admissions test used in the United States. The following two 
# multi-part questions will ask you some questions about SAT testing.

# An old version of the SAT college entrance exam had a -0.25 point penalty for every incorrect 
# answer and awarded 1 point for a correct answer. The quantitative test consisted of 44 
# multiple-choice questions each with 5 answer choices. Suppose a student chooses answers by 
# guessing for all questions on the test.
set.seed(21)
questions_total = 44
point_correct_1q = 1
point_incorrect_1q = -0.25

# What is the expected value of points for guessing on one question?
p_correct_1q <- 1/5
p_incorrect_1q <- 4/5
ev_guessing_1q <- 1*p_correct_1q - 0.25*p_incorrect_1q

# What is the expected score of guessing on all 44 questions?
ev_guessing_ALL <- questions_total*ev_guessing_1q

# What is the standard error of guessing on all 44 questions?
SD_guessing_1q <- abs(point_incorrect_1q - point_correct_1q)*sqrt(p_correct_1q*p_incorrect_1q)

SE_guessing_ALL <- sqrt(questions_total)*SD_guessing_1q

# Use the Central Limit Theorem to determine the probability that a guessing student 
# scores 8 points or higher on the test.
prob_score_8_or_more <- 1 - pnorm(8, mean = ev_guessing_ALL, sd = SE_guessing_ALL)

# Set the seed to 21, then run a Monte Carlo simulation of 10,000 students guessing on the test.
# What is the probability that a guessing student scores 8 points or higher?
B <- 10000
monte_8_or_more <- replicate(B, {
  score <- sum(sample(c(1, -0.25), questions_total, replace=TRUE, prob=c(p_correct_1q, p_incorrect_1q)))
  score >=8
})
p_monte_8_or_more <- mean(monte_8_or_more)
p_monte_8_or_more

# The SAT was recently changed to reduce the number of multiple choice options from 5 to 4 and 
# also to eliminate the penalty for guessing. In this two-part question, you'll explore how 
# that affected the expected values for the test.Suppose that the number of multiple choice 
# options is 4 and that there is no penalty for guessing - that is, an incorrect question 
# gives a score of 0.
new_point_incorrect_1q = 0
new_point_correct_1q = 1
new_p_correct_1q <- 1/4
new_p_incorrect_1q <- 1 - new_p_correct_1q
new_ev_guessing_1q <- 1*new_p_correct_1q + 0*new_p_incorrect_1q
new_ev_guessing_ALL <- questions_total*new_ev_guessing_1q


# Consider a range of correct answer probabilities p <- seq(0.25, 0.95, 0.05) representing a range 
# of student skills. What is the lowest p such that the probability of scoring over 35 exceeds 80%?
p <- seq(0.25, 0.95, 0.05)
# Step 1: Generate expected values and SEs for each p
expected_scores <- questions_total * p
standard_errors <- sqrt(questions_total) * sqrt(p * (1 - p))

# Step 2: Calculate probability of scoring over 35 for each p
prob_over_35 <- 1 - pnorm(35, mean = expected_scores, sd = standard_errors)
p
prob_over_35
which(prob_over_35 > 0.8)
min(which(prob_over_35 > 0.8))

# Step 3: Find the lowest p where probability exceeds 80%
min_p_meeting_threshold <- p[min(which(prob_over_35 > 0.8))]

# Output the result
min_p_meeting_threshold





