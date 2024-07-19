import streamlit as st

# Define the decision process
def process_flow(leak, damage, equipment_type, low_risk, thickness_available, remaining_life):
    if leak:
        return "<h4>Perform Temporary Repair (CR GR HSE 426)</h4>"
    elif damage:
        if equipment_type in ["Non-pressure", "Jacket", "Lifting heavy", "Lifting secondary", "Main beam-col"]:
            return "<h4>Use NI Tool (Structure & Lifting) - Evaluate Acceptability</h4>"
        elif equipment_type == "Pressure":
            if low_risk:
                return "<h4>Acceptable (NC)</h4>"
            elif thickness_available:
                if remaining_life:
                    return "<h4>Use NI Tool</h4>"
                else:
                    return "<h4>Not Acceptable</h4>"
            else:
                return "<h4>Proceed with further Inspection</h4><p>Detail steps based on GS-511...</p>"
    else:
        return "<h4>Generate Inspection Report</h4>"

# Streamlit app
st.markdown("<h2>NI Decision Process</h2>", unsafe_allow_html=True)

st.sidebar.markdown("<h3>Inspection Inputs</h3>", unsafe_allow_html=True)
leak = st.sidebar.checkbox("Leak?")
damage = st.sidebar.checkbox("Damage?")

if damage:
    equipment_type = st.sidebar.selectbox("Equipment Type", ["Non-pressure", "Pressure", "Jacket", "Lifting heavy", "Lifting secondary", "Main beam-col"])
else:
    equipment_type = None

low_risk = st.sidebar.checkbox("Low Risk Fluid and No Rupture?") if damage and equipment_type == "Pressure" else False
thickness_available = st.sidebar.checkbox("Thickness Available?") if damage and equipment_type == "Pressure" and not low_risk else False
remaining_life = st.sidebar.checkbox("Acceptable Remaining Life (T > T_req before next inspection)?") if damage and equipment_type == "Pressure" and thickness_available else False

# Process the inputs and display the result
result = process_flow(leak, damage, equipment_type, low_risk, thickness_available, remaining_life)
st.markdown(f"### Decision: {result}", unsafe_allow_html=True)

# Chat input streamer
st.markdown("<h3>Chat Input</h3>", unsafe_allow_html=True)
user_input = st.text_input("Enter your query or input:")

# Display the chat input
if user_input:
    st.write(f"You entered: {user_input}")