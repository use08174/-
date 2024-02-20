document.getElementById('generateButton').addEventListener('click', function() {
    const inputText = document.getElementById('inputText').value;
    
    const nickname = generateNickname(inputText); // 닉네임 생성 로직(예시) - 수정 필요
    document.getElementById('nicknameOutput').innerText = nickname ? nickname : "올바른 문장을 입력해주세요.";
});


// 닉네임 생성 로직(예시)
function generateNickname(text) {
    // Your nickname generation logic here
    // Placeholder example: just returns the first word + "TheGreat"
    const words = text.trim().split(/\s+/);
    if (words.length > 0) {
        return words[0] + "TheGreat";
    }
    return "";
}
