document.addEventListener('DOMContentLoaded', function() {
    // 버튼 클릭 
    document.getElementById('generateButton').addEventListener('click', function() {
        const inputText = document.getElementById('inputText').value;
        
        const nickname = generateNickname(inputText); // 닉네임 생성 로직(예시로 단어의 첫 글자 + TheGreat로 생성)
        document.getElementById('nicknameOutput').innerText = nickname ? nickname : "올바른 문장을 입력해주세요.";
    });

    // nickname 생성 로직(예시로 단어의 첫 글자 + TheGreat로 생성)
    function generateNickname(text) {
       
        const words = text.trim().split(/\s+/);
        if (words.length > 0) {
            return words[0] + "TheGreat";
        }
        return "";
    }

    // textarea 글자수 제한
    $('#inputText').keyup(function() {
        var content = $(this).val();
        $('#counter').html("(" + content.length + " / 최대 100자)"); //글자수 실시간 카운팅

        if (content.length > 100) {
            alert("최대 100자까지 입력 가능합니다.");
            $(this).val(content.substring(0, 100));
            $('#counter').html("(100 / 최대 100자)");
        }
    }); 
});
