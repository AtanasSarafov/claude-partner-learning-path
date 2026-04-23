# Claude Partner Learning Path

A comprehensive learning path for mastering Claude API integration, prompt engineering, and evaluation techniques.

## Overview

This repository contains hands-on notebooks and exercises designed to help developers and AI practitioners effectively work with Claude's API and develop robust prompt engineering skills.

## Structure

### Accessing Claude API (`accessing_claude_api/`)
Learn the fundamentals of interacting with Claude's API:
- **001_requests.ipynb** - Basic API requests and response handling
- **002_system_prompt.ipynb** - Understanding and using system prompts
- **003_temperature.ipynb** - Controlling response randomness with temperature
- **004_streaming.ipynb** - Implementing streaming responses
- **005_controlling_output.ipynb** - Advanced output control techniques

### Prompt Evaluation (`prompt_evaluation/`)
Develop systematic approaches to evaluate and improve prompt quality:
- **001_prompt_evals.ipynb** - Introduction to prompt evaluation
- **002_prompt_evals_grader.ipynb** - Building automated graders for prompt evaluation
- **003_prompt_evals_fns.ipynb** - Functional approaches to evaluation
- **004_prompt_evals_complete.ipynb** - Complete evaluation workflows
- **dataset.json** - Evaluation dataset with task descriptions and solution criteria

### Prompt Engineering (`prompt_engineering/`)
Master the art and science of crafting effective prompts:
- **001_prompting.ipynb** - Prompting fundamentals and best practices
- **002_prompting_completed.ipynb** - Completed examples with explanations
- **003_exercise.ipynb** - Hands-on exercises for prompt engineering
- **dataset.json** - Exercise dataset with scenarios and criteria

## Getting Started

### Prerequisites
- Python 3.8+
- Anthropic API key
- Virtual environment (recommended)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/AtanasSarafov/claude-partner-learning-path.git
cd claude-partner-learning-path
```

2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install anthropic python-dotenv
```

4. Set up your API key:
```bash
echo "ANTHROPIC_API_KEY=your_api_key_here" > .env
```

5. Launch Jupyter:
```bash
jupyter notebook
```

## Learning Path

### 1. Start with API Basics
Begin with the `accessing_claude_api` notebooks to understand how to make requests, handle responses, and control Claude's behavior.

### 2. Learn Prompt Evaluation
Move to `prompt_evaluation` to understand how to systematically assess and improve your prompts using automated evaluation techniques.

### 3. Master Prompt Engineering
Complete the `prompt_engineering` section to develop advanced prompt crafting skills through hands-on exercises.

## Key Concepts

- **System Prompts**: Setting behavior and context for Claude
- **Temperature**: Balancing creativity vs. consistency
- **Streaming**: Handling real-time response generation
- **Prompt Evaluation**: Systematic assessment of prompt quality
- **Solution Criteria**: Defining success metrics for prompts
- **Iterative Improvement**: Using evaluation data to refine prompts

## Resources

- [Anthropic API Documentation](https://docs.anthropic.com/)
- [Claude Prompt Engineering Guide](https://docs.anthropic.com/claude/docs/prompt-engineering)
- [Model Information](https://docs.anthropic.com/claude/docs/about-claude/models)

## License

This learning path is provided for educational purposes.

## Contributing

This is a personal learning repository. Feel free to fork and adapt for your own learning journey.
