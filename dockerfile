FROM python:3.14

WORKDIR /Structured_enquiry

COPY . .

RUN pip install pytest

# Run pytest AND generate report.xml
CMD ["python","student.py"]
