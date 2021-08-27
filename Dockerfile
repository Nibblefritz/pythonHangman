FROM python:3
WORKDIR /kfife/scripts
COPY . .
ENTRYPOINT ["python3", "./Hangman.py"]