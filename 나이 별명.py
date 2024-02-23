######예시 

list_ex=["내", "이름", "송예한","대학생","20"]
list_end=[]
import random

#세,살, 초딩 
list_0=[]
list_1=[]
list_2=[]
for i in range(8,40):
    list_0.append("{}".format(i))
    list_1.append("{}세".format(i))
    list_2.append("{}살".format(i))
list_final1=list_1+list_2
list_final=list_0+list_1+list_2+["초딩", "초등학생", "중딩", "중학생", "고딩","고등학생", "대딩", "대학생","아저씨","아줌마","늙은이"]
########################################################################
list_ele=["급식도둑", "잼민이", "급식 소세지 도둑", "변기 막힐만큼 싸는 똥쟁이", "어쩔 시크릿쥬쥬리미티드에디션", "와!샌즈 외치는", "리얼 금쪼이", "무서운 이야기 듣고 밤에 지도 그리는", "피구하는데 느려서 못 피하고 얼굴로 다 맞는", "화장실에 몰래 똥싸고 안내린", "노는게 제일 좋아 친구들 모여라", "로블록스만 15시간 째", "키치타니핑 광팬", "색종이 도둑", "짝퉁 제티 도둑", "당근 못 먹는"]
list_mid=["청개구리", "어둠의 자식", "여전히 잼민이", "장난치다 급식판 엎은", "장기자랑에서 공개 고백 받은", "수련회 발냄새 빌런", "필터 때문에 시공간이 뒤틀려진", "체육대회에서 자빠진", "소리 없는 살인방구 뀌어서 반 전체 기절시킨", "뛰다가 교복 찢어진", "급식 소세지 도둑", "틱톡 팔로워 0인", "인스타 무몰보 질문 셀프로 하는", "인스타 라방키고 오열하는"]
list_high=["모의고사 올 9등급 찍는", "급식충", "OMR카드 맨날 밀려 쓰는", "수학여행에서 틱톡춤 추다 넘어진", "시험 찍은 것보다 푼 게 더 많이 틀린", "스터디카페 쌀과자 도둑", "급식 요구르트 도둑", "발표하다 트름한", "학교 매점 털이범", "달리기 하다가 자빠진", "공개고백 하다가 차인", "독서실 방구 빌런", "야자시간에 형광등 조명 삼아 춤추는 고딩"]    
list_2022=["매일 술 먹고 전애인한테 전화해서 퇴짜맞은", "처음 클럽 간 날 입벤당한", "중학생한테 삥 뜯기는", "술주정뱅이", "술찌", "아직 잼민이티나는"]
list_2325=["자기가 다 큰 줄 아는", "술독에 빠진", "매번 지하철에서 헤매는", "마음만은 20대 초반", "체력이 예전 같지 않은", "20대 중반"]
list_2629=["청춘끝", "아직 어리다고 우기는", "곧 20대 후반 진입자", "명절에 항상 결혼 언제하냐 소리 듣는", "영양제 콜렉터", "체력이 예전 같지 않은"]
list_univ=["술고래", "프로자체휴강러" ,"강제헤르미온느", "술 먹고 필름 끊긴", "술먹고 공개 고백한", "MT 발냄새 빌런", "교수님 애제자", "출튀하다 걸린", "술 게임 짱 못하는", "과제 사간 맨날 잘 못 체크하는", "학점 1.5인", "화장실에서 혼자 밥먹는", "딸기", "수강신청 날짜 헷갈린", "공강 만들기 실패자", "\"지쳤나요? 아니요\""]
list_30=["늙은이", "불통의 아이콘", "젊어보이려 애쓰는", "진정한 으른", "마음만은 20대인", "내 나이가 어때서 열창하는", "젊은 척해도 숨겨지지 않는"]
#######################################################################################

def f1():
    list_inter=[]
    for i in range(len(list_ex)):
        if list_ex[i] in list_final:
            list_inter.append(list_ex[i])
    return list_inter

list_rem=[]
list_nrem=[]
for i in range(len(f1())):
    if f1()[i] in list_final1:
            list_rem.append(f1()[i])
    else:
        if f1()[i] in list_0:
            list_nrem.insert(0,f1()[i])
        else:
            list_nrem.append(f1()[i])
        
if list_rem!=[]:
    if "살" in list_rem[0]:
        f_new=list_rem[0].replace("살","")
    elif "세" in list_rem[0]:
        f_new=list_rem[0].replace("세","")
    else:
        f_new=list_rem[0]
    list_rem.clear()
    list_rem.append(f_new)

list_sum=list_rem+list_nrem

if list_sum[0] not in list_0:
    if str(list_sum[0])=="초딩" or str(list_sum[0])=="초등학생":
        chosen_word=random.choice(list_ele)
        print(chosen_word)
        list_end.append(chosen_word)

    if str(list_sum[0])=="중딩" or str(list_sum[0])=="중학생":
        chosen_word=random.choice(list_mid)
        print(chosen_word)
        list_end.append(chosen_word)

    if str(list_sum[0])=="고딩" or str(list_sum[0])=="고등학생":
        chosen_word=random.choice(list_high)
        print(chosen_word)
        list_end.append(chosen_word)

    if  str(list_sum[0])=="대딩" or str(list_sum[0])=="대학생":
        chosen_word=random.choice(list_univ)
        print(chosen_word)
        list_end.append(chosen_word)

    if str(list_sum[0])=="아저씨" or str(list_sum[0])=="아줌마" or str(list_sum[0])=="늙은이":
        chosen_word=random.choice(list_30)
        print(chosen_word)
        list_end.append(chosen_word)

else:
    if 8<=int(list_sum[0])<=13:
        chosen_word=random.choice(list_ele)
        print(chosen_word)
        list_end.append(chosen_word)

    if 14<=int(list_sum[0])<=16:
        chosen_word=random.choice(list_mid)
        print(chosen_word)
        list_end.append(chosen_word)

    if 17<=int(list_sum[0])<=19:
        chosen_word=random.choice(list_high)
        print(chosen_word)
        list_end.append(chosen_word)

    if 20<=int(list_sum[0])<=22:
        chosen_word=random.choice(list_2022)
        print(chosen_word)
        list_end.append(chosen_word)

    if 23<=int(list_sum[0])<=25:
        chosen_word=random.choice(list_2325)
        print(chosen_word)
        list_end.append(chosen_word)

    if 26<=int(list_sum[0])<=29:
        chosen_word=random.choice(list_2629)
        print(chosen_word)
        list_end.append(chosen_word)

    if 30<=int(list_sum[0]) or str(list_sum[0])=="아저씨" or str(list_sum[0])=="아줌마" or str(list_sum[0])=="늙은이":
        chosen_word=random.choice(list_30)
        print(chosen_word)
        list_end.append(chosen_word)

print(list_end)

        



        






















