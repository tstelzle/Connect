FROM python:3

VOLUME /usr/src
WORKDIR /usr

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r /usr/requirements.txt

CMD ["bash"]