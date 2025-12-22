import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import pickle

# 数据读取与预处理
def load_and_check_data(file_path, encoding='utf-8-sig'):
    # 读取CSV，兼容带BOM的UTF-8文件
    df = pd.read_csv(file_path, encoding=encoding)
     
    # 数据清洗：直接指定列名，彻底移除COLUMNS_CONFIG
    missing_check_columns = [
        '性别', '专业', '每周学习时长（小时）', 
        '上课出勤率', '期中考试分数', '作业完成率', '期末考试分数'
    ]
    df.dropna(subset=missing_check_columns, inplace=True)  

    # 特征与目标变量定义 
    features = df[['性别', '专业', '每周学习时长（小时）', '上课出勤率', '期中考试分数', '作业完成率']]
    target = df['期末考试分数']  
    
    # 必须添加返回语句，否则无法解包得到df、features、target
    return df, features, target

# 调用函数（请确认文件路径正确）
df, features, target = load_and_check_data("student_data_adjusted_rounded.csv") 

# 对分类特征独热编码
features_encoded = pd.get_dummies(features, columns=['性别', '专业'], drop_first=False)
print(" 特征编码完成，编码后特征数：", len(features_encoded.columns))

# 模型训练
x_train, x_test, y_train, y_test = train_test_split(
    features_encoded, target, train_size=0.8, random_state=42
)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(x_train, y_train)

# 模型评估
y_pred = model.predict(x_test)
r2 = r2_score(y_test, y_pred)
print(f" 模型训练完成，R²评分：{r2:.2f}（≥0.5为良好）")

# 保存模型与关键信息
with open('student_score_model.pkl', 'wb') as f:
    pickle.dump(model, f)

majors = df['专业'].unique().tolist()
with open('majors_list.pkl', 'wb') as f:
    pickle.dump(majors, f)

print('保存成功，已生成相关文件。')