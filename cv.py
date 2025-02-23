# Autor: Tania Echague
# Date: 2025/02/22
# Descripción: CV in Streamlit

## Base Code of the CV in Streamlit
import streamlit as st
import streamlit.components.v1 as components

# --- Page Settings ---
st.set_page_config(page_title="Mi CV Digital", page_icon="📄", layout="wide")

# --- Personal Information ---
st.title("👩🏻‍💻 Tania Echagüe")
col1, col2 = st.columns([3,1])
with col1:
    st.text("📍 Center, Montevideo, Uruguay \n"
            "📧 tania.echague@gmail.com \n"
            "📞 +59898321677 \n"
            "Birthdate: 12/05/1988 \n"
            "Nationality: Uruguayan \n"
            "Languages: Spanish (native), English (intermediate) \n")
    st.write("[LinkedIn](https://www.linkedin.com/in/tania-echag%C3%BCe-053aa1342/) | [GitHub](https://github.com/Taniaechague)")
with col2:
    st.image("fotoperfil.jpg", width=200)
st.write("---")


# --- Section: Profile ---
st.header("🎯 About me")
st.text(
    "Economist | Data Analytics | Data Scientist \n"
    "Candidate for Master's Degree in International Economics (Udelar) \n"
    "Passionate about data analysis, data science and economics \n"
    "Specialized in Visualization and Machine Learning \n"
    "Python, SQL, VSC, Tableau, R \n"
)
st.write("---")

# --- Section: Work experience ---
st.header("💼 Work Experience")

st.subheader("📌 Professional Economist, Gr. 12 - UETSS")
st.write("📅 Nov, 2013 - Current")
st.text(" 🔹 Micro and macroeconomic analysis with focus on Sectors of Activity \n"
         "🔹 ETL, EDA and Modeling \n" 
         "🔹 Data Management and Database Design \n"
         "🔹 Visualization Analysis \n"
         "🔹 Impact evaluation of Policies and Programs with Econometric techniques \n" 
         "🔹 Preparation of Statistical-Economic Reports for Informed Decision Making \n"
         )

st.subheader("📌 Economics and Finance Teacher - UTU")
st.write("📅 2012 - 2014")
st.write("---")

# --- Section: Education ---
st.header("🎓 Education")
st.subheader("**📌 Graduate in Economics** - UCUDAL")
st.write("📅 2007 - 2012")

st.subheader("**📌 Data Scientist** - IBM")
st.write("📅 2023 - 2025")

st.subheader("**📌 Master in Economics** - Udelar")
st.write("📅 Estimated completion date: Feb, 2026")

st.subheader("**Python** - IBM")
st.write("📅 February 2024 to March 2025")

st.subheader("**R** - DINAE")
st.write("📅 May to December 2024")

st.subheader("**Data Management** - AGESIC")
st.write("📅 August to September 2023")

st.subheader("**Big Data and skills gaps** - OIT/Cinterfor")
st.write("📅 September to December 2022")

st.subheader("**STATA** - BIOS")
st.write("📅 October to December 2021")

st.subheader("**SQL** - UDE")
st.write("📅 September to October 2021")

st.subheader("**Institutional capacity building for effective labour market information systems** - OIT")
st.write("📅 November to December 2020")

st.subheader("**Metadata course** - INE")
st.write("📅 August 2018")

st.subheader("**Georeferencing course** - INE")
st.write("📅 December 2017")

st.subheader("**Diploma in gender and public policies** - Flacso")
st.write("📅 March to December 2016")

st.subheader("**Policy Impact Assessment** - University of Montevideo, ALJPAL")
st.write("📅 March 2014")

st.subheader("**First Certificate in English** - University of Cambridge")
st.write("📅 November 2011")
st.write("---")


# --- Section: Skills ---
st.header("🛠️ Skills")
st.write("""
-  Python
-  SQL
-  R
-  Tableau
-  Scikit-learn
-  TensorFlow
-  PyTorch
-  Pandas
-  Numpy
-  Seaborn
-  Matplotlib
-  Plotly
-  HTML/CSS
-  ETL
-  EDA
-  Data Analysis
-  Data Visualization
-  Machine Learning
-  Preparation of reports for decision making
""")
st.write("---")

st.header("📄 Download CV in PDF")
if st.checkbox("Download CV in PDF"):
    pdf_url = "https://raw.githubusercontent.com/Taniaechague/CV/main/CV_TE.pdf"
    components.html(
        f'<iframe src="{pdf_url}" width="700" height="1000" type="application/pdf"></iframe>',
        height=1000,
    )