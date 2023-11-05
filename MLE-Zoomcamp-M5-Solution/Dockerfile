
# Use the ml-zoomcamp image
FROM svizor/zoomcamp-model:3.10.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container
# Copy the Pipfile and Pipfile.lock into the container
COPY ["pycode/", "ml-zoomcamp-module-5-env/", "./"]

# Install pipenv and the project dependencies
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

# Expose the port that Flask will run on
EXPOSE 9696

# Start the Flask application using pipenv
# CMD ["pipenv", "run", "waitress-serve", "--listen=0.0.0.0:9696", "q6_predictor:app"]
ENTRYPOINT ["pipenv", "run", "waitress-serve", "--listen=0.0.0.0:9696", "q6_predictor:app"]
