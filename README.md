# Debate Agent

A multi-agent debate system built with **CrewAI** and **Groq**.

The system researches a given topic, builds arguments from both perspectives, challenges the opposing position, and produces a final evidence-based assessment through a dedicated judge agent.

## Overview

The project uses a sequential multi-agent workflow:

```text
                ┌──────────────┐
                │   Researcher │
                └──────┬───────┘
                       │
              Research Brief
                       │
              ┌────────┴────────┐
              ▼                 ▼
      ┌──────────────┐  ┌──────────────┐
      │   Advocate   │  │  Challenger  │
      └──────┬───────┘  └──────┬───────┘
             │                 │
             └────────┬────────┘
                      ▼
               ┌──────────────┐
               │     Judge    │
               └──────┬───────┘
                      │
                      ▼
              Debate Report
```

## Features

* Multi-agent debate workflow
* Dedicated research agent
* Argument construction from both perspectives
* Counterargument and rebuttal generation
* Impartial judge agent
* Sequential task execution
* Groq-powered LLM inference
* YAML-based agent and task configuration
* Markdown debate report generation
* Built with CrewAI

## Agents

### Researcher

Collects concise and balanced information about the debate topic, including:

* Key facts
* Arguments for and against
* Statistics and examples
* Risks and weaknesses

### Debate Advocate

Builds the strongest argument supporting the assigned position using the research produced by the Researcher.

### Debate Challenger

Analyzes the opposing argument, identifies weaknesses and assumptions, and develops evidence-based counterarguments.

### Debate Judge

Reviews both sides based on:

* Evidence quality
* Logical reasoning
* Argument strength
* Rebuttals
* Consistency
* Unresolved questions

The Judge produces the final debate assessment.

## Tech Stack

* **Python**
* **CrewAI**
* **Groq**
* **LiteLLM**
* **Pydantic**
* **UV**
* **YAML**

## Project Structure

```text
debater/
│
├── src/
│   └── debater/
│       ├── config/
│       │   ├── agents.yaml
│       │   └── tasks.yaml
│       │
│       ├── crew.py
│       └── main.py
│
├── tests/
│
├── output/
│
├── .env
├── pyproject.toml
├── uv.lock
└── README.md
```

## Workflow

The crew runs using a sequential process:

1. **Research**

   * Analyze the topic.
   * Prepare a balanced research brief.

2. **Advocate**

   * Use the research to construct the supporting position.
   * Anticipate opposing arguments.
   * Prepare rebuttals.

3. **Challenger**

   * Review the opposing argument.
   * Identify weaknesses.
   * Construct counterarguments.

4. **Judge**

   * Compare both positions.
   * Evaluate evidence and reasoning.
   * Identify weaknesses and unresolved questions.
   * Generate the final debate report.

## Installation

Clone the repository and enter the project directory:

```bash
git clone <repository-url>
cd debater
```

Install dependencies:

```bash
uv sync
```

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

## Running the Project

Run the CrewAI workflow with:

```bash
crewai run
```

The final debate report is generated as:

```text
debate_report.md
```

## Example

Input:

```text
Should companies adopt Large Language Models across their business operations?
```

The system will:

```text
Research the topic
      ↓
Build the supporting argument
      ↓
Build the opposing argument
      ↓
Challenge the arguments
      ↓
Evaluate both sides
      ↓
Generate debate_report.md
```

## Configuration

Agents and tasks are separated from the Python implementation.

### `agents.yaml`

Defines each agent's:

* Role
* Goal
* Backstory
* LLM configuration

### `tasks.yaml`

Defines:

* Task descriptions
* Expected outputs
* Agent assignments
* Context between tasks

This makes the debate workflow easier to modify without changing the core Python code.

## Environment

The project uses **Groq** as the LLM provider through LiteLLM.

The configured model can be changed in the agent configuration:

```yaml
llm: groq/openai/gpt-oss-120b
```

## Output

The final output contains:

* Summary of both positions
* Strongest arguments
* Key weaknesses
* Evidence assessment
* Unresolved questions
* Final evidence-based assessment

## Current Limitation

The Researcher currently relies on the LLM's available knowledge unless an external research/search tool is configured.

For production use, a future version can integrate web search so that research claims include:

```text
Claim
Source
Evidence
URL
Confidence
```

This would make the debate pipeline more suitable for evidence-grounded research.


## License

This project is intended for educational and portfolio purposes.
