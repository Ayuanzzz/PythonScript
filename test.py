import uuid

# 生成UUID4
random_uuid = uuid.uuid4()

# 将UUID4转化为格式 "8-4-4-4-8"
formatted_uuid = '-'.join([random_uuid.hex[:8], random_uuid.hex[8:12], random_uuid.hex[12:16], random_uuid.hex[16:20], random_uuid.hex[20:]])

# 提取前32位字符
unique_code = formatted_uuid[:32]

print("唯一码:", unique_code)
