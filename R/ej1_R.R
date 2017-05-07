library(tidyr)
library(dplyr)

df <- read.csv("/home/cloudera/Downloads/dataset1.csv",stringsAsFactors=FALSE)

df <- df %>%
  fill(Year,Quarter,Balance) %>%
  replace_na(list(Withdrawal = 0))

summary(df$withdrawal)

summary(df)

plot(df$Withdrawal, type ="l")
plot(df$Balance, type="l")

df %>% filter(Withdrawal > 0) %>% select(Month, Balance)
df %>% filter(Withdrawal > 0) %>% select(Month, Balance) %>% arrange(desc(Month))

df %>% mutate(Quarter=gsub('Q','Quarter',Quarter)) %>%
  group_by(Quarter) %>% 
  summarize(Withdrawals = sum(Withdrawal), AverageMonthlyWithdrawal=round(mean(Withdrawal),2))

