def makeNickName(nounArr,adjective,name):
    nickName=""
    if (len(nounArr)>=3):
        for i in range(len(nounArr)):
            nickName+=nounArr[i]
            nickName+=" "
    if(adjective):
        nickName+=adjective
        nickName+=" "
        for j in range(len(nounArr)):
            nickName+=nounArr[j]
            nickName+=" "

    nickName+=name
    return nickName

nounList = ["왕코", "바나나", "사나이"]
adjective = ""
name = "철수"

nounList2 = ["방구쟁이", "아저씨"]
adjective2 = "멋있는"
name2 = "철수"

# 닉네임 생성 예시
resultNickName = makeNickName(nounList, adjective, name)
print("생성된 닉네임:", resultNickName)

resultNickName2 = makeNickName(nounList2, adjective2, name2)
print("생성된 닉네임2:", resultNickName2)