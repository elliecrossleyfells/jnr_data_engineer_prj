# Use lightweight python env.
FROM python:3.12-slim

# instruct to create and use /app as proj folder in Docker. 
WORKDIR /app

# copies into docker
COPY requirements.txt .

# install required libs 
RUN pip install --no-cache-dir -r requirements.txt 

# copy proj files into docker
COPY . .

#notes that the app used port 5000
EXPOSE 5000

#creates/fills db first, then starts webpage. 
CMD ["sh", "-c", "python main.py && python app.py"]