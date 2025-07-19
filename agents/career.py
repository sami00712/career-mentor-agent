from api.openrouter import call_openrouter  

def get_career_roadmap(user_input: str) -> str:
    prompt = f"""
    You are a career expert AI. Based on the user's interest, generate a complete step-by-step roadmap,
    including:
    - Essential skills
    - Learning resources (free if possible)
    - Timeline
    - Suggested job roles
    User interest: {user_input}
    """
    
    try:
        response = call_openrouter(prompt)
        return response
    except Exception as e:
        return f"❌ Failed to get roadmap: {e}"
