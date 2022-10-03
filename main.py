
import streamlit as st
import streamlit_highcharts as hg


st.write("## Example")
selSample=st.selectbox("Choose a sample",[hg.SAMPLE,hg.SAMPLE2,hg.SAMPLE3,hg.SAMPLE4,hg.SAMPLE5,hg.SAMPLE6,hg.SAMPLE7,hg.SAMPLE8,hg.SAMPLE9,hg.SAMPLE10],format_func=lambda x: str(x["title"]["text"])
)
value = hg.streamlit_highcharts(selSample,640)
with st.expander("Show code...",expanded=False):
    st.code(str(selSample).replace("},","},\r\n"),language="python")

