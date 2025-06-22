#  AI Task Agent

This is an AI-powered Task Agent that reads tasks from a file (or ticket sources), intelligently categorizes them by priority, and supports future integration with tools like Slack, Notion, and email.

---

##  Goal

The purpose of this AI Agent is to **automate task understanding and prioritization** using a smart planning workflow powered by generative AI.

It follows a precise 3-step planning-execution cycle:

1. **Input**: Read tasks (currently from a file, future: emails or ticketing systems).
2. **Planning**: Use AI to analyze and categorize into:
   - High Priority
   - Medium Priority
   - Low Priority
3. **Execution** *(planned)*:
   - Update task boards (like **Notion**)
   - Send updates/alerts on **Slack**
   - Ingest tasks from **emails**

---

##  Tools & Technologies

- **Python**
- **Gemini (Google Generative AI)** — for intelligent categorization
- **dotenv** — for secret key management
- *(Planned)* Email parser, Notion API, Slack Webhooks

---

##  Memory

The agent retains task context from a provided `.txt` file (`tasks.txt`), acting as its "memory." You can also extend this to store conversation history or past task responses.

---



