import requests
from emoji import emojize


def telegram_bot_sendtext(bot_message):
    
    bot_token = '1022661921:AAFSCX73U3iNoRlNTVKbM5RumEuu4pQQ8lY'
#     bot_chatID = '1070670361'
    bot_chatID = '@testingeducas'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
#removing Remove text between () and [] in python


import re
def strip_character(dataCol):
    r = re.compile('[\(\[].*?[\)\]]')
    return r.sub('', dataCol)

import pandas as pd
import time
import datetime
from IPython.display import Markdown, display
ind=0
print(datetime.datetime.now())

while 1:    
    df = pd.read_csv('data/job_details.csv')
    df = df.dropna()
    df.About_Work = df.About_Work.str.replace(r'Selected interns day-to-day responsibilities include:','').str.replace('Only those','')
    x=df
    x = x.applymap(lambda x: x.strip())
    x['ApplyBy']=pd.to_datetime(x['ApplyBy']).map(lambda x: x.strftime('%d-%m-%Y'))
    x=x.sort_values('ApplyBy',ascending=False)
    x=x.reset_index(drop=True)


    x.Skills = x.Skills.apply(strip_character)
    x = x.applymap(lambda x: str(x).strip())
    y=x.iloc[ind:ind+6]
    
    start_time = time.time()
    for index, row in y.iterrows():
            JobTItle            =  row['JobTItle']
            Company             =  row['Company']
            URL                 =  row['Url']
            StartDate           =  row['StartDate']
            Duration            =  row['Duration']
            Stipend             =  row['Stipend']
            ApplyBy             =  row['ApplyBy']
            About_Company       =  row['About_Company']
            About_Work          =  row['About_Work']
            Skills              =  row['Skills']
            class color:
                BOLD = '\033[1m'
                END = '\033[0m'
            time.sleep(1)
            telegram_bot_sendtext("\n" +"*JobTitle :*" + "  "+str(JobTItle) + "\n" + "*Company :*" + "  "+str(Company) + "\n" + "*Url :*" + "  "+str(URL)+ "\n"+"*StartDate :*" + "  "+str(StartDate) + "\n" + "*Duration :*" + "  "+str(Duration)+ "\n" +  "*Stipend :*" + "  "+str(Stipend) + "\n" + "*ApplyBy :*" + "  "+str(ApplyBy) + "\n" + "*Skills :*" + "  "+str(Skills)+ "\n"+"\n"+"*For More Updates*: [Register here](https://forms.gle/ayhd1WyafUKijJm79) "+"\n"+" ")   
            print("message sent for Index " + str(index)+ " " + str(datetime.datetime.now()))

    end_time = time.time()
    ind=y.index[-1]
    print(f"Runtime of the program is {end_time - start_time}")

    if end_time - start_time > 1:
        print('Testing Telegram bot ' + emojize("yummy :thumbsup:", use_aliases=True))
        telegram_bot_sendtext("Testing Telegram bot" + emojize("yummy :thumbsup:", use_aliases=True))


    print("Resetting Index = "+ str(ind))
    # t = time.time()


 

