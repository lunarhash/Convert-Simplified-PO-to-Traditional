import polib
from opencc import OpenCC
import argparse
import os

def convert_po_file(input_file, output_file):
    # 初始化OpenCC转换器（简体到繁体）
    cc = OpenCC('s2t')
    
    # 直接读取文件内容
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print(f'源文件行数: {len(lines)}')
    
    # 只转换msgstr行
    converted_lines = []
    for line in lines:
        if line.startswith('msgstr "'):
            # 提取引号中的内容
            start = line.index('"') + 1
            end = line.rindex('"')
            text = line[start:end]
            # 只有当文本非空时才转换
            if text:
                converted_text = cc.convert(text)
                line = line[:start] + converted_text + line[end:]
        converted_lines.append(line)
    
    print(f'转换后行数: {len(converted_lines)}')
    
    # 保存文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(converted_lines)

def main():
    parser = argparse.ArgumentParser(description='将PO文件中的简体中文转换为繁体中文')
    parser.add_argument('input', help='输入PO文件路径')
    parser.add_argument('-o', '--output', help='输出PO文件路径（可选）')
    
    args = parser.parse_args()
    
    input_file = args.input
    output_file = args.output or os.path.splitext(input_file)[0] + '_traditional.po'
    
    try:
        convert_po_file(input_file, output_file)
        print(f'转换完成！输出文件：{output_file}')
    except Exception as e:
        print(f'转换过程中出现错误：{str(e)}')

if __name__ == '__main__':
    main()
