import os

# 要生成的任务名称列表
tasks = [
"ODS_IAMTA2_ZBD_YN_BXZGCPYWKZQKYBB_dm2dm",
"ODS_IAMTA2_ZBD_YN_BXZGCPYWKZQKZBB_dm2dm",
"ODS_IAMTA2_ZBD_YN_CPXYFXJCB_dm2dm",
"ODS_IAMTA2_ZBD_YN_JGJBXXB_dm2dm",
"ODS_IAMTA2_ZBD_YN_ZHLCPCYRMXB_dm2dm",
"ODS_IAMTA2_ZBD_YN_ZHLCPCYWYZQZCXXB_dm2dm",
"ODS_IAMTA2_ZBD_YN_ZHLCPDXJGXXB_dm2dm",
"ODS_IAMTA2_ZBD_YN_ZHLCPFXZBJXXB_dm2dm",
"ODS_IAMTA2_ZBD_YN_ZHLCPJBXXB_dm2dm",
"ODS_IAMTA2_ZBD_YN_ZHLCPJZXXB_dm2dm",
"ODS_IAMTA2_ZBD_YN_ZHLCPZCFZMXB_dm2dm",
"ODS_IAMTA2_ZBD_YN_ZXCPCYRFEXXB_dm2dm",
"ODS_IAMTA2_ZBD_YN_ZXCPJBXXB_dm2dm",
"ODS_IAMTA2_ZBD_YN_ZXCPTZZCCCMXB_dm2dm",
"ODS_IAMTA2_ZBD_YN_ZXCPTZZCJYMXB_dm2dm",
"ODS_IAMTA2_ZBD_YN_ZXCPZCFZB_dm2dm",
"ODS_IAMTA2_ZBD_YW_BXJGCYCKZSSXXB_dm2dm",
"ODS_IAMTA2_ZBD_YW_BXJGCYJNBDCXXB_dm2dm",
"ODS_IAMTA2_ZBD_YW_BXJGCYJWBDCDYXXB_dm2dm",
"ODS_IAMTA2_ZBD_YW_BXJGCYJWBDCGTTZFXXB_dm2dm",
"ODS_IAMTA2_ZBD_YW_BXJGCYJWBDCNBWDXXB_dm2dm",
"ODS_IAMTA2_ZBD_YW_BXJGCYJWBDCSZDXXB_dm2dm",
"ODS_IAMTA2_ZBD_YW_BXJGCYJWBDCXXB_dm2dm",
"ODS_IAMTA2_ZBD_YW_BXJGCYJWBDCZCCZXXB_dm2dm",
"ODS_IAMTA2_ZBD_YW_BXJGCYLCCPXXB_dm2dm",
"ODS_IAMTA2_ZBD_YW_BXJGCYXTJHXXB_dm2dm",
"ODS_IAMTA2_ZBD_YW_BXJGCYZCZQHCPXXB_dm2dm",
"ODS_IAMTA2_ZBD_YW_BXJGLCCPJYXXB_dm2dm",
"ODS_IAMTA2_ZBD_YW_BXJGLCCPTZZCXXB_dm2dm",
"ODS_IAMTA2_ZBD_YW_BXJGZCZQHCPJYXXB_dm2dm",
"ODS_IAMTA2_ZBD_YW_CKZSSCYBDXXB_dm2dm",
"ODS_IAMTA2_ZBD_YW_CKZSSJBXXB_dm2dm",
"ODS_IAMTA2_ZBD_YW_CPXYFXJCB_dm2dm",
"ODS_IAMTA2_ZBD_YW_JGJBXXB_dm2dm",
"ODS_IAMTA2_ZBD_YW_XTJHCYFEBDXXB_dm2dm",
"ODS_IAMTA2_ZBD_YW_XTJHDBZTXXB_dm2dm",
"ODS_IAMTA2_ZBD_YW_XTJHJBXXB_dm2dm",
"ODS_IAMTA2_ZBD_YW_XTJHRZZTXXB_dm2dm",
"ODS_IAMTA2_ZBD_YW_XMGSDWJKQKB_dm2dm",
"ODS_IAMTA2_ZBD_YW_XMGSGDQKB_dm2dm",
"ODS_IAMTA2_ZBD_YW_XMGSGQTZQKB_dm2dm",
"ODS_IAMTA2_ZBD_YW_XMGSJBXXB_dm2dm",
"ODS_IAMTA2_ZBD_YW_XMGSRZXXB_dm2dm",
"ODS_IAMTA2_ZBD_YW_XMGSTZQTZCQKB_dm2dm",
"ODS_IAMTA2_ZBD_YW_XMGSYBDCGXB_dm2dm",
]

# 脚本模板
script_template = """#!/bin/bash

# 设置程序出错时不再继续执行
set -e

# 获取 dataDate 参数
dataDate=$1

# 检查是否传入了 dataDate 参数
if [ -z "$dataDate" ]; then
    echo "Error: dataDate 参数未提供"
    exit 1
fi

echo "Data Date: $dataDate"

# 定义DataX的安装路径和任务配置文件路径
DATAX_HOME="/home/zbd/datax/datax"  
JOB_DIR="/home/zbd/datax/datax/source_config/ODS_IAMTA2"
LOG_DIR="/home/zbd/datax/datax/log"  

# 使用 date 命令获取日期
LOG_FOLDER_DATE=$(date +%F)
LOG_FOLDER="$LOG_DIR/ODS_IAMTA2-$LOG_FOLDER_DATE"

# 创建日志文件夹（如果不存在）
mkdir -p "$LOG_FOLDER"

# 定义需要执行的任务列表
TASKS=("{task}.json")
LOG_FILES="$LOG_FOLDER/{task}.log"

# 删除已有的日志文件
if [ -e "$LOG_FILES" ]; then
    rm "$LOG_FILES"
fi

# 循环遍历任务列表，执行每个任务
for task in "${TASKS[@]}"; do
    echo "开始执行任务: $task"
    python "$DATAX_HOME/bin/datax.py" -p "-DdataDate='$dataDate'" "$JOB_DIR/$task" > "$LOG_FILES" 2>&1
    echo "任务执行完毕: $task"
done

echo "所有任务执行完毕"
""".replace('\r\n', '\n')  # 替换为Linux换行符

# 指定生成的路径
output_dir = r"C:\Users\yjjc02\Desktop\datax\linux_测试_ODS_IAMTA2"

# 创建输出目录（如果不存在）
os.makedirs(output_dir, exist_ok=True)

# 生成脚本
for task in tasks:
    script_content = script_template.replace("{task}", task)
    script_filename = os.path.join(output_dir, f"{task}.sh")

    # 写入文件，设置为UTF-8编码
    with open(script_filename, 'w', encoding='utf-8', newline='\n') as f:
        f.write(script_content)

print("脚本生成完毕！")
