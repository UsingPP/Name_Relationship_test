import os
import sys
import urllib.request
import json

def translate() :
    isRunning = True
    while (isRunning):
        print("choose your target language you want translate")
        print("당신이 원하는 번역 언어를 선택해주세요")
        print("1.EN  2. JP  3. zh-CN  4. zh-TW      0. QUIT")
        while(True) :
            target_lan = input()
            if target_lan == '1' :
                target = "en"
                break
            elif target_lan == '2' :
                target = 'ja'
                break	
            elif target_lan == '3' :
                target ='zh-CN'
                break
            elif target_lan == '4' :
                target ='zh-TW'
                break
            elif target_lan == '0' :
                isRunning = False
                return
            else :
                print("RANGE OVER::CHOOSE 1~4 NUM")

        while(isRunning) :
            print("번역하고 싶은 문장을 작성하세요(-1을 입력 시 종료, 0을 선택 시 언어 선택)")
            target_str = input()

            if ( target_str == '-1') :
                isRunning = False
                break
            if ( target_str == '0') :
                break

            client_id = "Xhm5XP0diWwEpFvlOw6a" # 개발자센터에서 발급받은 Client ID 값
            client_secret = "TauLte7a_q" # 개발자센터에서 발급받은 Client Secret 값
            encText = urllib.parse.quote(target_str) # 번역하려는 문장

            source =  "ko" #출발 언어 코드

            data = "source=" + source + "&target=" + target + "&text=" + encText
            url = "https://openapi.naver.com/v1/papago/n2mt"

            request = urllib.request.Request(url)
            request.add_header("X-Naver-Client-Id",client_id)
            request.add_header("X-Naver-Client-Secret",client_secret)
            response = urllib.request.urlopen(request, data=data.encode("utf-8"))

            rescode = response.getcode()

            if(rescode==200):
                response_body = response.read().decode('utf-8')
                responseTojson = json.loads(response_body)
                response_body_target = responseTojson['message']['result']['translatedText']
                print(response_body_target)
                print()
                print("+++++++++")
                print()
            else:
                print("Error Code:" + rescode)
                
translate()