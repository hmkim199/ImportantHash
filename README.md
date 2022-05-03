# 중요해시_백엔드
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

 ## 프로젝트 구조도
 - [프로젝트 구조도 이미지](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/610c6ffc-9b7b-4fe9-9b82-197a0126709b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220503%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220503T123240Z&X-Amz-Expires=86400&X-Amz-Signature=cb83971ec4d39a88ef21e01dd47c32cb15d40d1bfc3d5fffa249ff0eb2ab41a0&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)
 
 ## 와이어프레임
 - [Figma 링크](https://www.figma.com/file/nHD2ULiwSqMcPQFeEZk3Pr/%EC%98%A4%EB%A6%AC%EB%84%88%EA%B5%AC%EB%A6%AC?node-id=0%3A1)
 
 ## ER-Diagram
 - [ER-Diagram 이미지](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/dd2b5b31-f72a-4cec-b3c7-0a52a743db05/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220503%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220503T123323Z&X-Amz-Expires=86400&X-Amz-Signature=2d1ffa8af548991a390170609d801885376f358cbc9feb76b4b897ee31522a16&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)
 
# **기능 설명**

## 서비스의 핵심 기능과 구현 방법

→ 핵심 기능은 유튜브 링크를 삽입하면 해당 영상의 스크립트(대본)를 분석하여 키워드를 뽑아내고 타임라인별 중요도를 시각화하는 기능입니다. 사용자가 입력한 유튜브 영상의 타임라인 별 스크립트를 가져와서, hanspell 라이브러리로 자동 맞춤법 교정하여 보다 정확한 스크립트를 만들어 냅니다. 그 결과를 다시 KR-WordRank AI모델을 사용하여 키워드와 키워드 별 중요도를 뽑아내고, 결과를 종합하여 타임라인별 중요도를 만들어 보여줍니다.

## 어려웠던 점과 해결 방법

### 1) 프론트엔드

1. **TypeScript와 Tailwind CSS**
: TypeScript와 Tailwind CSS를 처음 사용해 보았기 때문에 초반 러닝 커브가 있었으나 공식 문서를 통해 검색하며 익혀나가면서 개발을 진행했습니다.
2. **그래프 선정, 겹쳐보이는 문제**
: 기존에 시간에 따른 중요도를 시각화하기 위해 사용했던 Nivo의 그래프는 타임 라인이 겹쳐 보이는 이슈가 있었습니다. 해결 방법을 모색 중, 좀 더 자료를 찾아보며 Recharts로 라이브러리를 바꾸면서 이슈를 해결할 수 있었습니다.

### 2) 백엔드

1. **SQLite -> MySQL**
:  'default': (2002, "Can't connect to local MySQL server through socket '/var/run/mysqld/mysqld.sock' (2)") 오류가 나서 해결하기 어려웠습니다.  
    
    → WSL을 쓰고 있었던 점을 간과해서 발생한 문제였고, WSL 환경에서 MySQL을 설치했더니 간단하게 해결되었습니다. 이 일을 겪은 후 에러가 발생했을 때 검색하기 이전에 메시지를 더 자세히 읽어보는 습관을 가질 수 있었습니다.
    
2. **Nginx, Gunicorn 적용**
: 적용이 오류 문구 없이 마무리 되었는데, 설정해 준 API로 접근했을 때 제대로 요청이 가지 않는 문제가 있었습니다. 
    
    → 이는 nginx.conf 파일과 default 설정 파일이 충돌해서 생긴 문제였음을 알게 되어 default 파일 include문은 주석 처리하여 해결했습니다.
    
    → 하지만 AI 모델을 돌리는 과정에서 시간이 오래 걸리다 보니, 배포 VM 사양 문제인지 504 timeout 에러가 종종 발생하여 일단 개발 서버로 5000번 포트에 배포하였고 이를 해결하기 위해 자료 조사 중입니다.
    
3. **JWT 적용**
    
    : 처음에는 JWT의 개념과 적용에 대해 잘 알지 못해서 사용하는 데에 조금 어려움을 겪었습니다. 예전에는 세션 방식으로 로그인 처리를 하였지만, stateless 방식을 사용하기 위해 JWT를 적용해보았습니다. 처음이라 어려운 부분이 다소 있었지만 강의 자료나 여러 공식 문서 등을 찾아보면서 대략적인 개념을 익힐 수 있었고 팀원들끼리 모르는 부분을 공유하고 현직 코치님께 조언을 구하여 해결할 수 있었습니다.
    

### 3) AI

1. **AI 모델 결정.**
어떤 AI 모델이 적합한지 결정해보기 위해서는 여러 모델들을 테스트 해봐야 했었는데 시간이 부족해 비지도학습 방식으로 결정했었습니다. 결과적으로 원하는 결과를 얻을 수 있었으나 다양한 AI 모델을 살펴본다면 좀 더 정확도가 높을 결과를 얻을 수 있지 않았을까 싶습니다.
2. **환경 문제**
다양한 모델과 라이브러리를 적용하기 위해서 환경 구축이 필요했는데, 사용 중인 개발 환경의 문제로 사용해보지 못한 라이브러리가 많습니다. 혼자 진행하다보니 당장 개발 환경을 개선할 수 없어 다양한 라이브러리를 사용하지 못해서 아쉬웠습니다.
