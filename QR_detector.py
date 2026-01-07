import cv2
import webbrowser

cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()

opened_links = set()

while True:
    ret, frame = cap.read()
    data, _, _ = detector.detectAndDecode(frame)

    if data:
        if data not in opened_links:
            print(f"Found new link: {data}")
            webbrowser.open(data)
            opened_links.add(data)

        cv2.putText(frame, data, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("QR Code Reader", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()