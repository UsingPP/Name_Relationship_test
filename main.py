import korean_handler as KoreanHandler

def CountYourName(lst) :
    result = []
    num = 0
    for i in range(0, len(lst)) :
        if i % 3 == 0 :
            num += CHOSUNG_COUNTER_LIST[lst[i]]
        elif i % 3 == 1 :
            num += JUNGSUNG_COUNTER_LIST[lst[i]]
        else : # 종성
            num += JONGSUNG_COUNTER_LIST[lst[i]]
            result.append(num)
            num = 0
    return result

def HowMuchCloseYourPartner (name1, name2, convert_name_1, convert_name_2) :
    name1_length = len(convert_name_1)
    name2_length = len(convert_name_2)
    result = []
    for one, two in zip(convert_name_1, convert_name_2) :
        result.append(one)
        result.append(two)
    if name1_length > name2_length :
        result.append(convert_name_1[name1_length-1])
    elif name1_length < name2_length :
        result.append(convert_name_2[name2_length-1])
    
    Print_Name(name1, name2)
    running = True

    while running :
        temp = []

        if len(result) % 2 == 0 :
            for k in range(1, len(result), 2) :
                temp.append((int(result[k]) + int(result[k-1]))%10)
            result = temp


        else :
            for k in range(1, len(result), 2) :
                temp.append((int(result[k]) + int(result[k-1]))%10)
            temp.append(int(result[len(result) -1]))
            result = temp

        for i in result :
            print(i , end = "  ")
        print()
        if len(result) <= 2 :
            result = str(result[0]) + str(result[1])
            running = False
        
    return result

def Print_Name(str_name_1, str_name_2)  :
    for i, j in zip(str_name_1, str_name_2) : 
        print( i, j , end = " ")
    if len(str_name_1) > len(str_name_2) :
        print(str_name_1[-1])
    elif len(str_name_1) < len(str_name_2) :
        print(str_name_2[-1])


CHOSUNG_COUNTER_LIST = {"ㄱ" : 1, "ㄲ" : 2, "ㄴ" : 1, "ㄷ" : 2, "ㄸ" : 4, "ㄹ" : 3, "ㅁ" : 3, "ㅂ" : 4, "ㅃ" : 8, "ㅅ" : 2, "ㅆ" : 4, "ㅇ" : 1, "ㅈ" : 3, "ㅉ" : 6, "ㅊ" : 4, "ㅋ" : 2, "ㅌ" : 3, "ㅍ" : 4, "ㅎ" : 3 }
JUNGSUNG_COUNTER_LIST = {"ㅏ" : 2, "ㅐ" : 3, "ㅑ" : 3, "ㅒ" : 4, "ㅓ" : 2, "ㅔ" : 3, "ㅕ" : 3, "ㅖ" : 4, "ㅗ" : 2, "ㅘ" : 4, "ㅙ" : 5, "ㅚ" : 3, "ㅛ" : 3, "ㅜ" : 2, "ㅝ" : 4, "ㅞ" : 5, "ㅟ" : 3, "ㅠ" : 3, "ㅡ" : 2, "ㅢ" : 2, "ㅣ" : 1 }
JONGSUNG_COUNTER_LIST = {"#" : 0, "ㄱ" : 1, "ㄲ" : 2, "ㄳ" : 3, "ㄴ" : 1, "ㄵ" : 3, "ㄶ" : 4, "ㄷ" : 2, "ㄹ" : 3, "ㄺ" : 4, "ㄻ" : 5, "ㄼ" : 7, "ㄽ" : 5, "ㄾ" : 6, "ㄿ" : 7, "ㅀ" : 6, "ㅁ" : 3, "ㅂ" : 4, "ㅄ" : 6, "ㅅ" : 2, "ㅆ" : 4, "ㅇ" : 1, "ㅈ" : 3, "ㅊ" : 4, "ㅋ" : 2, "ㅌ" : 3, "ㅍ" : 4, "ㅎ" : 3, }


print("이름은 2~3글자만 가능합니다")
#name1 = input("첫번째 이름 : ")
#name2 = input("두번째 이름 : ")
name1 = "김떡순"
name2 = "피탕"
name_1 = KoreanHandler.convert(name1)
name_2 = KoreanHandler.convert(name2)
cv_name1 = CountYourName(name_1)
cv_name2 = CountYourName(name_2)

#print(name_1, name_2)
#print(cv_name1, cv_name2)

result = HowMuchCloseYourPartner(name1, name2, cv_name1, cv_name2)

print(result)
