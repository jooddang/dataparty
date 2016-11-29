# Data Party

데이터 포트럭 파티 스터디 그룹 (가칭) 리포지토리입니다.
참여를 원하시는 분은 아래 페이스북 그룹에 가입해 주세요.

 * [페이스북 페이지][fb-potluck]

## 목적

기계학습, 딥러닝 등에 관심은 있으나 어디에서부터 시작할지 모르는 분들끼리 모여, 서로의 학습 데이터를 공유하고 서로의 문제에 관심을 가지며 함께 공부해 봅시다.

## 준비물

 * Github 계정
 * Python3
   * 이제 2016년이니까요
 * 서로에 대한 따뜻한 관심

## 규칙

 * numpy, matplotlib 사용을 권장드립니다.
 * 데이터는 numpy에서 쉽게 읽을 수 있는 포맷으로 만들어 주세요.
   * CSV 좋아요
   * tar.gz 로 압축된 png/jpg + json 형태도 괜찮습니다.
 * 데이터에 대한 간략한 설명을 markdown (.md) 형태로 남겨주세요.
 * 데이터를 시각화할 수 있는 간단한 스크립트를 만들어주셔도 좋습니다.
   * Jupyter Notebook 좋아요.
 * 10MB 가 넘어가는 큰 파일은 드롭박스나 구글 드라이브에 올려주시고 공유 링크나 다운로드 스크립트를 만들어 주세요.
 * 학습 프레임워크는 Tensorflow, Keras, Caffe, Theano 등을 자유롭게 쓰셔도 괜찮습니다.

 * 배경 지식이 서로 다른 분들이 모여 있으니 서로서로 격려하고 배려해 주세요.

## 디렉토리 구조

 * 아래와 같은 형태의 디렉토리에 데이터 또는 데이터 생성 프로그램을 만들어 주세요.
  * `dataparty/[year]/[data_provider_id]/[dataset_name]`
  * 예:
    * `dataparty/2016/j6lim/sine_1d`,
    * `dataparty/2016/j6lim/sine_2d`
  * 만약 프로그램이 큰 경우 본인 github repository에 올려주시고 링크를 `README.md` 에 올려주세요.
 * 솔루션은 아래 디렉토리에 올려주세요.
  * `dataparty/[year]/[data_provider_id]/[dataset_name]/[solver_id]`
  * 예:
    * `dataparty/2016/j6lim/sine_1d/silvergo`

[fb-potluck]: https://www.facebook.com/groups/datapotluckparty/
