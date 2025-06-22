from ultralytics import YOLO

if __name__ == '__main__':
    # 모델 선택 (성능을 원하면 s 또는 m 사용)
    model = YOLO('yolov8s.pt')  # 또는 'yolov8m.pt'

    # 모델 학습
    model.train(
        data='dataset/data.yaml',  # 데이터셋 경로
        epochs=100,                # epoch 수 증가
        imgsz=640,                 # 이미지 크기
        batch=8,                   # GPU 메모리에 따라 조절
        patience=10,               # 조기 종료 기준
        degrees=10,                # 회전 증강
        scale=0.5,                 # 스케일 증강
        shear=2.0,                 # 기울이기
        perspective=0.0005,        # 원근 왜곡
        flipud=0.2,                # 상하 반전
        mosaic=1.0,                # 모자이크 적용
        mixup=0.2,                 # MixUp 적용
        project='runs',            # 결과 저장 폴더
        name='trash_exp1',         # 실험 이름
        pretrained=True,           # 전이 학습 (기본값 True)
        verbose=True,              # 학습 로그 출력
        workers=4,                 # 데이터 로더 워커 수 (속도 향상)
    )
