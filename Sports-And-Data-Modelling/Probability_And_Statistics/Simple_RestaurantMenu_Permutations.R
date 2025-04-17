#The manager isn't sure he can afford to put that many entree choices on the lunch menu and thinks it 
#would be cheaper for him to expand the number of sides. He wants to know how many sides he would have 
#to offer to meet his goal of at least 365 combinations.

#- Write a function that takes a number of side choices and returns the number of meal combinations 
#possible given 6 entree choices, 3 drink choices, and a selection of 2 sides from the specified number 
#of side choices.

#- Use sapply() to apply the function to side counts ranging from 2 to 12.

#What is the minimum number of side options required in order to generate more than 365 combinations?

drink_combo <- 3
entree_combo <- 6
n = 2:12
sides_combo <- function(sides){
  (choose(sides, 2)) * entree_combo * drink_combo
}
combo_counts <- sapply(n, sides_combo)
combo_counts
combo_counts[6]
combo_counts[7]

plot(n, combo_counts)
n[which(combo_counts >= 365)[1]]