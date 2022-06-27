# 경제지표를 활용한 금값 예측

# directory
sc3
 ┣ .ipynb_checkpoints
 ┣ __pycache__
 ┃ ┗ modul.cpython-39.pyc
 ┣ goldprice
 ┃ ┣ .ipynb_checkpoints
 ┃ ┣ __pycache__
 ┃ ┃ ┗ __init__.cpython-39.pyc
 ┃ ┣ model
 ┃ ┃ ┗ model1.pkl
 ┃ ┣ templates
 ┃ ┃ ┣ .DS_Store
 ┃ ┃ ┣ main.html
 ┃ ┃ ┣ predict.html
 ┃ ┃ ┗ result.html
 ┃ ┣ views
 ┃ ┃ ┣ .ipynb_checkpoints
 ┃ ┃ ┣ __pycache__
 ┃ ┃ ┃ ┣ input_views.cpython-39.pyc
 ┃ ┃ ┃ ┣ main_views.cpython-39.pyc
 ┃ ┃ ┃ ┗ predict_views.cpython-39.pyc
 ┃ ┃ ┣ main_views.py
 ┃ ┃ ┗ predict_views.py
 ┃ ┣ .DS_Store
 ┃ ┣ __init__.py
 ┃ ┗ model1.pkl
 ┣ modeling
 ┃ ┣ .ipynb_checkpoints
 ┃ ┣ dataset
 ┃ ┃ ┣ date.csv
 ┃ ┃ ┣ modeldata.csv
 ┃ ┃ ┣ monthly.csv
 ┃ ┃ ┗ quarter.csv
 ┃ ┣ .DS_Store
 ┃ ┣ analysis.ipynb
 ┃ ┣ data.db
 ┃ ┣ dataload.ipynb
 ┃ ┣ model1.pickle
 ┃ ┗ modeling.ipynb
 ┣ .DS_Store
 ┣ .gitignore
 ┣ Procfile
 ┣ model1.pkl
 ┣ project3.key
 ┣ readme.md
 ┣ requirements.txt
 ┗ 나의 동영상 1.mp4
 
## 테이블 설명

### 금값
* gold
* date
* price (종가)

### 비트코인(원화)
* btc
* date
* price

## 각 인덱스
### 코스피
* kospi
* date
* price (종가)
### 코스닥
* kosdaq
* date
* price (종가)
### S&P500
* sp500
* date
* price (종가)
### 나스닥
* nasdaq
* date
* price
### 환율(원달러)
* exchangerate
* date
* price

## 지표
### 한국은행기준금리
* bok
* date
* price
