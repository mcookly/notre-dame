## Part 1
library(glmbb)
data(crabs)
hist(crabs$width,
     main = "Histogram of Carapace Widths",
     xlab = "Widths (cm)",
     breaks = 20
)

# Find sample average and standard deviation
y_bar <- mean(crabs$width)
s <- sd(crabs$width)
nCrabs = 10

# Find 90% Confidence Interval
ts = qt(.95, nCrabs - 1)
conLower = y_bar - ts*(s/sqrt(nCrabs))
conUpper = y_bar + ts*(s/sqrt(nCrabs))

# Test carapace hypothesis
t.test(crabs$width, alternative = "less", mu = 28, conf.level = .99)

## Part 2
Auto <- read.table("Auto.csv", header = TRUE)
hist(Auto$Cost, breaks = 5)
yBar <- mean(Auto$Cost)
s <- sd(Auto$Cost)
t.test(Auto$Cost, conf.level = .95)
t.test(Auto$Cost, alternative = "greater", mu = 75.50, conf.level = .95)
