import json, requests, smtplib, schedule

def umbrella():
    """
    Checks weather of a desired location at openweathermap.org every morning 
    at 8 AM and if a forecast is going to be rainy, it logs into an e-mail and 
    sends an e-mails to take an umbrella.
    """  
    location = 'Brno, Czech republic'
    url ='http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % \
         (location)
    response = requests.get(url)
    response.raise_for_status()
    weatherData = json.loads(response.text)
    emails = ['xxx']
    if weatherData[0]['weather'] = 'Rainy'
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login('xxx', sys.argv[1])
        body = 'Subject = rain\nDon\'t forget to take your umbrella today.'
        for email in emails:
            sendmail = smtpObj.sendmail('xxx', email, body)
        smtpObj.quit()
      
if _name_ == '_name_':
    schedule.every().day.at("08:00").do(umbrella)
