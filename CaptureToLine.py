import pyautogui
import time
import requests

'''
def linenotify(message):
  url = 'https://notify-api.line.me/api/notify'
  token = 'HL2hTGfnH2JeSvthfTTbbmW0XE9Wf7KeHZJkR3Ef4Y' # Line Notify Token
  #img = {'imageFile': open('.png','rb')} #Local picture File
  data = {'message': message}
  headers = {'Authorization':'Bearer ' + token}
  session = requests.Session()
  session_post = session.post(url, headers=headers, data =data)
  print(session_post.text) 
  
message = 'Hello Python' #Set your message here!
linenotify(message)

'''


message = 'Hello Python' #Set your message here!
i=1
while i<10 :

    
  # time.sleep(3) #3 วิค่อยรัน
  pyautogui.screenshot(str(i)+".png")
  print(i)
  
  
  url = 'https://notify-api.line.me/api/notify'
  #token = 'HL2hTGfnH2JeSvthfTTbbmW0XE9Wf7KeHZJkR3Ef4Y4' # Line Notify Token drone
  token ='u4iZzAuWHY4E5UzB3bcxv9viLV5JIeFxtNvaURKywUj' #บาดเจ็บ
    
  photo = str(i)+".png"#ใส่เพิ่ม photo เป็น str

  img = {'imageFile': open(photo,'rb')} #Local picture File
  data = {'message': message}
  headers = {'Authorization':'Bearer ' + token}
  session = requests.Session()
  session_post = session.post(url, headers=headers, files=img, data =data,)
  

  i+=1
  
