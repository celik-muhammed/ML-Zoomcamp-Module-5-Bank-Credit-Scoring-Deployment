
# Use the ml-zoomcamp image
FROM svizor/zoomcamp-model:3.10.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container
COPY pycode/ /app/

# Copy the Pipfile and Pipfile.lock into the container
COPY ml-zoomcamp-module-5-env/ /app/

# Install pipenv and the project dependencies
RUN pip install pipenv && \
    pipenv install --deploy --ignore-pipfile

# Expose the port that Flask will run on
EXPOSE 8000

# Start the Flask application using pipenv
CMD ["pipenv", "run", "python", "app2.py"]
