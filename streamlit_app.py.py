import streamlit as st

#institution logo
st.image("logo.jpeg", width=100)

st.title("Mission 1:")
st.title("Desmos Coefficient Checker")

users = {
    "alpha": {   
        "name":"Team Alpha", #bat
        "changed_eqs": [5,6,7,14,16],
        "graph_img": "graphs/alpha.jpeg",  
        "wrong":   [9,5,4,10,2],
        "correct": [5,2,2,3,7],
        "desmos_link":"https://www.desmos.com/calculator/humiuhrtmi"
    },
    "bravo": {
        "name":"Team Bravo", #pattern
        "changed_eqs": [2,4,7,15,22],
        "graph_img": "graphs/bravo.jpeg",
        "wrong":   [5,5,13,2,6],
        "correct": [2,10,4,8,4],
        "desmos_link":"https://www.desmos.com/calculator/r7pg3mzlis"
    },
    "charlie": {
        "name":"Team Charlie", #spider
        "changed_eqs": [1,7,12,24,60],
        "graph_img": "graphs/charlie.jpeg",
        "wrong":   [8,27,27,13,55],
        "correct": [5,19,17,24,26],
        "desmos_link":"https://www.desmos.com/calculator/a1pwvc72te"
    },
    "delta": {
        "name":"Team Delta", #cat
        "changed_eqs": [9,15,21,23,28],
        "graph_img": "graphs/delta.jpeg",
        "wrong":   [15,17,12,10,16],
        "correct": [18,24,21,16,20],
        "desmos_link":"https://www.desmos.com/calculator/c5u3g1dxox"
    },
    "echo": {
        "name":"Team Echo", #yin yang
        "changed_eqs": [1,3,5,6,9],
        "graph_img": "graphs/echo.jpeg",
        "wrong":   [0.5,0.4,1,3.14,9],
        "correct": [1,1,2,1,3],
        "desmos_link":"https://www.desmos.com/calculator/r3cdfgceq7"
    },
    "shadow":{
        "name":"Team Shadow", #cat
        "changed_eqs": [9,15,21,23,28],
        "graph_img": "graphs/delta.jpeg",
        "wrong":   [15,17,12,10,16],
        "correct": [18,24,21,16,20],
        "desmos_link":"https://www.desmos.com/calculator/c5u3g1dxox"
    }
}

# --- Step 1: Key Entry ---
st.subheader("Team Name:")
key = st.text_input("", type="password").lower()

if key:
    try:
        if key not in users:
            st.error("Invalid team name! Please check with the supervisor.")
        else:
            user_info = users[key]
            st.success(f"Welcome, {user_info['name']}!")


            # Show Graph Image
            st.image(user_info["graph_img"], caption="Your Desmos Graph", use_container_width=True)

            ## Desmos graph
            desmos_link = user_info.get("desmos_link", "#")
            st.markdown(
                        f"[🔗 Open in Desmos]({desmos_link})",
                        unsafe_allow_html=True
                    )
            
            true_wrong  = user_info["wrong"]
            true_correct = user_info["correct"]
            eq_numbers   = user_info["changed_eqs"]
            
            st.markdown("### Enter BOTH your guessed **WRONG** and **CORRECT** coefficients:")

            user_wrong = []
            user_correct = []
            
            for i, eq_no in enumerate(eq_numbers):
                col1, col2 = st.columns(2)
                with col1:
                    w = st.number_input(
                        f"WRONG coefficient for **Equation {eq_no}**",
                        step=0.01, key=f"w_{i}"
                    )
                with col2:
                    c = st.number_input(
                        f"CORRECT coefficient for **Equation {eq_no}**",
                        step=0.01, key=f"c_{i}"
                    )
                user_wrong.append(w)
                user_correct.append(c)
                
            if st.button("Check My Answers"):
                if user_wrong == true_wrong and user_correct == true_correct:
                    st.balloons()
                    st.success("Perfect! All WRONG & CORRECT coefficients match!")
                else:
                    st.info("Keep trying!")

    except Exception as e:
        st.error(f"⚠️ Unexpected error occurred: {e}")

# --- Footer ---
footer = """
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #f1f1f1;
    color: #333;
    text-align: center;
    padding: 8px;
    font-size: 14px;
}
</style>
<div class="footer">
    Limited Access
</div>
"""
st.markdown(footer, unsafe_allow_html=True)