# 한글 텍스트를 음성(mp3)으로 변환하는 파이썬 프로그램

이 프로젝트는 사용자가 입력한 한글 문장을 mp3 음성 파일로 저장하고, 저장된 파일을 자동으로 재생하는 파이썬 예제입니다. 무료 라이브러리인 gTTS(Google Text-to-Speech)와 playsound를 사용합니다.

---

## 주요 기능
- 사용자가 입력한 한글 문장을 mp3 파일로 저장
- 저장된 mp3 파일을 자동으로 재생
- 초보자도 이해할 수 있도록 상세한 주석 포함

---

## 파일 목록
- `korean_tts.py` : 한글 텍스트를 음성으로 변환하고 재생하는 메인 파이썬 코드

---

## 라이브러리 설치 방법
아래 명령어를 터미널(명령 프롬프트, PowerShell 등)에 입력하여 필요한 라이브러리를 설치하세요.

```
conda run --name weekend_python pip install gtts playsound==1.2.2
```

> **참고:**
> - conda 환경을 사용하지 않는 경우, 일반적으로 `pip install gtts playsound==1.2.2` 명령어를 사용하면 됩니다.
> - Windows 환경에서는 playsound 1.2.2 버전이 mp3 재생에 가장 호환성이 좋습니다.

---

## 실행 방법
1. 터미널에서 프로젝트 폴더로 이동합니다.
   ```
   cd D:\copilot
   ```
2. 아래 명령어로 프로그램을 실행합니다.
   ```
   conda run --live-stream --name weekend_python python korean_tts.py
   ```
   또는(환경에 따라)
   ```
   python korean_tts.py
   ```
3. 안내에 따라 한글 문장을 입력하면, mp3 파일이 생성되고 자동으로 재생됩니다.

---

## 코드 예시
```python
from gtts import gTTS  # 텍스트를 음성으로 변환
from playsound import playsound  # mp3 파일을 재생
import os

text = input("음성으로 변환할 한글 문장을 입력하세요: ")
tts = gTTS(text=text, lang='ko')
filename = "output.mp3"
tts.save(filename)
print(f"음성 파일이 '{filename}'로 저장되었습니다.")
print("음성 파일을 재생합니다...")
playsound(filename)
# os.remove(filename)  # 재생 후 파일 삭제를 원하면 주석 해제
```

---

## 입력 및 실행 예시
```
음성으로 변환할 한글 문장을 입력하세요: 안녕하세요. 파이썬으로 한글을 음성으로 변환합니다.
음성 파일이 'output.mp3'로 저장되었습니다.
음성 파일을 재생합니다...
(입력한 문장이 음성으로 재생됨)
```

---

## 문의
추가적인 질문이나 개선 요청이 있으면 언제든 문의해 주세요!
