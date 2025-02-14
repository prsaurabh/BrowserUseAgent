# Browser-Use Agent

This project contains a Python-based agent that uses the `browser_use` library to interact with web browsers and perform various tasks.

## Demo


https://github.com/user-attachments/assets/1dccd0f2-3645-49b5-873c-d0ddcb113ca7



## Project Structure

- `Agent.py`: Main script to run the agent.
- `config.py`: Configuration file containing API keys.
- `controllers.py`: Contains controller actions for the agent.
- `credentials.py`: Stores login credentials for various websites.
- `entity.py`: Defines Pydantic models for data validation.
- `prompts.py`: Contains task and system prompts.
- `requirements.txt`: Lists the dependencies required for the project.

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Browser-Use
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Agent

To run the agent, execute the following command:
```bash
python Agent.py
```

## Configuration

Update the `config.py` file with your OpenAI API keys.

## License

This project is licensed under the MIT License.
