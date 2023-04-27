# kosmos-backend
강화학습을 활용한 밀집 군중 제어 서비스, 코스모스(KOSMOS, Keep Own Space Make Our Space) | Backend Repository

2022년 이태원 참사와 같은 수많은 사상자를 내는 압사사고는 주로 방향 안내가 없고 인파가 극도로 몰려 보행 흐름이 무너지게 되는 군중 난류 현상 때문에 발생합니다.
본 논문에서는 군중난류를 해결하는 서비스인 KOSMOS를 제시하여 시민들의 이동을 효율적으로 개선하고자 합니다.


2022 Korea Science Engineering Fair Invention 분야 은상 수상작입니다.  
2023 EUCYS (European Union Contest for Young Scientists) 대회 한국대표단 선정작입니다.

## API 사용 방법

REST API 형식으로 API 주소( https://api.kosmos.dohui.me )에 API Request를 보내면 실행 결과가 반환됩니다.

### 도로 좌표 데이터 불러오기

`/roadPath` Path로 `POST` 형식으로 Request를 보내면 좌표 데이터가 반환됩니다.

Request 형식
```json
{
  "location": [],  /* 도로 데이터를 불러올 범위의 중심 좌표 ex) [37.53545, 126.99311] */
  "distance": 500 /* 도로 데이터를 불러올 범위 크기 */
}
```

 
 Response 형식
 ```json
{
  "edge": [[145327, 148321145], [145327, 10024226633]],  /* 도로 단위를 구성하는 좌표점의 ID */
  "edge_geometry": {"145327-148321145": [[4.3591456, 50.8459793], []]},  /* 도로 단위의 곡선 좌표 데이터 (존재할경우) */
  "node": [[4.3591456, 50.8459793], []]  /* 도로 단위를 구성하는 좌표점의 좌표 데이터 */
}
```
  - Status Code: `200` - 정상
