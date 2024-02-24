
const express = require('express');
const { spawn } = require("child_process");
const app = express();
const port = 3000;

app.use(express.json());

app.use(express.static(".")); // 현재 디렉토리를 정적 파일 디렉토리로 사용

app.post("/", (req, res) => {
  //이름과 문장을 받아서 닉네임 생성
  console.log(req.body);
  const { name, sentence } = req.body;

  const pythonProcess = spawn("python3", [
    "nickname_generator.py",
    name, sentence,
  ]);

  pythonProcess.stdout.on("data", (data) => {
    console.log(`stdout: ${data}`);
    const response = JSON.parse(data);
    res.json(response);
  });

  pythonProcess.stderr.on("data", (data) => {
    console.error(`stderr: ${data}`);
    res.status(500).send("Error generating nickname");
  });

  pythonProcess.on("close", (code) => {
    console.log(`Child process exited with code ${code}`);
  });
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});
