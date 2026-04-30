# 1. Start with a tiny, pre-configured Python environment
FROM python:3.9-slim

# 2. Create a folder named /app inside the container to hold our code
WORKDIR /app

# 3. Copy our app.py from the repository into the /app folder
COPY app.py .

# 4. Install the only dependency we have
RUN pip install flask

# 5. Tell Docker that this container will listen on Port 80
EXPOSE 80

# 6. The final command that runs when the container starts
CMD ["python", "app.py"]