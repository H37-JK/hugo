import os
import shutil
import subprocess
from dotenv import load_dotenv
from datetime import datetime
import random

load_dotenv()

your_domain = "housescares.com"
sites = [{"name": "seoul"}, {"name": "paju"}, {"name": "gyungi"}]
categories = [
    {"category": "변기"},
    {"category": "세면대"},
    {"category": "수전"},
    {"category": "배관"},
    {"category": "싱크대"},
    {"category": "하수구"},
    {"category": "화장실"}
]
dos = ['막힘', '교체', '수리', '고장', '뚫음']
titles = ['업체', '10곳 비교', '업체 리스트', '업체', '업체', '업체']

if os.path.exists('dong2.txt'):
    with open('dong2.txt', 'r', encoding='utf-8') as f:
        regions = [line.strip() for line in f if line.strip()]
else:
    regions = ['경기도 파주시']

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
        "휴지, 플라스틱, 장난감 등 변기에 빠진 각종 이물지 완벽 뚫음",
        "이물질로 인한 변기막힘 완벽 해결",
        "변기 문제 빠르게 해결 해드립니다."
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
        "세면대 고장 문제 바로 해결"
    ],
    "수전": [
        "노후된 수전에서 발생하는 누수, 전문 기술로 완벽하게 해결합니다.",
        "주방 및 욕실 수전 교체, 최신 디자인으로 공간의 품격을 높여보세요.",
        "수전 호스 노후화, 수압 저하 등 다양한 문제를 정밀 점검합니다.",
        "수전 연결부 누수 차단 및 패킹 교체 전문.",
        "수전 연결부 수리 완벽게 해드립니다.",
        "수전 문제가 악취로 이어집니다.",
        "수전 고장 신속하게 해결 해드립니다.",
        "수전 고장, 막힘, 뚫음 바로 해결 해드립니다."
    ],
    "배관": [
        "배관 내 기름 슬러지 제거, 막힘 문제를 뿌리부터 뽑습니다.",
        "노후 배관 교체 및 점검, 아윗집 피해 예방을 위해 즉시 조치하세요.",
        "배관 악취의 원인, 배관 트랩 설치로 100% 차단해 드립니다.",
        "배관 누수 정밀 탐지, 최첨단 장비로 원인을 정확히 찾아 수리합니다.",
        "고압 세척을 통한 배관 내부 스케일링, 원활한 배수를 약속합니다.",
        "기름 슬러지가 악취의 원인입니다"
        "배관 빠르게 해결하지 않으면 악치의 원인 입니다."
    ],
    "싱크대": [
        "싱크대 배수구 막힘은 음식물 찌꺼기가 원인인 경우가 많습니다. 전문가의 석션 작업으로 완벽하게 해결해 드립니다.",
        "오래된 싱크대 수전에서 누수가 발생한다면 교체가 정답입니다. 최신형 수전으로 깔끔하게 설치해 드립니다.",
        "싱크대 배관에서 올라오는 악취, 배관 트랩 설치만으로도 확실하게 차단할 수 있습니다.",
        "싱크대 하부장 누수는 아랫집 피해로 이어질 수 있습니다. 즉시 점검하여 원인을 찾아 수리합니다.",
        "싱크대 상판 코팅 및 수리, 낡은 주방을 새것처럼 복원하는 전문 기술력을 갖추고 있습니다.",
        "싱크대 막힘은 심각한 악취로 이어집니다.",
        "싱크대 문제는 배관에서 악취로 이어집니다. 확실하게 해결해 드립니다."
    ],
    "하수구": [
        "하수구 막힘의 주원인인 기름 슬러지와 머리카락을 고압 세척으로 말끔히 제거합니다.",
        "악취가 올라오는 하수구, 전용 트랩과 밀폐 시공으로 완벽하게 차단해 드립니다.",
        "오래된 하수구 배관의 노후 상태를 정밀 점검하고, 필요 시 부분 교체로 배수를 원활하게 합니다.",
        "화장실 및 베란다 하수구 역류 방지 장치 설치, 이제 물 넘침 걱정 없이 사용하세요.",
        "반복되는 하수구 막힘, 내시경 카메라를 통해 원인을 정확히 파악하고 근본적인 해결책을 제시합니다.",
        "막힌 하수구 신속하게 해결 해드립니다."
    ],
    "화장실": [
        "화장실 전체 배수 불량 및 하수구 막힘, 전문 장비로 신속하게 해결해 드립니다.",
        "오래된 화장실 실리콘 재시공 및 줄눈 보수, 곰팡이 없는 쾌적한 공간으로 복원합니다.",
        "변기, 세면대, 수전 등 화장실 내 노후 부속품을 한 번에 점검하고 교체해 드립니다.",
        "화장실 타일 들뜸 및 파손 보수, 안전하고 깔끔하게 마무리해 드립니다.",
        "화장실에서 올라오는 원인 불명의 악취, 배관 및 환풍기 정밀 점검을 통해 원인을 뿌리 뽑습니다.",
        "화장실 악취, 집안 각종 악취로 이어집니다.",
        "모든 화장실 문제 빠르게 해결해드립니다."
    ]
}

today_str = datetime.now().strftime("%Y-%m-%dT%H:%M:%S+09:00")


def get_service_description(category_service):
    for category, description in service_descriptions.items():
        if category in category_service:
            return random.choice(description)
    return ""


def get_category_list():
    return ", ".join([random.choice([c['category'] for c in categories]) + random.choice(dos) for _ in range(3)])


def get_category():
    return random.choice([c['category'] for c in categories]) + random.choice(dos)


def get_random_body(region, category):
    return f"{region} {category} 서비스 전문 업체 싹뚫어 입니다! 24시간 무료 상담 가능 합니다!"


def get_random_title(region, category):
    return f"{region} {category} {random.choice(titles)}"


def prepare_content(content_dir):
    if os.path.exists(content_dir):
        shutil.rmtree(content_dir)
    os.makedirs(content_dir)

    captions = []

    region = '경기도 파주시'
    category = get_category_list()
    title = f"{region} {category} 싹뚫어"
    body = get_random_body(region, category)
    description = get_random_body(region, category)
    selected_images = random.sample(all_images, 6)
    images = str(selected_images).replace("'", '"')

    # index 파일 생성
    index_path = os.path.join(content_dir, "_index.md")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(f'''---
title: "{title}"
description: "{description}"
region: "{region}"
category: "{category}"
date: "{today_str}"
unique_body: "{body}"
images: {images}
id: "0"
layout: "index"
---
''')

    counter = 1

    for i in range(1, 4):
        for reg in regions:
            check = True
            title = ''
            body = ''
            cat = ''

            while check:
                cat = get_category()
                body = get_random_body(reg, cat)
                title = get_random_title(reg, cat)
                if title not in captions:
                    captions.append(title)
                    check = False

            category1 = get_category_list()
            category2 = get_category_list()
            category3 = get_category_list()
            category4 = get_category_list()
            category5 = get_category_list()

            sink_desc = get_service_description("싱크대") if "싱크대" in cat else ""
            sink_desc2 = get_service_description("싱크대") if "싱크대" in cat else ""
            sink_desc3 = get_service_description("싱크대") if "싱크대" in cat else ""
            sujun_desc = get_service_description("수전") if "수전" in cat else ""
            sujun_desc2 = get_service_description("수전") if "수전" in cat else ""
            sujun_desc3 = get_service_description("수전") if "수전" in cat else ""
            byeongi_desc = get_service_description("변기") if "변기" in cat else ""
            byeongi_desc2 = get_service_description("변기") if "변기" in cat else ""
            byeongi_desc3 = get_service_description("변기") if "변기" in cat else ""
            semyondae_desc = get_service_description("세면대") if "세면대" in cat else ""
            semyondae_desc2 = get_service_description("세면대") if "세면대" in cat else ""
            semyondae_desc3 = get_service_description("세면대") if "세면대" in cat else ""
            baegwan_desc = get_service_description("배관") if "배관" in cat else ""
            baegwan_desc2 = get_service_description("배관") if "배관" in cat else ""
            baegwan_desc3 = get_service_description("배관") if "배관" in cat else ""
            hasu_desc = get_service_description("하수구") if "하수구" in cat else ""
            hasu_desc2 = get_service_description("하수구") if "하수구" in cat else ""
            hasu_desc3 = get_service_description("하수구") if "하수구" in cat else ""
            hwajang_desc = get_service_description("화장실") if "화장실" in cat else ""
            hwajang_desc2 = get_service_description("화장실") if "화장실" in cat else ""
            hwajang_desc3 = get_service_description("화장실") if "화장실" in cat else ""

            # individual markdown 파일 생성
            file_path = os.path.join(content_dir, f"{counter}.md")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(f'''---
title: "{title}"
description: "{body}"
region: "{reg}"
category: "{cat}"
date: "{today_str}"
unique_body: "{body}"
images: {images}
sink_description: "{sink_desc}"
sink_description3: "{sink_desc2}"
sink_description2: "{sink_desc3}"
sujun_description: "{sujun_desc}"
sujun_description2: "{sujun_desc2}"
sujun_description3: "{sujun_desc3}"
byeongi_description: "{byeongi_desc}"
byeongi_description2: "{byeongi_desc2}"
byeongi_description3: "{byeongi_desc3}"
semyondae_description: "{semyondae_desc}"
semyondae_description2: "{semyondae_desc2}"
semyondae_description3: "{semyondae_desc3}"
baegwan_description: "{baegwan_desc}"
baegwan_description2: "{baegwan_desc2}"
baegwan_description3: "{baegwan_desc3}"
hasu_desc: "{hasu_desc}"
hasu_desc2: "{hasu_desc2}"
hasu_desc3: "{hasu_desc3}"
hwajang_Desc: "{hwajang_desc}"
hwajang_Desc2: "{hwajang_desc2}"
hwajang_Desc3: "{hwajang_desc3}"
cat1: "{category1}"
cat2: "{category2}"
cat3: "{category3}"
cat4: "{category4}"
cat5: "{category5}"
---
''')
            counter += 1


def deploy_to_cloudflare(site_name, content_dir, output_dir):
    print(f"\n--- 🚀 [{site_name}] Pages 배포 시작 ---")
    try:
        target_url = f"https://{site_name}.{your_domain}"

        cmd = f'hugo -c "{content_dir}" -b "{target_url}" --destination "{output_dir}" --cleanDestinationDir'
        subprocess.run(cmd, shell=True, check=True)
        print(f"✅ [{site_name}] 빌드 성공: {target_url} (소스: {content_dir} -> 출력: {output_dir})")

        # cmd_deploy = f"wrangler pages deploy {output_dir} --project-name={site_name}"
        # subprocess.run(cmd_deploy, shell=True, check=True)
        # print(f"✅ [{site_name}] 배포 성공: {target_url}")
    except Exception as e:
        print(f"❌ 배포/빌드 실패: {e}")


def deploy():
    for site in sites:
        site_name = site['name']
        content_dir = f"content_{site_name}"
        output_dir = f"public_{site_name}"

        prepare_content(content_dir)

        deploy_to_cloudflare(site_name, content_dir, output_dir)


if __name__ == "__main__":
    deploy()