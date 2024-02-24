
const express = require('express');
const { spawn } = require("child_process");
const app = express();
const port = 3000;

app.use(express.json());

app.use(express.static(".")); // 현재 디렉토리를 정적 파일 디렉토리로 사용


app.post("/", (req, res) => {
  //이름과 문장을 받아서 닉네임 생성

  const { name, sentence } = req.body;

  const pythonProcess = spawn("python3", [
    "nickname_generator.py",
    name, sentence,
  ]);


  let outputData = '';
  pythonProcess.stdout.on("data", (data) => {
    outputData += data.toString();
    console.log(`stdout: ${data}`);
  });

  pythonProcess.on("close", (code) => {
    console.log(`Child process exited with code ${code}`);
    if (code === 0) { // Check if the child process exited successfully
      console.log('outputData:', outputData);
      res.json({ nickname: outputData.trim() }); // Send the nickname as a response
    } else {
      console.error('Error generating nickname');
      res.status(500).send("Error generating nickname");
    }
  });

  pythonProcess.stderr.on("data", (data) => {
    console.error(`stderr: ${data.toString()}`);
  });
});


app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});
