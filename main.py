
import streamlit as st
from streamlit_highcharts import streamlit_highcharts

chart_def={
   "title":{
      "text":"Sales of petroleum products March, Norway",
      "align":"left"
   },
   "xAxis":{
      "categories":["Jet fuel","Duty-free diesel"]
   },
   "yAxis":{
      "title":{"text":"Million liter"}
   },
   "series":[
        {"type":"column",
            "name":"2020",
            "data":[59,83]},
        {"type":"column",
            "name":"2021",
            "data":[24,79]
        },
        {"type":"column",
            "name":"2022",
            "data":[58,88]
        },
        {"type":"spline",
            "name":"Average",
            "data":[47,83.33],
            "marker":{
                "lineWidth":2,
                "fillColor":"black",
            }
        }
    ]
}
value = streamlit_highcharts(chart_def,640) #640 is the chart height

# def main():
#     st.write("## Example")
#     selSample=st.selectbox("Choose a sample",[SAMPLE,SAMPLE2,SAMPLE3,SAMPLE4,SAMPLE5,SAMPLE6,SAMPLE7,SAMPLE8,SAMPLE9,SAMPLE10],format_func=lambda x: str(x["title"]["text"])
# )
#     value = streamlit_highcharts(selSample,640)
#     with st.expander("Show code...",expanded=False):
#         st.code(str(selSample).replace("},","},\r\n"),language="python")

