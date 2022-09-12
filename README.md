# 중요해시
- 유튜브 링크를 넣으면 스크립트(대본)을 만들어 주고, 스크립트에서 주요 키워드를 분석한 후 타임라인에 따른 중요도를 시각화해주는 서비스입니다.

## 기획 의도

→ 현대 사회에서는 많은 정보를 쉽게 접할 수 있습니다. 이에 사람들은 피로를 느끼기도 하고 핵심만 간단히, 빠르게 알고 싶어합니다. 많은 사람들이 유튜브 영상이나 강의 영상을 시청할 때 배속 기능을 활용하는 이유라고 생각합니다. 그렇기 때문에 사람들에게 영상 속에서 **중요한 키워드나 중요한 타임라인**을 빠르게 확인할 수 있는 서비스를 구상했습니다.
# 3. **기술 스택**

## 1) Frontend

- React
- Typescript
- Tailwind CSS
- Nginx
- Axios
- Nivo line

## 2) Backend

- **Python**
- **Django Rest Framework (API Server)**
- **simple-jwt (Login)**
- **Swagger(drf-yasg) (API 명세)**
- **MySQL (RDBMS) → 배포용**
- **SQLite (RDBMS) → 개발용**
- **Nginx (Web Server)**
- **Gunicorn (Web Application Server)**
- **Azure VM (infra)**

## 3) AI

- Python
- pytube
- kr-workrank
- youtube transcript api
- hanspell spell checker

# 각 팀원의 역할과 기여한 부분

## **김혜민**

- **백엔드**
- DRF로 Video 관련 Restful API CRUD 구현
- 테스트 코드 작성
- Azure VM에 배포
- SQLite(개발용) → MySQL(배포용) DBMS 전환 작업
- AI 코드 모듈화하여 백엔드에 삽입
- DB 설계, ERD 작성
- drf-yasg 이용 Swagger 설정
- Postman으로 API 테스트
- Gunicorn과 Nginx를 이용한 배포작업

## 김형석

- **프론트엔드/팀장**
- typescript, react, tailwind css 이용하여 전체 페이지 구현
- 타임라인에 따른 중요도 그래프 nivo line 이용하여 구현
- 와이어프레임 작성
- 스크럼과 미팅 진행, 기록

## 진병수

- **백엔드**
- 모델 설계 및 적용
- JWT 적용 및 Postman을 이용한 API테스트
- Gunicorn과 Nginx를 이용한 배포작업
- drf-yasg 이용 Swagger 설정

## 김정인

- **AI**
- 불용어 데이터 전처리
- 맞춤법 검사 자동화(hanspell spell checker)
- AI 모델(kr-workrank) 이용 키워드 분석 알고리즘 적용

 ## 와이어프레임
 - [Figma 링크](https://www.figma.com/file/nHD2ULiwSqMcPQFeEZk3Pr/%EC%98%A4%EB%A6%AC%EB%84%88%EA%B5%AC%EB%A6%AC?node-id=0%3A1)
 
 
# **기능 설명**

## 서비스의 핵심 기능과 구현 방법

→ 핵심 기능은 유튜브 링크를 삽입하면 해당 영상의 스크립트(대본)를 분석하여 키워드를 뽑아내고 타임라인별 중요도를 시각화하는 기능입니다. 사용자가 입력한 유튜브 영상의 타임라인 별 스크립트를 가져와서, hanspell 라이브러리로 자동 맞춤법 교정하여 보다 정확한 스크립트를 만들어 냅니다. 그 결과를 다시 KR-WordRank AI모델을 사용하여 키워드와 키워드 별 중요도를 뽑아내고, 결과를 종합하여 타임라인별 중요도를 만들어 보여줍니다.
