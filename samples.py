import streamlit as st
import os

sampleKnowledgeBaseText = '''
Narayana Health Insurance - AI Sales Assistant Knowledge Base
For Real-Time Sales Call Support
🚨 CRITICAL ELIGIBILITY CHECK
Narayana Aditi V3 - Geographic Restriction:
ONLY available in: Mysore, Chamraj Nagar, Coorg, Mandya, Hassan, Bengaluru, Ramanagara (Karnataka)
Always verify customer location first
🏥 Hospital Network Coverage
States: Karnataka, West Bengal, Delhi, Gujarat, Maharashtra, Rajasthan, Haryana, Assam, Chhattisgarh, Jharkhand, J&K
Key Hospitals:
Bangalore: Mazumdar Shaw Medical Centre, Narayana Institute of Cardiac Sciences
Ahmedabad: Narayana Multispeciality Hospital
Kolkata: Rabindranath Tagore International Institute
Delhi: Dharamshila Narayana Superspeciality Hospital
Gurugram: Narayana Superspeciality Hospital
💰 Product Portfolio & Pricing
1. Narayana Aditi V3 (Individual/Family)
Two Plans Available:
Plan 1: ₹1 Cr surgical + ₹5L non-surgical | ₹2K/day deductible on ALL claims
Plan 2: ₹1 Cr surgical + ₹5L non-surgical | ₹2K/day deductible ONLY on non-surgical
Sample Premium (Family: 45, 39, 9, 5 years):
Plan 1: ₹13,819 | Plan 2: ₹14,107
2. Arya Group Health Insurance (Corporate)
Key Features:
One Health Promise: Premium refund for surgical hospitalizations
Pre-hospitalization: 60 days | Post-hospitalization: 180 days
Annual health checkup mandatory (or 2.5% premium hike)
3. Narayana Group Health Insurance
Flexible corporate plans with optional coverage:
Maternity, Baby Cover, AYUSH treatments
AccumulatePlus & Revive options
Technological treatments covered
⏰ Waiting Periods
Narayana Aditi V3: NIL waiting period (after medical examination)
Arya Group: 30 days general, 24 months specific conditions, 36 months pre-existing
Group Health: 30 days general, 2 years specific, 3 years pre-existing
💳 Claims & Co-payment
Cashless: Available at Narayana network hospitals Co-payment:
Network hospitals: 0%
Non-network without intimation: 10-30% Processing: Pre-auth 1 hour, Discharge 3 hours, Settlement 15 days
🎯 Sales Strategy Points
Premium Reduction Tactics
Aggregate Deductible Option:
Merge existing corporate policy as deductible
Example: ₹69K premium → ₹35K with ₹5L corporate deductible
Key Objection Handlers
"Limited Network": Emphasize quality over quantity + emergency reimbursement "Third-party Issues": Our in-house claims = faster, hassle-free processing "Price Concerns": Family floater savings + comprehensive coverage value
OPD Benefits (Bangalore only)
9 clinics available
Free GP consultations (unlimited)
20% medicine discount
45% diagnostic discount
15% specialist consultation discount
5% cashback on all transactions
🌟 Unique Selling Points
Zero Waiting Period (post medical examination)
In-house Claims Processing (no TPA delays)
100% Reimbursement for emergencies at any hospital
Non-medical Charges Covered (unique feature)
Pre/Post Hospitalization extensive coverage
📋 Sales Process Checklist
Location Verification (eligibility check)
Family Composition (ages for premium calculation)
Existing Corporate Policy (deductible opportunity)
Medical History (waiting period implications)
eKYC Requirements (Bangalore address proof needed)
⚠️ Important Notes
No Claim Bonus: Not yet designed (be transparent)
Payment: Annual only (no monthly/quarterly options)
Emergency Protocol: 24-hour intimation required for non-network hospitals
Documentation: Pre/post hospitalization claims within 15 days
🎲 Quick Premium Calculator Reference
Age-based pricing increases significantly after 50+ Family floater always cheaper than individual policies Deductible options can reduce premium by 40-50%
'''

def main():

    file_path = "AUDIO-2025-03-02-12-43-14.mp3"
    with open(file_path, "rb") as f:
        file_bytes = f.read()
    st.markdown("""
        <style>
        /* Download button styling */
        .stDownloadButton button {
            background-color: #90ee90;
            color: black;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
            border: none;
        }
        .stDownloadButton button:hover {
            background-color: #77dd77;
            box-shadow: 0px 6px 8px rgba(0, 0, 0, 0.3);
        }

        /* Proceed button specific styling using a unique container class */
        .proceed-container button {
            background-color: #228B22;
            color: white;
            font-weight: bold;
            font-size: 1.1em;
            padding: 0.75em 2em;
            border: none;
            border-radius: 8px;
            box-shadow: 0px 6px 10px rgba(0, 0, 0, 0.25);
            transition: all 0.3s ease;
            margin-top: 30px;
        }
        .proceed-container button:hover {
            background-color: #1e7b1e;
            box-shadow: 0px 8px 12px rgba(0, 0, 0, 0.35);
        }
        </style>
    """, unsafe_allow_html=True)

    st.download_button(
        label="Download Audio File",
        data=file_bytes,
        file_name=os.path.basename(file_path),
        mime="application/octet-stream"
    )

    # Sample knowledgebase text to copy
    KNOWLEDGEBASE_TEXT = sampleKnowledgeBaseText
    st.info('Copy below text.')
    st.code(KNOWLEDGEBASE_TEXT, language='')
