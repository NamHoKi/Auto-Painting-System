# __Capstone-Desige__
----------
## __Object__
#### 자동 채색 프로그램
##### 이미지 전처리
##### 이미지 인식
##### 이미지 자동 채색
----------
## __Step__
#### 1. 이미지 전처리 - 여백 자르기
#### 2. 이미지 색 채우기 - 객체내부 색 채우기
----------
### 1. 이미지 전처리
#### 필요없는 여백 자르기
![1](https://user-images.githubusercontent.com/48282708/75118676-76cb5200-56bf-11ea-82ce-bb8d468d6616.png)
----------
### 2. 이미지 색 채우기
#### + 끊긴 부분이 있을 수도 있으니 전처리후 팽창
![apple1](https://user-images.githubusercontent.com/48282708/74900788-2e244800-53e4-11ea-8063-cbb9bb2f296a.png)
#### + 닫힌 객체 내부 채우기
![result](https://user-images.githubusercontent.com/48282708/74900790-2fee0b80-53e4-11ea-9145-e73a55ea7d6a.png)
#### + 내부 채운 부분을 RGB로 변환
![1](https://user-images.githubusercontent.com/48282708/74938640-bf6ddb80-5431-11ea-89d9-4d8d2384621d.png)
----------
### 3. Segmentation
#### 영역 구분 후 영역 개수로 색 정하고 색칠
#### + 영역 개수 <= 5
![ap](https://user-images.githubusercontent.com/48282708/75381892-ebe79300-591c-11ea-8351-aeadca8e5f81.png)
![ch](https://user-images.githubusercontent.com/48282708/75381896-ed18c000-591c-11ea-853b-630de44beb17.png)
#### + 영역 개수 > 5
![g](https://user-images.githubusercontent.com/48282708/75381890-eb4efc80-591c-11ea-8bf7-3708da3a0706.png)
----------
