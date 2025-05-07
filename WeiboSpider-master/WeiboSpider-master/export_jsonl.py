import pandas as pd
import json

# 定义JSONL文件路径和Excel文件路径
jsonl_file_path = 'C:/Users/SHANXIN/Downloads/WeiboSpider-master/WeiboSpider-master/output/tweet_spider_by_keyword_20250409194331.jsonl'
excel_file_path = 'C:/Users/SHANXIN/Downloads/WeiboSpider-master/WeiboSpider-master/output/output.xlsx'

# 读取JSONL文件
data = []
with open(jsonl_file_path, 'r',encoding='utf-8') as file:
    for line in file:
        data.append(json.loads(line))

# 将数据转换为DataFrame
df = pd.DataFrame(data)

# 导出为Excel文件
df.to_excel(excel_file_path, index=False)