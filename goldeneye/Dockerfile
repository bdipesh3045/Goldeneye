FROM python:3.11

# Allows docker to cache installed dependencies between builds
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Mounts the application code to the image
COPY . code
WORKDIR /code


# Expose the port your Django app will run on
EXPOSE 8000

# Run Django migrations
RUN python manage.py makemigrations
RUN python manage.py migrate

# Run the production server
ENTRYPOINT ["python", "mysite/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]


