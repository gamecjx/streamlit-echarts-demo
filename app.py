import inspect
import textwrap

import streamlit as st

from demo_echarts import ST_DEMOS
from demo_pyecharts import ST_PY_DEMOS


def main():
    st.title("Streamlit ECharts Demo")

    with st.sidebar:
        st.header("选择算法与应用场景")
        api_options = ("MSDBO", "DBO","SSA","BWO","GWO","PO","KOA","WOA")
        selected_api = st.selectbox(
            label="请选择算法:",
            options=api_options,
        )
        page_options = ("CEC2017", "CEC2021")
        selected_page = st.selectbox(
            label="请选择应用场景",
            options=page_options,
        )
        demo, url = (
            ST_DEMOS[selected_page]
            if selected_api == "echarts"
            else ST_PY_DEMOS[selected_page]
        )
    image_path = get_image_path(selected_api, selected_page)
    st.image(image_path)

def get_image_path(selected_api, selected_page):
    # 这里是一个示例，您需要根据实际情况来设置图片路径
    if selected_api == 'MSDBO' and selected_page == 'CEC2017':
        return 'data/26.jpg'
    elif selected_api == 'DBO' and selected_page == 'CEC2021':
        return 'data/27.jpg'
    # 添加更多条件以覆盖所有选择组合
    else:
        return 'data/26.jpg'

    
if __name__ == "__main__":
    st.set_page_config(
        page_title="Streamlit ECharts Demo", page_icon=":chart_with_upwards_trend:"
    )
    main()
