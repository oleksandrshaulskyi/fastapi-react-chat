FROM python:3.11

WORKDIR /chat_app

COPY ./backend/chat_app/requirements.txt /chat_app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /chat_app/requirements.txt

COPY ./backend/chat_app/application /chat_app/application

CMD ["uvicorn", "application.main:application", "--host", "0.0.0.0", "--port", "8000"]
