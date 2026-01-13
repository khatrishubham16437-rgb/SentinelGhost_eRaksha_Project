import streamlit as st
import os

st.set_page_config(page_title="SentinelGhost AI Monitor", layout="wide")
st.title("🛡️ SentinelGhost: Real-time Threat Monitor")

col1, col2 = st.columns([1, 1])

with col1:
    st.header("🌐 Network Scan")
    # JSON file empty hai toh handle karega
    if os.path.exists('network_log.json'):
        with open('network_log.json', 'r') as f:
            st.json(f.read()) 
    else:
        st.info("Scanning...")

with col2:
    st.header("🪤 Captured Intruders")
    if os.path.exists('hacker_attempts.txt'):
        with open('hacker_attempts.txt', 'r') as f:
            log_data = f.read()
            # Tera raw text file yahan dikhega
            st.text_area("Live Intruder Logs", log_data, height=400)
            
            if "NEW INTRUDER CAPTURED" in log_data:
                st.error("🚨 ALERT: Intruder Detected in Honeypot!")
    else:
        st.success("System Secure")

# Refresh button
if st.button('Refresh Dashboard'):
    st.rerun()