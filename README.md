## Setup
- Clone the repository, and navigate to its root.
- The app uses the OpenAI LLM APIs, for which you'll need to obtain an api key.
- Create the environment file at ```./language-tutor-app/language-tutor-app/.env```, and insert your key in the file as below
```
OPENAI_API_KEY=<YOUR KEY HERE>
```
- Run the following commands to create the conda environment and install the packages
```
conda create --name language-tutor-app python=3.10 -y
conda activate language-tutor-app
pip install -r requirements.txt
```

## Running the app
### Using streamlit
- Navigate to the root of the repository directory, and run ```streamlit run language-tutor-app/app.py```.
- This will start the app on port *8501*

### Using docker
- Ensure docker is installed on the host system, and the service is running.
- Navigate to the root of the repository directory, and run ```docker compose up -d```
- Run ```docker ps``` to verify that the app has started

Navigate then to [localhost:8501](localhost:8501) in your browser
