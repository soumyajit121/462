# import streamlit as st
# import pandas as pd

# st.set_page_config(
#     page_title="Complete Streamlit Tutorial",
#     page_icon="🚀",
#     layout="wide",
#     initial_sidebar_state="expanded")

# st.title("My first Dashboard")

# st.divider()
# x = pd.read_csv(r"C:\Users\WTS-LAP-81\Downloads\retail_sales_dataset.csv")

# # st.dataframe(x)

# st.sidebar.header("Sidebar")

# st.sidebar.date_input("Select Date")

# # st.text_input("Enter your name")

# # st.camera_input("Take a picture")

# # st.audio_input("Upload an audio fil

# # st.audio("Upload an audio file")

# # y = st.file_uploader("Upload a file", type="csv")

# # z = pd.read_csv(y)

# cl1 , cl2 , cl3 = st.columns(3)

# with cl1:
#     st.metric("Total Sales", x['Sales'].sum(),width=200,border = True ,chart_data=x['Sales'],chart_type="line",delta=x['Sales'].sum()-x['Sales'].mean())

#     c = x.groupby('CustomerName')['Sales'].sum()

#     st.bar_chart(c,color="blue")
    

# with cl2:
#     st.metric("Total Discount", x['Discount'].sum(),width=200,border = True ,chart_data=x['Discount'],chart_type="line",delta=x['Discount'].sum()-x['Discount'].mean())

#     d = x.groupby('CustomerName')['Quantity'].mean()
    
#     st.bar_chart(d,color="green")
        
# with cl3:
#     st.metric("Total Quantity", x['Quantity'].sum(),width=200,border = True ,chart_data=x['Quantity'],chart_type="line",delta=x['Quantity'].sum()-x['Quantity'].mean())

#     e = x.groupby('Product')['Quantity'].mean()
        
#     st.bar_chart(e,color="green")
            

# # if y is not None:
# #     st.write("File uploaded successfully")
# #     st.dataframe(z)
# # else:
# #     st.write("Please upload a file")

# cf = st.sidebar.multiselect("Choose your options",x['CustomerName'].unique())

# fd = x[x['CustomerName'].isin(cf)]

# tab1 , tab2 , tab3 = st.tabs(["Customer","region","Product"])

# with tab1:
#     if cf:
#       a = fd.groupby('CustomerName')['Quantity'].sum()
#       st.dataframe(a)
#       st.bar_chart(a,color="green")
#     else :
#       st.dataframe(x)  

# with tab2: 
#     b =  x.groupby('Region')['Sales'].sum()   

#     st.area_chart(b,color="red")

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Complete Streamlit Tutorial",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ------------------------------------------------------------------ STYLE
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&display=swap');

html, body, [class*="css"], .stApp { font-family: 'Space Grotesk', sans-serif; }

/* ---- crazy shifting gradient background ---- */
.stApp {
    background: linear-gradient(-45deg, #ff0057, #7b2ff7, #00d4ff, #00ff9d, #ffb800, #ff0057);
    background-size: 500% 500%;
    animation: gradientShift 14s ease infinite;
}
@keyframes gradientShift {
    0%   { background-position: 0% 50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* dark veil so content stays readable */
.stApp::before {
    content: ""; position: fixed; inset: 0;
    background: rgba(8, 6, 25, 0.55);
    pointer-events: none; z-index: 0;
}
header[data-testid="stHeader"] { background: transparent; }

/* ---- rainbow animated title ---- */
h1 {
    font-weight: 700 !important; font-size: 3.4rem !important;
    background: linear-gradient(90deg, #fff, #ffe600, #ff4fd8, #00f0ff, #fff);
    background-size: 300% 100%;
    -webkit-background-clip: text; background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: titleFlow 6s linear infinite;
    text-shadow: 0 0 30px rgba(255,255,255,.25);
}
@keyframes titleFlow { to { background-position: 300% 0; } }

h2, h3, p, label, span, div { color: #fff; }

hr { border: none !important; height: 3px !important; border-radius: 3px;
     background: linear-gradient(90deg, #ff0057, #ffb800, #00ff9d, #00d4ff, #7b2ff7, #ff0057);
     background-size: 300% 100%; animation: titleFlow 5s linear infinite; }

/* ---- glass metric cards ---- */
[data-testid="stMetric"] {
    background: rgba(255,255,255,.10);
    backdrop-filter: blur(14px);
    border: 1px solid rgba(255,255,255,.35) !important;
    border-radius: 20px; padding: 18px;
    box-shadow: 0 8px 32px rgba(0,0,0,.35);
    transition: transform .25s ease, box-shadow .25s ease;
}
[data-testid="stMetric"]:hover {
    transform: translateY(-6px) scale(1.03);
    box-shadow: 0 0 28px rgba(0,255,200,.6);
}
[data-testid="stMetricValue"] { font-weight: 700; font-size: 2.2rem; }

/* ---- charts in glass panels ---- */
[data-testid="stVegaLiteChart"], [data-testid="stDataFrame"] {
    background: rgba(255,255,255,.08);
    border-radius: 18px; padding: 10px;
    border: 1px solid rgba(255,255,255,.25);
}

/* ---- sidebar ---- */
[data-testid="stSidebar"] {
    background: linear-gradient(200deg, #12002b, #3a0ca3, #f72585);
    background-size: 100% 300%;
    animation: sideShift 10s ease infinite;
    border-right: 1px solid rgba(255,255,255,.3);
}
@keyframes sideShift { 0%,100% {background-position: 50% 0%;} 50% {background-position: 50% 100%;} }

/* ---- tabs ---- */
button[data-baseweb="tab"] {
    background: rgba(255,255,255,.12); border-radius: 12px 12px 0 0;
    margin-right: 6px; font-weight: 600; transition: all .2s ease;
}
button[data-baseweb="tab"]:hover { background: rgba(255,255,255,.28); }
button[data-baseweb="tab"][aria-selected="true"] {
    background: linear-gradient(90deg, #ff0057, #7b2ff7);
}
[data-baseweb="tab-highlight"] { background: #ffe600 !important; }

@media (prefers-reduced-motion: reduce) {
    .stApp, h1, hr, [data-testid="stSidebar"] { animation: none; }
}
</style>
""",
    unsafe_allow_html=True,
)

# ------------------------------------------------------------------ HEADER
st.title("🚀 My first Dashboard")
st.divider()

# ------------------------------------------------------------------ DATA
DEFAULT_PATH = r"retail_sales_dataset.csv"


@st.cache_data
def load_data(path):
    return pd.read_csv(path)


try:
    x = load_data(DEFAULT_PATH)
except FileNotFoundError:
    up = st.sidebar.file_uploader("Upload retail_sales_dataset.csv", type="csv")
    if up is None:
        st.warning("CSV not found at the default path. Upload it from the sidebar.")
        st.stop()
    x = pd.read_csv(up)

# ------------------------------------------------------------------ SIDEBAR
st.sidebar.header("🎛️ Controls")
st.sidebar.date_input("Select Date")
cf = st.sidebar.multiselect("Choose your customers", x["CustomerName"].unique())

# ------------------------------------------------------------------ KPI + CHARTS
cl1, cl2, cl3 = st.columns(3)

with cl1:
    st.metric(
        "Total Sales", x["Sales"].sum(), width=200, border=True,
        chart_data=x["Sales"], chart_type="line",
        delta=x["Sales"].sum() - x["Sales"].mean(),
    )
    st.bar_chart(x.groupby("CustomerName")["Sales"].sum(), color="#00d4ff")

with cl2:
    st.metric(
        "Total Discount", x["Discount"].sum(), width=200, border=True,
        chart_data=x["Discount"], chart_type="line",
        delta=x["Discount"].sum() - x["Discount"].mean(),
    )
    st.bar_chart(x.groupby("CustomerName")["Quantity"].mean(), color="#00ff9d")

with cl3:
    st.metric(
        "Total Quantity", x["Quantity"].sum(), width=200, border=True,
        chart_data=x["Quantity"], chart_type="line",
        delta=x["Quantity"].sum() - x["Quantity"].mean(),
    )
    st.bar_chart(x.groupby("Product")["Quantity"].mean(), color="#ffe600")

# ------------------------------------------------------------------ TABS
fd = x[x["CustomerName"].isin(cf)]

tab1, tab2, tab3 = st.tabs(["👤 Customer", "🌍 Region", "📦 Product"])

with tab1:
    if cf:
        a = fd.groupby("CustomerName")["Quantity"].sum()
        st.dataframe(a, use_container_width=True)
        st.bar_chart(a, color="#ff4fd8")
    else:
        st.dataframe(x, use_container_width=True)

with tab2:
    b = x.groupby("Region")["Sales"].sum()
    st.area_chart(b, color="#ff0057")

with tab3:
    p = x.groupby("Product")["Sales"].sum()
    st.bar_chart(p, color="#ffb800")




