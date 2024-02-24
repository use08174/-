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

def f1(keywords):
    list_inter=[]
    for i in range(len(keywords)):
        if keywords[i] in list_final:
            list_inter.append(keywords[i])
    return list_inter

def random_age_word(keywords,dataset) :
    list_inter = f1(keywords)
    
    list_rem=[]
    list_nrem=[]
    for i in range(len(list_inter)):
        if list_inter[i] in list_final1:
                list_rem.append(list_inter[i])
        else:
            if list_inter[i] in list_0:
                list_nrem.insert(0,list_inter[i])
            else:
                list_nrem.append(list_inter[i])

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
    
    if (len(list_sum) == 0) :
        return None
    
    if list_sum[0] not in list_0:
        if str(list_sum[0])=="초딩" or str(list_sum[0])=="초등학생":
            filtered_dataset = dataset[dataset['단어'] == '초등학생']
            random_word_row = filtered_dataset.sample()
            
            generated_word = random_word_row['생성'].values[0]
            word_type = random_word_row['유형'].values[0]
            list_end.append((generated_word, word_type))
            
        if str(list_sum[0])=="중딩" or str(list_sum[0])=="중학생":
            filtered_dataset = dataset[dataset['단어'] == '중학생']
            random_word_row = filtered_dataset.sample()
            
            generated_word = random_word_row['생성'].values[0]
            word_type = random_word_row['유형'].values[0]
            list_end.append((generated_word, word_type))

        if str(list_sum[0])=="고딩" or str(list_sum[0])=="고등학생":
            filtered_dataset = dataset[dataset['단어'] == '고등학생']
            random_word_row = filtered_dataset.sample()
            
            generated_word = random_word_row['생성'].values[0]
            word_type = random_word_row['유형'].values[0]
            list_end.append((generated_word, word_type))

        if  str(list_sum[0])=="대딩" or str(list_sum[0])=="대학생":
            filtered_dataset = dataset[dataset['단어'] == '대학생']
            random_word_row = filtered_dataset.sample()
            
            generated_word = random_word_row['생성'].values[0]
            word_type = random_word_row['유형'].values[0]
            list_end.append((generated_word, word_type))

        if str(list_sum[0])=="아저씨" or str(list_sum[0])=="아줌마" or str(list_sum[0])=="늙은이":
            filtered_dataset = dataset[dataset['단어'] == '30살 이상']
            random_word_row = filtered_dataset.sample()
            
            generated_word = random_word_row['생성'].values[0]
            word_type = random_word_row['유형'].values[0]
            list_end.append((generated_word, word_type))

    else:
        if 8<=int(list_sum[0])<=13:
            filtered_dataset = dataset[dataset['단어'] == '초등학생']
            random_word_row = filtered_dataset.sample()
            
            generated_word = random_word_row['생성'].values[0]
            word_type = random_word_row['유형'].values[0]
            list_end.append((generated_word, word_type))

        if 14<=int(list_sum[0])<=16:
            filtered_dataset = dataset[dataset['단어'] == '중학생']
            random_word_row = filtered_dataset.sample()
            
            generated_word = random_word_row['생성'].values[0]
            word_type = random_word_row['유형'].values[0]
            list_end.append((generated_word, word_type))

        if 17<=int(list_sum[0])<=19:
            filtered_dataset = dataset[dataset['단어'] == '고등학생']
            random_word_row = filtered_dataset.sample()
            
            generated_word = random_word_row['생성'].values[0]
            word_type = random_word_row['유형'].values[0]
            list_end.append((generated_word, word_type))

        if 20<=int(list_sum[0])<=22:
            filtered_dataset = dataset[dataset['단어'] == '20대 초반']
            random_word_row = filtered_dataset.sample()
            
            generated_word = random_word_row['생성'].values[0]
            word_type = random_word_row['유형'].values[0]
            list_end.append((generated_word, word_type))

        if 23<=int(list_sum[0])<=25:
            filtered_dataset = dataset[dataset['단어'] == '20대 중반']
            random_word_row = filtered_dataset.sample()
            
            generated_word = random_word_row['생성'].values[0]
            word_type = random_word_row['유형'].values[0]
            list_end.append((generated_word, word_type))

        if 26<=int(list_sum[0])<=29:
            filtered_dataset = dataset[dataset['단어'] == '20대 후반']
            random_word_row = filtered_dataset.sample()
            
            generated_word = random_word_row['생성'].values[0]
            word_type = random_word_row['유형'].values[0]
            list_end.append((generated_word, word_type))

        if 30<=int(list_sum[0]) or str(list_sum[0])=="아저씨" or str(list_sum[0])=="아줌마" or str(list_sum[0])=="늙은이":
            filtered_dataset = dataset[dataset['단어'] == '30살 이상']
            random_word_row = filtered_dataset.sample()
            
            generated_word = random_word_row['생성'].values[0]
            word_type = random_word_row['유형'].values[0]
            list_end.append((generated_word, word_type))
            
    print(list_end)
    return list_end



        



        






















