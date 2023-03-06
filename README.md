# StreamGPT
This is a streamline web application project, using the chatGPT openAI API 

#### Prerequisites 
1. Anaconda installed on the system 
2. Create an environment for this project (recommended) and install the packages listed in requirements.txt 
```bash 
conda create -n openai python==3.10 
conda activate openai 
pip install -r requirements.txt 
``` 
3. Run the python app GPT.py from streamlit
```bash
streamlit run GPT.py
```

#### Project Preview 
https://user-images.githubusercontent.com/40188935/222928458-b41dba76-612b-4f72-b4cb-619a66339560.mp4

- To create a Docker container, a Dockerfile is provided. Make sure Docker Desktop is installed, and the OpenAI API key is stored in a .env folder, the Dockerfile contains the following.  
```bash
FROM python:3.10-slim
ADD . .
RUN pip install -r requirements.txt 
EXPOSE 8500
ENTRYPOINT ["streamlit","run"] 
CMD ["./GPT.py","--server.headless","true","--server.fileWatcherType","none","--browser.gatherUsageStats","false","--server.port=8500","--server.address=0.0.0.0"]
```
- To build the Docker image from the Dockerfile, run the following command: 
```bash
docker build -t streamgpt . 
```
- To run a Docker container of the application on port 8500: 
```bash
docker run -p 8500:8500 streamgpt 
```