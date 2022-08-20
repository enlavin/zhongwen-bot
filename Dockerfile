FROM python:3.10-slim-bullseye as base
WORKDIR /app
RUN apt-get update
RUN apt-get upgrade -y --no-install-recommends build-essential gcc

FROM base as build
RUN python -m venv ./venv
ENV PATH="/app/venv/bin:$PATH"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN python -m spacy download zh_core_web_lg
COPY data ./data

FROM base as final
COPY --from=build /app/venv ./venv
COPY --from=build /app/data ./data
COPY *.py ./
ENV PATH="/app/venv/bin:$PATH"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
CMD ['python', 'bot.py']
