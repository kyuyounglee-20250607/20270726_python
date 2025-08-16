# GQ 코드만드는 프로그램이 한개의  url로 한개의 qr 코드만드는 걸 응용해서
# 여러개의 url로 여러개의 qr 코드를 만드는 프로그램으로 확장한 것
# 이 프로그램은 여러개의 url을 리스트로 입력받아 각각의 qr 코드를 생성합니다.
# 입력은 url 리스트로, 출력은 각 url에 해당하는 qr 코드 이미지 파일리스트
QR_LISTS = ['www.daum.net','www.naver.com','www.youtube.com']
QR_IMG_LISTS = ['daum.png','naver.png','youtube.png']


import qrcode

def make_qr_code(url,i):    

    # QR 코드 생성
    qr = qrcode.QRCode(
        version=1,  # QR 코드 크기 (1~40, 숫자가 클수록 큼)
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # 오류 보정 수준
        box_size=10,  # QR코드 네모 하나의 크기
        border=4,  # 테두리 두께
    )
    qr.add_data(url)   # 데이터(여기서는 URL) 추가
    qr.make(fit=True)

    # QR 코드 이미지 생성
    img = qr.make_image(fill_color="black", back_color="white")

    # 파일 저장
    filename = QR_IMG_LISTS[i]
    img.save(filename)

    print(f"✅ QR 코드가 생성되었습니다! 파일명: {filename}")


for i,url in enumerate(QR_LISTS):
    make_qr_code(url,i)