FROM python:3.14

WORKDIR /Structured_enquiry

COPY . .

RUN pip install pytest

# Run tests first
CMD ["sh", "-c", "pytest --junitxml=/Structured_enquiry/report.xml && python student.py"]
