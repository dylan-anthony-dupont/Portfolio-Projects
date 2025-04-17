# A casino offers a House Special bet on roulette, which is a bet on five pockets (00, 0, 1, 2, 3) 
# out of 38 total pockets. The bet pays out 6 to 1. In other words, a losing bet yields -$1 and a 
# successful bet yields $6. A gambler wants to know the chance of losing money if he places 500 bets 
# on the roulette House Special.

#What is the expected value of the payout for one bet?
n_bets <- 500
p_win_1bet <- 5/38
p_lose_1bet <- 1 - p_win_1bet
payout_win_1bet <- 6
loss_lose_1bet <- -1
EV_1bet <- payout_win_1bet*p_win_1bet + loss_lose_1bet*p_lose_1bet
EV_1bet

# What is the standard error of the payout for one bet?
SE_1bet <- abs(loss_lose_1bet-payout_win_1bet)*sqrt(p_win_1bet*p_lose_1bet)
SE_1bet

# What is the expected value of the average payout over 500 bets? Remember there 
# is a difference between expected value of the average and expected value of the sum.
EV_avg_payout_500bets <- EV_1bet
EV_avg_payout_500bets

# What is the standard error of the average payout over 500 bets? Remember there is a 
# difference between the standard error of the average and standard error of the sum.
SE_avg_payout_500bets <- SE_1bet / sqrt(n_bets)
SE_avg_payout_500bets

# What is the expected value of the sum of 500 bets?
EV_sum_500bets <- n_bets*EV_1bet
EV_sum_500bets

# What is the standard error of the sum of 500 bets?
SE_sum_500bets <- n_bets*SE_avg_payout_500bets
SE_sum_500bets

# Use pnorm() with the expected value of the sum and standard error of the sum to calculate 
# the probability of losing money over 500 bets, Pr(X <= 0).
p_lose_money_over_500bets <- pnorm(0, EV_sum_500bets, SE_sum_500bets)
p_lose_money_over_500bets
