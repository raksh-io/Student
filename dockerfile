# Use Python 3.14 base image
FROM python:3.14

# Set working directory inside the container
WORKDIR /Structured_enquiry

# Copy all files from your project to the container
COPY . .

# Install pytest (and any other dependencies)
RUN pip install pytest

# Default command (can be your Python program)
CMD ["python", "student.py"]
