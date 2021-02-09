# TEAM AGEOSTE 🐊
#### 2021.01.11 ~ 2021.01.22
안녕하세요, [lacoste](https://www.lacoste.com/kr/) 사이트의 클론 코딩 프로젝트를 진행하게 된 Team AGEOSTE(아거스테🐊) 입니다. 녹빛의 악어 모양 로고로 유명한 Lacoste 는 1933년 테니스 선수 르네 라코스트에 의해 설립된 프랑스의 패션 브랜드입니다. 클래식하면서도 캐쥬얼한 이미지의 스포츠 웨어들을 판매하며, 해당 사이트에서는 라코스테의 제품들을 컬러별, 테마별로 분류하여 게시해두고 있습니다. 약 2주간의 기간동안 초기 세팅부터 디자인, 회원가입/로그인/장바구니 를 포함한 기본적인 기능은 UI 까지 연결하여 전부 구현하였으나 검색/필터/리뷰 등의 기능은 시간 상 기능만 구현해두고 연결로는 이어지지 못했습니다.

## Preview
[![team ageoste](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/6fb92acc-8aed-4aff-a694-d4ee043e8028/Group_95_%281%29.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210124T084056Z&X-Amz-Expires=86400&X-Amz-Signature=cbc165403752a589df75b54c1cdbf7d5c5f3625e30a6acf2b46bd009bf4b4e66&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Group_95_%281%29.png%22)](https://youtu.be/AaLQSa29Ias)
##### 이미지를 클릭하면 영상으로 이동됩니다.

## Member 🕺🏻 <br>
### Front <a href="https://github.com/wecode-bootcamp-korea/AGEOSTE-frontend"> git repo </a> <br>
유재현 <a href="https://github.com/JaehyunYoo"> git repo </a> // 박영호 <a href="https://github.com/youngho052"> git repo </a> <br>
### Back <a href="https://github.com/wecode-bootcamp-korea/AGEOSTE-backend"> git repo</a> <br>
장진욱 <a href="https://github.com/jinukix"> git repo </a> <a href="https://velog.io/@jinukix/2차-프로젝트-후기">review</a> <br>
최수아 <a href="https://github.com/sue517"> git repo</a> <a href="https://velog.io/@sue517/1%EC%B0%A8-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%ED%9B%84%EA%B8%B0"> review </a> <br>

## Back Technologies 🛠
- Python
- Django
- MySQL
- AWS EC2, RDS, S3
- Docker

## Progress ⛓
- <a href="https://trello.com/b/IIL6vdmM/%F0%9D%92%9C%F0%9D%91%94%F0%9D%91%92%F0%9D%91%9C%F0%9D%93%88%F0%9D%93%89%F0%9D%91%92"> TEAM Trello </a> <br>
trello 를 이용하여 서로간의 진행 상황을 공유할 수 있도록 하였습니다. trello 는 front / back / 공통 의 부분으로 나누어져 구분되어 있으며, 진행중인 사항에도 내부에 check list 를 달아 보다 더 상세한 진행 사항을 표시해 두었습니다.
- <a href="https://www.notion.so/team-AGEOSTE-Json-b6664ee5935746b3a61e8a4a6e68c592"> API document notion </a> <br>
front / back 간의 의사 소통을 수월히 하기 위하여 Json API document 를 만들어 공유하였습니다. 

## Modeling 📑
<img src="https://media.vlpt.us/images/sue517/post/8ac3296a-f516-48cf-9203-2cf9c2b4d77b/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-01-12%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%207.24.11.png">

## Functions 🔍
- 회원가입 (using validators)
- bcrypt 를 이용한 비밀번호 암호화
- JWT 를 이용하여 access token 발행
- 로그인 (using validators) // decorator 생성
- 마이페이지 read & update
- smtp 를 이용한 이메일 인증 구현
- kakao 소셜 로그인 기능 구현

- 상품 리스트, 상세 페이지 뷰
- 상품 검색, 필터
- 상품 리뷰, 댓글
- DB 업로드 작성 

- 장바구니 기능
- 배송지 read & update 기능 구현

## Reference 

- 이 프로젝트는 [lacoste](https://www.lacoste.com/kr/) 사이트를 참조하여 학습목적으로 만들었습니다.
- 실무수준의 프로젝트이지만 학습용으로 만들었기 때문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다.
- 이 프로젝트에서 사용하고 있는 사진 대부분은 위코드에서 구매한 것이므로 해당 프로젝트 외부인이 사용할 수 없습니다.
