import os
import shutil
import subprocess
from dotenv import load_dotenv
from datetime import datetime
import random

load_dotenv()

# Cloudflare 설정
# .env 파일에 다음을 추가해야 합니다:
# CF_API_TOKEN=your_token
# CF_ACCOUNT_ID=your_account_id
# CF_API_TOKEN = os.getenv('CLOUDFLARE_API_TOKEN')
# CF_ACCOUNT_ID = os.getenv('CLOUDFLARE_ACCOUNT_ID')
# 구매하신 도메인을 여기에 입력하세요
your_domain = "housescares.com"

# 사용할 템플릿: layouts/_default/housecares.html
LAYOUT = "housecares2"
# 네이버 검색결과에 보일 사이트명 / 대표 이미지(og:image)
SITE_NAME = "홈케어"
OG_IMAGE = "/images/housecare/1.jpg"

# Cloudflare Pages 프로젝트명 (대시보드에서 미리 생성해둔 프로젝트명)
CF_PROJECT_NAME = ""

# headers = {"Authorization": f"Bearer {CF_API_TOKEN}", "Content-Type": "application/json"}

sites = [{"name": "doctor"}, {"name": "home"}, {"name": "cares"}]
categories = [
      {"category": "변기"}
    , {"category": "세면대"}
    , {"category": "수전"}
    , {"category": "배관"}
    , {"category": "싱크대"}
    , {"category": "하수구"}
    , {"category": "화장실"}
]
dos = ['막힘', '교체', '수리', '고장', '뚫음', '문제', '수리', '교체', '고장', '막힘']
titles = ['업체', '10곳 비교', '업체 리스트', '업체', '업체', '업체', '현금 영수증 가능한 곳', '비교', '리스트', '전문 업체', '서비스 업체']

with open('dong2.txt', 'r', encoding='utf-8') as f:
    regions = [line.strip() for line in f if line.strip()]

all_images = [f"/images/{i}.png" for i in range(1, 7)]

service_descriptions = {
    "변기": [
        "변기 막힘은 배관 내 이물질이 주원인입니다. 최신 장비로 막힘을 완벽하게 해결합니다.",
        "오래된 변기 부속품 교체로 물 내림 소음을 해결하고 수명을 늘려드립니다.",
        "변기 하단 누수나 흔들림은 즉시 보수하지 않으면 큰 피해를 줄 수 있습니다. 전문 수리팀이 대기 중입니다.",
        "변기 배관 악취 차단, 완벽한 시공으로 쾌적한 화장실 환경을 만들어 드립니다.",
        "최신형 절수형 변기 설치, 정직한 비용으로 도와드립니다.",
        "변기 문제 어떤 문제든 완벽하게 해결 해드립니다.",
        "각종 변기 막힘 문제 시원하게 해결 해드립니다",
        "휴지, 플라스틱, 장난감 등 변기에 빠진 각종 이물질 완벽 뚫음",
        "이물질로 인한 변기막힘 완벽 해결",
        "변기 문제 빠르게 해결 해드립니다.",
        "물을 내려도 수위가 천천히 빠진다면 변기 트랩 안쪽이 반쯤 막힌 상태일 수 있습니다.",
        "뚫어뻥으로도 해결되지 않는 변기 막힘은 스프링 장비로 트랩 깊숙한 곳까지 뚫어드립니다.",
        "변기 물탱크에서 물이 계속 흐르는 소리가 난다면 필밸브나 플러시밸브 점검이 필요합니다.",
        "변기 레버가 헛돌거나 물이 약하게 내려가는 증상, 부속 교체로 간단히 해결됩니다.",
        "물티슈와 생리대는 물에 풀리지 않아 변기 막힘의 대표적인 원인이 됩니다.",
        "변기 바닥 실리콘이 누렇게 변했다면 재시공으로 위생과 미관을 함께 잡을 수 있습니다.",
        "변기와 바닥 사이로 물이 스민다면 정화조 연결부 패킹 손상을 의심해 보셔야 합니다.",
        "아이가 장난감을 빠뜨린 변기도 변기를 탈거해 이물질을 직접 꺼내드립니다.",
        "변기 시트와 커버 교체, 비데 설치까지 한 번의 방문으로 처리해 드립니다.",
        "금이 간 변기는 갑자기 파손될 수 있어 빠른 교체를 권해드립니다.",
        "원피스 변기, 투피스 변기 등 욕실 구조에 맞는 제품으로 교체해 드립니다.",
        "변기 물이 넘칠 듯 차오른다면 더 이상 물을 내리지 마시고 바로 연락 주세요.",
        "변기 배수구에서 올라오는 냄새는 바닥 플랜지 밀착 불량이 원인인 경우가 많습니다.",
        "오래 사용한 변기 물탱크 부속을 일체형 부속으로 교체해 고장을 줄여드립니다.",
        "변기 고정 볼트가 헐거워져 흔들린다면 재고정 작업으로 안전하게 마무리합니다.",
        "변기 막힘 작업 후 물 내림 테스트를 여러 번 진행해 완전히 뚫린 것을 확인해 드립니다.",
        "고양이 모래나 음식물을 변기에 버리면 배관 안에서 굳어 심한 막힘을 일으킵니다.",
        "절수형 변기로 교체하면 한 번 물 내림에 쓰이는 물의 양을 줄일 수 있습니다.",
        "변기 하단 벽배수, 바닥배수 구조를 확인한 뒤 맞는 방식으로 시공해 드립니다.",
        "변기 물이 자꾸 저절로 내려간다면 물탱크 내부 고무패킹이 마모된 경우가 많습니다.",
        "상가 화장실 변기 막힘도 영업 시간에 지장이 없도록 신속하게 처리해 드립니다.",
        "변기 교체 시 기존 변기 철거와 폐기물 처리까지 함께 진행해 드립니다.",
        "화장실 리모델링 없이 변기만 새것으로 바꿔도 욕실 분위기가 확 달라집니다."
    ],
    "세면대": [
        "세면대 배수구 막힘, 머리카락과 이물질을 완벽히 제거합니다.",
        "세면대 수전에서 물이 샌다면 즉시 교체하세요. 고급 수전으로 깔끔하게 설치해 드립니다.",
        "세면대 하부 배관 부식 및 누수, 신속하고 정확하게 점검하여 수리합니다.",
        "세면대 팝업 및 트랩 교체, 물 빠짐이 시원하도록 해결합니다.",
        "세면대 벽면 타일 마감 보수 및 꼼꼼한 설치 서비스.",
        "세면대 고장 완벽 해결 해드립니다",
        "세면대 뚫음 문제 완벽 해결 해드립니다",
        "세면대 고장 문제 즉시 해결",
        "세면대 타일 보수 서비스",
        "세면대 고장 문제 바로 해결",
        "세면대 물이 고였다가 천천히 빠진다면 팝업 아래에 머리카락이 엉켜 있는 경우가 대부분입니다.",
        "세면대 S트랩, P트랩 교체로 배수 불량과 하수구 냄새를 함께 잡아드립니다.",
        "세면대가 벽에서 떨어질 듯 흔들린다면 고정 브라켓 보강이 필요합니다.",
        "금이 가거나 깨진 세면대는 날카로운 파편으로 다칠 수 있어 교체를 권해드립니다.",
        "탑볼 세면대, 반다리 세면대, 긴다리 세면대 등 원하시는 형태로 교체해 드립니다.",
        "세면대 하부장 안쪽이 젖어 있다면 배수 호스 연결부를 먼저 점검해야 합니다.",
        "치약 찌꺼기와 비누 때가 쌓이면 세면대 배수관이 점점 좁아집니다.",
        "세면대 팝업 버튼이 눌리지 않거나 내려가지 않는 고장도 부품 교체로 해결됩니다.",
        "세면대 오버플로우 구멍에서 냄새가 난다면 내부 청소와 점검이 필요합니다.",
        "세면대와 벽 사이 실리콘 틈으로 물이 스며들지 않도록 깔끔하게 재시공해 드립니다.",
        "세면대 교체와 함께 수전, 배수구, 트랩까지 새것으로 맞춰 설치할 수 있습니다.",
        "세면대 배수구에 반지나 귀걸이를 빠뜨렸다면 트랩을 분리해 찾아드립니다.",
        "오래된 세면대의 누런 물때는 세척으로도 한계가 있어 교체가 더 경제적일 수 있습니다.",
        "세면대 수도 밸브가 잠기지 않는다면 앵글밸브 교체가 함께 필요합니다.",
        "욕실 크기에 맞는 세면대 사이즈를 현장에서 측정한 뒤 추천해 드립니다.",
        "세면대 배관을 벽 안쪽까지 내시경으로 확인해 반복되는 막힘의 원인을 찾습니다.",
        "세면대 하부 배관 플렉시블 호스를 교체해 미세 누수를 예방해 드립니다.",
        "세면대 물이 역류해 올라온다면 공용 배관 쪽 막힘일 수 있어 정밀 점검이 필요합니다.",
        "세면대를 분리해야 하는 작업도 원래대로 깔끔하게 재설치해 드립니다.",
        "세면대 막힘 작업 후 물을 가득 채워 한 번에 빠지는지 직접 확인시켜 드립니다.",
        "상가, 사무실, 식당 화장실 세면대도 동일하게 출동해 작업해 드립니다."
    ],
    "수전": [
        "노후된 수전에서 발생하는 누수, 전문 기술로 완벽하게 해결합니다.",
        "주방 및 욕실 수전 교체, 최신 디자인으로 공간의 품격을 높여보세요.",
        "수전 호스 노후화, 수압 저하 등 다양한 문제를 정밀 점검합니다.",
        "수전 연결부 누수 차단 및 패킹 교체 전문.",
        "수전 연결부 수리 완벽하게 해드립니다.",
        "수전 문제가 악취로 이어집니다.",
        "수전 고장 신속하게 해결 해드립니다.",
        "수전 고장, 막힘, 뚫음 바로 해결 해드립니다.",
        "수전을 잠가도 물이 똑똑 떨어진다면 내부 카트리지 마모가 원인인 경우가 많습니다.",
        "냉수와 온수 조절이 잘 되지 않는 수전은 카트리지 교체로 해결할 수 있습니다.",
        "해바라기 샤워수전 설치로 욕실 샤워 환경을 시원하게 바꿔드립니다.",
        "주방 수전 헤드가 늘어나지 않거나 고정되지 않는다면 풀아웃 호스 교체가 필요합니다.",
        "벽 안쪽 수전 연결부에서 물이 샌다면 타일 아래 누수로 이어질 수 있어 빠른 조치가 필요합니다.",
        "욕조 수전, 샤워 수전, 세면대 수전 등 위치별로 맞는 제품을 추천해 드립니다.",
        "수전 토수구에 석회가 끼면 물줄기가 갈라지고 수압이 약해집니다.",
        "수전 레버가 뻑뻑하거나 헐거워졌다면 내부 부품이 마모된 신호입니다.",
        "수전 교체 시 앵글밸브와 연결 호스까지 함께 점검해 누수 위험을 줄여드립니다.",
        "녹물이 나오는 수전은 배관 상태까지 확인한 뒤 교체 여부를 안내해 드립니다.",
        "원홀, 투홀 등 기존 타공 구조에 맞춰 수전을 교체해 드립니다.",
        "샤워기 호스와 헤드 교체만으로도 수압 체감이 크게 달라질 수 있습니다.",
        "겨울철 동파로 갈라진 수전도 신속하게 교체해 드립니다.",
        "수전 아래 하부장이 젖어 있다면 냉온수 공급 호스 연결 상태를 점검해야 합니다.",
        "절수형 수전으로 교체하면 생활 속 물 사용량을 줄이는 데 도움이 됩니다.",
        "벽붙이형 주방 수전과 싱크대 상판형 수전 모두 시공 가능합니다.",
        "수전 교체 후 냉온수 방향과 누수 여부를 함께 확인한 뒤 마무리합니다.",
        "욕실 수전 교체로 오래된 욕실도 한결 깔끔한 분위기로 바뀝니다.",
        "온수가 늦게 나오는 문제는 수전보다 배관 쪽 점검이 필요한 경우도 있습니다.",
        "수전 고정 너트가 풀려 흔들리는 문제도 재고정으로 간단히 해결해 드립니다.",
        "식당, 카페 등 업소용 주방 수전 교체도 출동 가능합니다."
    ],
    "배관": [
        "배관 내 기름 슬러지 제거, 막힘 문제를 뿌리부터 뽑습니다.",
        "노후 배관 교체 및 점검, 아랫집 피해 예방을 위해 즉시 조치하세요.",
        "배관 악취의 원인, 배관 트랩 설치로 100% 차단해 드립니다.",
        "배관 누수 정밀 탐지, 최첨단 장비로 원인을 정확히 찾아 수리합니다.",
        "고압 세척을 통한 배관 내부 스케일링, 원활한 배수를 약속합니다.",
        "기름 슬러지가 악취의 원인입니다",
        "배관 빠르게 해결하지 않으면 악취의 원인 입니다.",
        "배관 내시경 카메라로 막힘 위치와 상태를 화면으로 직접 보여드립니다.",
        "오래된 아파트는 주방 공용 배관에 기름때가 쌓여 여러 세대가 함께 역류하기도 합니다.",
        "배관에서 꾸르륵 소리가 난다면 공기 흐름이 막혀 배수가 원활하지 않다는 신호입니다.",
        "아랫집 천장에 물 자국이 생겼다면 우리 집 배관 누수를 먼저 확인해야 합니다.",
        "철 배관은 오래되면 내부가 부식돼 녹물과 누수가 함께 생길 수 있습니다.",
        "PVC 배관 연결부가 빠지거나 갈라진 부분을 찾아 부분 교체로 보수해 드립니다.",
        "겨울철 동파된 배관은 해빙 작업 후 손상 부위를 확인해 보수합니다.",
        "배관 누수는 수도 계량기 확인만으로도 어느 정도 여부를 판단할 수 있습니다.",
        "배관 고압 세척은 배관 벽에 붙은 찌꺼기까지 씻어내 재발을 줄여줍니다.",
        "베란다 세탁기 배관에서 거품이 역류한다면 세제 찌꺼기가 쌓인 경우가 많습니다.",
        "식당과 상가 배관은 기름 사용량이 많아 정기적인 세척이 필요합니다.",
        "배관 교체 전 내시경 점검으로 꼭 필요한 구간만 교체해 비용을 줄여드립니다.",
        "바닥 아래 매립 배관 누수도 탐지 장비로 위치를 찾아 최소한으로 철거해 수리합니다.",
        "배관 연결부 보온재가 없으면 겨울철 동파 위험이 높아집니다.",
        "배관 막힘을 화학 약품으로만 해결하려 하면 배관이 손상될 수 있습니다.",
        "주택, 빌라, 아파트, 상가 등 건물 구조에 맞춰 배관 작업을 진행합니다.",
        "배관 작업 후 물을 충분히 흘려보내 배수가 원활한지 마지막까지 확인합니다.",
        "오래된 배관의 녹물은 수도 배관 교체나 세척으로 개선할 수 있습니다.",
        "배관에서 물 새는 소리가 들린다면 벽 안쪽 누수를 의심해 보셔야 합니다.",
        "배관 역류로 바닥이 젖었다면 추가 피해가 생기기 전에 바로 연락 주세요."
    ],
    "싱크대": [
        "싱크대 배수구 막힘은 음식물 찌꺼기가 원인인 경우가 많습니다. 전문가의 석션 작업으로 완벽하게 해결해 드립니다.",
        "오래된 싱크대 수전에서 누수가 발생한다면 교체가 정답입니다. 최신형 수전으로 깔끔하게 설치해 드립니다.",
        "싱크대 배관에서 올라오는 악취, 배관 트랩 설치만으로도 확실하게 차단할 수 있습니다.",
        "싱크대 하부장 누수는 아랫집 피해로 이어질 수 있습니다. 즉시 점검하여 원인을 찾아 수리합니다.",
        "싱크대 상판 코팅 및 수리, 낡은 주방을 새것처럼 복원하는 전문 기술력을 갖추고 있습니다.",
        "싱크대 막힘은 심각한 악취로 이어집니다.",
        "싱크대 문제는 배관에서 악취로 이어집니다. 확실하게 해결해 드립니다.",
        "설거지할 때 쓰는 기름이 배관 안에서 굳으면 싱크대 막힘의 주원인이 됩니다.",
        "싱크대 물이 천천히 빠진다면 배수 호스 안쪽에 음식물 찌꺼기가 쌓인 상태일 수 있습니다.",
        "싱크대 배수구 거름망과 배수 호스 교체로 냄새와 막힘을 함께 줄일 수 있습니다.",
        "음식물 분쇄기를 사용하는 싱크대는 배관에 찌꺼기가 쌓이기 쉬워 주기적 점검이 필요합니다.",
        "싱크대 하부장 바닥이 부풀었다면 오랫동안 물이 샌 흔적일 수 있습니다.",
        "싱크대 배수구와 상판 사이 실리콘을 새로 시공해 틈새 누수를 막아드립니다.",
        "싱크대 물을 내렸더니 옆집이나 베란다에서 물이 올라온다면 공용 배관 점검이 필요합니다.",
        "싱크대 배수 트랩을 교체하면 하수구 냄새가 주방으로 올라오는 것을 줄일 수 있습니다.",
        "아파트 저층 세대는 싱크대 역류가 자주 생길 수 있어 배관 세척이 도움이 됩니다.",
        "싱크대 수전 교체와 배수구 교체를 함께 진행하면 출동 비용을 한 번에 아낄 수 있습니다.",
        "싱크대 하부 배관이 흔들리거나 처져 있다면 연결부가 빠지기 전에 보강해야 합니다.",
        "싱크대 배수구 뚜껑과 거름망이 맞지 않는다면 규격에 맞는 제품으로 교체해 드립니다.",
        "뜨거운 물만 부어서는 싱크대 기름 막힘이 근본적으로 해결되지 않습니다.",
        "싱크대 막힘 작업 시 하부장 물건을 보호하고 작업 후 깔끔하게 정리해 드립니다.",
        "식당과 카페의 업소용 싱크대 막힘도 영업에 지장 없도록 빠르게 처리합니다.",
        "싱크대 배관 내시경 점검으로 막힌 위치를 정확히 찾아 필요한 구간만 작업합니다.",
        "싱크대 배수구에서 하수 냄새가 난다면 트랩 안에 고인 물이 말랐는지 확인해 보세요.",
        "싱크대 하부장에 습기가 차고 곰팡이가 핀다면 미세 누수를 의심해 봐야 합니다.",
        "커피 찌꺼기와 밥알도 싱크대 배관 안에 쌓이면 단단하게 굳어 막힘을 일으킵니다.",
        "싱크대 막힘이 반복된다면 배관 기울기 불량 여부까지 점검해 드립니다."
    ],
    "하수구": [
        "하수구 막힘의 주원인인 기름 슬러지와 머리카락을 고압 세척으로 말끔히 제거합니다.",
        "악취가 올라오는 하수구, 전용 트랩과 밀폐 시공으로 완벽하게 차단해 드립니다.",
        "오래된 하수구 배관의 노후 상태를 정밀 점검하고, 필요 시 부분 교체로 배수를 원활하게 합니다.",
        "화장실 및 베란다 하수구 역류 방지 장치 설치, 이제 물 넘침 걱정 없이 사용하세요.",
        "반복되는 하수구 막힘, 내시경 카메라를 통해 원인을 정확히 파악하고 근본적인 해결책을 제시합니다.",
        "막힌 하수구 신속하게 해결 해드립니다.",
        "욕실 바닥 하수구에 물이 고인다면 배수구 아래 머리카락 뭉치가 원인인 경우가 많습니다.",
        "베란다 하수구는 세탁기 배수와 빗물이 함께 흘러 막히기 쉬운 곳입니다.",
        "하수구 냄새가 밤에 더 심해진다면 트랩 봉수가 말라 냄새가 그대로 올라오는 상태일 수 있습니다.",
        "하수구 날파리가 계속 생긴다면 배수구 안쪽 오염물 청소와 트랩 교체가 필요합니다.",
        "하수구 뚜껑을 열기 어려운 구조도 전용 공구로 손상 없이 분리해 작업합니다.",
        "외부 맨홀과 연결된 하수구 막힘도 장비를 이용해 깊은 구간까지 뚫어드립니다.",
        "비가 많이 오는 날 하수구가 역류한다면 우수관과 오수관 연결 상태를 점검해야 합니다.",
        "하수구 막힘을 오래 방치하면 바닥 방수층이 손상돼 누수로 이어질 수 있습니다.",
        "상가 주방 하수구는 기름과 음식물이 쌓이기 쉬워 정기적인 고압 세척을 권해드립니다.",
        "하수구 배수구 커버를 냄새 차단형으로 교체하면 생활 악취를 크게 줄일 수 있습니다.",
        "하수구 막힘 작업 후 물을 충분히 흘려 배수가 시원하게 되는지 확인해 드립니다.",
        "주차장, 마당, 옥상 하수구 막힘도 출동해 처리해 드립니다.",
        "하수구에서 꾸르륵 소리가 나며 물이 올라온다면 배관 안쪽이 거의 막힌 상태입니다.",
        "하수구 막힘에 강한 약품을 반복해서 쓰면 배관이 상할 수 있어 주의가 필요합니다.",
        "하수구 배관 안쪽을 내시경으로 촬영해 막힘 원인을 사진으로 확인시켜 드립니다.",
        "오래된 주택 하수구는 배관 이음부가 벌어져 흙과 뿌리가 들어오는 경우도 있습니다.",
        "하수구 냄새 차단 트랩 설치는 짧은 시간에 끝나 생활 불편이 거의 없습니다.",
        "빌라 1층 하수구 역류는 건물 전체 배관과 연결돼 있어 정밀 점검이 필요합니다.",
        "하수구 청소와 함께 주변 실리콘과 줄눈 상태도 같이 확인해 드립니다."
    ],
    "화장실": [
        "화장실 전체 배수 불량 및 하수구 막힘, 전문 장비로 신속하게 해결해 드립니다.",
        "오래된 화장실 실리콘 재시공 및 줄눈 보수, 곰팡이 없는 쾌적한 공간으로 복원합니다.",
        "변기, 세면대, 수전 등 화장실 내 노후 부속품을 한 번에 점검하고 교체해 드립니다.",
        "화장실 타일 들뜸 및 파손 보수, 안전하고 깔끔하게 마무리해 드립니다.",
        "화장실에서 올라오는 원인 불명의 악취, 배관 및 환풍기 정밀 점검을 통해 원인을 뿌리 뽑습니다.",
        "화장실 악취, 집안 각종 악취로 이어집니다.",
        "모든 화장실 문제 빠르게 해결해드립니다.",
        "화장실 환풍기가 돌지 않거나 소음이 심하다면 모터 교체나 환풍기 교체가 필요합니다.",
        "화장실 천장에서 물이 떨어진다면 윗집 배관이나 방수층 문제일 수 있어 빠른 확인이 필요합니다.",
        "화장실 바닥 물빠짐이 나쁘면 바닥 구배 문제인지 배수구 막힘인지부터 확인합니다.",
        "화장실 줄눈이 검게 변했다면 줄눈 재시공으로 곰팡이와 물때를 한 번에 정리할 수 있습니다.",
        "욕조 배수구 막힘과 욕조 실리콘 보수도 함께 진행해 드립니다.",
        "화장실 문턱 아래로 물이 새어 나온다면 바닥 방수 상태 점검이 필요합니다.",
        "샤워부스 유리 실리콘이 떨어졌다면 물이 새기 전에 재시공하는 것이 좋습니다.",
        "화장실 수건걸이, 휴지걸이, 선반 등 욕실 액세서리 교체도 함께 가능합니다.",
        "화장실 리모델링 전에 배관 상태를 먼저 점검하면 공사 후 문제를 줄일 수 있습니다.",
        "아이와 어르신이 있는 집은 미끄럼 방지 시공과 안전 손잡이 설치를 함께 권해드립니다.",
        "화장실 배수구에서 냄새가 올라온다면 냄새 차단 트랩 설치만으로도 크게 개선됩니다.",
        "화장실 벽 타일 한 장이 깨졌다면 같은 규격 타일로 부분 교체가 가능합니다.",
        "화장실 곰팡이가 반복된다면 환기 상태와 실리콘 상태를 함께 점검해야 합니다.",
        "상가와 사무실 공용 화장실 막힘, 누수도 빠르게 출동해 처리합니다.",
        "화장실 작업 후 물을 직접 흘려보며 배수와 누수 여부를 최종 확인해 드립니다.",
        "오래된 화장실 문 손잡이와 경첩 교체도 함께 문의하실 수 있습니다.",
        "화장실 조명이 어둡다면 욕실 전용 방습 조명으로 교체해 드립니다.",
        "화장실 바닥 타일 들뜸은 아래쪽 누수 신호일 수 있어 그대로 두지 않는 것이 좋습니다.",
        "변기, 세면대, 샤워기 문제가 한꺼번에 있다면 한 번의 방문으로 모두 점검해 드립니다."
    ]
}


def get_service_description(category_string):
    for cat, desc in service_descriptions.items():
        if cat in category_string:
            return random.choice(desc)
    return ""


def get_random_category():
    return ", ".join([random.choice([c['category'] for c in categories]) + random.choice(dos) for _ in range(3)])


def get_category():
    return random.choice([c['category'] for c in categories]) + random.choice(dos)


def generate_random_body(region, category):
    return f"{region} {category} 전문 업체입니다. 24시 신속 출동 및 정직한 비용으로 해결해 드립니다."


def generate_random_title(region, category):
    return f"{region} {category} {random.choice(titles)}"


today_str = datetime.now().strftime("%Y-%m-%dT%H:%M:%S+09:00")


def prepare_content(content_dir, site):
    if os.path.exists(content_dir):
        shutil.rmtree(content_dir)
    os.makedirs(content_dir)
    file_name = f"{site}_{your_domain}.txt"
    captions = []
    # with open(file_name, "r", encoding="utf-8") as f:
        # captions = f.read().split(" ")


    region = '서울 특별시'
    cat = get_random_category()
    unique_body = generate_random_body(region, cat)
    summary = f"{region} {cat} 전문 업체입니다. 24시 신속 출동 및 정직한 비용으로 해결해 드립니다."
    selected_imgs = random.sample(all_images, 6)
    img_param = str(selected_imgs).replace("'", '"')
    # index 파일 생성
    index_path = os.path.join(content_dir, "_index.md")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(f'''---
title: "{region} {cat} 전문 업체 홈케어"
description: "{summary}"
region: "{region}"
category: "{cat}"
date: {today_str}
unique_body: "{unique_body}"
images: {img_param}
id: "0"
layout: "{LAYOUT}"
site_name: "{SITE_NAME}"
og_image: "{OG_IMAGE}"
---
''')
        f.write("\n### 📍 추천 서비스 지역\n")
        for i, reg in enumerate(random.sample(regions, min(20, len(regions)))):
            f.write(f"[{reg}](/{regions.index(reg) + 1}/)  \n")

    counter = 1

    for i in range(1, 7):
        for region in regions:
            check = True
            unique_title = ''
            unique_body = ''
            summary = ''
            category = ''

            while check:
                category = get_category()
                summary = f"{region} {category} 전문 업체입니다. 24시 신속 출동 및 정직한 비용으로 해결해 드립니다."
                unique_title = generate_random_title(region, category)
                unique_body = generate_random_body(region, category)
                if unique_title not in captions:
                    captions.append(unique_title)
                    check = False

            cat1 = get_random_category()
            cat2 = get_random_category()
            cat3 = get_random_category()
            cat4 = get_random_category()
            cat5 = get_random_category()

            # 서비스별 설명 추출
            sink_desc = get_service_description("싱크대") if "싱크대" in category else ""
            sujun_desc = get_service_description("수전") if "수전" in category else ""
            byeongi_desc = get_service_description("변기") if "변기" in category else ""
            semyondae_desc = get_service_description("세면대") if "세면대" in category else ""
            baegwan_desc = get_service_description("배관") if "배관" in category else ""
            hasu_desc = get_service_description("하수구") if "하수구" in category else ""
            hwajang_Desc = get_service_description("화장실") if "화장실" in category else ""

            selected_imgs = random.sample(all_images, 6)
            img_param = str(selected_imgs).replace("'", '"')

            # individual markdown 파일 생성
            file_path = os.path.join(content_dir, f"{counter}.md")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(f'''---
title: "{unique_title}"
description: "{summary}"
region: "{region}"
category: "{category}"
date: {today_str}
images: {img_param}
id: "{counter}"
layout: "{LAYOUT}"
site_name: "{SITE_NAME}"
og_image: "{OG_IMAGE}"
unique_body: "{unique_body}"
sink_description: "{sink_desc}"
sujun_description: "{sujun_desc}"
byeongi_description: "{byeongi_desc}"
semyondae_description: "{semyondae_desc}"
baegwan_description: "{baegwan_desc}"
hasu_desc: "{hasu_desc}"
hwajang_Desc: "{hwajang_Desc}"
cat1: "{cat1}"
cat2: "{cat2}"
cat3: "{cat3}"
cat4: "{cat4}"
cat5: "{cat5}"
---
''')
            counter += 1

            # with open(file_name, "w", encoding="utf-8") as f:
            #     f.write("\n".join(captions))  # \n 은 줄바꿈(엔터)입니다.


def deploy_to_cloudflare(site_name, content_dir, output_dir):
    print(f"\n--- 🚀 [{site_name}] Pages 배포 시작 ---")
    try:
        target_url = f"https://{site_name}.{your_domain}"

        cmd = f'hugo -c "{content_dir}" -b "{target_url}" --destination "{output_dir}" --cleanDestinationDir'
        subprocess.run(cmd, shell=True, check=True)
        print(f"✅ [{site_name}] 빌드 성공: {target_url} (소스: {content_dir} -> 출력: {output_dir})")

        cmd_deploy = f"wrangler pages deploy {output_dir} --project-name={site_name}"
        subprocess.run(cmd_deploy, shell=True, check=True)
        print(f"✅ [{site_name}] 배포 성공: {target_url}")
    except Exception as e:
        print(f"❌ 배포/빌드 실패: {e}")


def deploy():
    for site in sites:
        site_name = site['name']
        content_dir = f"content_{site_name}_{your_domain}"
        output_dir = f"public_{site_name}_{your_domain}"

        prepare_content(content_dir, site_name)

        deploy_to_cloudflare(site_name, content_dir, output_dir)
        # cmd_deploy = f"rmdir /s /q {content_dir}"
        # subprocess.run(cmd_deploy, shell=True, check=True)
        # cmd_deploy = f"rmdir /s /q {output_dir}"
        # subprocess.run(cmd_deploy, shell=True, check=True)


if __name__ == "__main__":
    deploy()
