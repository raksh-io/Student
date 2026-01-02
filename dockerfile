FROM python:3.14

WORKDIR /Structured_enquiry

COPY . .
RUN pip install pytest
# Set student.py as the default command
ENTRYPOINT ["python", "student.py"]
