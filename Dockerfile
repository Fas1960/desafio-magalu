from python:3
ENV NODE_ENV=production
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
workdir / usr / src / app
copy . .
expose 5000
CMD ["desafiofernando.ipynb"]
ENTRYPOINT ["python3"]
