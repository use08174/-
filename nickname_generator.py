import fasttext
import numpy as np
import pandas as pd 
from konlpy.tag import Okt
import re
import random
from util import load_csv_dataset
from age_random import random_age_word

# Load the FastText model
model = fasttext.load_model('/Users/suminss/github/name_generator_project/cc.ko.300.bin')

def find_most_similar(word, words, model):
    word_vec = model.get_word_vector(word)
    max_similarity = -1
    most_similar_word = None
    for w in words:
        vec = model.get_word_vector(w)
        similarity = np.dot(word_vec, vec) / (np.linalg.norm(word_vec) * np.linalg.norm(vec))
        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_word = w
    return most_similar_word, max_similarity

def keyword_by_similarity(keywords, dataset,):
    similarity=[]
    result = []
    for word in keywords :
        excluded_categories = ['나이', 'MBTI', '거주지', '랜덤']
        filtered_dataset = dataset[~dataset['카테고리'].isin(excluded_categories)]
        words = filtered_dataset['단어']
        
        most_similar_word, max_similarity = find_most_similar(word, words, model)
        
        # 유사도가 0.4 이상인 경우에만 결과 저장
        if max_similarity >= 0.4:
            similarity.append((word, most_similar_word))
        print(f"{word}은/는 {most_similar_word}와 {max_similarity} 만큼 유사합니다.")
    
    for word, most_similar_word in similarity:
        filtered_dataset = dataset[dataset['단어'] == most_similar_word]
        random_word_row = filtered_dataset.sample()
        
        generated_word = random_word_row['생성'].values[0]
        word_type = random_word_row['유형'].values[0]
        result.append((generated_word, word_type))
    return result

def extract_keywords(sentence):
    okt = Okt()

    nouns = okt.nouns(sentence)
    english_words = re.findall(r'\b[a-zA-Z]+\b', sentence)

    #불용어(stopword) 리스트에 기반하여 의미 없는 한국어 제외

    stopwords_file = "./stopword.txt"

    with open(stopwords_file) as f:
        lines = f.readlines()

    stopwords = [line.rstrip('\n') for line in lines]


    # 추출된 명사를 기반으로 복합 명사 재조합 시도
    recombined_nouns = []
    skip = False
    for i in range(len(nouns)):
        if skip:
            skip = False
            continue
        # 현재 명사와 다음 명사를 조합하여 복합 명사 생성 시도
        if i < len(nouns) - 1:
            compound_noun = nouns[i] + nouns[i + 1]
            # 조합된 복합 명사가 원문에 존재하는 경우
            if compound_noun in sentence:
                recombined_nouns.append(compound_noun)
                skip = True
                continue
        recombined_nouns.append(nouns[i])

    filtered_nouns = [noun for noun in recombined_nouns if noun not in stopwords]
    filtered_english_words = [word for word in english_words if word.lower() not in stopwords]

    final_keywords = filtered_nouns + filtered_english_words
    result = sorted(set(final_keywords), key=final_keywords.index)

    return result

# mbti 생성 코드 
def random_mbti_word(keywords, df):
    # 입력된 키워드 목록에서 MBTI 유형을 찾습니다.
    mbti_dataset = df[df['카테고리'].str.lower() == 'mbti']
    
    mbti_type = None
    for key in keywords:
        if key.lower() in mbti_dataset['단어'].str.lower().unique() :
            mbti_type = key.lower()
            break
    
    if mbti_type:
        filtered_df = df[df['단어'].str.lower() == mbti_type.lower()]
        random_word_row = filtered_df.sample()
        generated_word = random_word_row['생성'].values[0]
        word_type = random_word_row['유형'].values[0]
        
        used_word = mbti_type
        return used_word, generated_word, word_type
    else:
        return None
    
# 지역 생성 코드 
def random_city_word(keywords, df):
    # 입력된 키워드 목록에서 MBTI 유형을 찾습니다.
    city_dataset = df[df['카테고리'] == '거주지']
    
    city_name = None
    for key in keywords:
        if key.lower() in city_dataset['단어'].unique() :
            city_name = key.lower()
            break
    
    if city_name:
        filtered_df = df[df['단어']== city_name]
        random_word_row = filtered_df.sample()
        generated_word = random_word_row['생성'].values[0]
        word_type = random_word_row['유형'].values[0]
        
        used_word = city_name
        return used_word, generated_word, word_type
    else:
        return None

def makeNickName(nounArr,adjective,name):
    nickName=""
    if (len(nounArr)>=3):
        for i in range(len(nounArr)):
            nickName+=nounArr[i]
    if(adjective):
        nickName+=adjective[0]
        nickName+=" "
        for j in range(len(nounArr)):
            nickName+=nounArr[j]

    nickName+=name
    nickName = nickName.replace(" ", "")

    return nickName

def count_noun_adj(word_list):
    nounlist = []
    adjectivelist = []

    # 리스트 순회하면서 분류
    for item in word_list:
        word, pos = item  # 튜플 언패킹
        if pos == '명사':
            nounlist.append(word)
        elif pos == '관형사':
            adjectivelist.append(word)
    count_noun = len(nounlist)
    count_adj = len(adjectivelist)
    return count_noun, count_adj

# 생성 메인 코드 
def generate_words(keywords, dataset) :
    print("extracted keywords", keywords)
    
    generated_keyword_count = 0
    generated_result = []
    # age 생성
    age_word = random_age_word(keywords, dataset)
    print(age_word)
    
    # mbti 생성
    mbti_word = random_mbti_word(keywords, dataset)
    if mbti_word :
        used_word, mbti_word, mbti_type = mbti_word
        generated_result.append((mbti_word, mbti_type))
        generated_keyword_count += 1
        keywords.remove(used_word)
    
    # 도시 생성 
    city_word = random_city_word(keywords, dataset)
    if city_word :
        used_word, city_word, city_type = city_word
        generated_result.append((city_word, city_type))
        generated_keyword_count += 1
        keywords.remove(used_word)
    
    # 다른 키워드 유사도 측정
    result = keyword_by_similarity(keywords, dataset)
    generated_result += result 
    
    # 중복 제거
    generated_result = list(set(generated_result))
    print("추출된 키워드 바탕으로 생성된 단어들", generated_result)
    
    # 랜덤 생성으로 개수 맞추기
    count_noun, count_adj = count_noun_adj(generated_result)

    
    if (len(generated_result) == 2) :
        filtered_dataset = dataset[dataset['카테고리'] == '랜덤']
        random_word_row = filtered_dataset.sample()
        
        generated_word = random_word_row['생성'].values[0]
        word_type = random_word_row['유형'].values[0]
        generated_result.append((generated_word, word_type))
    
    elif (len(generated_result) == 1) :
        for i in range(2) :
            filtered_dataset = dataset[dataset['카테고리'] == '랜덤']
            random_word_row = filtered_dataset.sample()
            
            generated_word = random_word_row['생성'].values[0]
            word_type = random_word_row['유형'].values[0]
            generated_result.append((generated_word, word_type))
    elif (len(generated_result) == 0) : 
        for i in range(3) :
            filtered_dataset = dataset[dataset['카테고리'] == '랜덤']
            random_word_row = filtered_dataset.sample()
            
            generated_word = random_word_row['생성'].values[0]
            word_type = random_word_row['유형'].values[0]
            generated_result.append((generated_word, word_type))
    
    
    # 3개보다 많으면 랜덤으로 3개 추출
    if (len(generated_result) > 3) :
        generated_result = random.sample(generated_result, 3)
    
    return generated_result




if __name__ == "__main__":
    sentence_1 = "안녕하세요! 저는 김지은이고 26살입니다. 서울에서 태어나고 자랐으며, 현재는 웹 개발자로 일하고 있어요. 코딩과 새로운 기술을 배우는 것을 정말 좋아하고, 여가 시간에는 사진 찍기와 여행을 즐깁니다. 또한, 자연을 사랑해서 자주 등산을 가요. 앞으로 다양한 프로젝트에 참여하며 경험을 쌓아가고 싶어요."
    sentence_2 = "내 이름은 심수민이고, 대학생이야. 프로메테우스라는 인공지능 동아리에서 개발부 부장을 맡고 있어. 서울에서 살고 있어. mbti는 istj 이고, 사람들을 좋아하지만 때론 낯을 가리는 것 같아. 코딩 학원에서 학생들을 가르치고 있고, 평소에는 그냥 누워서 핸드폰하는 것을 좋아해."
    sentence_3 = "안녕"
    name = "철수"

    # 1. load dataset
    file_path = './assets/category.xlsx' 
    df = pd.read_excel(file_path, engine='openpyxl')

    # 2. keyword 추출
    keywords = extract_keywords(sentence_2)
    # + keyword에서 이름 삭제
    # + 이야기에서 나이, 거주지, mbti가 있는지 체크해서 있다면 keyword에 넣기
    
    # 3. generate keywords
    generated_words = generate_words(keywords, df) # 중요 키워드 추출
    #print("generated_words", generated_words)

    # 4. 품사에 따른 닉네임 생성
    nounlist = []
    adjectivelist = []

    for item in generated_words:
        word, pos = item  
        if pos == '명사':
            nounlist.append(word)
        elif pos == '관형사':
            adjectivelist.append(word)
        
    nickname = makeNickName(nounlist, adjectivelist, name)
    print(nickname)




