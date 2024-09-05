import streamlit as st
from kangjian import healthy_aide

st.title("康健助手 2.1")

with st.sidebar:
    st.text("""温馨提示""")
    st.markdown("""康健助手是一个健康管理助手，不过它也会犯错，请检查您重要的信息。
    ————————开发者Jason""")

situation = st.text_input("请输入您的病情:")
duration_illness = st.number_input("请输入生病的大致时间（单位：天）",min_value=0.5,step=0.5)

submit = st.button("生成分析")

if submit and not situation:
    st.info("请输入您的病况")
    st.stop()
if submit and not duration_illness >=0.5:
    st.info("请输入您正的确生病时长")
    st.stop()
if submit:
    with st.spinner(("AI正在思考中哦，客官请稍等~~~😁😁😁")):
        search_result, analyse = healthy_aide(situation, duration_illness,)
    st.success("分析已完成！💕😘")
    st.subheader("分析")
    st.write(analyse)
    with st.expander("维基百科搜索结果  👀"):
        st.info(search_result)
