# `N` represents the number of people polled
N <- 25

# Create a variable `p` that contains 100 proportions ranging from 0 to 1 using the `seq` function
p <- seq(0, 1, length.out=100)


se <- sqrt((p*(1-p)) / N)

# The vector `sample_sizes` contains the three sample sizes
sample_sizes <- c(25, 100, 1000)

# Write a for-loop that calculates the standard error `se` for every value of `p` for each of 
# the three samples sizes `N` in the vector `sample_sizes`. Plot the three graphs, using the `ylim` 
# argument to standardize the y-axis across all three plots.

# Loop through each sample size
for (N in sample_sizes) {
  se <- sqrt((p * (1 - p)) / N)
  plot(p, se, ylim = c(0, 0.1), main = paste("SE with N =", N))
}