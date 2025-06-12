import requests
import os
from pathlib import Path

image_url = "https://p.aoe.top/cdn/tarot/images/{x}.webp"

# 定义所有需要下载的图片代码
image_codes = []
# 大阿卡纳牌 a1-a21
for i in range(1, 22):
    image_codes.append(f"a{i}")
# 小阿卡纳牌 - 权杖(w)、圣杯(c)、宝剑(s)、钱币(p) 各1-14
for prefix in ["w", "c", "s", "p"]:
    for i in range(1, 15):
        image_codes.append(f"{prefix}{i}")

# 确保目标目录存在
target_dir = Path("docs/public/images")
target_dir.mkdir(parents=True, exist_ok=True)

# 下载图片
for code in image_codes:
    url = image_url.format(x=code)
    filename = target_dir / f"{code}.webp"
    
    print(f"正在下载 {code}...")
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # 确保请求成功
        
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"已保存 {filename}")
    except Exception as e:
        print(f"下载 {code} 失败: {e}")

print(f"共下载了 {len(image_codes)} 张图片")