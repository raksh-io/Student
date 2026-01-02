FROM python:3.14
WORKDIR /Structured_enquiry
COPY . .
CMD ["python", "student.py"]