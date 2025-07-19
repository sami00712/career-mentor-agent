# 🎓 Career Mentor AI Agent

An intelligent Streamlit-based agentic app that helps students explore careers, generate personalized skill-building roadmaps, and discover job roles — powered by OpenRouter AI.

🔗 **Live App:** [career-mentor-agent-01.streamlit.app](https://career-mentor-agent-01.streamlit.app/)

---

## 🚀 Features

- 🔍 **Career Suggestions:** Get personalized career fields based on interests or input.
- 🛠 **Skill Roadmaps:** Generate skill-building plans (e.g., Frontend Developer).
- 💼 **Job Role Insights:** Understand potential job titles for a chosen field.
- 🤖 **Multi-Agent Powered:** Uses specialized agents like `CareerAgent`, `SkillAgent`, and `JobAgent`.
- 🌐 **OpenRouter API:** Seamless AI integration for dynamic text responses.

---

## 🧠 How It Works

The app uses a unified `career.py` agent containing logic for:
- Generating careers
- Suggesting skill paths
- Providing relevant job roles

All responses are fetched from OpenRouter API via `api/openrouter.py`.

---

## 🖥️ Tech Stack

- [Streamlit](https://streamlit.io/) — UI/UX frontend
- OpenRouter API — AI backend
- Python 3.10+
- `.env` for local development API keys
