import pandas as pd
import datetime
import smtplib
import os
os.chdir(r"C:/Users/mini9/Desktop/New folder")
#os.mkdir("testing")

# Enter your details
GMAIL_ID=''
GMAIL_PSWD=''


def sendEmail(to, sub, msg):
    print(f"Email to {to} sent with subject: {sub} and message {msg}")
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(GMAIL_ID,GMAIL_PSWD)

    s.sendmail(GMAIL_ID,to,f"Subject: {sub}\n\n{msg}")
    s.quit()


if __name__ == "__main__":

    df = pd.read_excel("data.xlsx")
    today = datetime.datetime.now().strftime("%d-%m")  # here we have taken today in string format
    writeInd=[]
    yearNow = datetime.datetime.now().strftime("%Y")


    for index,item in df.iterrows():  # to read index and item from the dataframe
        bday =item['Birthday'].strftime("%d-%m")


        if (today == bday) and yearNow not in str(item['Year']):
            sendEmail(item['E-mail'],"Happy Birthday",item['Dialogue'])
            writeInd.append(index)


    for i in writeInd:
        yr= df.loc[i,'Year']
        df.loc[i,'Year']=str(yr) + ", "+ str(yearNow)
        print (df.loc[i,'Year'])


    df.to_excel('data.xlsx',index=False)
