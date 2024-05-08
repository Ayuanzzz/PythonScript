from docx import Document

def read_word_table_by_row_and_cell(doc_path):
    try:
        doc = Document(doc_path)
        for table in doc.tables:
            for row_index, row in enumerate(table.rows):
                print(f"Row {row_index}:")
                for cell_index, cell in enumerate(row.cells):
                    print(f"  Cell {cell_index}: {cell.text}")
            print("----------------------------------------------------------------")
    except Exception as e:
        print(f"Error: {e}")

# 用法示例
doc_path = r"D:\Python\test\记录表装订\记录表装订\1-检查报告及记录\安顺场镇-664\共和村-检查记录表-20.docx"
read_word_table_by_row_and_cell(doc_path)