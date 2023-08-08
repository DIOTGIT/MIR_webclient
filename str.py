import streamlit as st
import MIR_status as m

a = st.title('egyedem, begye')
b = st.text('bla')

while True:
    b.text(m.get_status_uptime())
