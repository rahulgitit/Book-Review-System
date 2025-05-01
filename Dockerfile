FROM python:3.11-slim-buster
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r  requirements.txt

COPY . .


# Expose port 8000
EXPOSE 8000

# Run Django server 
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# # CMD python manage.py runserver



# Dockerfile
