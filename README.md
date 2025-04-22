<p align="center">
  <img src="https://raw.githubusercontent.com/taynamghz/Audim8model/main/audimatelogov5-txt.png" alt="Audimate Logo" width="100%" />
</p>
# Audimate – AI-Powered Casting Assistant for the Saudi Film Industry

## What is Audimate?

**Audimate** is a localized, AI-driven casting assistant built to streamline and modernize the audition process for the **Saudi film and television industry**. It leverages advanced multimodal AI and an agent-based system to evaluate self-taped auditions based on **emotional tone**, **facial expressions**, **vocal delivery**, and **character alignment**.

Built using [CrewAI](https://github.com/crewAIInc/crewAI)'s modular agent architecture, Audimate automates the casting pipeline, incorporating Arabic-language support and cultural intelligence powered by:

- **Allam**: Saudi Arabia's Arabic Large Language Model
- **SADAIA & Ministry of Media datasets**: for cultural and linguistic localization
- **Multimodal AI models**: for video, speech, and text analysis

---

## 🚀 Key Features

### 🎯 Localized AI Audition Filtering
- Designed specifically for the Saudi market
- Supports Arabic text, dialects, and performance nuances
- Uses Saudi-specific datasets and the Allam LLM

### 📜 Script-Based Character Matching
- Directors upload role descriptions or scripts
- An LLM agent extracts emotional and psychological traits
- Example output:  
  `Female, 30s, quiet intensity, emotional resilience, conservative appearance`

### 🧠 Hybrid Trait Matching
- Manual override and customization of extracted traits
- Presets like “charismatic outsider” or “villain with a conscience”

### 🎥 AI-Driven Performance Analysis
- Video evaluation using models like **MediaPipe** and **OpenCV**
- Facial emotion recognition, body language cues, vocal tone scoring
- Speech and tone analysis using **Whisper** and **pyAudioAnalysis**

### 📊 Smart Shortlisting
- Actors are matched to character profiles using similarity scoring
- Outputs a ranked shortlist of best-fit performers

### 🔁 Real-Time Feedback Learning
- Director feedback trains the system over time
- Adaptive trait weighting for continuous improvement

### 🛠️ Agent-Based Workflow (CrewAI)
- **Script Analyst Agent**: Parses uploaded scripts
- **Rubric Editor Agent**: Enables director to refine traits
- **Video Analyzer Agent**: Processes and scores video submissions
- **Matching Agent**: Ranks talent by match score
- **Learning Agent**: Integrates director feedback into future rankings

### 📈 Scalable & Extensible
- Initially focused on feature films
- Roadmap includes support for:
  - Series
  - Commercials
  - Streaming content
  - Integration with script breakdown and compliance tools

---

## 🤖 Tech Stack

| Layer             | Technology / Model                              | Purpose                                       |
|------------------|--------------------------------------------------|-----------------------------------------------|
| NLP               | GPT-4 / Allam                                    | Character trait extraction from scripts       |
| Speech Analysis   | Whisper, pyAudioAnalysis                         | Emotion and vocal profile detection           |
| Video Analysis    | MediaPipe, DeepFace, OpenCV                      | Facial expression and body language analysis  |
| Agent Framework   | [CrewAI](https://github.com/crewAIInc/crewAI)   | Modular orchestration of AI tasks             |
| Learning Engine   | Custom feedback-based trait reweighting system  | Improves over time using director input       |

---

## 🌍 Why Audimate?

The Saudi film industry is growing fast—but casting remains slow, subjective, and labor-intensive. Audimate solves this by:

- Reducing review time by up to **80%**
- Delivering consistent, objective evaluations
- Empowering discovery of emerging **Saudi talent**
- Supporting directors with **data-driven** recommendations
- Aligning casting decisions with cultural and narrative goals

Audimate is not just a casting tool—it’s a step toward a smarter, scalable, and culturally aware creative industry in Saudi Arabia.

---

## 📦 Project Status

- ✅ MVP: Trait extraction, video analysis, shortlisting
- 🚧 In Progress: Web dashboard and dataset onboarding
- 🔜 Coming Soon: Arabic speech emotion classifier, talent database, production CRM integration

---

## 📂 Folder Structure (Planned)

```bash
audimate/
├── agents/
│   ├── script_agent.py
│   ├── rubric_agent.py
│   ├── video_agent.py
│   └── feedback_agent.py
├── data/
│   ├── sample_scripts/
│   └── audition_videos/
├── models/
│   └── emotion_classifier.pkl
├── dashboard/
│   └── streamlit_app.py
├── README.md
└── requirements.txt
