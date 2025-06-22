from ultralytics import YOLO
import cv2
import random

# 쓰레기 분류 기준
trash_class = {
    'radish_box': 'recycle',
    'chopstick': 'general',
    'spoon': 'general',
    'receipt': 'general',
    'can': 'recycle',
    'pet_bottle': 'recycle',
    'plastic_box': 'recycle',
    'plastic_bag': 'general',   # 오염 우려 시
    'paper_cup': 'general',     # 일반으로 보수적으로 분류
}

# 모델 로드
model = YOLO('runs/trash_exp1/weights/best.pt')

# 색상 설정
colors = {
    i: (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    for i in range(len(model.names))
}

# 웹캠 또는 IP Webcam 사용
# url = 'http://172.17.155.233:4747/video'
# cap = cv2.VideoCapture(url)
cap = cv2.VideoCapture(0)  # USB 웹캠일 경우

# 해상도 설정
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

if not cap.isOpened():
    print("웹캠 열기 실패")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("프레임 읽기 실패")
        break

    height, width, _ = frame.shape
    mid_x = width // 2

    # 예측
    results = model.predict(source=frame, conf=0.25, stream=True, verbose=False)

    for result in results:
        for box in result.boxes:
            cls_id = int(box.cls.item())
            label = model.names[cls_id]
            x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
            cx = (x1 + x2) // 2  # 중심 x좌표
            class_type = trash_class.get(label, 'unknown')

            # 기본 색상 및 메시지
            alert_color = (0, 255, 0)
            alert_text = "Good Job!"

            if cx < mid_x:
                # 왼쪽 (일반 쓰레기 영역)
                if class_type != 'general':
                    alert_color = (0, 0, 255)
                    alert_text = "Warning!"
            else:
                # 오른쪽 (재활용 영역)
                if class_type != 'recycle':
                    alert_color = (0, 0, 255)
                    alert_text = "Warning!"

            # 박스 및 라벨
            cv2.rectangle(frame, (x1, y1), (x2, y2), colors[cls_id], 2)
            cv2.putText(frame, label, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, colors[cls_id], 2)

            # 알림 메시지
            cv2.putText(frame, alert_text, (x1, y2 + 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, alert_color, 3)

    # 구역 선 표시
    cv2.line(frame, (mid_x, 0), (mid_x, height), (255, 255, 255), 2)
    cv2.putText(frame, "General", (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (200, 200, 200), 3)
    cv2.putText(frame, "Recycle", (mid_x + 50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (200, 200, 200), 3)

    cv2.imshow("YOLOv8 Trash Sorter", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
