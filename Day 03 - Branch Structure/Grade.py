"""
百分制成绩转换为等级制成绩
"""
score = float(input('请输入成绩: '))
if score >= 90:
    level = "A"
elif score >= 80:
    level = "B"
elif score >= 70:
    level = "C"
elif score >= 60:
    level = "D"
elif score >= 50:
    level = "E"
else:
    level = "F"
print("您的成绩等级为: ", level)
