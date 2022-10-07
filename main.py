
import streamlit as st
import streamlit_highcharts as hg
import pprint


st.write("## Example")
selSample=st.selectbox("Choose a sample",[hg.SAMPLE11,hg.SAMPLE,hg.SAMPLE2,hg.SAMPLE3,hg.SAMPLE4,hg.SAMPLE5,hg.SAMPLE6,hg.SAMPLE7,hg.SAMPLE8,hg.SAMPLE9,hg.SAMPLE10],format_func=lambda x: str(x["title"]["text"])
)
value = hg.streamlit_highcharts(selSample,640)
with st.expander("Show code...",expanded=False):
    
    var=pprint.pformat(selSample,width=40,indent=2)
    st.code("import streamlit as st \
             \r\nimport streamlit_highcharts as hg \
             \r\n\r\nchartDef="+
            var + "\r\n\r\n\r\n" +
            "hg.streamlit_highcharts(chartDef,640)"
            ,language="python")

