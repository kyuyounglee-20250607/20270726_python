# 필요한 라이브러리 불러오기
from gtts import gTTS  # 텍스트를 음성으로 변환
from playsound import playsound  # mp3 파일을 재생
import os

# 입력 파일에서 텍스트 읽기
input_file = "input.txt"
try:
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()
    print(f"'{input_file}' 파일에서 다음 내용을 읽었습니다:")
    print("-" * 50)
    print(text)
    print("-" * 50)
except FileNotFoundError:
    print(f"'{input_file}' 파일을 찾을 수 없습니다.")
    exit(1)

# gTTS 객체 생성 (lang='ko'는 한국어 설정)
tts = gTTS(text=text, lang='ko')

# mp3 파일로 저장
filename = "output.mp3"
tts.save(filename)
print(f"음성 파일이 '{filename}'로 저장되었습니다.")

# 저장된 mp3 파일 재생
print("음성 파일을 재생합니다...")
playsound(filename)

# (선택) 재생 후 파일 삭제를 원하면 아래 주석을 해제하세요
# os.remove(filename)
