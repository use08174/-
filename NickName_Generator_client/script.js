document.addEventListener("DOMContentLoaded", function () {
  // 버튼 클릭 시 닉네임 생성
  document
    .getElementById("generateButton")
    .addEventListener("click", function () {
      const inputName = document.getElementById("inputName").value;
      const inputText = document.getElementById("inputText").value;

      const button = this;
      const originalButtonText = button.innerText;
      button.disabled = true;
      button.innerText = "생성 중...";

      // API 호출
      fetch("/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ name: inputName, sentence: inputText }),
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error("Network response was not ok");
          }
          return response.json();
        })
        .then((data) => {
          console.log("결과:", data);
          document.getElementById("nicknameOutput").innerText = data.nickname;
        })
        .catch((error) => {
          console.error("오류:", error);
          document.getElementById("nicknameOutput").innerText =
            "오류 발생! 다시 시도하시오.";
        })
        .finally(() => {
          button.innerText = originalButtonText; // Revert button text to original
          button.disabled = false; // Re-enable button
        });
    });

  // 텍스트 입력 시 글자 수 제한
  document.getElementById("inputText").addEventListener("keyup", function () {
    var content = this.value;
    document.getElementById("counter").innerText =
      "(" + content.length + " / 최대 100자)"; // Update character count

    if (content.length > 100) {
      alert("최대 100자까지 입력 가능합니다.");
      this.value = content.substring(0, 100);
      document.getElementById("counter").innerText = "(100 / 최대 100자)";
    }
  });
});
