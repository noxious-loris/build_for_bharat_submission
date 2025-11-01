import streamlit as st
import requests

st.set_page_config(page_title="Rainfall Comparison", page_icon="🌧️", layout="centered")

st.title("🌦️ Rainfall Comparison App")

question = st.text_input("Ask about rainfall:", "Compare rainfall between Kerala and Maharashtra from 2010 to 2024")

if st.button("Ask"):
    with st.spinner("Fetching data from backend..."):
        try:
            response = requests.post(
                "http://127.0.0.1:8000/ask",  # FastAPI endpoint
                json={"question": question},
                timeout=10,
            )

            if response.status_code == 200:
                result = response.json()

                st.success("✅ Response received successfully!")
                st.markdown(f"**Answer:** {result.get('answer', 'No answer returned')}")

                # Display detailed data if available
                if "data" in result:
                    st.subheader("📊 Detailed Data")
                    for state, data in result["data"].items():
                        st.markdown(f"**{state}:**")
                        st.dataframe(data)

            else:
                st.error(f"⚠️ Server error: {response.status_code}")

        except requests.exceptions.RequestException as e:
            st.error(f"❌ Connection error: {e}")
