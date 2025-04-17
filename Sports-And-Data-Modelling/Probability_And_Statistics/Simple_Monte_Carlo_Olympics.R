
set.seed(1)  # for reproducibility
B <- 10000

runners <- c("Jamaica", "Jamaica", "Jamaica", "USA", "Ecuador", "Netherlands", "France", "South Africa")

results <- replicate(B, {
  medalists <- sample(runners, 3)
  all(medalists == "Jamaica")  # returns TRUE if all 3 are Jamaican
})
# Estimated probability
mean(results)




