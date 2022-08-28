# 자가진단 자동화
셀레니움 사용

## 사용법
1. https://chromedriver.chromium.org/downloads 에서 자신의 크롬 버젼에 맞는 크롬 드라이버를 다운로드 후 같은 폴더 경로에 넣는다.
2. main.py를 실행한다.

## config.json 작성법.

School: 학교 풀네임 (ex. 영광고등학교)  
City: 시/도
```
01 = 서울특별시
02 = 부산광역시
03 = 대구광역시
04 = 인천광역시
05 = 광주광역시
06 = 대전광역시
07 = 울산광역시
09 = 없음
08 = 세종특별자치시
10 = 경기도
11 = 강원도
12 = 충청북도
13 = 충청남도
14 = 전라북도
15 = 전라남도
16 = 경상북도
17 = 경상남도
18 = 제주특별자치도
```
Level: 학교급
```
1 = 유치원
2 = 초등학교
3 = 중학교
4 = 고등학교
4 = 특수학교 등.
```
User:  
    name: 이름  
    birthday: 생년월일(YYMMDD)  
    password: 자가진단 비밀번호 4자리  

## To-do

#### 1.등록된 모든 사람 자가진단.
#### 2.잘못된 학교 이름 등 예외처리.
-----
#### Developed by. Lee hyowon (https://github.com/leehyowon14)
##### Email. dev.leehyowon14@gmail.com