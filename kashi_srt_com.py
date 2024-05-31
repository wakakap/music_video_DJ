def insert_text_into_placeholders(a_file_path, b_file_path, output_file_path):
    # 读取a文件，去除空行
    with open(a_file_path, 'r', encoding='utf-8') as a_file:
        a_lines = [line.strip() for line in a_file if line.strip()]  # 读取非空行

    # 读取b文件
    with open(b_file_path, 'r', encoding='utf-8') as b_file:
        b_lines = b_file.readlines()  # 保持行的结构

    # 准备插入内容
    a_content = iter(a_lines)  # 转换为可迭代对象
    new_b_lines = []

    # 遍历b_lines，找到并替换"j"为a中的内容
    for line in b_lines:
        if "j" in line:
            try:
                replacement = next(a_content)  # 获取下一个a中的行
                line = line.replace("j", replacement)  # 替换"j"
            except StopIteration:
                # 如果a中的内容用完了，保留"j"不动
                pass
        new_b_lines.append(line)

    # 将结果写入c文件
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.writelines(new_b_lines)

    print("New content written to:", output_file_path)


# 示例调用
insert_text_into_placeholders("E:\\record\\subject\\音乐视频\\秒針を噛む\\秒針を噛む.srt", "E:\\record\\subject\\音乐视频\\秒針を噛む\\kashi.srt", "kashi_com.srt")
