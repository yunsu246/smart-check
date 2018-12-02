## Project Info
 1. 이름: Smart Check
 2. 내용 : Blockchain을 활용한 출결관리 dApp
    - 핵심기능
      - Smart Contract를 활용한 _출석부_ 생성 및 관리
      - 수업별 출결 현황 조회 
      - 참여자별 해당 수업에 대한 출석여부 확인  
    - 구현형태 : Hybrid App
    - 주요 리소스 및 아키텍쳐
      - Front-End : Vue.js, OnsenUI 
      - Back-End : Web3, Flask(Python) 
      - 이외: AWS, Docker
    - 블록체인 네트워크 구성
      - Network type : Private Network(KALEIDO)
      - Consensus algorithm : PoA
      - Core : [go-ethereum](https://github.com/ethereum/go-ethereum)


## Build Setup

``` bash
# install dependencies
yarn install

# serve with hot reload at localhost:7000
yarn run dev

# build for production with minification
yarn run build
```

## Licensing

[MIT License](LICENSE.md)
