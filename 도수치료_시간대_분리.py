data<- read_csv('20230717_totalinfo 2.csv')
data1<- data %>% filter(npayCd=='MX1220000')
data1 %>% View()
#rmkTxt에서 시간을 나타내는 숫자 분리
# 분 추출 및 정제
data1 <- data1 %>%  mutate(min = substr(rmkTxt, regexpr("분", rmkTxt)-3, regexpr("분", rmkTxt)-1))
data1 <- data1 %>%  mutate(min = ifelse(is.na(gsub('\\D',"",min)), "0", gsub('\\D',"",min)))
data1$min <- as.numeric(data1$min)data1$min[is.na(data1$min)] <- 0

# 시간 추출 및 정제
data1 <- data1 %>%  mutate(hour = substr(rmkTxt, regexpr("시간", rmkTxt)-1, regexpr("시간", rmkTxt)+1))

data1 <- data1 %>%  mutate(hour = ifelse(is.na(gsub('\\D',"",hour)), "0", gsub('\\D',"",hour)))
data1$hour <- as.numeric(data1$hour)
data1$hour <- data1$hour *60data1$hour[is.na(data1$hour)] <- 0
# 시간과 분 합치기
data1$time <- data1$hour + data1$min

# 10분대, 20분대 ~ 60분 이상 구분하는 열 추가
data2<- data1 %>% mutate(time_div=case_when(  data1$time<=0~'기타',  data1$time<=9~'10분 미만',  data1$time<=19~'10분 대',  data1$time<=29~'20분 대',  data1$time<=39~'30분 대',  data1$time<=49~'40분 대',  data1$time<=59~'50분 대',  data1$time>=60~'60분 이상'))
View(data2)
write.csv(data2, 'dosu_time_div.csv')
