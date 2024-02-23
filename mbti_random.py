import random

'''mbti_datasets = {
    'infp': ['갬성충'],
    'entp': ['토론충'],
    'intj': ['시건방진너드'],
    'enfp': ['에너지 넘치는 관종'],
    'isfp': ['자유영혼'],
    'istp': ['주우재','박명수'],
    'infj': ['정신연령 80세인','어르신'],
    'enfp': ['금쪽이','육아 Lv.99999…인'],
    'esfj': ['권력자의 맛 티비'],
    'enfj': ['프로오지라퍼'],
    'esfp': ['이렇게 시끄러울 순 없었다 이건 사람인가 스피커인가','관종 그 자체'],
    'istj': ['매 들고 다니는 로봇'],
    'estp': ['개썅 마이웨이'],
    'estj': ['꼰대'],
    'intp': ['회피형','고집불통','침착맨'],
    'isfj': ['esfp랑 최상의 궁합인']
}
'''
def random_element_from_dataset_for_mbti(dataset_name):
    dataset = mbti_datasets.get(dataset_name)
    if dataset:
        return random.choice(dataset)
    else:
        return None

def find_mbti_keyword(keyword):
    for mbti_keyword in keyword:
        if mbti_keyword in mbti_datasets:
            return mbti_keyword
    return None

found_mbti_keyword = find_mbti_keyword(keyword)
if found_mbti_keyword:
    random_element = random_element_from_dataset_for_mbti(found_mbti_keyword)
    if random_element:
        print(random_element)
    else:
        print("데이터 셋 {}에서 랜덤하게 원소를 선택할 수 없습니다.".format(found_mbti_keyword))
else:
    print("주어진 키워드 중에 MBTI 데이터셋의 키가 없습니다.")