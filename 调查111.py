import streamlit as st

# 标题
st.title("皮肤类型问卷调查")
st.write("请回答以下问题，以帮助我们确定您的皮肤类型。")

# 使用会话状态来跟踪当前问题的进度
if "question_index" not in st.session_state:
    st.session_state.question_index = 0

# 定义问卷问题
questions = [
    ("你的年龄段是？", ["14-18 岁", "18-24 岁", "24-35 岁", "35 岁及以上"]),
    ("你的皮肤是否容易过敏？", ["A. 是的，我的皮肤非常敏感", "B. 偶尔会有反应，但不算太严重", "C. 我的皮肤很耐受，没有明显的敏感问题"]),
    ("你的皮肤大部分时间是什么状态？", [
        "A. 非常干燥，总是需要补水",
        "B. 脸颊干燥，T区轻微油光",
        "C. 脸颊干燥，T区出油严重",
        "D. 全脸油腻，容易出油",
        "E. 水油平衡，皮肤状态比较稳定"
    ]),
    # 以下是皮肤问题部分的问题示例
    ("你是否经常在 T 区或脸颊出现痘痘？", ["A. 经常", "B. 偶尔", "C. 很少或没有"]),
    ("你的痘痘是否伴随炎症？", ["A. 是的，总是这样", "B. 有时会", "C. 基本没有"]),
    ("你的痘痘是否反复出现在相同的地方？", ["A. 是的，一直如此", "B. 偶尔会", "C. 几乎没有"]),
    ("你是否感到皮肤油脂分泌多，导致毛孔粗大？", ["A. 是的，油光满面", "B. 偶尔会有", "C. 基本没有"]),
    ("你的毛孔是否集中在 T 区？", ["A. 是的，T 区特别明显", "B. 有一些，但不是很明显", "C. 没有特别的感觉"]),
    ("你的毛孔是否容易堵塞，出现黑头或粉刺等问题？", ["A. 是的，常常如此", "B. 偶尔会有", "C. 几乎没有出现过"]),
    # 添加更多问题...
]

# 定义结果计算
def calculate_skin_type():
    # 根据用户回答计算皮肤类型
    # 此处为示例，需根据逻辑替换为实际评分和判断
    return "您的皮肤类型代码是：RCAP"

# 获取当前问题
current_question, options = questions[st.session_state.question_index]

# 显示当前问题
st.write(f"问题 {st.session_state.question_index + 1}: {current_question}")
response = st.radio("选择一个选项：", options)

# 保存回答到会话状态中
if f"answer_{st.session_state.question_index}" not in st.session_state:
    st.session_state[f"answer_{st.session_state.question_index}"] = response

# 按钮控制问题进度
if st.button("下一题"):
    # 将当前答案记录到会话状态
    st.session_state[f"answer_{st.session_state.question_index}"] = response
    st.session_state.question_index += 1

# 如果达到最后一个问题，显示结果
if st.session_state.question_index >= len(questions):
    st.write("问卷完成！")
    skin_type = calculate_skin_type()
    st.write(skin_type)
    st.write("感谢您的参与！")