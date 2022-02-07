### Large Sample Size ###

#1. Import voter responses from 1996 US Pres. Election
nes96 <- read.table("nes96.txt", header = TRUE)

#2. Obtain ages vectors for Reps and Dems
ageDem <- nes96$age[nes96$PID == "Democrat"]
ageRep <- nes96$age[nes96$PID == "Republican"]

#3. Calculate sample variances
s2Dem <- var(ageDem)
s2Rep <- var(ageRep)

#4. Find number of Reps and Dems
nDem <- length(ageDem)
nRep <- length(ageRep)

#5. Run a t-test
t.test(ageDem, ageRep, alternative = "less", conf.level = 0.95)

### Small Sample Size ###

#1. Import
baseball <- read.csv("baseball.csv", header = TRUE)

#2. Split into vectors
hrAL <- baseball$HRs[baseball$League == "American"]
hrNL <- baseball$HRs[baseball$League == "National"]

#3. Conduct t-test
t.test(hrAL, hrNL, alternative = "two.sided", conf.level = 0.95)


### Wilcoxon Rank-sum Test ###

#1. Get data
volume <- c(27, 31, 26, 25, 32, 29, 35, 28)
group <- c(rep("A", 4), rep("B", 4))

#2. Test
wilcox.test(volume~group, alternative = "less")
