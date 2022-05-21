
FROM python: 3
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
WORKDIR /usr/src/app
COPY  teste.py /usr/src/app
CMD ["teste.py"]
ENTRYPOINT ["python3"]