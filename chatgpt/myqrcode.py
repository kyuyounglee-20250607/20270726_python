import qrcode

def make_qr_code():
    # 사용자로부터 URL 입력받기
    url = input("QR 코드로 변환할 URL 주소를 입력하세요: ")

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
    filename = "my_qr_code.png"
    img.save(filename)

    print(f"✅ QR 코드가 생성되었습니다! 파일명: {filename}")

if __name__ == "__main__":
    make_qr_code()
