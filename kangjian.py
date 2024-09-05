from langchain.prompts import ChatPromptTemplate  # 从langchain中导入提示模板
from langchain_openai import ChatOpenAI
from langchain_community.utilities import WikipediaAPIWrapper

# 对与AI进行交互的封装
def healthy_aide(situation,duration_illness):  # 接收的参数
    # ChatPromptTemplate.from_template这个方法可以接收消息列表作为参数

    condition_analyse = ChatPromptTemplate.from_messages([

        ("human", """你是一位专业且经验丰富的全科医生。根据以下的症状和病情相关信息，为这位病人进行病情分析以及给出符合专业医学的建议和解决办法。
        生病情况：{situation}，生病时间：{duration_illness}。
        要求分析后要详细且易懂的告知病人发病可能的原因，生成的内容格式按照【原因、建议】分隔。
        整体内容要详细且易懂，尽量缓解病人生病的焦虑情绪。
        回答的内容可以结合以下维基百科搜索出的信息但仅作为参考只结合相关的即可对不相关的进行忽略：
        '''{wikipedia_search}'''""")   # 分析消息提示模板
    ]
    )
    # 定义模型
    model = ChatOpenAI(model="gpt-4o",openai_api_key = "sk-6a8A06LIsWTyt8z8501d5048B50447B3B3F81c9cD52eA54c",
                   openai_api_base = "https://api.aigc369.com/v1")
    # 获得视频标题以及脚本的链给组装起来
    condition_chain = condition_analyse | model


    search = WikipediaAPIWrapper(lang="zh")
    search_result = search.run(situation)

    analyse = condition_chain.invoke({"situation": situation, "duration_illness":duration_illness, "wikipedia_search": search_result}).content    # AI的回复是包含那些很多一些乱七八糟的东西但是通过content可以返回AI里面的一个实际的一个内容

    return  search_result, analyse
#print(healthy_aide("d肚子痛",2,0.5))
