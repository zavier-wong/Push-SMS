from datetime import datetime
import time
import requests
from datetime import datetime
from twilio.rest import Client # 需要装twilio库
from apscheduler.schedulers.blocking import BlockingScheduler#定时框架

def send_message():
    weekday={0:'周日\n',1:'周一\n',2:'周二\n',3:'周三\n',4:'周四\n',5:'周五\n',6:'周六\n'}

    tu=(    ('英语 ','中文\n'),\
            ('高数 ','中金梯二\n'),\
            ('导论 ','中文东梯\n'),\
            ('离散 ','中金梯八\n'),\
            ('物理 ','中实梯一\n'),\
            ('形势 ','中金梯一\n'),\
            ('思修 ','中金梯一\n'),\
            ('体育 ','本部操场\n'),\
            )
    moon=('上午:','中午:','晚上:')
    kebiao=(((tu[0]),(tu[1],tu[2]),(tu[3])),\
            ((tu[3],tu[4]),(),(tu[5])),\
            ((tu[0]),(tu[1],tu[6]),()),\
            ((tu[4],tu[7]),(),()),\
            ((),(tu[1],tu[6]),()),\
        )
    weekda=int(datetime.now().strftime("%w"))-5
    week=int(datetime.now().strftime("%W"))-5

    if weekda>0 and weekda<6:
        b=''
        #当天课程表
        daykecheng=([],[],[])
        index=0
        for i in kebiao[weekda-1]:
            for j in i:
                if j!=():
                    daykecheng[index].append(j)
            index+=1
        #当天课程表字符串    

        index=0
        for i in daykecheng:
            if i!=[]:
                b+=" %s\n"%moon[index]
            for j in i:
                for z in j:
                    b+=("%s"%z)
                
            index+=1
    elif weekda==6:
        b="今天是周六啊\n好好休息吧！\n"
    else:
        b="今天是周日啊\n好好休息吧！\n"

    #time.strftime("今天是%Y/%m/%d\n", time.localtime()),
    a=("第%s周%s早上好啊！\n"%(week,weekday[weekda]),\
       b,\
       time.strftime("%Y/%m/%d\n", time.localtime()))

    #转换成字符串
    string=''
    for i in a:
        string+=i
      
    account_sid = 'AC141c958a0c65cf622b7d22d61060d48f' # api参数 复制粘贴过来
    auth_token = '04c714744ed7ba0ea70385a0b28e48cb' # api参数 复制粘贴过来
    client = Client(account_sid, auth_token) # 账户认证
    message = client.messages.create(
      to="+8613295931195", # 接受短信的手机号 注意写中国区号 +86
      from_="+12073673307", # api参数 Number(领取的虚拟号码
      body=string) #自定义短信内容
send_message()        

sched = BlockingScheduler()
sched.add_job(send_message,'cron',month='1-7',day='1-31',hour=7,minute=1)
sched.start()

