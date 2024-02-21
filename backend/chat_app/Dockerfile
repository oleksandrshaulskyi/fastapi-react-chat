FROM python:3.11

WORKDIR /backend

COPY ./backend/chat_app/requirements.txt /backend/chat_app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /backend/chat_app/requirements.txt

COPY ./backend/chat_app /backend/chat_app/backend

CMD ["uvicorn", "backend.chat_app.main:application", "--host", "0.0.0.0", "--port", "8000"]
