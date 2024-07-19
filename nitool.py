import streamlit as st
 
# Define the decision process
def process_flow(leak, damage, equipment_type, low_risk, thickness_available, remaining_life):
    if leak:
        return "Perform Temporary Repair (CR GR HSE 426)"
    elif damage:
        if equipment_type == "Non-pressure":
            return "Use NI Tool (Structure & Lifting) - Evaluate Acceptability"
        elif equipment_type == "Pressure":
            if low_risk:
                return "Acceptable (NC)"
            elif thickness_available:
                if remaining_life:
                    return "Use NI Tool"
                else:
                    return "Not Acceptable"
            else:
                return "Proceed with further Inspection"
    else:
        return "Generate Inspection Report"
 
# Streamlit app
st.title("NI Decision Process")
 
st.sidebar.title("Inspection Inputs")
leak = st.sidebar.checkbox("Leak?")
damage = st.sidebar.checkbox("Damage?")
 
if damage:
    equipment_type = st.sidebar.selectbox("Equipment Type", ["Non-pressure", "Pressure"])
    elif Non-pressure:
          equipment_type = st.sidebar.selectbox("Equipment Type", ["Jacket", "Lifting heavy", "Lifting secondary", "Main beam-col",:"Main beam-col"])
else:
    equipment_type = None
 
low_risk = st.sidebar.checkbox("Low Risk Fluid and No Rupture?") if damage and equipment_type == "Pressure" else False
thickness_available = st.sidebar.checkbox("Thickness Available?") if damage and equipment_type == "Pressure" and not low_risk else False
remaining_life = st.sidebar.checkbox("Acceptable Remaining Life (T > T_req before next inspection)?") if damage and equipment_type == "Pressure" and thickness_available else False
 
# Process the inputs and display the result
result = process_flow(leak, damage, equipment_type, low_risk, thickness_available, remaining_life)
st.markdown(f"### Decision: {result}")
 
# Chat input streamer
st.markdown("### Chat Input")
user_input = st.text_input("Enter your query or input:")
 
# Display the chat input
if user_input:
    st.write(f"You entered: {user_input}") 


