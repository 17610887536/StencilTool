import os
import json

# 定义要处理的文件夹路径
folder_path = r'C:\Users\yjjc02\Desktop\datax\linux_生产_ODS_IAMTA2_SQL'

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        file_path = os.path.join(folder_path, filename)

        # 读取 JSON 文件
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # 修改 jdbcUrl 和 password
        for content in data.get("job", {}).get("content", []):
            reader = content.get("reader", {}).get("parameter", {})
            writer = content.get("writer", {}).get("parameter", {})

            # 更新 reader 的 jdbcUrl 和 password
            if "connection" in reader:
                for conn in reader["connection"]:
                    if "querySql" in conn:
                        conn["querySql"] = [sql.replace("sysdate-1", "'${dataDate}'") for sql in conn["querySql"]]
                    else:
                        reader["password"] = "NHCH4Ont1M"  # 如果不存在则添加

            # 更新 writer 的 jdbcUrl 和 password
            if "connection" in writer:
                for conn in writer["connection"]:
                    if "preSql" in writer:
                        writer["preSql"] = [sql.replace("sysdate-1", "'${dataDate}'") for sql in writer["preSql"]]
                    else:
                        writer["password"] = "NHCH4Ont1M"  # 如果不存在则添加

        # 将修改后的数据写回到文件
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

print("所有文件已处理完成。")
