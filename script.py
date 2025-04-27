import os
import re

def convert_to_markdown_format(text):
    """将文本转换为指定的Markdown格式"""
    
    # 将指定标题转换为H2
    h2_titles = ['正位牌意', '逆位牌意']
    for title in h2_titles:
        pattern = r'(?<!\#)(?<!\#\s)' + re.escape(title) + r'(?!\#)'
        text = re.sub(pattern, f'\n\n## {title}', text)
    
    # 将指定标题转换为H3
    h3_titles = ['含义', '关键要素', '基本牌意', '爱情婚姻', '事业学业', '人际财富']
    for title in h3_titles:
        pattern = r'(?<!\#)(?<!\#\s)' + re.escape(title) + r'(?!\#)'
        text = re.sub(pattern, f'\n### {title}', text)
    
    # 将"要素|解释"和"象征|释义"转换为表格格式
    # 查找形如"要素|解释"的行
    table_patterns = [
        (r'要素\s*\|\s*解释', '| 要素 | 解释 |\n| --- | --- |'),
        (r'象征\s*\|\s*释义', '| 象征 | 释义 |\n| --- | --- |')
    ]
    
    for pattern, replacement in table_patterns:
        text = re.sub(pattern, replacement, text)
    
    # 查找可能的表格内容并格式化
    lines = text.split('\n')
    for i in range(len(lines)):
        # 如果在表格标题行后面的行中包含|，但没有正确的表格格式，则进行格式化
        if i > 0 and ('| 要素 | 解释 |' in lines[i-1] or '| 象征 | 释义 |' in lines[i-1] or '| --- | --- |' in lines[i-1]):
            if '|' in lines[i] and not lines[i].strip().startswith('|'):
                parts = lines[i].split('|', 1)
                if len(parts) == 2:
                    lines[i] = f'| {parts[0].strip()} | {parts[1].strip()} |'
    
    return '\n'.join(lines)

def process_markdown_files(directory):
    """处理目录下的所有Markdown文件"""
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    formatted_content = convert_to_markdown_format(content)
                    
                    if content != formatted_content:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(formatted_content)
                        print(f"已格式化文件: {file_path}")
                except Exception as e:
                    print(f"处理文件 {file_path} 时出错: {e}")

def process_single_file(file_path):
    """处理单个Markdown文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        formatted_content = convert_to_markdown_format(content)
        
        if content != formatted_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(formatted_content)
            print(f"已格式化文件: {file_path}")
        else:
            print("文件内容未改变")
    except Exception as e:
        print(f"处理文件 {file_path} 时出错: {e}")

if __name__ == "__main__":
    
    # 处理指定的文件
    file_path = "docs\\suit\\1.wands\\wands14.md"
    if os.path.isfile(file_path) and file_path.endswith('.md'):
        process_single_file(file_path)
    elif os.path.isdir(file_path):
        process_markdown_files(file_path)
    else:
        print(f"错误: {file_path} 不是有效的Markdown文件或目录")
    
