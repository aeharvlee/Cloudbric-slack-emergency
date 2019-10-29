import calendar
import numpy as np
import pandas as pd

emergency_manager_csv = pd.read_csv('clb_error_manager_list.csv', encoding='utf-8')
df = pd.DataFrame(emergency_manager_csv)
df = df.replace(np.nan, '', regex=True) # remove nan from DataFrame


year_and_month = df.columns[0]
df.columns = ['sun', 'mon', 'tue', 'wed', 'thr', 'fri', 'sat']

year = year_and_month[0:4]
month = year_and_month[6:8].zfill(2)
month_name = calendar.month_name[int(month)]
week_days = df.iloc[0, ] # 일요일, 월요일, ... , 금요일, 토요일

output_file = open('slack_reminder_emergency.txt', 'w+')

for row_index, rows in df.iterrows():
    if row_index != 0 and row_index % 2 == 0:
        for column_index in range(0, 7):
            day = df.iloc[row_index - 1, column_index]
            day = day[:2].strip().zfill(2)

            # day에 해당하는 요일 정보
            day_of_week = week_days[column_index]

            # day에 해당되는 장애대응 담당자들
            managers_of_day = rows[column_index]
            if managers_of_day:
                # managers_of_day는 하이푼을 비롯하여 개행 문자 등이 섞여 있으므로 적절한 토큰화가 필요
                tokenized_strings = managers_of_day.split()
                token_len = len(tokenized_strings)
                if (token_len >= 9):
                    dev_manager = tokenized_strings[2]
                    tech_manager = tokenized_strings[5]
                    tech_sub_manager = tokenized_strings[8]
                    sub_flag = True
                else:
                    dev_manager = tokenized_strings[2]
                    tech_manager = tokenized_strings[5]
                    sub_flag = False

                if sub_flag:
                    text_with_sub = f'/remind #emergency "장애대응 담당 {year}.{month}.{day}({day_of_week[0]}) - {dev_manager},{tech_manager}({tech_sub_manager})" {month_name} {day}\n'
                    output_file.write(text_with_sub)
                else:
                    text= f'/remind #emergency "장애대응 담당 {year}.{month}.{day}({day_of_week[0]}) - {dev_manager},{tech_manager}" {month_name} {day}\n'
                    output_file.write(text)

output_file.close()
file = open('slack_reminder_emergency.txt', 'r')
print(file.read())
