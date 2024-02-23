FROM python:3.11

WORKDIR /auth_app

COPY ./backend/auth_app/requirements.txt /auth_app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /auth_app/requirements.txt

COPY /backend/auth_app/application /auth_app/application

CMD ["uvicorn", "application.main:application", "--host", "0.0.0.0", "--port", "8080"]
