# Use a slim Python image
FROM python:3.11-slim

# Install OS packages needed for Tkinter GUI and a virtual X server for headless runs
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      python3-tk \
      xvfb \
      x11-utils \
      ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# Create app directory
WORKDIR /app

# Copy project files
COPY . /app

# Install Python dependencies if requirements.txt exists
RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

# Expose nothing (GUI). Set a default display for xvfb
ENV DISPLAY=:99 \
    PYTHONUNBUFFERED=1 \
    FLASK_APP=run.py \
    PORT=5000

# Default command: start an X virtual framebuffer and run the script
# Use xvfb-run so Tkinter can start even in headless containers
CMD ["bash", "-lc", "xvfb-run -s '-screen 0 1024x768x24' python ACEest_Fitness-V1.1.py"]

EXPOSE ${PORT}

# Expect run.py to expose a WSGI app named `app` (e.g. app = create_app())
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "run:app"]