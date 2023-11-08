# Use the official lightweight Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Flask app files to the container
COPY predict.py /app/predict.py
COPY model.pkl /app/model.pkl

# Install necessary dependencies
RUN pip install flask scikit-learn numpy

# Expose the port where the app will run
EXPOSE 9696

# Command to run the application
CMD ["python", "predict.py"]