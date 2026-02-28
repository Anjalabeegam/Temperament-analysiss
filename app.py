st.caption("Developed by Dr. Anjala Beegam, BUMS | Unani Physician")

import streamlit as st

st.set_page_config(page_title=" Temperament Analysis - Dr Anjala", page_icon="🌿")

st.title("🌿 Unani Temperament (Mizaj) Analysis")
st.write("Discover your dominant body temperament with a personalised Unani report by Dr. Anjala Beegam.")

st.subheader("Enter Your Details")

name = st.text_input("Full Name")
age = st.number_input("Age", min_value=10, max_value=100)
instagram = st.text_input("Your Instagram Username")

st.subheader("Answer the Following Questions")

q1 = st.radio("1. Do you feel hot more often than others?", ["Yes", "No"])
q2 = st.radio("2. Is your skin usually dry?", ["Yes", "No"])
q3 = st.radio("3. Do you sweat easily?", ["Yes", "No"])
q4 = st.radio("4. Do you feel sluggish or heavy often?", ["Yes", "No"])
q5 = st.radio("5. Do you get angry quickly?", ["Yes", "No"])
q6 = st.radio("6. Do you prefer warm climate?", ["Yes", "No"])
q7 = st.radio("7. Do you experience acidity frequently?", ["Yes", "No"])
q8 = st.radio("8. Do you feel cold easily?", ["Yes", "No"])
q9 = st.radio("9. Do you make decisions quickly without overthinking?", ["Yes", "No"])
q10 =  st.radio("9. Do you feel emotionally sensitive and easily hurt?", ["Yes", "No"])
q11 =  st.radio("9. Do you prefer solitude over social gatherings?", ["Yes", "No"])
q12 =  st.radio("9. Do you lose patience if things move slowly?", ["Yes", "No"])
q13 =  st.radio("9. Do you feel sleepy immediately after eating?", ["Yes", "No"])
q14 =  st.radio("9. Is your body frame lean and well defined rather than soft?", ["Yes", "No"])
q15 =  st.radio("9. Do you gain weight easily even with normal eating?", ["Yes", "No"])
q16 =  st.radio("9. Do you hold on past hurts for a long time?", ["Yes", "No"])
q17 =  st.radio("9. Once you start something, do you feel compelled to finish it perfectly before moving on?", ["Yes", "No"])


if st.button("🔒 Reveal My Hidden Temperament"):

    st.markdown("---")
    st.subheader("💰 Payment Required – ₹49 Only")

    st.write("To unlock your personalised Unani Temperament Analysis, please complete the payment below.")

    st.info("UPI ID: 9847239664@yescred")

    st.write("After payment, please send the screenshot via Instagram DM to:")
    st.markdown("### 👉 @dr.anjala_beegam")

    st.write("Mention your full name used in this test.")

    st.warning("Your detailed temperament report will be delivered within 24 hours after payment verification.")

    st.success("Thank you for choosing Dr. Anjala Beegam's Unani Analysis 🌿")

st.markdown("---")
st.caption("© 2026 Dr. Anjala Beegam. All rights reserved.")
