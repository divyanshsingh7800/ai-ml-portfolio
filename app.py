import streamlit as st
import plotly.graph_objects as go

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Divyansh Singh | AI/ML Developer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    /* =====================================================
       GLOBAL
       ===================================================== */

    .stApp {
        background: #080d18;
        color: #f8fafc;
    }

    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1250px;
    }

    /* Normal text */
    p {
        color: #cbd5e1;
        line-height: 1.7;
    }

    /* Headings */
    h1 {
        color: #f8fafc !important;
    }

    h2 {
        color: #f1f5f9 !important;
        margin-top: 1.8rem;
    }

    h3 {
        color: #e2e8f0 !important;
    }


    /* =====================================================
       SIDEBAR
       ===================================================== */

   section[data-testid="stSidebar"] {
    background: #0d1422;
}
    section[data-testid="stSidebar"] * {
        color: #e2e8f0;
    }


    /* =====================================================
       BUTTONS
       ===================================================== */

    .stLinkButton a,
    .stButton button,
    .stDownloadButton button {

        background: #111c2e !important;
        color: #f8fafc !important;

        border: 1px solid #334155 !important;
        border-radius: 10px !important;

        min-height: 48px;

        font-weight: 600;

        transition: all 0.2s ease;
    }

    .stLinkButton a:hover,
    .stButton button:hover,
    .stDownloadButton button:hover {

        background: #172943 !important;
        border-color: #38bdf8 !important;

        color: #ffffff !important;

        transform: translateY(-2px);
    }


    /* =====================================================
       METRIC CARDS
       ===================================================== */

    div[data-testid="stMetric"] {

        background: linear-gradient(
            145deg,
            #111c2e,
            #0d1626
        );

        border: 1px solid #24344d;

        border-radius: 14px;

        padding: 20px;

        min-height: 125px;

        box-shadow:
            0 8px 25px rgba(0,0,0,0.20);
    }

    div[data-testid="stMetric"] label {

        color: #94a3b8 !important;

        font-size: 14px !important;

        font-weight: 600 !important;
    }

    div[data-testid="stMetric"] div[data-testid="stMetricValue"] {

        color: #f8fafc !important;

        font-size: 28px !important;

        font-weight: 700 !important;
    }


    /* =====================================================
       INFO / SUCCESS BOX
       ===================================================== */

    div[data-testid="stAlert"] {

        border-radius: 12px;
        border: 1px solid #334155;
    }


    /* =====================================================
       CODE BLOCK
       ===================================================== */

    pre {

        background: #0d1422 !important;

        border: 1px solid #1e293b !important;

        border-radius: 12px !important;
    }


    /* =====================================================
       DIVIDERS
       ===================================================== */

    hr {

        border-color: #1e293b !important;

        margin: 2rem 0 !important;
    }


    /* =====================================================
       LINKS
       ===================================================== */

    a {
        color: #38bdf8;
    }


    /* =====================================================
       MOBILE
       ===================================================== */

    @media (max-width: 768px) {

        .main .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }

        h1 {
            font-size: 36px !important;
        }

        h2 {
            font-size: 26px !important;
        }

    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        """
        <div style="text-align:center;">

        <h2>🤖 Divyansh Singh</h2>

        <p style="color:#7dd3fc;">
        AI/ML Engineer
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    page = st.radio(
        "Navigation",
        [
            "🏠 Home",
            "👨‍💻 About",
            "🛠️ Skills",
            "🚀 Projects",
            "📚 AI/ML Journey",
            "🏆 Certifications",
            "📄 Resume",
            "📬 Contact"
        ]
    )

    st.markdown("---")

    st.markdown(
        """
        ### 🔗 Connect

        **Python • ML • DL • NLP • LLMs • RAG**
        """
    )

    st.link_button(
        "💼 LinkedIn",
        "https://www.linkedin.com/in/divyansh-singh-7973433a0/",
        use_container_width=True
    )

    st.link_button(
        "🐙 GitHub",
        "https://github.com/divyanshsingh7800",
        use_container_width=True
    )


# =========================================================
# HOME
# =========================================================

if page == "🏠 Home":

    st.html("""
    <div style="
        text-align: center;
        padding: 50px 20px 30px 20px;
    ">

        <h1 style="
            font-size: 52px;
            font-weight: 800;
            margin: 0 0 8px 0;
            color: white;
        ">
            Divyansh Singh
        </h1>

       <h2 style="
        color:#38bdf8;
        font-size:28px;
        margin-top:5px;
    ">
        AI/ML Engineer
    </h2>

        <p style="
        color:#cbd5e1;
        font-size:18px;
        max-width:850px;
        margin:auto;
        line-height:1.8;
    ">
        Building intelligent applications with
        <span style="color:#ffffff; font-weight:600;">
        Machine Learning, Deep Learning, NLP,
        Explainable AI, LLMs and RAG.
        </span>
    </p>

    </div>
    """)

    st.markdown("---")

    st.markdown("")


    # -----------------------------------------------------
    # QUICK LINKS
    # -----------------------------------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.link_button(
            "🐙 GitHub",
            "https://github.com/divyanshsingh7800",
            use_container_width=True
        )

    with col2:
        st.link_button(
            "💼 LinkedIn",
            "https://www.linkedin.com/in/divyansh-singh-7973433a0/",
            use_container_width=True
        )

    with col3:

        try:
            with open(
                "assets/Divyansh Singh resume.pdf",
                "rb"
            ) as file:

                resume_data = file.read()

            st.download_button(
                "📄 Resume",
                data=resume_data,
                file_name="Divyansh_Singh_AI_ML_Engineer_Resume.pdf",
                mime="application/pdf",
                use_container_width=True
            )

        except FileNotFoundError:
            st.error("Resume PDF nahi mili.")

    with col4:
        st.link_button(
            "📧 Contact",
            "mailto:singhanuj04639@gmail.com",
            use_container_width=True
        )

    st.markdown("---")


 

# =========================================================
# AT A GLANCE
# =========================================================

    st.markdown("## ⚡ At a Glance")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.markdown(
            """
            <div style="
                background:linear-gradient(145deg,#111c2e,#0d1626);
                border:1px solid #24344d;
                border-radius:14px;
                padding:22px;
                text-align:center;
                min-height:120px;
            ">

            <div style="
                color:#38bdf8;
                font-size:14px;
                font-weight:600;
            ">
            PROJECTS
            </div>

            <div style="
                color:#ffffff;
                font-size:32px;
                font-weight:700;
                margin-top:10px;
            ">
            6+
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with col2:

        st.markdown(
            """
            <div style="
                background:linear-gradient(145deg,#111c2e,#0d1626);
                border:1px solid #24344d;
                border-radius:14px;
                padding:22px;
                text-align:center;
                min-height:120px;
            ">

            <div style="
                color:#38bdf8;
                font-size:14px;
                font-weight:600;
            ">
            PRIMARY LANGUAGE
            </div>

            <div style="
                color:#ffffff;
                font-size:27px;
                font-weight:700;
                margin-top:12px;
            ">
            Python
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with col3:

        st.markdown(
            """
            <div style="
                background:linear-gradient(145deg,#111c2e,#0d1626);
                border:1px solid #24344d;
                border-radius:14px;
                padding:22px;
                text-align:center;
                min-height:120px;
            ">

            <div style="
                color:#38bdf8;
                font-size:14px;
                font-weight:600;
            ">
            FOCUS
            </div>

            <div style="
                color:#ffffff;
                font-size:27px;
                font-weight:700;
                margin-top:12px;
            ">
            AI / ML
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with col4:

        st.markdown(
            """
            <div style="
                background:linear-gradient(145deg,#111c2e,#0d1626);
                border:1px solid #24344d;
                border-radius:14px;
                padding:22px;
                text-align:center;
                min-height:120px;
            ">

            <div style="
                color:#38bdf8;
                font-size:14px;
                font-weight:600;
            ">
            GENERATIVE AI
            </div>

            <div style="
                color:#ffffff;
                font-size:25px;
                font-weight:700;
                margin-top:12px;
            ">
            RAG + LLM
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    # -----------------------------------------------------
    # WHAT I DO
    # -----------------------------------------------------

    st.markdown("## 🧠 What I Do")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### 🤖 Machine Learning")

        st.write(
            """
            I build supervised and unsupervised Machine Learning
            solutions including classification, regression,
            clustering, feature engineering and model evaluation.
            """
        )

        st.markdown(
            """
            **Scikit-learn · XGBoost · CatBoost · K-Means**
            """
        )


    with col2:

        st.markdown("### 🧠 Deep Learning")

        st.write(
            """
            I work with neural networks and sequence-based models
            for solving Deep Learning and NLP problems.
            """
        )

        st.markdown(
            """
            **PyTorch · CNN · RNN · LSTM · Transformers**
            """
        )


    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### 💬 NLP")

        st.write(
            """
            Building systems for text classification, embeddings,
            language understanding and modern NLP applications.
            """
        )

        st.markdown(
            """
            **NLP · LSTM · BERT · RoBERTa · Embeddings**
            """
        )


    with col2:

        st.markdown("### ✨ Generative AI")

        st.write(
            """
            Exploring modern AI applications using Large Language
            Models, vector search and Retrieval Augmented Generation.
            """
        )

        st.markdown(
            """
            **LLMs · Hugging Face · RAG · FAISS**
            """
        )


    # -----------------------------------------------------
    # FEATURED PROJECTS
    # -----------------------------------------------------

    st.markdown("## 🚀 Featured Projects")

    st.write(
        """
        A selection of my end-to-end AI/ML projects.
        """
    )

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### 🛒 E-Commerce Analytics")

        st.write(
            """
            Customer segmentation, repeat purchase prediction,
            CLV prediction and Explainable AI.
            """
        )

        st.markdown(
            """
            `K-Means` `XGBoost` `CatBoost` `SHAP`
            """
        )


    with col2:

        st.markdown("### 🧠 Wikipedia RAG Assistant")

        st.write(
            """
            Dynamic knowledge assistant using embeddings,
            FAISS retrieval and Gemma 2B.
            """
        )

        st.markdown(
            """
            `RAG` `FAISS` `Embeddings` `Gemma`
            """
        )


    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### 💬 Toxic Comment Detection")

        st.write(
            """
            NLP classification system using an LSTM-based
            Deep Learning model.
            """
        )

        st.markdown(
            """
            `NLP` `LSTM` `PyTorch`
            """
        )


    with col2:

        st.markdown("### 🚦 Traffic Crash Analytics")

        st.write(
            """
            Large-scale traffic crash analytics platform using
            Python, SQL and Streamlit.
            """
        )

        st.markdown(
            """
            `Python` `SQL` `Streamlit`
            """
        )


    # -----------------------------------------------------
    # CURRENT FOCUS
    # -----------------------------------------------------

    st.markdown("## 🎯 Currently Exploring")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown("### 🔄 Transformers")

        st.write(
            """
            Self-Attention, Multi-Head Attention,
            Positional Encoding and Transformer architecture.
            """
        )

    with col2:

        st.markdown("### ✨ LLMs")

        st.write(
            """
            Hugging Face Transformers, text generation,
            inference and modern language models.
            """
        )

    with col3:

        st.markdown("### 🔎 RAG")

        st.write(
            """
            Chunking, embeddings, vector databases,
            retrieval and context-aware generation.
            """
        )


    # -----------------------------------------------------
    # CTA
    # -----------------------------------------------------

    st.markdown("---")

    st.markdown(
        """
        <div style="
            text-align:center;
            padding:30px;
        ">

        <h2>
        Let's Build Something Intelligent 🚀
        </h2>

        <p style="color:#94a3b8;">
        Open to AI/ML opportunities, projects and collaborations.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# ABOUT
# =========================================================

elif page == "👨‍💻 About":

    st.markdown(
        "## 👨‍💻 About Me"
    )

    st.markdown(
        """
        ### Hi, I'm Divyansh Singh 👋

        I'm an aspiring **AI/ML Engineer** focused on building
        practical and end-to-end Artificial Intelligence solutions.

        My work spans **Machine Learning, Deep Learning, NLP,
        Explainable AI, Large Language Models and Retrieval
        Augmented Generation (RAG)**.

        I enjoy taking a problem from raw data and preprocessing
        through model development, evaluation, explainability and
        finally deployment using Python and Streamlit.
        """
    )

    st.markdown("---")

    st.markdown("## 🎯 What I Work With")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            """
            ### 🤖 Machine Learning

            Regression, Classification, Clustering,
            Feature Engineering, Ensemble Learning and
            Model Evaluation.

            **Tools:** Scikit-learn, XGBoost, LightGBM, CatBoost
            """
        )

    with col2:

        st.markdown(
            """
            ### 🧠 Deep Learning & NLP

            Neural Networks, LSTM, Transformers,
            Embeddings and modern NLP techniques.

            **Tools:** PyTorch, TensorFlow, BERT, RoBERTa
            """
        )

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            """
            ### ✨ Generative AI

            Large Language Models, Prompt Engineering,
            Retrieval Augmented Generation and semantic search.

            **Tools:** Hugging Face, LangChain, Gemma, Ollama, FAISS
            """
        )

    with col2:

        st.markdown(
            """
            ### 🚀 Deployment

            Building interactive AI applications and dashboards.

            **Tools:** Streamlit, Git, GitHub, Jupyter, VS Code
            """
        )

    st.markdown("---")

    st.markdown("## 🎓 Education")

    st.markdown(
        """
        **Bachelor of Computer Applications (BCA)**

        Prof. Rajendra Singh (Rajju Bhaiya) University, Prayagraj

        **Aug 2024 – June 2027**
        """
    )

    st.markdown("---")

    st.markdown("## 🏆 Certification")

    st.markdown(
        """
        **Advanced AI & Machine Learning Program**

        HCL GUVI
        """
    )




# =========================================================
# SKILLS
# =========================================================

elif page == "🛠️ Skills":

    st.markdown(
        '<div class="section-title">Technical Skills</div>',
        unsafe_allow_html=True
    )

    st.write(
        """
        My technical toolkit covers the complete AI/ML development
        lifecycle — from data preparation and Machine Learning to
        Deep Learning, NLP, LLMs, RAG and deployment.
        """
    )

    st.markdown("---")

    # =====================================================
    # PROGRAMMING
    # =====================================================

    st.markdown("## 🐍 Programming & Data")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            """
            <div class="skill-card">

            <div class="skill-title">
            Python
            </div>

            <div class="skill-list">
            NumPy · Pandas · Functions · OOP ·
            Data Structures · File Handling
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            """
            <div class="skill-card">

            <div class="skill-title">
            SQL
            </div>

            <div class="skill-list">
            Joins · CTEs · Window Functions ·
            Aggregations · Analytical Queries
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    # =====================================================
    # MACHINE LEARNING
    # =====================================================

    st.markdown("## 🤖 Machine Learning")

    ml_skills = {
        "Scikit-learn": 0.85,
        "Feature Engineering": 0.85,
        "Model Evaluation": 0.85,
        "XGBoost": 0.75,
        "LightGBM": 0.70,
        "CatBoost": 0.75,
        "K-Means": 0.80
    }

    for skill, value in ml_skills.items():

        st.markdown(f"**{skill}**")

        st.progress(value)


    # =====================================================
    # DEEP LEARNING
    # =====================================================

    st.markdown("## 🧠 Deep Learning")

    dl_skills = {
        "PyTorch": 0.75,
        "Neural Networks": 0.80,
        "CNN": 0.70,
        "RNN": 0.70,
        "LSTM": 0.75,
        "Attention": 0.65,
        "Transformers": 0.65
    }

    for skill, value in dl_skills.items():

        st.markdown(f"**{skill}**")

        st.progress(value)


    # =====================================================
    # NLP
    # =====================================================

    st.markdown("## 💬 Natural Language Processing")

    nlp_skills = {
        "Text Preprocessing": 0.80,
        "Tokenization": 0.80,
        "Word Embeddings": 0.70,
        "Sequence Models": 0.75,
        "BERT": 0.65,
        "RoBERTa": 0.65
    }

    for skill, value in nlp_skills.items():

        st.markdown(f"**{skill}**")

        st.progress(value)


    # =====================================================
    # GENERATIVE AI
    # =====================================================

    st.markdown("## ✨ Generative AI")

    genai_skills = {
        "LLMs": 0.65,
        "Hugging Face Transformers": 0.70,
        "Embeddings": 0.75,
        "RAG": 0.75,
        "FAISS": 0.75,
        "Prompt Engineering": 0.65
    }

    for skill, value in genai_skills.items():

        st.markdown(f"**{skill}**")

        st.progress(value)


    # =====================================================
    # DATA VISUALIZATION
    # =====================================================

    st.markdown("## 📊 Data Visualization")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            """
            <div class="skill-card">

            <div class="skill-title">
            📈 Matplotlib
            </div>

            <div class="skill-list">
            Statistical & analytical plots
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            """
            <div class="skill-card">

            <div class="skill-title">
            📊 Plotly
            </div>

            <div class="skill-list">
            Interactive visualizations
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            """
            <div class="skill-card">

            <div class="skill-title">
            🎨 Streamlit
            </div>

            <div class="skill-list">
            Interactive ML dashboards
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    # =====================================================
    # TOOLS
    # =====================================================

    st.markdown("## 🛠️ Tools & Deployment")

    tools = [
        "Git",
        "GitHub",
        "Jupyter Notebook",
        "Streamlit",
        "MySQL",
        "SQLAlchemy"
    ]

    cols = st.columns(3)

    for i, tool in enumerate(tools):

        with cols[i % 3]:

            st.markdown(
                f"""
                <div class="skill-card">

                <div class="skill-title">
                {tool}
                </div>

                </div>
                """,
                unsafe_allow_html=True
            )


    # =====================================================
    # AI/ML STACK
    # =====================================================

    st.markdown("## 🧩 My AI/ML Stack")

    st.code(
        """
                    AI / ML
                       │
        ┌──────────────┼──────────────┐
        │              │              │
    Machine        Deep Learning      NLP
    Learning           │              │
        │              │              │
  Scikit-learn     PyTorch       BERT/RoBERTa
  XGBoost          CNN           Tokenization
  CatBoost         LSTM          Embeddings
        │              │              │
        └──────────────┼──────────────┘
                       │
                 Generative AI
                       │
             Transformers / LLMs
                       │
                  Embeddings
                       │
                     RAG
                       │
                    FAISS
                       │
                   Streamlit
        """,
        language="text"
    )


# =========================================================
# PROJECTS
# =========================================================

elif page == "🚀 Projects":

    st.markdown(
        '<div class="section-title">Featured Projects</div>',
        unsafe_allow_html=True
    )

    project = st.selectbox(
        "Select Project",
        [
            "🛒 E-Commerce Customer Analytics",
            "🧠 Wikipedia AI Knowledge Assistant",
            "💬 Toxic Comment Detection",
            "🚦 Traffic Crash Analytics",
            "🎵 Amazon Music Clustering",
            "📈 YouTube Revenue Prediction"
        ]
    )

    st.markdown("---")


    # =====================================================
    # E-COMMERCE PROJECT
    # =====================================================

    if project == "🛒 E-Commerce Customer Analytics":

        st.markdown(
            """
            # 🛒 Intelligent E-Commerce Customer Analytics Platform

            ### Turning customer data into actionable business intelligence
            """,
            unsafe_allow_html=True
        )

        st.write(
            """
            An end-to-end Machine Learning platform designed to understand
            customer behavior, segment customers, predict repeat purchases,
            estimate Customer Lifetime Value and provide explainable AI
            insights.
            """
        )

        # -------------------------------------------------
        # PROJECT STATS
        # -------------------------------------------------

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Dataset Size",
                "113K+",
                "Customer Records"
            )

        with col2:
            st.metric(
                "Features",
                "39",
                "Integrated Dataset"
            )

        with col3:
            st.metric(
                "ML Tasks",
                "3",
                "Segmentation + Prediction"
            )

        with col4:
            st.metric(
                "Best CLV R²",
                "0.2454",
                "CatBoost"
            )

        st.markdown("---")


        # -------------------------------------------------
        # BUSINESS PROBLEM
        # -------------------------------------------------

        st.markdown("## 🎯 Business Problem")

        st.write(
            """
            E-commerce businesses generate large amounts of customer
            transaction data, but raw transactional data does not directly
            answer important business questions.

            The objective of this project was to build an intelligent
            analytics system capable of answering:

            • Which customers are high-value?

            • Which customers are likely to purchase again?

            • What type of customers does the business have?

            • What is the expected customer lifetime value?

            • Why is the ML model making a particular prediction?
            """
        )


        # -------------------------------------------------
        # SOLUTION
        # -------------------------------------------------

        st.markdown("## 💡 Solution")

        st.write(
            """
            I developed an end-to-end customer intelligence pipeline that
            combines descriptive analytics, unsupervised learning,
            supervised learning, regression and Explainable AI.
            """
        )

        st.code(
            """
Raw Data
   ↓
Data Integration
   ↓
Data Cleaning
   ↓
EDA
   ↓
Feature Engineering
   ↓
Customer Segmentation
   ↓
Purchase Prediction
   ↓
CLV Prediction
   ↓
SHAP Explainability
   ↓
Streamlit Dashboard
            """,
            language="text"
        )


        # -------------------------------------------------
        # DATASET
        # -------------------------------------------------

        st.markdown("## 📊 Dataset")

        st.write(
            """
            After integrating and preprocessing the source datasets,
            the final analytical dataset contained:
            """
        )

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Rows",
                "113,425"
            )

        with col2:

            st.metric(
                "Columns",
                "39"
            )


        # -------------------------------------------------
        # CUSTOMER SEGMENTATION
        # -------------------------------------------------

        st.markdown("## 👥 Customer Segmentation")

        st.write(
            """
            K-Means clustering was used to identify groups of customers
            with similar purchasing behavior.

            The segmentation process was based on engineered customer-level
            behavioral features.
            """
        )

        st.code(
            """
Customer Features
       ↓
Feature Scaling
       ↓
K-Means
       ↓
Customer Clusters
       ↓
Business Interpretation
            """,
            language="text"
        )

        st.info(
            "Goal: Identify meaningful customer groups for targeted "
            "marketing and retention strategies."
        )


        # -------------------------------------------------
        # PURCHASE PREDICTION
        # -------------------------------------------------

        st.markdown("## 🔮 Repeat Purchase Prediction")

        st.write(
            """
            The second ML task was to predict whether a customer would
            make a repeat purchase within the next 90 days.

            Since the target classes were imbalanced, SMOTE was applied
            to improve learning from the minority class.
            """
        )

        st.markdown("### Models Evaluated")

        models = [
            "Logistic Regression",
            "Decision Tree",
            "Random Forest",
            "Gradient Boosting",
            "XGBoost",
            "LightGBM"
        ]

        for model in models:
            st.write(f"• {model}")

        st.success(
            "Selected Model: GradientBoostingClassifier"
        )

        st.code(
            """
GradientBoostingClassifier(
    n_estimators=200,
    learning_rate=0.1,
    random_state=42
)
            """,
            language="python"
        )


        # -------------------------------------------------
        # CLV
        # -------------------------------------------------

        st.markdown("## 💰 Customer Lifetime Value Prediction")

        st.write(
            """
            Customer Lifetime Value was modeled as a regression problem.

            The objective was to estimate the customer's future monetary
            value using behavioral and transactional features.
            """
        )

        st.markdown("### Features Used")

        features = [
            "Total_Orders",
            "Avg_Freight",
            "Avg_Review",
            "Unique_Products",
            "Unique_Categories",
            "Recency"
        ]

        for feature in features:
            st.write(f"• `{feature}`")


        # -------------------------------------------------
        # MODEL COMPARISON
        # -------------------------------------------------

        st.markdown("### 📈 Model Comparison")

        clv_results = {
            "Linear Regression": {
                "RMSE": 192.01,
                "MAE": 101.83,
                "MAPE": 90.23,
                "R²": 0.1942
            },
            "Random Forest": {
                "RMSE": 198.53,
                "MAE": 93.61,
                "MAPE": 64.79,
                "R²": 0.1385
            },
            "Gradient Boosting": {
                "RMSE": 187.58,
                "MAE": 96.74,
                "MAPE": 81.94,
                "R²": 0.2309
            },
            "XGBoost": {
                "RMSE": 185.97,
                "MAE": 90.92,
                "MAPE": 67.88,
                "R²": 0.2441
            },
            "CatBoost": {
                "RMSE": 185.81,
                "MAE": 94.52,
                "MAPE": 77.66,
                "R²": 0.2454
            }
        }

        import pandas as pd

        results_df = pd.DataFrame(clv_results).T

        st.dataframe(
            results_df,
            use_container_width=True
        )

        st.success(
            "🏆 Best R²: CatBoost — 0.2454"
        )


        # -------------------------------------------------
        # EXPLAINABLE AI
        # -------------------------------------------------

        st.markdown("## 🔍 Explainable AI — SHAP")

        st.write(
            """
            SHAP was used to understand how individual features influence
            model predictions.

            This makes the ML system more transparent and helps identify
            which customer characteristics contribute most strongly to
            predicted value.
            """
        )

        st.code(
            """
explainer = shap.TreeExplainer(model)

shap_values = explainer(X)

shap.plots.waterfall(
    shap_values[0]
)
            """,
            language="python"
        )


        # -------------------------------------------------
        # BUSINESS IMPACT
        # -------------------------------------------------

        st.markdown("## 📌 Business Insights")

        insights = [
            "Identify high-value customers",
            "Identify customers at risk of churn",
            "Target customers likely to purchase again",
            "Create customer-specific marketing strategies",
            "Estimate customer monetary value",
            "Explain individual ML predictions"
        ]

        for insight in insights:
            st.write(f"✓ {insight}")


        # -------------------------------------------------
        # TECH STACK
        # -------------------------------------------------

        st.markdown("## 🛠️ Technology Stack")

        st.markdown(
            """
            **Python** · Pandas · NumPy · Scikit-learn ·
            XGBoost · LightGBM · CatBoost · SHAP ·
            Matplotlib · Plotly · Streamlit · MySQL
            """
        )


        # -------------------------------------------------
        # PROJECT PIPELINE
        # -------------------------------------------------

        st.markdown("## 🔄 End-to-End Pipeline")

        pipeline_steps = [
            "Data Integration",
            "Data Cleaning",
            "Exploratory Data Analysis",
            "Feature Engineering",
            "Customer Segmentation",
            "Purchase Prediction",
            "CLV Prediction",
            "Explainable AI",
            "Streamlit Deployment"
        ]

        for i, step in enumerate(pipeline_steps, 1):

            st.markdown(
                f"""
                **{i}. {step}**
                """
            )


        # -------------------------------------------------
        # LINKS
        # -------------------------------------------------

        st.markdown("## 🔗 Project Links")

        col1, col2 = st.columns(2)

        with col1:

            st.link_button(
                "🐙 GitHub Repository",
                "https://github.com/divyanshsingh7800"
            )

        with col2:

            st.link_button(
                "🚀 Live Demo",
                "https://streamlit.io/"
            )
    # =====================================================
    # WIKIPEDIA RAG PROJECT
    # =====================================================

    elif project == "🧠 Wikipedia AI Knowledge Assistant":

        st.markdown(
            """
            # 🧠 Wikipedia Dynamic AI Knowledge Assistant

            ### Retrieval Augmented Generation system for dynamic knowledge retrieval
            """,
            unsafe_allow_html=True
        )

        st.write(
            """
            A Retrieval Augmented Generation (RAG) based AI knowledge assistant
            that dynamically retrieves information from Wikipedia and uses
            semantic search with an LLM to generate contextual answers.
            """
        )

        # -------------------------------------------------
        # PROJECT STATS
        # -------------------------------------------------

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Wikipedia Articles",
                "42"
            )

        with col2:
            st.metric(
                "Embedding Dimension",
                "384"
            )

        with col3:
            st.metric(
                "Top-1 Accuracy",
                "86.67%"
            )

        with col4:
            st.metric(
                "Top-3 Accuracy",
                "100%"
            )

        st.markdown("---")


        # -------------------------------------------------
        # PROBLEM
        # -------------------------------------------------

        st.markdown("## 🎯 Problem Statement")

        st.write(
            """
            Traditional question-answering systems depend heavily on the
            knowledge already stored inside the language model.

            This creates two major problems:

            • The model may not contain the latest information.

            • The model may hallucinate information when it does not have
            sufficient context.

            The objective of this project was to build a system that retrieves
            relevant external knowledge before generating an answer.
            """
        )


        # -------------------------------------------------
        # SOLUTION
        # -------------------------------------------------

        st.markdown("## 💡 Solution")

        st.write(
            """
            A complete RAG pipeline was implemented where Wikipedia acts as
            the external knowledge source.

            Instead of asking the LLM to answer directly, the system first
            retrieves relevant document chunks and then provides those chunks
            as context to the language model.
            """
        )


        # -------------------------------------------------
        # ARCHITECTURE
        # -------------------------------------------------

        st.markdown("## 🏗️ RAG Architecture")

        st.code(
            """
                        Wikipedia API
                            │
                            ▼
                    Article Collection
                            │
                            ▼
                        Text Cleaning
                            │
                            ▼
                        Chunking
                ┌───────────┼───────────┐
                ▼           ▼           ▼
            Fixed      Recursive    Semantic
                │           │           │
                └───────────┼───────────┘
                            ▼
                    Text Embeddings
                            │
                            ▼
                    Sentence Transformer
                    all-MiniLM-L6-v2
                            │
                            ▼
                        FAISS
                    Vector Index
                            │
    User Query ──────────────┤
                            ▼
                        Similarity
                        Retrieval
                            │
                            ▼
                    Retrieved Context
                            │
                            ▼
                        Gemma 2B
                            │
                            ▼
                    Final Answer
            """,
            language="text"
        )


        # -------------------------------------------------
        # DATA COLLECTION
        # -------------------------------------------------

        st.markdown("## 🌐 Data Collection")

        st.write(
            """
            Wikipedia was used as the external knowledge source.

            A total of 42 Wikipedia articles were dynamically downloaded
            through the Wikipedia API and processed for retrieval.
            """
        )

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Articles Collected",
                "42"
            )

        with col2:
            st.metric(
                "Knowledge Source",
                "Wikipedia API"
            )


        # -------------------------------------------------
        # CHUNKING
        # -------------------------------------------------

        st.markdown("## ✂️ Chunking Strategies")

        st.write(
            """
            Since long documents cannot be directly passed to the retrieval
            system efficiently, the documents were divided into smaller
            chunks.

            Three chunking strategies were evaluated.
            """
        )

        chunk_data = {
            "Method": [
                "Fixed Chunking",
                "Recursive Chunking",
                "Semantic Chunking"
            ],
            "Chunks": [
                2767,
                3105,
                1395
            ],
            "Processing Time": [
                "2.32 sec",
                "0.08 sec",
                "236.42 sec"
            ]
        }

        import pandas as pd

        chunk_df = pd.DataFrame(chunk_data)

        st.dataframe(
            chunk_df,
            use_container_width=True,
            hide_index=True
        )


        # -------------------------------------------------
        # CHUNKING INSIGHTS
        # -------------------------------------------------

        col1, col2, col3 = st.columns(3)

        with col1:

            st.markdown("### 📦 Fixed")

            st.write(
                """
                Splits text into chunks using a predefined size.

                Simple, fast and produced the best retrieval performance
                in this experiment.
                """
            )

        with col2:

            st.markdown("### 🔄 Recursive")

            st.write(
                """
                Recursively splits text while attempting to preserve
                meaningful boundaries.
                """
            )

        with col3:

            st.markdown("### 🧠 Semantic")

            st.write(
                """
                Attempts to create chunks based on semantic similarity.

                Produced fewer optimized chunks but required significantly
                more processing time.
                """
            )


        # -------------------------------------------------
        # EMBEDDINGS
        # -------------------------------------------------

        st.markdown("## 🔢 Text Embeddings")

        st.write(
            """
            Each document chunk was converted into a numerical vector using
            the Sentence Transformers model:

            `sentence-transformers/all-MiniLM-L6-v2`
            """
        )

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Embedding Model",
                "all-MiniLM-L6-v2"
            )

        with col2:

            st.metric(
                "Vector Dimension",
                "384"
            )


        # -------------------------------------------------
        # FAISS
        # -------------------------------------------------

        st.markdown("## 🔎 Vector Search with FAISS")

        st.write(
            """
            FAISS was used to efficiently store and search the generated
            embeddings.

            During inference, the user's query is converted into an embedding
            and compared against the indexed document vectors to retrieve
            the most relevant chunks.
            """
        )

        st.code(
            """
    User Query
        ↓
    Query Embedding
        ↓
    FAISS Similarity Search
        ↓
    Top-K Relevant Chunks
        ↓
    Context
            """,
            language="text"
        )


        # -------------------------------------------------
        # RETRIEVAL EVALUATION
        # -------------------------------------------------

        st.markdown("## 📊 Retrieval Evaluation")

        st.write(
            """
            Different chunking strategies were evaluated to determine which
            approach produced the most useful retrieval results.
            """
        )

        retrieval_data = {
            "Retrieval Method": [
                "Fixed Chunking",
                "Recursive Chunking",
                "Semantic Chunking"
            ],
            "Top-1 Accuracy": [
                "86.67%",
                "Evaluated",
                "Evaluated"
            ],
            "Top-3 Accuracy": [
                "100%",
                "Evaluated",
                "Evaluated"
            ]
        }

        retrieval_df = pd.DataFrame(retrieval_data)

        st.dataframe(
            retrieval_df,
            use_container_width=True,
            hide_index=True
        )

        st.success(
            "🏆 Best Retrieval Strategy: Fixed Chunking"
        )


        # -------------------------------------------------
        # LLM
        # -------------------------------------------------

        st.markdown("## 🤖 Language Model")

        st.write(
            """
            The retrieved context was passed to a lightweight language model
            to generate the final answer.

            **LLM:** Gemma 2B
            """
        )

        st.code(
            """
    Retrieved Context
            +
    User Question
            ↓
    Prompt Construction
            ↓
    Gemma 2B
            ↓
    Context-Aware Answer
            """,
            language="text"
        )


        # -------------------------------------------------
        # RAG PIPELINE
        # -------------------------------------------------

        st.markdown("## 🔄 Complete RAG Pipeline")

        pipeline = [
            "Collect Wikipedia articles",
            "Clean and preprocess text",
            "Generate chunks",
            "Create embeddings",
            "Build FAISS indexes",
            "Convert user query into embedding",
            "Retrieve relevant chunks",
            "Construct context",
            "Generate answer using Gemma 2B"
        ]

        for i, step in enumerate(pipeline, 1):

            st.markdown(
                f"**{i}. {step}**"
            )


        # -------------------------------------------------
        # KEY RESULTS
        # -------------------------------------------------

        st.markdown("## 🏆 Key Results")

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Top-1 Retrieval",
                "86.67%"
            )

        with col2:

            st.metric(
                "Top-3 Retrieval",
                "100%"
            )

        with col3:

            st.metric(
                "Best Method",
                "Fixed"
            )


        # -------------------------------------------------
        # LEARNINGS
        # -------------------------------------------------

        st.markdown("## 🧠 Key Learnings")

        learnings = [
            "Chunking strategy has a major impact on retrieval quality.",
            "Semantic chunking can produce fewer chunks but may have higher computational cost.",
            "Vector embeddings transform textual information into searchable numerical representations.",
            "FAISS enables efficient similarity search over large embedding collections.",
            "RAG allows an LLM to use external knowledge instead of relying only on parametric knowledge.",
            "Retrieval quality directly influences the quality of the final generated answer."
        ]

        for learning in learnings:

            st.write(
                f"✓ {learning}"
            )


        # -------------------------------------------------
        # TECH STACK
        # -------------------------------------------------

        st.markdown("## 🛠️ Technology Stack")

        st.markdown(
            """
            **Python** · Wikipedia API · Pandas · Sentence Transformers ·
            FAISS · Gemma 2B · Hugging Face · RAG
            """
        )


        # -------------------------------------------------
        # PROJECT LINKS
        # -------------------------------------------------

        st.markdown("## 🔗 Project Links")

        col1, col2 = st.columns(2)

        with col1:

            st.link_button(
                "🐙 GitHub Repository",
                "https://github.com/divyanshsingh7800"
            )

        with col2:

            st.link_button(
                "🚀 Live Demo",
                "https://streamlit.io/"
            )        

    elif project == "💬 Toxic Comment Detection":

        st.markdown(
            """
            # 💬 Toxic Comment Detection using LSTM

            ### Deep Learning based NLP system for toxic text classification
            """,
            unsafe_allow_html=True
        )

        st.write(
            """
            A Natural Language Processing and Deep Learning project designed
            to automatically identify toxic comments using an LSTM-based
            neural network.
            """
        )

        # -------------------------------------------------
        # PROJECT STATS
        # -------------------------------------------------

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Dataset Size",
                "159K+",
                "Comments"
            )

        with col2:
            st.metric(
                "Model",
                "LSTM"
            )

        with col3:
            st.metric(
                "Test Accuracy",
                "99.39%"
            )

        with col4:
            st.metric(
                "Problem Type",
                "Text Classification"
            )

        st.markdown("---")


        # -------------------------------------------------
        # PROBLEM
        # -------------------------------------------------

        st.markdown("## 🎯 Problem Statement")

        st.write(
            """
            Online platforms receive a huge volume of user-generated content.
            Manually identifying abusive or toxic comments is difficult and
            does not scale effectively.

            The goal of this project was to build an NLP model capable of
            automatically classifying comments based on their toxicity.
            """
        )


        # -------------------------------------------------
        # DATASET
        # -------------------------------------------------

        st.markdown("## 📊 Dataset")

        st.write(
            """
            The project used a large toxic-comment dataset containing more
            than 159,000 text records.

            The text data was transformed into numerical representations
            before being passed to the neural network.
            """
        )

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Total Records",
                "159,571"
            )

        with col2:
            st.metric(
                "Data Type",
                "Text"
            )


        # -------------------------------------------------
        # NLP PIPELINE
        # -------------------------------------------------

        st.markdown("## 🔤 NLP Preprocessing Pipeline")

        st.code(
            """
    Raw Comment
        ↓
    Text Cleaning
        ↓
    Tokenization
        ↓
    Vocabulary Creation
        ↓
    Sequence Conversion
        ↓
    Padding
        ↓
    LSTM Model
        ↓
    Toxic / Non-Toxic Prediction
            """,
            language="text"
        )


        # -------------------------------------------------
        # TOKENIZATION
        # -------------------------------------------------

        st.markdown("## 🔢 Text Tokenization")

        st.write(
            """
            Neural networks cannot directly process raw text.

            Therefore, comments were converted into sequences of numerical
            token IDs. Padding was then used to make sequences compatible
            with batch-based training.
            """
        )

        st.code(
            """
    Text
    ↓
    Tokenizer
    ↓
    Token IDs
    ↓
    Padding
    ↓
    Fixed-Length Input
            """,
            language="text"
        )


        # -------------------------------------------------
        # LSTM
        # -------------------------------------------------

        st.markdown("## 🧠 Why LSTM?")

        st.write(
            """
            LSTM (Long Short-Term Memory) networks are designed to process
            sequential data and maintain information from previous tokens.

            This makes LSTM suitable for NLP tasks where the meaning of a
            sentence depends on the relationship between words.
            """
        )

        st.code(
            """
    Word Sequence
        ↓
    Embedding
        ↓
    LSTM
        ↓
    Hidden Representation
        ↓
    Classification
        ↓
    Prediction
            """,
            language="text"
        )


        # -------------------------------------------------
        # MODEL
        # -------------------------------------------------

        st.markdown("## ⚙️ Model Architecture")

        st.write(
            """
            The core model was implemented using PyTorch and an LSTM-based
            architecture.
            """
        )

        st.code(
            """
    Input Text
        ↓
    Token IDs
        ↓
    Embedding Layer
        ↓
    LSTM
        ↓
    Fully Connected Layer
        ↓
    Classification Output
            """,
            language="text"
        )


        # -------------------------------------------------
        # TRAINING
        # -------------------------------------------------

        st.markdown("## 🏋️ Model Training")

        st.write(
            """
            The processed text sequences were supplied to the LSTM model
            through batches during training.

            The model learned patterns in the text that helped distinguish
            toxic comments from non-toxic content.
            """
        )

        st.markdown(
            """
            **Framework:** PyTorch

            **Architecture:** LSTM

            **Task:** Text Classification

            **Input:** Tokenized text sequences

            **Output:** Toxicity prediction
            """
        )


        # -------------------------------------------------
        # RESULTS
        # -------------------------------------------------

        st.markdown("## 📈 Model Results")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Training Accuracy",
                "99.36%"
            )

        with col2:

            st.metric(
                "Test Accuracy",
                "99.39%"
            )


        st.success(
            "🏆 Test Accuracy: 99.39%"
        )


        # -------------------------------------------------
        # PERFORMANCE
        # -------------------------------------------------

        st.markdown("## 📊 Performance")

        st.write(
            """
            The model achieved very high classification accuracy on the
            available test data, demonstrating its ability to learn useful
            textual patterns for toxicity detection.
            """
        )

        st.info(
            """
            Important: Accuracy alone should not be treated as the complete
            evaluation of a toxicity classifier. For a production system,
            Precision, Recall, F1-score and confusion matrix analysis should
            also be considered, particularly when classes are imbalanced.
            """
        )


        # -------------------------------------------------
        # BUSINESS / REAL WORLD APPLICATION
        # -------------------------------------------------

        st.markdown("## 🌍 Real-World Applications")

        applications = [
            "Social media moderation",
            "Online community moderation",
            "Comment filtering",
            "Content safety systems",
            "Automated moderation pipelines",
            "Online discussion platforms"
        ]

        for application in applications:
            st.write(f"✓ {application}")


        # -------------------------------------------------
        # CHALLENGES
        # -------------------------------------------------

        st.markdown("## ⚠️ Challenges")

        challenges = [
            "Natural language contains spelling variations and informal expressions.",
            "Toxicity can depend heavily on context.",
            "Some comments may be ambiguous.",
            "Class imbalance can affect model evaluation.",
            "High accuracy does not always guarantee robust real-world moderation."
        ]

        for challenge in challenges:
            st.write(f"• {challenge}")


        # -------------------------------------------------
        # TECH STACK
        # -------------------------------------------------

        st.markdown("## 🛠️ Technology Stack")

        st.markdown(
            """
            **Python** · Pandas · NumPy · PyTorch · NLP ·
            LSTM · Tokenization · Deep Learning
            """
        )


        # -------------------------------------------------
        # PROJECT PIPELINE
        # -------------------------------------------------

        st.markdown("## 🔄 End-to-End Pipeline")

        pipeline = [
            "Load toxic comment dataset",
            "Clean and preprocess text",
            "Tokenize comments",
            "Create numerical sequences",
            "Apply padding",
            "Prepare training and testing data",
            "Train LSTM model",
            "Evaluate model",
            "Generate toxicity predictions"
        ]

        for i, step in enumerate(pipeline, 1):
            st.markdown(
                f"**{i}. {step}**"
            )


        # -------------------------------------------------
        # KEY LEARNINGS
        # -------------------------------------------------

        st.markdown("## 🧠 Key Learnings")

        learnings = [
            "How raw text is converted into numerical sequences.",
            "How tokenization and padding prepare NLP data for neural networks.",
            "How LSTM processes sequential text information.",
            "How PyTorch can be used to build NLP deep learning models.",
            "Why multiple evaluation metrics are important for classification.",
            "How NLP models can be applied to real-world content moderation."
        ]

        for learning in learnings:
            st.write(f"✓ {learning}")


        # -------------------------------------------------
        # PROJECT LINKS
        # -------------------------------------------------

        st.markdown("## 🔗 Project Links")

        col1, col2 = st.columns(2)

        with col1:
            st.link_button(
                "🐙 GitHub Repository",
                "https://github.com/divyanshsingh7800"
            )

        with col2:
            st.link_button(
                "🚀 Live Demo",
                "https://streamlit.io/"
            )
# =====================================================
# TRAFFIC CRASH ANALYTICS
# =====================================================

    elif project == "🚦 Traffic Crash Analytics":

        st.markdown(
            """
            # 🚦 Traffic Crash Analytics & Safety Intelligence Platform

            ### Data-driven analysis of traffic crashes and road safety
            """,
            unsafe_allow_html=True
        )

        st.write(
            """
            An end-to-end data analytics platform built to analyze a large
            traffic crash dataset, identify accident patterns, discover
            high-risk conditions and transform raw crash records into
            actionable safety insights.
            """
        )

        # -------------------------------------------------
        # PROJECT STATS
        # -------------------------------------------------

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Crash Records",
                "700K+"
            )

        with col2:
            st.metric(
                "Features",
                "49"
            )

        with col3:
            st.metric(
                "Analytics",
                "SQL + Python"
            )

        with col4:
            st.metric(
                "Dashboard",
                "Streamlit"
            )

        st.markdown("---")


        # -------------------------------------------------
        # PROBLEM STATEMENT
        # -------------------------------------------------

        st.markdown("## 🎯 Problem Statement")

        st.write(
            """
            Traffic crash datasets contain a large amount of information
            about accidents, locations, contributing factors and other
            circumstances.

            However, raw crash records are difficult to interpret directly.

            The goal of this project was to transform a large-scale crash
            dataset into an interactive safety intelligence platform that
            could answer questions such as:

            • When do crashes occur most frequently?

            • What patterns are associated with crashes?

            • Which conditions are associated with higher crash frequency?

            • How can SQL and data visualization be used to extract safety
            insights from hundreds of thousands of records?
            """
        )


        # -------------------------------------------------
        # DATASET
        # -------------------------------------------------

        st.markdown("## 📊 Dataset")

        st.write(
            """
            The project used a large traffic crash dataset containing
            approximately 700,000 records and 49 columns.
            """
        )

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Rows",
                "700K+"
            )

        with col2:
            st.metric(
                "Columns",
                "49"
            )


        # -------------------------------------------------
        # DATA ANALYTICS PIPELINE
        # -------------------------------------------------

        st.markdown("## 🔄 Data Analytics Pipeline")

        st.code(
            """
    Raw Crash Data
        ↓
    Data Loading
        ↓
    Data Cleaning
        ↓
    Data Transformation
        ↓
    SQL Analysis
        ↓
    Exploratory Data Analysis
        ↓
    Pattern Discovery
        ↓
    Interactive Visualization
        ↓
    Streamlit Dashboard
            """,
            language="text"
        )


        # -------------------------------------------------
        # PYTHON
        # -------------------------------------------------

        st.markdown("## 🐍 Python Data Processing")

        st.write(
            """
            Python was used for data loading, preprocessing, transformation
            and exploratory analysis.

            Pandas provided the primary data manipulation layer while
            visualization tools were used to communicate important patterns.
            """
        )

        st.code(
            """
    import pandas as pd

    df = pd.read_csv(
        "Traffic_CrashesData.csv"
    )

    print(df.shape)
    print(df.info())
            """,
            language="python"
        )


        # -------------------------------------------------
        # SQL ANALYTICS
        # -------------------------------------------------

        st.markdown("## 🗄️ SQL Analytics")

        st.write(
            """
            SQL was used to perform structured analytical queries over the
            crash dataset.

            This allowed the project to answer business-style questions
            efficiently and generate aggregated safety metrics.
            """
        )

        st.markdown("### Example Analytical Questions")

        questions = [
            "How many crashes occurred?",
            "Which conditions are associated with higher crash frequency?",
            "What patterns can be observed across different crash attributes?",
            "How can crash records be aggregated for dashboard KPIs?",
            "Which categories contribute most to overall crash counts?"
        ]

        for question in questions:
            st.write(f"• {question}")


        st.markdown("### Example SQL Pattern")

        st.code(
            """
    SELECT
        category,
        COUNT(*) AS crash_count
    FROM traffic_crashes
    GROUP BY category
    ORDER BY crash_count DESC;
            """,
            language="sql"
        )


        # -------------------------------------------------
        # EDA
        # -------------------------------------------------

        st.markdown("## 📈 Exploratory Data Analysis")

        st.write(
            """
            Exploratory Data Analysis was used to understand the distribution
            of crash records and identify meaningful patterns within the data.
            """
        )

        eda_sections = [
            "Crash frequency analysis",
            "Categorical variable analysis",
            "Trend analysis",
            "Distribution analysis",
            "High-frequency category identification",
            "Relationship exploration"
        ]

        for item in eda_sections:
            st.write(f"✓ {item}")


        # -------------------------------------------------
        # KPI DASHBOARD
        # -------------------------------------------------

        st.markdown("## 📊 Safety Intelligence Dashboard")

        st.write(
            """
            The processed data was transformed into an interactive Streamlit
            dashboard.

            The dashboard focuses on presenting important crash statistics
            and analytical insights in an easy-to-understand format.
            """
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            st.markdown(
                """
                ### 🚨 Crash Overview

                Total crash records and major crash-level KPIs.
                """
            )

        with col2:

            st.markdown(
                """
                ### 📈 Trend Analysis

                Identify patterns and changes across relevant dimensions.
                """
            )

        with col3:

            st.markdown(
                """
                ### 🔎 Safety Insights

                Highlight important categories and patterns.
                """
            )


        # -------------------------------------------------
        # VISUALIZATION
        # -------------------------------------------------

        st.markdown("## 📊 Data Visualization")

        st.write(
            """
            Interactive visualizations help convert hundreds of thousands
            of raw records into understandable safety information.
            """
        )

        visualization_types = [
            "Bar charts",
            "Distribution plots",
            "Trend visualizations",
            "Category comparisons",
            "KPI cards",
            "Interactive filters"
        ]

        for visualization in visualization_types:
            st.write(f"• {visualization}")


        # -------------------------------------------------
        # BUSINESS VALUE
        # -------------------------------------------------

        st.markdown("## 💡 Business & Safety Value")

        insights = [
            "Transforms raw crash records into actionable information.",
            "Makes large-scale crash data easier to explore.",
            "Supports identification of important crash patterns.",
            "Provides an interactive interface for analytical exploration.",
            "Demonstrates practical SQL + Python data analytics.",
            "Creates a foundation for future predictive road-safety models."
        ]

        for insight in insights:
            st.write(f"✓ {insight}")


        # -------------------------------------------------
        # TECH STACK
        # -------------------------------------------------

        st.markdown("## 🛠️ Technology Stack")

        st.markdown(
            """
            **Python** · Pandas · NumPy · SQL · MySQL ·
            Matplotlib · Plotly · Streamlit
            """
        )


        # -------------------------------------------------
        # PROJECT WORKFLOW
        # -------------------------------------------------

        st.markdown("## 🔄 End-to-End Workflow")

        workflow = [
            "Collect traffic crash dataset",
            "Load data using Python",
            "Inspect and clean the dataset",
            "Transform analytical fields",
            "Run SQL analytical queries",
            "Perform exploratory data analysis",
            "Identify important crash patterns",
            "Create visualizations",
            "Build Streamlit dashboard",
            "Present safety intelligence"
        ]

        for i, step in enumerate(workflow, 1):

            st.markdown(
                f"**{i}. {step}**"
            )


        # -------------------------------------------------
        # KEY LEARNINGS
        # -------------------------------------------------

        st.markdown("## 🧠 Key Learnings")

        learnings = [
            "How to work with very large tabular datasets.",
            "How SQL can be combined with Python for analytics.",
            "How to convert business questions into analytical queries.",
            "How EDA helps discover patterns hidden inside raw data.",
            "How Streamlit can turn analytical work into an interactive application.",
            "How data visualization improves communication of analytical insights."
        ]

        for learning in learnings:
            st.write(f"✓ {learning}")


        # -------------------------------------------------
        # PROJECT LINKS
        # -------------------------------------------------

        st.markdown("## 🔗 Project Links")

        col1, col2 = st.columns(2)

        with col1:

            st.link_button(
                "🐙 GitHub Repository",
                "https://github.com/divyanshsingh7800"
            )

        with col2:

            st.link_button(
                "🚀 Live Dashboard",
                "https://streamlit.io/"
            )
# =====================================================
# AMAZON MUSIC ARTIST CLUSTERING
# =====================================================

    elif project == "🎵 Amazon Music Clustering":

        st.markdown(
            """
            # 🎵 Amazon Music Artist Clustering

            ### Unsupervised Machine Learning for discovering artist groups
            """,
            unsafe_allow_html=True
        )

        st.write(
            """
            An unsupervised Machine Learning project designed to discover
            natural groups of music artists based on their available
            numerical characteristics.

            The project combines feature scaling, dimensionality reduction
            and K-Means clustering to identify meaningful artist segments.
            """
        )

        # -------------------------------------------------
        # PROJECT STATS
        # -------------------------------------------------

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Learning Type",
                "Unsupervised"
            )

        with col2:
            st.metric(
                "Algorithm",
                "K-Means"
            )

        with col3:
            st.metric(
                "Best K",
                "3"
            )

        with col4:
            st.metric(
                "Silhouette Score",
                "0.2377"
            )

        st.markdown("---")


        # -------------------------------------------------
        # PROBLEM STATEMENT
        # -------------------------------------------------

        st.markdown("## 🎯 Problem Statement")

        st.write(
            """
            Music platforms contain artists with different musical
            characteristics and listening patterns.

            Without predefined labels, it can be difficult to understand
            which artists share similar characteristics.

            The objective of this project was to use unsupervised learning
            to automatically discover groups of similar artists.
            """
        )


        # -------------------------------------------------
        # DATASET
        # -------------------------------------------------

        st.markdown("## 📊 Dataset")

        st.write(
            """
            The project used the `single_genre_artists.csv` dataset.

            Since clustering is an unsupervised learning task, predefined
            target labels were not required for the clustering process.
            """
        )

        st.markdown(
            """
            **Dataset:** `single_genre_artists.csv`

            **Task:** Artist Clustering

            **Learning Type:** Unsupervised Learning
            """
        )


        # -------------------------------------------------
        # PIPELINE
        # -------------------------------------------------

        st.markdown("## 🔄 Machine Learning Pipeline")

        st.code(
            """
    Artist Dataset
        ↓
    Data Preparation
        ↓
    Feature Selection
        ↓
    StandardScaler
        ↓
    PCA
        ↓
    K-Means
        ↓
    Cluster Evaluation
        ↓
    Artist Segments
            """,
            language="text"
        )


        # -------------------------------------------------
        # FEATURE SCALING
        # -------------------------------------------------

        st.markdown("## ⚖️ Feature Scaling")

        st.write(
            """
            StandardScaler was applied before clustering so that features
            with different numerical scales would contribute more fairly
            to the distance calculations used by K-Means.
            """
        )

        st.code(
            """
    from sklearn.preprocessing import StandardScaler

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)
            """,
            language="python"
        )


        # -------------------------------------------------
        # WHY STANDARDIZATION?
        # -------------------------------------------------

        st.markdown("### Why StandardScaler?")

        st.write(
            """
            K-Means relies on distance calculations.

            If one feature has a much larger numerical range than another,
            it can dominate the clustering process.

            Standardization transforms features approximately to:

            Mean = 0

            Standard Deviation = 1
            """
        )


        # -------------------------------------------------
        # PCA
        # -------------------------------------------------

        st.markdown("## 🧩 Principal Component Analysis — PCA")

        st.write(
            """
            PCA was used for dimensionality reduction.

            The purpose was to represent the original feature space using
            fewer principal components while retaining important variation
            in the data.
            """
        )

        st.code(
            """
    from sklearn.decomposition import PCA

    pca = PCA(
        n_components=2
    )

    X_pca = pca.fit_transform(X_scaled)
            """,
            language="python"
        )


        # -------------------------------------------------
        # WHY PCA?
        # -------------------------------------------------

        st.markdown("### Why PCA?")

        reasons = [
            "Reduce dimensionality.",
            "Remove redundant information.",
            "Make high-dimensional data easier to visualize.",
            "Create a compact representation for exploratory clustering.",
            "Help visualize clusters in two dimensions."
        ]

        for reason in reasons:
            st.write(f"✓ {reason}")


        # -------------------------------------------------
        # K-MEANS
        # -------------------------------------------------

        st.markdown("## 🎯 K-Means Clustering")

        st.write(
            """
            K-Means was used to divide artists into groups based on
            similarity in the transformed feature space.
            """
        )

        st.code(
            """
    from sklearn.cluster import KMeans

    kmeans = KMeans(
        n_clusters=3,
        random_state=42
    )

    clusters = kmeans.fit_predict(X_pca)
            """,
            language="python"
        )


        # -------------------------------------------------
        # CHOOSING K
        # -------------------------------------------------

        st.markdown("## 🔍 Selecting the Number of Clusters")

        st.write(
            """
            Different values of K were evaluated to determine an appropriate
            number of clusters.

            The final selected value was:
            """
        )

        st.success(
            "🏆 Best Number of Clusters (K) = 3"
        )


        # -------------------------------------------------
        # SILHOUETTE
        # -------------------------------------------------

        st.markdown("## 📐 Silhouette Score")

        st.write(
            """
            The Silhouette Score was used to evaluate the quality of the
            clustering structure.

            It measures how similar a data point is to its own cluster
            compared with other clusters.
            """
        )

        st.metric(
            "Best Silhouette Score",
            "0.2377"
        )

        st.info(
            """
            The score indicates that the discovered clusters have some
            structure, although there is also overlap between artist groups.
            """
        )


        # -------------------------------------------------
        # CLUSTER INTERPRETATION
        # -------------------------------------------------

        st.markdown("## 👥 Artist Segments")

        cluster_data = {
            "Cluster": [
                "Cluster 0",
                "Cluster 1",
                "Cluster 2"
            ],
            "Interpretation": [
                "Artists with similar feature patterns",
                "Artists with different feature characteristics",
                "Another distinct artist group"
            ]
        }

        import pandas as pd

        cluster_df = pd.DataFrame(cluster_data)

        st.dataframe(
            cluster_df,
            use_container_width=True,
            hide_index=True
        )


        # -------------------------------------------------
        # VISUALIZATION
        # -------------------------------------------------

        st.markdown("## 📊 Cluster Visualization")

        st.write(
            """
            PCA reduced the feature space to two dimensions, allowing the
            discovered artist groups to be visualized on a 2D plane.
            """
        )

        # Demo visualization when actual dataset is not loaded
        st.info(
            """
            📌 Interactive PCA cluster visualization will be connected
            to the original dataset when the portfolio project files are
            added.
            """
        )


        # -------------------------------------------------
        # BUSINESS VALUE
        # -------------------------------------------------

        st.markdown("## 💡 Potential Applications")

        applications = [
            "Artist recommendation systems",
            "Music discovery",
            "Playlist generation",
            "Artist similarity analysis",
            "Music catalog segmentation",
            "Exploratory analysis of artist characteristics"
        ]

        for application in applications:
            st.write(f"✓ {application}")


        # -------------------------------------------------
        # TECH STACK
        # -------------------------------------------------

        st.markdown("## 🛠️ Technology Stack")

        st.markdown(
            """
            **Python** · Pandas · NumPy · Scikit-learn ·
            StandardScaler · PCA · K-Means · Matplotlib
            """
        )


        # -------------------------------------------------
        # END-TO-END WORKFLOW
        # -------------------------------------------------

        st.markdown("## 🔄 End-to-End Workflow")

        workflow = [
            "Load artist dataset",
            "Select relevant numerical features",
            "Standardize features using StandardScaler",
            "Apply PCA for dimensionality reduction",
            "Experiment with different K values",
            "Train K-Means clustering model",
            "Evaluate clusters using Silhouette Score",
            "Select K = 3",
            "Analyze resulting artist groups",
            "Visualize clusters"
        ]

        for i, step in enumerate(workflow, 1):

            st.markdown(
                f"**{i}. {step}**"
            )


        # -------------------------------------------------
        # KEY LEARNINGS
        # -------------------------------------------------

        st.markdown("## 🧠 Key Learnings")

        learnings = [
            "How unsupervised learning can discover hidden groups without target labels.",
            "Why feature scaling is important for distance-based algorithms.",
            "How PCA reduces dimensionality while preserving important information.",
            "How K-Means assigns observations to clusters.",
            "How the Silhouette Score helps evaluate clustering quality.",
            "How clustering can support recommendation and segmentation systems."
        ]

        for learning in learnings:
            st.write(f"✓ {learning}")


        # -------------------------------------------------
        # PROJECT LINKS
        # -------------------------------------------------

        st.markdown("## 🔗 Project Links")

        col1, col2 = st.columns(2)

        with col1:

            st.link_button(
                "🐙 GitHub Repository",
                "https://github.com/divyanshsingh7800"
            )

        with col2:

            st.link_button(
                "🚀 Live Demo",
                "https://streamlit.io/"
            )
# =====================================================
# YOUTUBE AD REVENUE PREDICTION
# =====================================================

    elif project == "📈 YouTube Revenue Prediction":

        st.markdown(
            """
            # 📈 YouTube Ad Revenue Prediction

            ### Machine Learning regression system for advertising revenue estimation
            """,
            unsafe_allow_html=True
        )

        st.write(
            """
            A supervised Machine Learning project designed to predict
            YouTube advertising revenue using historical channel and
            content-related data.
            """
        )

        # -------------------------------------------------
        # PROJECT STATS
        # -------------------------------------------------

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "ML Task",
                "Regression"
            )

        with col2:
            st.metric(
                "Selected Model",
                "Linear Regression"
            )

        with col3:
            st.metric(
                "Test R²",
                "0.9531"
            )

        with col4:
            st.metric(
                "Test MAE",
                "~3.09"
            )

        st.markdown("---")


        # -------------------------------------------------
        # PROBLEM STATEMENT
        # -------------------------------------------------

        st.markdown("## 🎯 Problem Statement")

        st.write(
            """
            YouTube creators and digital platforms generate revenue through
            advertising, but advertising revenue can vary significantly
            depending on different channel and content characteristics.

            The objective of this project was to build a Machine Learning
            regression model capable of estimating advertising revenue from
            historical data.
            """
        )


        # -------------------------------------------------
        # DATASET
        # -------------------------------------------------

        st.markdown("## 📊 Dataset")

        st.write(
            """
            The project used a cleaned YouTube advertising revenue dataset
            containing relevant numerical and categorical information
            associated with revenue generation.
            """
        )

        st.markdown(
            """
            **Dataset:** `youtube_ad_revenue_cleaned_dataset.csv`

            **Task:** Revenue Prediction

            **Learning Type:** Supervised Learning

            **Problem Type:** Regression
            """
        )


        # -------------------------------------------------
        # ML PIPELINE
        # -------------------------------------------------

        st.markdown("## 🔄 Machine Learning Pipeline")

        st.code(
            """
    Raw Dataset
        ↓
    Data Cleaning
        ↓
    Exploratory Data Analysis
        ↓
    Feature Engineering
        ↓
    Train / Test Split
        ↓
    Model Training
        ↓
    Prediction
        ↓
    Model Evaluation
        ↓
    Revenue Estimation
            """,
            language="text"
        )


        # -------------------------------------------------
        # DATA PREPROCESSING
        # -------------------------------------------------

        st.markdown("## 🧹 Data Preprocessing")

        st.write(
            """
            Before model training, the dataset was cleaned and prepared
            for regression modeling.

            The preprocessing stage focused on making the data suitable
            for supervised learning and reducing issues that could negatively
            affect model performance.
            """
        )

        preprocessing = [
            "Data cleaning",
            "Handling relevant data-quality issues",
            "Feature preparation",
            "Exploratory analysis",
            "Train-test split"
        ]

        for item in preprocessing:
            st.write(f"✓ {item}")


        # -------------------------------------------------
        # REGRESSION
        # -------------------------------------------------

        st.markdown("## 📈 Regression Modeling")

        st.write(
            """
            Since advertising revenue is a continuous numerical value,
            the problem was formulated as a regression task.

            Multiple regression approaches were explored before selecting
            the final model.
            """
        )

        st.code(
            """
    from sklearn.linear_model import LinearRegression

    model = LinearRegression()

    model.fit(
        X_train,
        y_train
    )

    predictions = model.predict(
        X_test
    )
            """,
            language="python"
        )


        # -------------------------------------------------
        # MODEL SELECTION
        # -------------------------------------------------

        st.markdown("## 🏆 Selected Model")

        st.success(
            "Linear Regression — Final Model"
        )

        st.write(
            """
            Linear Regression produced strong performance on the test
            dataset and was selected as the final model for this project.
            """
        )


        # -------------------------------------------------
        # RESULTS
        # -------------------------------------------------

        st.markdown("## 📊 Model Performance")

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "R² Score",
                "0.9531"
            )

        with col2:

            st.metric(
                "RMSE",
                "~13.423"
            )

        with col3:

            st.metric(
                "MAE",
                "~3.0905"
            )

        st.success(
            "🏆 Test R² = 0.9531"
        )


        # -------------------------------------------------
        # METRIC EXPLANATION
        # -------------------------------------------------

        st.markdown("## 📐 Evaluation Metrics")

        st.markdown(
            """
            ### R² Score

            Measures how much variance in the target variable is explained
            by the model.

            **R² = 0.9531** indicates that the model explains approximately
            95.31% of the variance in the test data.

            ### RMSE

            Measures the square root of the average squared prediction error.

            **RMSE ≈ 13.423**

            ### MAE

            Measures the average absolute difference between actual and
            predicted values.

            **MAE ≈ 3.0905**
            """
        )


        # -------------------------------------------------
        # WHY LINEAR REGRESSION?
        # -------------------------------------------------

        st.markdown("## 💡 Why Linear Regression?")

        reasons = [
            "Simple and interpretable baseline model.",
            "Fast to train and evaluate.",
            "Works well when relationships between features and target are approximately linear.",
            "Provides easily interpretable coefficients.",
            "Achieved strong test performance in this project."
        ]

        for reason in reasons:
            st.write(f"✓ {reason}")


        # -------------------------------------------------
        # BUSINESS VALUE
        # -------------------------------------------------

        st.markdown("## 💼 Business Applications")

        applications = [
            "Estimate potential advertising revenue.",
            "Support creator revenue planning.",
            "Analyze factors associated with revenue generation.",
            "Assist in content performance analysis.",
            "Support data-driven monetization decisions."
        ]

        for application in applications:
            st.write(f"✓ {application}")


        # -------------------------------------------------
        # VISUALIZATION
        # -------------------------------------------------

        st.markdown("## 📊 Model Visualization")

        st.info(
            """
            Interactive Actual vs Predicted revenue visualization can be
            connected here when the trained model and test predictions are
            added to the portfolio repository.
            """
        )


        # -------------------------------------------------
        # TECH STACK
        # -------------------------------------------------

        st.markdown("## 🛠️ Technology Stack")

        st.markdown(
            """
            **Python** · Pandas · NumPy · Scikit-learn ·
            Matplotlib · Regression · Machine Learning
            """
        )


        # -------------------------------------------------
        # END-TO-END WORKFLOW
        # -------------------------------------------------

        st.markdown("## 🔄 End-to-End Workflow")

        workflow = [
            "Load YouTube revenue dataset",
            "Inspect dataset structure",
            "Clean the data",
            "Perform exploratory data analysis",
            "Prepare model features",
            "Separate features and target",
            "Split data into training and testing sets",
            "Train regression models",
            "Generate predictions",
            "Evaluate using R², RMSE and MAE",
            "Select Linear Regression",
            "Use model for revenue estimation"
        ]

        for i, step in enumerate(workflow, 1):

            st.markdown(
                f"**{i}. {step}**"
            )


        # -------------------------------------------------
        # KEY LEARNINGS
        # -------------------------------------------------

        st.markdown("## 🧠 Key Learnings")

        learnings = [
            "How to formulate a business problem as a regression task.",
            "How to prepare real-world data for Machine Learning.",
            "How to train and evaluate regression models.",
            "How R², RMSE and MAE measure model performance.",
            "Why a simple model can sometimes outperform more complex approaches.",
            "How Machine Learning can support revenue forecasting."
        ]

        for learning in learnings:
            st.write(f"✓ {learning}")


        # -------------------------------------------------
        # PROJECT LINKS
        # -------------------------------------------------

        st.markdown("## 🔗 Project Links")

        col1, col2 = st.columns(2)

        with col1:

            st.link_button(
                "🐙 GitHub Repository",
                "https://github.com/divyanshsingh7800"
            )

        with col2:

            st.link_button(
                "🚀 Live Demo",
                "https://streamlit.io/"
            )
# =========================================================
# AI / ML JOURNEY
# =========================================================

elif page == "📚 AI/ML Journey":

    st.markdown(
        "## 📚 AI/ML Learning Journey"
    )

    st.write(
        """
        My journey from Python and Data Analytics to Machine Learning,
        Deep Learning, NLP, Transformers, LLMs and RAG.
        """
    )

    st.markdown("---")

    # =====================================================
    # JOURNEY DATA
    # =====================================================

    journey = [

        {
            "number": "01",
            "icon": "🐍",
            "title": "Python & Data",
            "description":
                "Python programming, NumPy, Pandas, SQL, "
                "data cleaning and exploratory data analysis.",
            "skills":
                "Python • NumPy • Pandas • SQL • EDA"
        },

        {
            "number": "02",
            "icon": "🤖",
            "title": "Machine Learning",
            "description":
                "Supervised and unsupervised learning with "
                "feature engineering and model evaluation.",
            "skills":
                "Regression • Classification • K-Means • XGBoost • CatBoost"
        },

        {
            "number": "03",
            "icon": "🧠",
            "title": "Deep Learning",
            "description":
                "Neural networks and sequence models using "
                "PyTorch.",
            "skills":
                "PyTorch • CNN • RNN • LSTM"
        },

        {
            "number": "04",
            "icon": "💬",
            "title": "Natural Language Processing",
            "description":
                "Processing and understanding human language "
                "using modern NLP techniques.",
            "skills":
                "Tokenization • Embeddings • LSTM • BERT • RoBERTa"
        },

        {
            "number": "05",
            "icon": "🔄",
            "title": "Transformers",
            "description":
                "Understanding the Transformer architecture and "
                "the attention mechanism behind modern NLP models.",
            "skills":
                "Self-Attention • Multi-Head Attention • Positional Encoding"
        },

        {
            "number": "06",
            "icon": "✨",
            "title": "LLMs & Generative AI",
            "description":
                "Working with modern Large Language Models and "
                "Generative AI technologies.",
            "skills":
                "GPT • Gemma • LLaMA • Mistral • Hugging Face"
        },

        {
            "number": "07",
            "icon": "🔎",
            "title": "Retrieval Augmented Generation",
            "description":
                "Building knowledge-grounded AI systems using "
                "retrieval, embeddings and vector search.",
            "skills":
                "Chunking • Embeddings • FAISS • Retrieval • RAG"
        },

        {
            "number": "08",
            "icon": "🚀",
            "title": "Deployment",
            "description":
                "Turning AI/ML models into usable applications "
                "and interactive dashboards.",
            "skills":
                "Streamlit • Git • GitHub • Deployment"
        }
    ]


    # =====================================================
    # JOURNEY CARDS
    # =====================================================

    for i in range(0, len(journey), 2):

        col1, col2 = st.columns(2)

        # -------------------------------------------------
        # CARD 1
        # -------------------------------------------------

        with col1:

            item = journey[i]

            st.markdown(
                f"### {item['icon']} {item['title']}"
            )

            st.caption(
                f"STEP {item['number']}"
            )

            st.write(
                item["description"]
            )

            st.info(
                item["skills"]
            )


        # -------------------------------------------------
        # CARD 2
        # -------------------------------------------------

        if i + 1 < len(journey):

            with col2:

                item = journey[i + 1]

                st.markdown(
                    f"### {item['icon']} {item['title']}"
                )

                st.caption(
                    f"STEP {item['number']}"
                )

                st.write(
                    item["description"]
                )

                st.info(
                    item["skills"]
                )

        st.markdown("---")


    # =====================================================
    # CURRENT FOCUS
    # =====================================================

    st.markdown("## 🎯 Current Focus")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown("### 🤖 Transformers")

        st.write(
            """
            Deep understanding of Transformer architecture,
            attention and modern NLP models.
            """
        )

    with col2:

        st.markdown("### ✨ LLMs")

        st.write(
            """
            Hugging Face Transformers, LLM inference,
            prompting and text generation.
            """
        )

    with col3:

        st.markdown("### 🔎 RAG")

        st.write(
            """
            Chunking, embeddings, vector search,
            retrieval evaluation and RAG pipelines.
            """
        )


    # =====================================================
    # JOURNEY SUMMARY
    # =====================================================

    st.markdown("## 🧩 My AI/ML Stack")

    st.code(
        """
Python
  │
  ├── Data Analytics
  │      ├── NumPy
  │      ├── Pandas
  │      └── SQL
  │
  ├── Machine Learning
  │      ├── Scikit-learn
  │      ├── XGBoost
  │      └── CatBoost
  │
  ├── Deep Learning
  │      └── PyTorch
  │
  ├── NLP
  │      ├── LSTM
  │      ├── BERT
  │      └── RoBERTa
  │
  ├── Transformers
  │      └── Attention
  │
  ├── Generative AI
  │      ├── LLMs
  │      └── Hugging Face
  │
  └── RAG
         ├── Embeddings
         ├── FAISS
         └── Retrieval
        """,
        language="text"
    )

# =========================================================
# CERTIFICATIONS
# =========================================================

elif page == "🏆 Certifications":

    st.markdown(
        '<div class="section-title">Certifications</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        ### 🏆 AI/ML Certification

        **GUVI — AI/ML Program**

        Completed training covering:

        - Python
        - Machine Learning
        - Deep Learning
        - NLP
        - Transformers
        - LLMs
        - RAG

        """
    )


# =========================================================
# RESUME
# =========================================================

elif page == "📄 Resume":

    st.markdown(
        "## 📄 Resume"
    )

    st.write(
        """
        My resume highlights my AI/ML projects, technical skills,
        education, certifications and practical experience.
        """
    )

    st.markdown("---")

    # =====================================================
    # PROFILE HEADER
    # =====================================================

    st.markdown(
        """
        # Divyansh Singh

        ### AI/ML Developer

        **Python • Machine Learning • Deep Learning • NLP • LLMs • RAG**
        """
    )

    st.markdown("---")


    # =====================================================
    # PROFESSIONAL SUMMARY
    # =====================================================

    st.markdown("## 👨‍💻 Professional Summary")

    st.write(
        """
        Aspiring AI/ML Developer focused on building practical
        Machine Learning, Deep Learning, NLP and Generative AI
        applications using Python.

        Hands-on experience with end-to-end ML workflows including
        data preprocessing, exploratory data analysis, feature
        engineering, model training, evaluation, explainability
        and deployment.

        Currently focused on Transformers, Large Language Models
        and Retrieval Augmented Generation.
        """
    )


    # =====================================================
    # CORE SKILLS
    # =====================================================

    st.markdown("## 🛠️ Core Skills")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            """
            **Programming**

            Python · SQL

            **Machine Learning**

            Scikit-learn · XGBoost · LightGBM · CatBoost ·
            K-Means · Feature Engineering

            **Deep Learning**

            PyTorch · CNN · RNN · LSTM
            """
        )

    with col2:

        st.markdown(
            """
            **NLP**

            Tokenization · Embeddings · BERT · RoBERTa

            **Generative AI**

            LLMs · Hugging Face · RAG · FAISS ·
            Prompt Engineering

            **Tools**

            Git · GitHub · MySQL · Streamlit
            """
        )


    # =====================================================
    # FEATURED PROJECTS
    # =====================================================

    st.markdown("## 🚀 Featured Projects")

    projects = [
        (
            "🛒 Intelligent E-Commerce Customer Analytics",
            "Customer segmentation, repeat purchase prediction, "
            "CLV prediction and SHAP explainability."
        ),

        (
            "🧠 Wikipedia Dynamic AI Knowledge Assistant",
            "RAG pipeline using Wikipedia API, embeddings, FAISS "
            "and Gemma 2B."
        ),

        (
            "💬 Toxic Comment Detection",
            "NLP text classification using an LSTM-based "
            "PyTorch model."
        ),

        (
            "🚦 Traffic Crash Analytics",
            "Large-scale traffic crash analytics using Python, "
            "SQL and Streamlit."
        )
    ]

    for title, description in projects:

        st.markdown(
            f"### {title}"
        )

        st.write(
            description
        )


    # =====================================================
    # CERTIFICATION
    # =====================================================

    st.markdown("## 🏆 Certification")

    st.markdown(
        """
        **GUVI — AI/ML Program**

        Completed training covering Python, Machine Learning,
        Deep Learning, NLP, Transformers, LLMs and RAG.
        """
    )


    # =====================================================
    # EDUCATION
    # =====================================================

    st.markdown("## 🎓 Education")

    st.markdown(
        """
        **Bachelor of Computer Applications (BCA)**

        Computer Applications / Computer Science related studies
        """
    )


# =========================================================
# DOWNLOAD RESUME
# =========================================================

    st.markdown("---")

    st.markdown("## 📥 Download Full Resume")

    try:

        with open("assets/Divyansh Singh resume.pdf", "rb") as file:
            resume_data = file.read()

        st.download_button(
            label="📄 Download My Resume",
            data=resume_data,
            file_name="Divyansh_Singh_AI_ML_Engineer_Resume.pdf",
            mime="application/pdf",
            use_container_width=True
        )

    except FileNotFoundError:

        st.error(
            "Resume PDF not found. Please add your CV as "
            "`assets/Divyansh Singh resume.pdf`."
        )

    # =====================================================
    # CONTACT CTA
    # =====================================================

    st.markdown("---")

    st.markdown(
        """
        ### 🚀 Interested in working together?

        I'm open to AI/ML opportunities, projects and collaborations.
        """
    )

    col1, col2 = st.columns(2)

    with col1:

        st.link_button(
            "💼 LinkedIn",
            "https://www.linkedin.com/in/divyansh-singh-7973433a0/",
            use_container_width=True
        )

    with col2:

        st.link_button(
            "🐙 GitHub",
            "https://github.com/divyanshsingh7800",
            use_container_width=True
        )



# =========================================================
# CONTACT
# =========================================================

elif page == "📬 Contact":

    st.markdown(
        "## 📬 Let's Connect"
    )

    st.write(
        """
        I'm open to AI/ML opportunities, interesting projects,
        collaborations and professional discussions.
        """
    )

    st.markdown("---")

    # =====================================================
    # CONTACT INFORMATION
    # =====================================================

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### 📧 Email")

        st.write(
            "singhanuj04639@gmail.com"
        )

        st.link_button(
            "Send Email",
            "mailto:singhanuj04639@gmail.com",
            use_container_width=True
        )


    with col2:

        st.markdown("### 📱 Phone")

        st.write(
            "+91 7393847800"
        )

        st.link_button(
            "Call Me",
            "tel:+917393847800",
            use_container_width=True
        )


    st.markdown("---")


    # =====================================================
    # SOCIAL PROFILES
    # =====================================================

    st.markdown("## 🌐 Professional Profiles")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### 🐙 GitHub")

        st.write(
            "My AI/ML projects, source code and development work."
        )

        st.link_button(
            "Visit GitHub",
            "https://github.com/divyanshsingh7800",
            use_container_width=True
        )


    with col2:

        st.markdown("### 💼 LinkedIn")

        st.write(
            "Connect with me professionally and follow my AI/ML journey."
        )

        st.link_button(
            "Visit LinkedIn",
            "https://www.linkedin.com/in/divyansh-singh-7973433a0/",
            use_container_width=True
        )


    st.markdown("---")


    # =====================================================
    # CONTACT CTA
    # =====================================================

    st.markdown(
        """
        <div style="
            text-align:center;
            padding:35px 20px;
        ">

        <h2>🚀 Let's Build Something Intelligent</h2>

        <p style="color:#94a3b8; font-size:17px;">
        AI/ML Development • Machine Learning • Deep Learning •
        NLP • LLMs • RAG
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.link_button(
            "📧 Email Me",
            "mailto:singhanuj04639@gmail.com",
            use_container_width=True
        )

    with col2:
        st.link_button(
            "🐙 GitHub",
            "https://github.com/divyanshsingh7800",
            use_container_width=True
        )

    with col3:
        st.link_button(
            "💼 LinkedIn",
            "https://www.linkedin.com/in/divyansh-singh-7973433a0/",
            use_container_width=True
        )

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown(
    """
    <center>
    Built with 🐍 Python & ❤️ using Streamlit
    <br>
    © 2026 Divyansh Singh
    </center>
    """,
    unsafe_allow_html=True
)

