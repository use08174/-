const express = require('express');
const app = express();
const port = 3000;

app.use(express.static('.')); // 현재 디렉토리를 정적 파일 디렉토리로 사용

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});
