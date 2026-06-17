import os
import shutil
import subprocess
import requests
from dotenv import load_dotenv
from datetime import datetime
import random

load_dotenv()
headers = {"Authorization": f"Bearer {os.getenv('NETLIFY_TOKEN')}"}

sites = [{"name": "hasugu-care"}, {"name": "semun-care"}, {"name": "sujun-care"}]
categories = [{"category": "변기"}, {"category": "세면대"}, {"category": "수전"}, {"category": "배관"}, {"category": "싱크대"},
              {"category": "하수구"},
              {"category": "화장실"}]
dos = ['막힘', '교체', '수리', '고장', '뚫음']
titles = ['업체', '10곳 비교', '업체 리스트', '비용', '저렴한 곳']

with open('dong.txt.new', 'r', encoding='utf-8') as f:
    regions = [line.strip() for line in f if line.strip()]

all_images = [f"/images/{i}.png" for i in range(1, 7)]

service_descriptions = {
    "변기": [
        "변기 막힘은 배관 내 이물질이 주원인입니다. 최신 장비로 막힘을 완벽하게 해결합니다.",
        "오래된 변기 부속품 교체로 물 내림 소음을 해결하고 수명을 늘려드립니다.",
        "변기 하단 누수나 흔들림은 즉시 보수하지 않으면 큰 피해를 줄 수 있습니다. 전문 수리팀이 대기 중입니다.",
        "변기 배관 악취 차단, 완벽한 시공으로 쾌적한 화장실 환경을 만들어 드립니다.",
        "최신형 절수형 변기 설치, 정직한 비용으로 도와드립니다."
    ],
    "세면대": [
        "세면대 배수구 막힘, 머리카락과 이물질을 완벽히 제거합니다.",
        "세면대 수전에서 물이 샌다면 즉시 교체하세요. 고급 수전으로 깔끔하게 설치해 드립니다.",
        "세면대 하부 배관 부식 및 누수, 신속하고 정확하게 점검하여 수리합니다.",
        "세면대 팝업 및 트랩 교체, 물 빠짐이 시원하도록 해결합니다.",
        "세면대 벽면 타일 마감 보수 및 꼼꼼한 설치 서비스."
    ],
    "수전": [
        "노후된 수전에서 발생하는 누수, 전문 기술로 완벽하게 해결합니다.",
        "주방 및 욕실 수전 교체, 최신 디자인으로 공간의 품격을 높여보세요.",
        "수전 호스 노후화, 수압 저하 등 다양한 문제를 정밀 점검합니다.",
        "수전 연결부 누수 차단 및 패킹 교체 전문.",
        "수전 고정 불량 및 흔들림, 기초부터 튼튼하게 다시 설치합니다."
    ],
    "배관": [
        "배관 내 기름 슬러지 제거, 막힘 문제를 뿌리부터 뽑습니다.",
        "노후 배관 교체 및 점검, 아랫집 피해 예방을 위해 즉시 조치하세요.",
        "배관 악취의 원인, 배관 트랩 설치로 100% 차단해 드립니다.",
        "배관 누수 정밀 탐지, 최첨단 장비로 원인을 정확히 찾아 수리합니다.",
        "고압 세척을 통한 배관 내부 스케일링, 원활한 배수를 약속합니다."
    ],
    "싱크대": [
        "싱크대 배수구 막힘은 음식물 찌꺼기가 원인인 경우가 많습니다. 전문가의 석션 작업으로 완벽하게 해결해 드립니다.",
        "오래된 싱크대 수전에서 누수가 발생한다면 교체가 정답입니다. 최신형 수전으로 깔끔하게 설치해 드립니다.",
        "싱크대 배관에서 올라오는 악취, 배관 트랩 설치만으로도 확실하게 차단할 수 있습니다.",
        "싱크대 하부장 누수는 아랫집 피해로 이어질 수 있습니다. 즉시 점검하여 원인을 찾아 수리합니다.",
        "싱크대 상판 코팅 및 수리, 낡은 주방을 새것처럼 복원하는 전문 기술력을 갖추고 있습니다."
    ],
    "하수구": [
        "하수구 막힘의 주원인인 기름 슬러지와 머리카락을 고압 세척으로 말끔히 제거합니다.",
        "악취가 올라오는 하수구, 전용 트랩과 밀폐 시공으로 완벽하게 차단해 드립니다.",
        "오래된 하수구 배관의 노후 상태를 정밀 점검하고, 필요 시 부분 교체로 배수를 원활하게 합니다.",
        "화장실 및 베란다 하수구 역류 방지 장치 설치, 이제 물 넘침 걱정 없이 사용하세요.",
        "반복되는 하수구 막힘, 내시경 카메라를 통해 원인을 정확히 파악하고 근본적인 해결책을 제시합니다."
    ],
    "화장실": [
        "화장실 전체 배수 불량 및 하수구 막힘, 전문 장비로 신속하게 해결해 드립니다.",
        "오래된 화장실 실리콘 재시공 및 줄눈 보수, 곰팡이 없는 쾌적한 공간으로 복원합니다.",
        "변기, 세면대, 수전 등 화장실 내 노후 부속품을 한 번에 점검하고 교체해 드립니다.",
        "화장실 타일 들뜸 및 파손 보수, 안전하고 깔끔하게 마무리해 드립니다.",
        "화장실에서 올라오는 원인 불명의 악취, 배관 및 환풍기 정밀 점검을 통해 원인을 뿌리 뽑습니다."
    ]

}


def get_service_description(category_string):
    for cat, descs in service_descriptions.items():
        if cat in category_string:
            return random.choice(descs)
    return ""


def get_random_category():
    return ", ".join([random.choice([c['category'] for c in categories]) + random.choice(dos) for _ in range(3)])


def generate_random_body(region, category):
    return f"{region} {category} 전문 업체입니다. 24시 신속 출동 및 정직한 비용으로 해결해 드립니다."


def generate_random_title(region, category):
    return f"{region} {category} {random.choice(titles)}"


today_str = datetime.now().strftime("%Y-%m-%dT%H:%M:%S+09:00")


def get_content_html(title, region, cat, body, naver_map, google_map):
    img = random.choice(all_images)
    return f'''{{{{< rawhtml >}}}}
<div style="border: 2px solid #3498db; padding: 20px; border-radius: 10px; background-color: #f9f9f9; text-align: center;">
    <h1 style="color: #2c3e50;">{title}</h1>
    <div style="margin: 20px 0;"><img src="{img}" alt="서비스" style="max-width: 100%; height: auto; border-radius: 10px;"></div>
    <div style="padding: 15px; background: #e1f5fe; border-left: 5px solid #03a9f4; margin: 15px 0;">
        <p><strong>주요 서비스:</strong> {cat}</p>
        <p><strong>지역:</strong> {region}</p>
        <p>{body}</p>
    </div>
    <div style="margin-top: 20px;">
        <a href="{naver_map}" target="_blank" style="background:#03c75a; color:white; padding:10px 20px; text-decoration:none; border-radius:5px; margin:5px; display:inline-block;">네이버 지도</a>
        <a href="{google_map}" target="_blank" style="background:#4285f4; color:white; padding:10px 20px; text-decoration:none; border-radius:5px; margin:5px; display:inline-block;">구글 지도</a>
    </div>
</div>
{{{{< /rawhtml >}}}}
'''


def prepare_content(num, images_str):
    if os.path.exists("content"): shutil.rmtree("content")
    os.makedirs("content")

    region = '서울 특별시'
    cat = get_random_category()
    unique_body = generate_random_body(region, cat)
    summary = f"{region} {cat} 전문 업체입니다. 24시 신속 출동 및 정직한 비용으로 해결해 드립니다."
    selected_imgs = random.sample(all_images, 6)
    img_param = str(selected_imgs).replace("'", '"')
    with open("content/_index.md", "w", encoding="utf-8") as f:
        f.write(f'''---
title: "{region} {cat} 전문 업체 홈케어"
description: "{summary}"
region: "{region}"
category: "{cat}"
date: {today_str}
unique_body: "{unique_body}"
images: {img_param}
id: "0"
layout: "index"
---
''')
        f.write("\n### 📍 추천 서비스 지역\n")
        for i, reg in enumerate(random.sample(regions, min(20, len(regions)))):
            f.write(f"[{reg}](/{regions.index(reg) + 1}/)  \n")

    counter = 1
    for region in regions:
        category = get_random_category()
        summary = f"{region} {category} 전문 업체입니다. 24시 신속 출동 및 정직한 비용으로 해결해 드립니다."
        unique_title = generate_random_title(region, category)
        unique_body = generate_random_body(region, category)

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

        with open(f"content/{counter}.md", "w", encoding="utf-8") as f:
            f.write(f'''---
title: "{unique_title}"
description: "{summary}"
region: "{region}"
category: "{category}"
date: {today_str}
images: {img_param}
id: "{counter}"
unique_body: "{unique_body}"
sink_description: "{sink_desc}"
sujun_description: "{sujun_desc}"
byeongi_description: "{byeongi_desc}"
semyondae_description: "{semyondae_desc}"
baegwan_description: "{baegwan_desc}"
hasu_desc: "{hasu_desc}"
hwajang_Desc: "{hwajang_Desc}"
---
''')
        counter += 1


def deploy_all():
    for i, site in enumerate(sites, start=1):
        site_name = site['name']
        print(f"\n--- 🚀 [{site_name}] 배포 프로세스 시작 ---")
        output_dir = f"public_{site_name}"
        prepare_content(i, "")
        subprocess.run(f'hugo -b "https://{site_name}.netlify.app/" --destination {output_dir} --cleanDestinationDir',
                       shell=True, check=True)

        if os.path.exists(f"{output_dir}/sitemap.xml"):
            with open(f"{output_dir}/sitemap.xml", 'r', encoding='utf-8') as f:
                content = f.read()
            idx = content.find('<?xml')
            if idx != -1:
                with open(f"{output_dir}/sitemap.xml", 'w', encoding='utf-8') as f:
                    f.write(content[idx:].strip())

        try:
            res = requests.post("https://api.netlify.com/api/v1/sites", headers=headers, json={"name": site_name})
            site_id = res.json().get('id') if res.status_code == 200 else next(
                s['id'] for s in requests.get("https://api.netlify.com/api/v1/sites", headers=headers).json() if
                s['name'] == site_name)
            subprocess.run(["netlify", "deploy", "--prod", "--dir", output_dir, "--site", site_id], shell=True,
                           check=True)
            print(f"✅ {site_name} 배포 완료!")
        except Exception as e:
            print(f"❌ 배포 실패: {e}")


if __name__ == "__main__":
    deploy_all()
