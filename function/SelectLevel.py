import pandas as pd
import EnterLevel
import pygetwindow as gw

# 读取Excel文件
file_path = "../proprieties/script_controller.xlsx"

# 使用pandas获取Excel文件中的所有sheet名称
excel_file = pd.ExcelFile(file_path)

# 获取所有的sheet名称
sheet_names = excel_file.sheet_names

# 显示所有的 sheet 名称并生成选单
print("请选择一个 sheet 读取内容:")
for index, sheet_name in enumerate(sheet_names, 1):
    print(f"{index}. {sheet_name}")

    # 获取用户输入的序号
    # choice = int(input("请输入序号: "))
    choice = 1

    # 判断输入的序号是否有效
    if 1 <= choice <= len(sheet_names):
        selected_sheet = sheet_names[choice - 1]  # 获取选中的 sheet 名称
        # 读取选中的 sheet 内容
        df = excel_file.parse(selected_sheet)
        print(f"您选择的 sheet 是: {selected_sheet}")
        print("该 sheet 的内容如下：")
        print(df)
        enterLevel = EnterLevel
        enterLevel.start(df)
    else:
        print("输入的序号无效，请输入一个有效的序号。")
