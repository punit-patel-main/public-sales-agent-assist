def render_suggestions(current_suggestion):
    suggestion_blocks = ""
    for item in current_suggestion:
        suggestion = item['suggestion']
        
        suggestion_blocks += f"""
            <div style="
                background: linear-gradient(135deg, #f8fafc 0%, #ffffff 100%); 
                border: 1px solid #e2e8f0; 
                padding: 20px 24px; 
                margin: 16px 0; 
                border-radius: 12px; 
                box-shadow: 0 1px 3px rgba(0,0,0,0.06), 0 1px 2px rgba(0,0,0,0.04);
                transition: all 0.2s ease;
                position: relative;
                overflow: hidden;
            ">
                <div style="
                    position: absolute;
                    left: 0;
                    top: 0;
                    bottom: 0;
                    width: 3px;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                "></div>
                <div style="
                    color: #334155; 
                    font-size: 15px; 
                    font-weight: 500;
                    line-height: 1.6;
                    letter-spacing: -0.01em;
                ">
                    {suggestion}
                </div>
            </div>
        """
    
    st.markdown(suggestion_blocks, unsafe_allow_html=True)

def get_wave_loader():
    return """
    <div style="display: flex; align-items: center; justify-content: flex-start; height: 80px; padding: 20px;">
        <div style="display: flex; align-items: end; height: 32px; gap: 4px;">
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.1s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.2s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.3s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.4s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.1s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.2s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.3s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.4s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.1s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.2s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.3s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.4s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.1s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.2s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.3s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.4s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.1s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.2s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.3s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.4s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.1s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.2s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.3s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.4s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.1s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.2s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.3s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.4s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.1s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.2s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.3s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.4s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.1s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.2s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.3s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.4s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.1s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.2s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.3s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.4s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.1s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.2s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.3s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.4s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.1s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.2s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.3s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.4s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.1s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.2s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.3s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.4s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.1s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.2s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.3s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.4s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.1s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.2s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.3s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.4s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.1s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.2s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.3s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.4s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.1s;"></div>
            <div class="wave-bar" style="width: 3px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); animation: wave 1.4s ease-in-out infinite; animation-delay: 0.2s;"></div>
        </div>
    </div>
    <style>
    @keyframes wave {
        0%, 100% { 
            height: 4px; 
            opacity: 0.4;
        }
        50% { 
            height: 28px; 
            opacity: 1;
        }
    }
    .wave-bar {
        height: 4px;
        border-radius: 2px;
        transition: all 0.3s ease;
    }
    </style>
    """
