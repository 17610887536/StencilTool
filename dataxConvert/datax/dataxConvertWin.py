import os

# 要生成的任务名称列表
tasks = [
    "ANAL_GQTZJHJBXXB_dm2dm",
    "ANAL_GQTZJHCYXXB_dm2dm_cw",
]

# 脚本模板
script_template = """@echo off
REM 设置程序出错时不再继续执行
setlocal enabledelayedexpansion

REM 定义DataX的安装路径和任务配置文件路径
set DATAX_HOME=D:\\Kaifa\\datax
set JOB_DIR=D:\\Kaifa\\datax\\source_config\\ANAL
set LOG_DIR=D:\\Kaifa\\datax\\log

REM 使用 PowerShell 获取日期
for /f %%i in ('powershell -command "Get-Date -Format 'yyyy-MM-dd'"') do set LOG_FOLDER_DATE=%%i
set LOG_FOLDER=%LOG_DIR%\\zdy-%LOG_FOLDER_DATE%

if not exist "!LOG_FOLDER!" (
    mkdir "!LOG_FOLDER!"
)

REM 定义当前任务
set task={task_name}
set LOG_FILES=!LOG_FOLDER!\\!task!.log

if exist "!LOG_FILES!" (
    del "!LOG_FILES!"
)

echo 开始执行任务: !task!
python "%DATAX_HOME%\\bin\\datax.py" "%JOB_DIR%\\!task!.json" > "!LOG_FILES!" 2>&1
echo 任务执行完毕: !task!

echo 所有任务执行完毕
endlocal
"""

# 指定生成的路径
output_dir = r"C:\Users\yjjc02\Desktop\datax\windows"

# 创建输出目录（如果不存在）
os.makedirs(output_dir, exist_ok=True)

# 生成每个任务的 .bat 文件
for task in tasks:
    # 替换模板中的任务名称
    script_content = script_template.replace("{task_name}", task)

    # 指定文件名
    script_filename = os.path.join(output_dir, f"{task}.bat")

    # 写入文件
    with open(script_filename, 'w') as f:
        f.write(script_content)

print("脚本生成完毕！")
