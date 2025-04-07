# ------------------------------------------
# Simulating and Visualizing Maximum IQ Growth
# ------------------------------------------------------------------------
# Author: Dylan Anthony Dupont
# Purpose: Estimate and extrapolate the maximum IQ expected in increasingly 
#          large populations using Monte Carlo simulation and continuous 
#          probability and statistics principles. 
# ------------------------------------------------------------------------

# Set random seed for reproducibility
set.seed(1)

# Define population sample sizes (from small to large)... Why these values in particular though?... 
# Because if you keep doubling them they extrapolate to 8.062 Billion - present world population est.
population_sizes <- c(492, 984, 1968, 3936, 7873, 15746,
                      31392, 62984, 125968, 251937, 503875, 1007750)

# Assign simulation repetitions: reverse population sizes to reduce time cost at high 'n'
B_values <- rev(population_sizes)

# Define x-axis range including log10 of global population
full_x_range <- c(log10(min(population_sizes)), log10(12e9))

# Set up an empty plotting window with extended y-axis
plot(NULL,
     xlim = full_x_range,
     ylim = c(100, 240),
     xlab = "log10(Population Size) ~> log10(8.062B) ~> 9.9",
     ylab = "Mean Maximum IQ",
     main = "Live Extrapolation of Max IQ vs Population Size")

# Vectors to store results
log10_pop <- c()
mean_maxIQ <- c()

# Begin simulation loop
for (i in seq_along(population_sizes)) {
  n <- population_sizes[i]
  b <- B_values[i]
  
  # Simulate max IQs and compute mean
  simulated_max <- replicate(b, max(rnorm(n, mean = 100, sd = 15)))
  avg_max <- mean(simulated_max)
  
  # Log-transform population size and store
  log_n <- log10(n)
  log10_pop <- c(log10_pop, log_n)
  mean_maxIQ <- c(mean_maxIQ, avg_max)
  
  # Redraw plot with extended axis
  plot(NULL,
       xlim = full_x_range,
       ylim = c(100, 240),
       xlab = "log10(Population Size) ~> log10(8.062B) ~> 9.9",
       ylab = "Mean Maximum IQ",
       main = "Live Extrapolation of Max IQ vs Population Size")
  
  # Add points and lines for data so far
  points(log10_pop, mean_maxIQ, pch = 19, col = "blue")
  lines(log10_pop, mean_maxIQ, col = "blue")
  
  # Fit regression and extrapolate if enough points exist
  if (length(log10_pop) >= 2) {
    model <- lm(mean_maxIQ ~ log10_pop)
    x_pred <- seq(log10(min(population_sizes)), log10(8.062e9), length.out = 100)
    y_pred <- predict(model, newdata = data.frame(log10_pop = x_pred))
    
    # Add regression line
    lines(x_pred, y_pred, col = "red", lty = 2)
    
    # Predict value at global population
    predicted_maxIQ <- predict(model, newdata = data.frame(log10_pop = log10(8.062e9)))
    
    # Mark prediction with red dot
    points(log10(8.062e9), predicted_maxIQ, pch = 19, col = "darkred")
    
    # Add label above point
    text(x = log10(8.062e9), y = predicted_maxIQ,
         labels = paste0("~", round(predicted_maxIQ, 1)),
         pos = 3, col = "darkred", font = 2)
    
    # Vertical line for reference at 8.062B
    abline(v = log10(8.062e9), col = "darkred", lty = 3)
    
    # Horizontal dotted line to y-axis from predicted point
    segments(x0 = 0,
             y0 = predicted_maxIQ,
             x1 = log10(8.062e9),
             y1 = predicted_maxIQ,
             lty = 3, col = "darkred")
  }
  
  # Delay for animation
  Sys.sleep(0.25)
}



