"""edu_success_demo: 수업용 성공 메시지 데모 라이브러리."""

from .install import check_install
from .run import run_demo, cleanup

# import 시 안내 메시지 (데모용 — 실제 프로젝트에서는 보통 로깅을 사용)
print("[edu-success-demo] 라이브러리가 로드되었습니다. (import 성공)")