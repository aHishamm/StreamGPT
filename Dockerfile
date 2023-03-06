FROM python:3.10-slim
ADD . .
RUN pip install -r requirements.txt 
EXPOSE 8500
ENTRYPOINT ["streamlit","run"] 
CMD ["./GPT.py","--server.headless","true","--server.fileWatcherType","none","--browser.gatherUsageStats","false","--server.port=8500","--server.address=0.0.0.0"]