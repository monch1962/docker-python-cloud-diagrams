FROM python:3-slim AS build-env
 
# Install dependencies:
COPY requirements.txt .
RUN pip install -r requirements.txt

# Now setup distroless and run the application:
FROM gcr.io/distroless/python3

WORKDIR /app
# Set Virtual ENV
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Copy the source code into the distroless image
COPY --from=build-env /app /app

CMD ["hello.py", "/etc"]