import pandas as pd
from datetime import date

date_today = str(date.today())
list1 = [date_today]

postcount = pd.DataFrame(columns=['Date','Angular','C++','Flutter','HTML','Java','JavaScript','Laravel','nodeJS','Perl','PHP','Python','React','Ruby','SQL','WordPress'])
files_list = ["angular.csv", "c++.csv", "flutter.csv", "html.csv", "java.csv", "javascript.csv", "laravel.csv", "nodejs.csv",
"perl.csv", "php.csv", "python.csv", "react.csv", "ruby.csv", "sql.csv", "wordpress.csv"]

for file_name in files_list:
    path_final = "C:\\Users\\Dell\\Documents\\PSV_vs\\1-7 New\\" + file_name
    df = pd.read_csv(path_final)
    l = len(df)
    list1.append(l)

postcount.loc[len(postcount)] = list1
#print(postcount)
postcount.to_csv("count.csv",mode='a',index=False,header=False)

