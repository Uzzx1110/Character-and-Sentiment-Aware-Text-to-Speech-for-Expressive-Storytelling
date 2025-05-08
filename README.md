# StoryGenEval
**A pipeline for short story generation, evaluation, and emotion-aware TTS using LLMs**
## Overview
This project explores automatic story generation and evaluation using Large Language Models (LLMs). It includes:
* Story generation from keywords using fine-tuned or pre-trained models
* Evaluation using perplexity, Distinct-n metrics, and LLM-based few-shot scoring
* Emotion-aware text-to-speech (TTS) output using ElevenLabs API
## Features
* 🔹 Generate 10 unique stories from different keyword sets
* 🔹 Calculate:
  * **Perplexity** (language fluency)
  * **Distinct-1/2** (lexical diversity)
* 🔹 Evaluate each story using LLMs (BART, GPT-2, T5) on:
  * Coherence
  * Creativity
  * Language fluency
* 🔹 Get natural-sounding TTS with emotion using ElevenLabs
## Evaluation Summary
* **Automatic Metrics**: Perplexity and Distinct-n show variability across generated stories
* **LLM Ratings**: Each story rated on a scale of 1–5
* **Average Scores**: Calculated per model and overall
* **Emotion-Aware Audio**: Final story synthesized using voice cloning
## Prompt Format (for LLM Rating)
```text
You are an expert story reviewer. Rate the following short fictional story on a scale of 1 to 5 based on,Evaluate the story below and provide JSON-formatted feedback with:

1. Coherence – Clear beginning, middle, and end.
2. Creativity – Original or interesting concept.
3. Language Fluency – Well-written and grammatically correct.

Do NOT compare this to novels or professional literature. Treat it as a short story by a beginner writer or AI.

Example Response:
{{
  "rating": 4,
  "justification": "Good keyword usage but could improve character development",
  "missing_keywords": ["Grandma"]
}}

Example:
keywords: ["Mathville", "puzzles", "riddles", "equations", "nature"]
script: [Narrator](neutral): In the small town of Mathville, lived two best friends, Algy and Sammy....
Rating: 5
Justification: The story is simple but creative, flows logically, and is grammatically correct.

Now rate this story:
keywords: {keywords}
script: {story}

Your JSON analysis:
```
## Requirements
* Python ≥ 3.8
* `transformers`, `torch`, `nltk`, `openai`, `json`, `numpy`, `requests`
* ElevenLabs API key for TTS
