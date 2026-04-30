from docx import Document
doc = Document('AIX Card 注册登录需求V1.0 (2).docx')

tables = doc.tables

# Table 6: account rules
print("========= TABLE 6 (账户规则) =========")
for r, row in enumerate(tables[6].rows):
    for c, cell in enumerate(row.cells):
        text = cell.text.strip()
        if text:
            print(f"[R{r}C{c}] {text}")
    print()

# Table 2-3: project background/purpose  
print("========= TABLE 2 (项目背景) =========")
for r, row in enumerate(tables[2].rows):
    for c, cell in enumerate(row.cells):
        text = cell.text.strip()
        if text:
            print(f"[R{r}C{c}] {text}")

print("\n========= TABLE 3 (项目目的) =========")
for r, row in enumerate(tables[3].rows):
    for c, cell in enumerate(row.cells):
        text = cell.text.strip()
        if text:
            print(f"[R{r}C{c}] {text}")

# Table 5: country line
print("\n========= TABLE 5 (国家线) =========")
for r, row in enumerate(tables[5].rows):
    for c, cell in enumerate(row.cells):
        text = cell.text.strip()
        if text:
            print(f"[R{r}C{c}] {text}", end=" | ")
    print()
