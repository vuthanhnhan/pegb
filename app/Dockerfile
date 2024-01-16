FROM python:3.9

# 
WORKDIR /pegb

# 
COPY ../requirements.txt /pegb/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /pegb/requirements.txt

# 
COPY . /pegb/app