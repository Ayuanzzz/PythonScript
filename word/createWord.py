from docx import Document

# 创建一个新的Word文档
doc = Document()

# 插入一个3x3的表格
num_rows = 3
num_cols = 3
table = doc.add_table(rows=num_rows, cols=num_cols)

# 设置表格样式（可选）
table.style = 'Table Grid'

# 遍历表格的行和列，并添加内容
for row in table.rows:
    for cell in row.cells:
        cell.text = "内容"  # 将此处的内容替换为您想要的表格单元格内容
        # 设置单元格的对齐方式（可选）
        # cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER

# 保存Word文档
word_file = r"D:\Python\data\2.docx"
doc.save(word_file)
