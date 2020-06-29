FROM python:3.8-alpine
COPY server.py /
RUN pip install flask
EXPOSE 5000
CMD python server.py
