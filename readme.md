# 🏠 Toch Project

**부동산 정보, 커뮤니티, 중고 거래 기능을 통합한 Django 기반 웹 애플리케이션**

---

## 📌 프로젝트 개요

**Toch**는 대학생들이 대학가 주변 원룸 매물을 탐색하고, 관심사를 공유하며, 안전하게 중고 물품을 거래할 수 있는 **종합 생활 플랫폼**입니다.  
대학생(특히 목포대학교)을 주요 대상으로 하며, 정보 공유의 단절 문제를 해결하고 신뢰 기반 커뮤니티를 지향합니다.



![메인화면 스크린샷](https://clyde0813.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Ff0ffea25-2718-4d2b-a987-bde651bde37d%2FUntitled.png?table=block&id=5049c3bd-95d5-433c-abdd-a720961d8f99&spaceId=357521ef-e3dc-432c-bc3c-174c72fd9911&width=660&userId=&cache=v2)

---

## 🛠️ 기술 스택

| 범주        | 스택 및 도구                  |
|-------------|------------------------------|
| Backend     | Django (Python)              |
| Frontend    | HTML, CSS, JavaScript        |
| DB          | MariaDB                      |
| 기타        | Docker, 이메일 발송 시스템 등 |

---

## 📁 프로젝트 구조

- `Toch/`: 프로젝트 설정 (settings, urls, wsgi 등)
- `common/`: 회원 관리, 로그인/로그아웃, 채팅 등 공통 기능
- `community/`: 커뮤니티 게시판 기능
- `oneroom/`: 원룸 매물 정보
- `usedtrade/`: 중고거래 기능
- `mobile/`: 모바일 전용 화면
- `templates/`, `static/`, `media/`: 템플릿, 정적 파일, 미디어 파일

---

## 🌐 주요 URL 경로

### ✅ 공통 (`common`)
- `/` : 메인 페이지
- `/login/`, `/signup/`, `/login/find/`
- `/mypage/info`, `/mypage/question`
- `/chat/`, `/community_chat/`, `/usedtrade_chat/`

### 📝 커뮤니티 (`community`)
- `/community/`
- `/community/detail/<int:pk>`

### 🏢 원룸 (`oneroom`)
- `/oneroom/`
- `/oneroom/detail/<int:pk>`

### 🔄 중고거래 (`usedtrade`)
- `/usedtrade/`
- `/usedtrade/detail/<int:pk>`
- `/usedtrade/create/`

### 📱 모바일 (`mobile`)
- `/mobile/`
- `/mobile/common/chat/`, `/chat_detail/`, `/login/`, `/mypage/`
- `/mobile/community/community/`, `/community_menu/`, `/community_write/`
- `/mobile/oneroom/oneroom/`, `/oneroom_detail/`, `/oneroom_edit/`, `/oneroom_forSale/`, `/oneroom_list/`, `/oneroom_review/`
- `/mobile/usedtrade/usedtrade/`, `/usedtrade_detail/`, `/usedtrade_write/`

---

## 🚀 실행 방법

1. **의존성 설치**
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **마이그레이션**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **서버 실행**
   ```bash
   python manage.py runserver
   # 또는 uwsgi 실행 (uwsgi.ini 참고)
   ```

4. **정적/미디어 파일 처리**
   ```bash
   python manage.py collectstatic
   ```

---

## 📦 기타 정보

- `Dockerfile` 및 `venvs/Toch.env`: Docker 환경 구성용
- `email_test.py`: 이메일 전송 테스트 스크립트
- `ip_gather.py`: 접속자 IP 수집용

---

## 📮 기여 및 문의

기여는 언제든 환영입니다.  
궁금한 점이나 버그 리포트는 [이슈 등록](https://github.com/clyde0813/Toch_Project/issues)을 통해 알려주세요.
