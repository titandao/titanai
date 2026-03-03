#!/usr/bin/env python3
"""
下载 TitanDAO 网站的所有远程资源到本地
"""
import os
import re
import urllib.request
import urllib.parse
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib

# 配置
PUBLIC_DIR = Path("/home/workspace/titanai/web/public")
ASSETS_DIR = PUBLIC_DIR / "assets"
MAX_WORKERS = 10

# 创建资源目录
for subdir in ["css", "js", "images", "media", "fonts"]:
    (ASSETS_DIR / subdir).mkdir(parents=True, exist_ok=True)

# 已下载的URL缓存
downloaded_urls = {}

def get_file_extension(url):
    """从URL获取文件扩展名"""
    parsed = urllib.parse.urlparse(url)
    path = parsed.path
    
    # 处理查询参数中的格式
    if '/v1/fill/' in url or 'format=' in url:
        if '.png' in url.lower():
            return '.png'
        elif '.jpg' in url.lower() or '.jpeg' in url.lower():
            return '.jpg'
        elif '.webp' in url.lower():
            return '.webp'
        elif '.svg' in url.lower():
            return '.svg'
    
    # 标准扩展名
    ext = Path(path).suffix
    if ext in ['.css', '.js', '.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp', '.woff', '.woff2', '.ttf', '.eot']:
        return ext
    
    # 根据内容类型猜测
    if '.css' in path:
        return '.css'
    elif '.js' in path:
        return '.js'
    
    return ''

def get_local_path(url):
    """获取本地存储路径"""
    # 根据URL类型确定子目录
    if '.css' in url.lower():
        subdir = 'css'
    elif '.js' in url.lower():
        subdir = 'js'
    elif any(ext in url.lower() for ext in ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp']):
        subdir = 'images'
    elif any(ext in url.lower() for ext in ['.woff', '.woff2', '.ttf', '.eot']):
        subdir = 'fonts'
    elif '/media/' in url:
        subdir = 'media'
    else:
        subdir = 'other'
    
    # 创建目录
    dir_path = ASSETS_DIR / subdir
    dir_path.mkdir(parents=True, exist_ok=True)
    
    # 使用URL哈希作为文件名，保留扩展名
    ext = get_file_extension(url)
    url_hash = hashlib.md5(url.encode()).hexdigest()[:12]
    filename = f"{url_hash}{ext}"
    
    return dir_path / filename, f"assets/{subdir}/{filename}"

def download_resource(url):
    """下载单个资源"""
    if url in downloaded_urls:
        return url, downloaded_urls[url], True
    
    try:
        # 处理URL中的特殊字符
        clean_url = url.replace('%7E', '~').replace('%2C', ',')
        
        local_path, local_url = get_local_path(url)
        
        # 如果文件已存在，跳过
        if local_path.exists():
            downloaded_urls[url] = local_url
            return url, local_url, True
        
        # 下载文件
        print(f"下载: {url[:80]}...")
        
        req = urllib.request.Request(clean_url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        
        with urllib.request.urlopen(req, timeout=30) as response:
            data = response.read()
            
            # 如果是CSS或JS，可能需要进一步处理
            with open(local_path, 'wb') as f:
                f.write(data)
        
        downloaded_urls[url] = local_url
        print(f"  ✓ 保存到: {local_url}")
        return url, local_url, True
        
    except Exception as e:
        print(f"  ✗ 失败: {e}")
        return url, None, False

def extract_urls_from_html(html_file):
    """从HTML文件提取所有远程URL"""
    with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # 匹配各种URL模式
    patterns = [
        r'https://static\.wixstatic\.com/[^"\'\s]+',
        r'https://static\.parastorage\.com/[^"\'\s]+',
        r'https://siteassets\.parastorage\.com/[^"\'\s]+',
        r'https://fonts\.googleapis\.com/[^"\'\s]+',
        r'https://fonts\.gstatic\.com/[^"\'\s]+',
    ]
    
    urls = set()
    for pattern in patterns:
        matches = re.findall(pattern, content)
        urls.update(matches)
    
    return list(urls)

def process_html_file(html_file):
    """处理单个HTML文件"""
    print(f"\n{'='*60}")
    print(f"处理文件: {html_file.name}")
    print('='*60)
    
    # 提取URL
    urls = extract_urls_from_html(html_file)
    print(f"发现 {len(urls)} 个远程资源")
    
    # 下载资源
    failed_count = 0
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(download_resource, url): url for url in urls}
        
        for future in as_completed(futures):
            url, local_url, success = future.result()
            if not success:
                failed_count += 1
    
    # 更新HTML文件
    with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    for url, local_url in downloaded_urls.items():
        if local_url:
            content = content.replace(url, local_url)
    
    # 保存更新后的HTML
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n✓ 完成: {html_file.name}")
    print(f"  成功: {len(downloaded_urls) - failed_count}")
    print(f"  失败: {failed_count}")

def main():
    """主函数"""
    print("="*60)
    print("TitanDAO 资源本地化工具")
    print("="*60)
    
    # 查找所有HTML文件
    html_files = list(PUBLIC_DIR.glob("*.html"))
    print(f"\n找到 {len(html_files)} 个HTML文件")
    
    # 处理每个文件
    for html_file in html_files:
        process_html_file(html_file)
    
    # 总结
    print("\n" + "="*60)
    print("处理完成！")
    print("="*60)
    print(f"总共下载: {len(downloaded_urls)} 个资源")
    print(f"资源目录: {ASSETS_DIR}")

if __name__ == "__main__":
    main()
