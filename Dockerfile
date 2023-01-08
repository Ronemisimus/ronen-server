FROM python:alpine
RUN mkdir /app
WORKDIR /app
COPY server.pyz /app/server.pyz
COPY logging.config /app/logging.config
EXPOSE 3769
CMD [ "python", "server.pyz" ]