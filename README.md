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

### Tools Use with Claude (`tools_use_with_claude/`)
Learn to integrate Claude with external tools and APIs:
- **001_tools.ipynb** - Introduction to tool use with Claude
- **002_tools_007.ipynb** - Tool use with Claude 3.7 Sonnet
- **003_tools_008.ipynb** - Tool use with Claude 3.8 Sonnet
- **004_tools_009.ipynb** - Tool use with Claude 3.9 Sonnet
- **005_tool_streaming.ipynb** - Streaming responses with tools
- **006_tool_streaming_completed.ipynb** - Complete tool streaming implementation
- **007_text_editor_tool.ipynb** - Building a text editor tool
- **008_web_search.ipynb** - Web search integration
- **009_web_search_complete.ipynb** - Complete web search tool
- **main.py** - Python functions for tool examples
- **json_schema_prompt.txt** - JSON schema generation prompt

### RAG (Retrieval-Augmented Generation) (`rag/`)
Build intelligent systems that combine retrieval with generation:
- **001_chunking.ipynb** - Document chunking strategies
- **002_embeddings.ipynb** - Creating and working with embeddings
- **003_vectordb.ipynb** - Vector database operations
- **004_bm25.ipynb** - BM25 keyword search
- **005_hybrid.ipynb** - Hybrid search combining semantic and keyword search
- **report.md** - Sample document for RAG experiments

### Claude Features (`claude_features/`)
Explore advanced Claude capabilities:
- **001_thinking.ipynb** - Introduction to Claude's thinking capabilities
- **001_thinking_complete.ipynb** - Complete thinking workflow examples
- **002_images.ipynb** - Image analysis with Claude
- **images/** - Sample images for analysis

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

### 4. Learn Tools Use with Claude
Explore the `tools_use_with_claude` section to understand how to integrate Claude with external tools and APIs for more powerful applications.

### 5. Build RAG Systems
Work through the `rag` section to learn retrieval-augmented generation techniques, from document chunking to hybrid search strategies.

### 6. Explore Claude Features
Discover advanced capabilities in the `claude_features` section, including thinking workflows and image analysis.

## Key Concepts

- **System Prompts**: Setting behavior and context for Claude
- **Temperature**: Balancing creativity vs. consistency
- **Streaming**: Handling real-time response generation
- **Prompt Evaluation**: Systematic assessment of prompt quality
- **Solution Criteria**: Defining success metrics for prompts
- **Iterative Improvement**: Using evaluation data to refine prompts
- **Tool Use**: Integrating Claude with external tools and APIs
- **JSON Schema**: Defining tool interfaces for Claude
- **Tool Streaming**: Real-time tool execution and response handling
- **Document Chunking**: Breaking documents into manageable pieces for retrieval
- **Embeddings**: Converting text to vector representations for semantic search
- **Vector Databases**: Storing and searching high-dimensional vectors
- **BM25**: Keyword-based ranking algorithm for information retrieval
- **Hybrid Search**: Combining semantic and keyword search approaches
- **Thinking Workflows**: Leveraging Claude's extended reasoning capabilities
- **Image Analysis**: Processing and understanding visual content with Claude

## Resources

- [Anthropic API Documentation](https://docs.anthropic.com/)
- [Claude Prompt Engineering Guide](https://docs.anthropic.com/claude/docs/prompt-engineering)
- [Model Information](https://docs.anthropic.com/claude/docs/about-claude/models)

## License

This learning path is provided for educational purposes.

## Contributing

This is a personal learning repository. Feel free to fork and adapt for your own learning journey.
