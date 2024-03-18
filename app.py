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
        return 'path/to/cec2017_msdbo_image.png'
    elif selected_api == 'DBO' and selected_page == 'CEC2021':
        return 'path/to/cec2021_dbo_image.png'
    # 添加更多条件以覆盖所有选择组合
    else:
        return 'path/to/default_image.png'


    demo()

    sourcelines, _ = inspect.getsourcelines(demo)
    with st.expander("Source Code"):
        st.code(textwrap.dedent("".join(sourcelines[1:])))
    st.markdown(f"Credit: {url}")
    
if __name__ == "__main__":
    st.set_page_config(
        page_title="Streamlit ECharts Demo", page_icon=":chart_with_upwards_trend:"
    )
    main()
    with st.sidebar:
        st.markdown("---")
        st.markdown(
            '<h6>Made in &nbsp<img src="https://streamlit.io/images/brand/streamlit-mark-color.png" alt="Streamlit logo" height="16">&nbsp by <a href="https://twitter.com/andfanilo">@andfanilo</a></h6>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div style="margin-top: 0.75em;"><a href="https://www.buymeacoffee.com/andfanilo" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a></div>',
            unsafe_allow_html=True,
        )
