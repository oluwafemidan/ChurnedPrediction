# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.9-slim

EXPOSE 5000

WORKDIR /app
COPY . /app

# Install pip requirements
COPY req.txt .
RUN python -m pip install -r req.txt




# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "flaskapi.app:app"]
