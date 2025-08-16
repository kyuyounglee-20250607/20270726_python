import cv2

def read_qr_code_opencv():
    filename = input("읽을 QR 코드 이미지 파일명 입력: ")
    img = cv2.imread(filename)
    if img is None:
        print("❌ 이미지 파일을 찾을 수 없습니다.")
        return

    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(img)
    if data:
        print(f"✅ QR 코드 내용: {data}")
    else:
        print("❌ QR 코드를 찾을 수 없습니다.")

if __name__ == "__main__":
    read_qr_code_opencv()
