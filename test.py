
import re
import requests as re

def www(www):
    he={'user_post':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'}
    cook={'isComfirmedSEY':'1'}


    www="www"
    urL='https://www.youtube.com/'
    html=re.get(urL)
    html.text
    html.content
    html.status_code
    html=re.get(urL,headers=he,cookies=cook)

    if html.status_code ==200:
        with open("ok_file","a") as f:
            f.write(html.text)
            print("yes")
            print(html.status_code)
    else:
        with open("file_error","a") as j:
            j.write(html.text)
            print("no")
            print(html.status_code)
            
        
    if www==www:
        print("yes")
    else:
        print("no")

    try:
        html.raise_for_status()
        print(html.raise_for_status())
    except Exception as exc:
        print(f'error:{exc}')




