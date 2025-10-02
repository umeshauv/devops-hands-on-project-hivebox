FROM python:3.14.0rc3-alpine3.21@sha256:592bfb37035117c38358602ef29741618d7d80e65d529f835ecac4259477b04a
WORKDIR /app
COPY . .
CMD ["python3", "sampleapp/version.py"]
