# edu-success-demo

수업 시간에 **라이브러리 설치 → import → 함수 실행**의 기본 흐름을 보여주기 위한 초간단 데모 패키지입니다.

- 설치 확인, 함수 실행, 정리 단계마다 `"...에 성공하였습니다!"` 메시지를 출력합니다.
- 가이드: 깃허브에 올린 다음 Colab에서 `pip install`로 설치해 사용하세요.

## ✅ 빠른 시작 (Colab)
```python
# 1) GitHub에서 설치
!pip install git+https://github.com/yourname/edu_success_demo.git@v0.1.0

# 2) import (가져오기)
import edu_success_demo  # import 시 안내 메시지 출력

# 3) 설치 확인
edu_success_demo.check_install()

# 4) 데모 함수 실행
edu_success_demo.run_demo("첫 실행")

# 5) 정리
edu_success_demo.cleanup()
```

## 🧱 제공 함수
```python
edu_success_demo.check_install()   # 설치 확인
edu_success_demo.run_demo(name)    # 데모 실행
edu_success_demo.cleanup()         # 마무리
```

## 📦 버전 고정 설치 예시
```python
!pip install git+https://github.com/yourname/edu_success_demo.git@v0.1.0
```

## 🐍 로컬 설치(선택)
```bash
pip install -e .
```

## 라이선스
MIT