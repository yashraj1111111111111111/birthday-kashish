import streamlit as st
import base64

# Set up the page configuration
st.set_page_config(
    page_title="Happy Birthday Kashish! 🎉",
    page_icon="👑",
    layout="centered"
)

# Helper function to convert files to base64 safely
def get_base64_encoded_file(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Injecting Custom CSS for premium animations, gradients, and custom fonts
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    
    .stApp {
        background: linear-gradient(135deg, #ffe4e6, #fbcfe8, #e0f2fe);
        background-size: 400% 400%;
        animation: gradientBg 12s ease infinite;
    }
    @keyframes gradientBg {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .birthday-card {
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(10px);
        padding: 40px;
        border-radius: 30px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.6);
        text-align: center;
    }
    
    .main-title {
        font-family: 'Poppins', sans-serif;
        font-weight: 800;
        background: linear-gradient(to right, #ec4899, #8b5cf6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.8rem;
        margin-bottom: 20px;
    }
    
    .cursive-letter {
        font-family: 'Sacramento', cursive;
        font-size: 3.5rem;
        color: #db2777;
        margin-top: 15px;
    }
    
    .balloon {
        position: absolute;
        font-size: 3rem;
        animation: floatUp 6s ease-in-out infinite alternate;
        opacity: 0.5;
    }
    @keyframes floatUp {
        0% { transform: translateY(0px) rotate(0deg); }
        100% { transform: translateY(-25px) rotate(6deg); }
    }
    
    .fade-in {
        animation: fadeInEffect 1.5s ease-out forwards;
    }
    @keyframes fadeInEffect {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    
    .grid-img {
        width: 100%;
        height: 180px;
        object-fit: cover;
        border-radius: 15px;
        border: 3px solid white;
        box-shadow: 0 4px 12px rgba(236,72,153,0.15);
    }
    </style>
""", unsafe_allow_html=True)

# Balloons Setup
st.markdown('<div class="balloon" style="top:10%; left:5%;">🎈</div>', unsafe_allow_html=True)
st.markdown('<div class="balloon" style="top:15%; right:5%; animation-delay:2s;">🎈</div>', unsafe_allow_html=True)

if "celebrated" not in st.session_state:
    st.session_state.celebrated = False

with st.container():
    st.markdown('<div class="birthday-card">', unsafe_allow_html=True)
    st.markdown('<h1 class="main-title">Happy Birthday, Kashish! 👑</h1>', unsafe_allow_html=True)
    
    # 2x2 Photo Grid Collage - Searching dynamically inside folders or main level
    try:
        # Check if files are in root directory or inside kashu subfolder
        import os
        prefix = "kashu/" if os.path.exists("kashu/sister1.jpg") else ""
        
        img1 = get_base64_encoded_file(f"{prefix}sister1.jpg")
        img2 = get_base64_encoded_file(f"{prefix}sister2.jpg")
        img3 = get_base64_encoded_file(f"{prefix}sister3.jpg")
        img4 = get_base64_encoded_file(f"{prefix}sister4.jpg")
        
        r1_c1, r1_c2 = st.columns(2)
        with r1_c1: st.markdown(f'<img src="data:image/jpeg;base64,{img1}" class="grid-img">', unsafe_allow_html=True)
        with r1_c2: st.markdown(f'<img src="data:image/jpeg;base64,{img2}" class="grid-img">', unsafe_allow_html=True)
        
        st.write("") 
        
        r2_c1, r2_c2 = st.columns(2)
        with r2_c1: st.markdown(f'<img src="data:image/jpeg;base64,{img3}" class="grid-img">', unsafe_allow_html=True)
        with r2_c2: st.markdown(f'<img src="data:image/jpeg;base64,{img4}" class="grid-img">', unsafe_allow_html=True)
    except Exception:
        st.info("🎨 Make sure your images (sister1.jpg, sister2.jpg, etc.) are named correctly and uploaded to GitHub!")

    if not st.session_state.celebrated:
        st.write("You're the absolute best sister in the entire world. Make a wish and blow out the candle below! 🎂")
        _, col2, _ = st.columns([1, 2, 1])
        with col2:
            if st.button("🌬️ Blow Out Candle & Open Gift", use_container_width=True):
                st.session_state.celebrated = True
                st.rerun()
    else:
        st.balloons()
                # Upgraded Audio rendering block triggered by button click
        try:
            import os
            prefix = "kashu/" if os.path.exists("kashu/birthday-song.mp3") else ""
            audio_base64 = get_base64_encoded_file(f"{prefix}birthday-song.mp3")
            
            # HTML5 Audio component with explicit browser play configurations
            st.markdown(f"""
                <audio autoplay="true" loop="true" style="display:none;">
                    <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
                </audio>
            """, unsafe_allow_html=True)
        except Exception:
            st.warning("🎵 Double-check that 'birthday-song.mp3' is named correctly in your repository!")


        st.markdown("""
            <div class="fade-in" style="background: linear-gradient(to bottom right, #fff5f5, #fff0f6); padding: 25px; border-radius: 20px; margin-top: 20px; border: 1px solid #fbcfe8;">
                <div class="cursive-letter">Dear Kashish...</div>
                <p style="color: #4b5563; font-size: 1.1rem; line-height: 1.7; font-family: 'Poppins', sans-serif;">
                    Wishing you a spectacular year ahead filled with infinite joy, success, and laughter! 
                    Here is a virtual coupon for a movie night, a giant dessert session, or anything your heart desires today.The best twin i found. 💖
                </p>
                <div style="font-size: 2.5rem; margin-top: 15px;">🎁 🍫 ✨</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

