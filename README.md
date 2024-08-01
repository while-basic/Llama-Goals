# Llama Goals
A terminal based AI-powered task planning and execution assistant that uses Ollama to generate responses. It helps users refine their goals, create detailed task plans, and guide them through task execution.

## Features

- Interactive goal refinement through clarifying questions
- AI-generated task plans with detailed steps
- Task execution tracking
- Integration with Ollama for local AI model inference

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher
- [Ollama](https://ollama.ai/) installed and running on your system
- Required Python packages (see `requirements.txt`)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/while-basic/Llama-Goals.git
   cd Llama-Goals
   ```

2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

3. Ensure Ollama is installed and running on your system. Follow the [Ollama installation guide](https://github.com/jmorganca/ollama#installation) if you haven't already set it up.

## Usage

1. Start the Ollama service if it's not already running.

2. Run the main script:
   ```
   python goal_planner.py
   ```

3. Follow the prompts to input your goal and answer clarifying questions.

4. The assistant will generate a task plan and guide you through the execution of each task.

## Configuration

- To change the Ollama model, modify the `model` parameter in the `send_prompt` function in `main.py`.
- The Ollama API endpoint is set to `http://localhost:11434/api/generate` by default. If your Ollama instance is running on a different address, update the `OLLAMA_API_URL` variable in `main.py`.

## Contributing

Contributions to Llama Goals are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- This project uses [Ollama](https://ollama.ai/) for local AI model inference.
