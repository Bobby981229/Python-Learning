"""
成绩表和平均分统计
录入5个学生3门课程的考试成绩
计算每个学生的平均分和每门课的平均分
"""
items = ['Python', 'Java', 'Go', 'Swift']

for index in range(len(items)):
    print(f'{index}: {items[index]}')
print()

for index, item in enumerate(items):
    print(f'{index}: {item}')
print()

names = ['关羽', '张飞', '赵云', '马超', '黄忠']
courses = ['语文', '数学', '英语']

# 用生成式创建嵌套的列表保存5个学生3门课程的成绩
score = [[0] * len(courses) for x in range(len(names))]

# 录入数据
for i, name in enumerate(names):  # 遍历姓名
    print(f'请输入{name}的成绩 ===> ')
    for j, course in enumerate(courses):  # 遍历科目
        score[i][j] = float(input(f'{course}: '))
print()
print('成绩列表: ', score)
print()

# 计算每个人的平均成绩
print('-' * 5, '学生平均成绩', '-' * 5)
for index, name in enumerate(names):
    avg_student = sum(score[index]) / len(courses)
    print(f'{name}的平均成绩为: {avg_student:.1f}分')
print()

# 计算每个科目的平均成绩
print('-' * 5, '科目平均成绩', '-' * 5)
for index, course in enumerate(courses):
    # 用生成式从scores中取出指定的列创建新列表
    sum_grade = [i[index] for i in score]
    avg_subject = sum(sum_grade) / len(names)
    print(f'{course}的平均成绩为: {avg_subject:.1f}分')
