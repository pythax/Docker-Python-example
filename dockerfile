
        FROM DEBIAN:latest
        COPY r.txt ./
        RUN pip install -r r.txt
        WORKDIR /container
        COPY app.py ./
        CMD [ "python", "./app.py" ]
        