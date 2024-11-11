import os

# 要生成的任务名称列表
tasks = [
"1_ODS_AMTA_TFUNDINFO_oracle2dm",
"2_ODS_AMTA_TPDTABSPLANINFO_oracle2dm",
"3_ODS_AMTA_TPDTBASICINFO_oracle2dm",
"4_ODS_AMTA_TPDTBATCHINFO_oracle2dm",
"5_ODS_AMTA_TPDTBUSICONTACTSINFO_oracle2dm",
"6_ODS_AMTA_TPDTCONTACTSINFO_oracle2dm",
"7_ODS_AMTA_TPDTCREDITENHANCEA_oracle2dm",
"8_ODS_AMTA_TPDTCREDITENHANCEB_oracle2dm",
"9_ODS_AMTA_TPDTCREDITENHANCEINSURE_oracle2dm",
"10_ODS_AMTA_TPDTCREDITENHANCEMORTGAGE_oracle2dm",
"11_ODS_AMTA_TPDTCREDITENHANCEOTHER_oracle2dm",
"12_ODS_AMTA_TPDTCREDITENHANCEPLEDGE_oracle2dm",
"13_ODS_AMTA_TPDTCREDITINFO_oracle2dm",
"14_ODS_AMTA_TPDTDEBTPLANINFO_oracle2dm",
"15_ODS_AMTA_TPDTEQUITYPLANINFO_oracle2dm",
"16_ODS_AMTA_TPDTFEEINFO_oracle2dm",
"17_ODS_AMTA_TPDTFUNDOTHERINFO_oracle2dm",
"18_ODS_AMTA_TPDTINFRAINFO_oracle2dm",
"19_ODS_AMTA_TPDTINTERMEDIARYSERORG_oracle2dm",
"20_ODS_AMTA_TPDTMAINPRJINFO_oracle2dm",
"21_ODS_AMTA_TPDTOPERATEINFO_oracle2dm",
"22_ODS_AMTA_TPDTORDERINFO_oracle2dm",
"23_ODS_AMTA_TPDTPRDCLASSINFO_oracle2dm",
"24_ODS_AMTA_TPDTPRJINFO_oracle2dm",
"25_ODS_AMTA_TPDTPROFIT_oracle2dm",
"26_ODS_AMTA_TPDTRATINGINFO_oracle2dm",
"27_ODS_AMTA_TPDTREGIONBALA_oracle2dm",
"28_ODS_AMTA_TPDTREPAYMENTDATERATIO_oracle2dm",
"29_ODS_AMTA_TPDTTRADECIRCULATE_oracle2dm",
"30_ODS_AMTA_TPDTWEIGHT_oracle2dm",
"31_ODS_AMTA_MEMBER_INFO_oracle2dm",
"32_ODS_AMTA_TDICTIONARY_oracle2dm",
"33_ODS_AMTA_TPDTMANDATOR_oracle2dm",
"34_ODS_AMTA_INFO_DETAIL_oracle2dm",
"35_ODS_AMTA_TSHARECURRENTS_oracle2dm",
"36_ODS_AMTA_TBONDINFO_oracle2dm",
"37_ODS_AMTA_TSTATICSHARES_oracle2dm",
"38_ODS_AMTA_TCUSTINFO_oracle2dm",
"39_ODS_AMTA_HOLDER_ACCOUNT_oracle2dm",
"40_ODS_AMTA_TPDTTEMPLETPRO_oracle2dm",
"41_ODS_AMTA_TBONDCASHSCHEMA_oracle2dm",
"42_ODS_AMTA_TREGIONALISM_oracle2dm",
"43_ODS_AMTA_TFUNDINFO_C_oracle2dm",
"44_ODS_AMTA_TPDTBASICINFO_C_oracle2dm",
"45_ODS_AMTA_TPDTBATCHINFO_C_oracle2dm",
"46_ODS_AMTA_TPDTCREDITENHANCEA_C_oracle2dm",
"47_ODS_AMTA_TPDTCREDITENHANCEB_C_oracle2dm",
"48_ODS_AMTA_TPDTCREDITENHANCEINSURE_C_oracle2dm",
"49_ODS_AMTA_TPDTCREDITENHANCEMORTGAGE_C_oracle2dm",
"50_ODS_AMTA_TPDTCREDITENHANCEPLEDGE_C_oracle2dm",
"51_ODS_AMTA_TPDTDEBTPLANINFO_C_oracle2dm",
"52_ODS_AMTA_TPDTFEEINFO_C_oracle2dm",
"53_ODS_AMTA_TPDTFUNDOTHERINFO_C_oracle2dm",
"54_ODS_AMTA_TPDTINTERMEDIARYSERORG_C_oracle2dm",
"55_ODS_AMTA_TPDTMAINPRJINFO_C_oracle2dm",
"56_ODS_AMTA_TPDTPROFIT_C_oracle2dm",
"57_ODS_AMTA_TPDTRATINGINFO_C_oracle2dm",
"58_ODS_AMTA_TPDTWEIGHT_C_oracle2dm",
"59_ODS_AMTA_TPDTCREDITENHANCEOTHER_C_oracle2dm",
"60_ODS_AMTA_TPDTPRJINFO_C_oracle2dm",
"61_ODS_AMTA_TDIVIDENDDETAIL_oracle2dm",
"62_ODS_AMTA_TPDTDURATIONPROGRAM_oracle2dm",
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
JOB_DIR="/home/zbd/datax/datax/source_config/ODS_AMTA"
LOG_DIR="/home/zbd/datax/datax/log"  

# 使用 date 命令获取日期
LOG_FOLDER_DATE=$(date +%F)
LOG_FOLDER="$LOG_DIR/ODS_AMTA-$LOG_FOLDER_DATE"

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
output_dir = r"C:\Users\yjjc02\Desktop\datax\linux_测试_ODS_AMTA"

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
