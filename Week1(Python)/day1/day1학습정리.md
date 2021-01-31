## day1 학습정리

- 구글 colab 사용법 

### < 중요 기능 >
<br/>
-- 셀 추가 관련 단축키
    
    1.코드 셀 위에 삽입(ctrl + M A)

    2.코드 셀 아래에 삽입(ctrl + M B)

    3.코드 셀 삭제(ctrl + M D)

-- 셀 타입 변경 단축키

    1. 코드 셀로 변경(ctrl + M Y)

    2. 마크다운 셀로 변경(ctrl + M Y)

-- 셀 실행 관련 단축키

    1. 해상 셀을 실행하고 커서는 해당 셀 (ctrl + Enter)

    2. 해당 셀은 실행하고 커서는 다음 셀 (Shift + Enter)

    3. 해당 셀을 실행하고 커서는 다음셀에 삽입 (Alt + Enter)

<br/>

### <파일 업로드>

1. 직접 업로드 하기
```
from google.colab import files
myfile = files.upload()
```

2. 드라이브에서 가져오기
```
from google.colab import drive
drive.mount('/content/drive')
filenames = '파일경로'
data = pd.read_csv(filenames)
```

<br/>

< github과 연동 >
<br/>
실행하고자하는 ipynb파일의 url을 복사 -> github.com 을 github으로 변경 -> colab.research.google.com을 맨 앞에 추가 
