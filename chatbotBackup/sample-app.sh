#!/bin/bash 

mkdir tempdir 
mkdir tempdir/templates 
mkdir tempdir/static

cp sample_app_copy.py tempdir/. 
cp -r templates/* tempdir/templates/. 
cp -r static/* tempdir/static/.

echo "FROM python" >> tempdir/Dockerfile 
echo "RUN pip install flask" >> tempdir/Dockerfile

echo "COPY  ./static /home/myapp/static/" >> tempdir/Dockerfile 
echo "COPY  ./templates /home/myapp/templates/" >> tempdir/Dockerfile 
echo "COPY  sample_app_copy.py /home/myapp/" >> tempdir/Dockerfile

echo "EXPOSE 8080" >> tempdir/Dockerfile

echo "CMD python3 /home/myapp/sample_app_copy.py" >> tempdir/Dockerfile

cd tempdir
docker build -t sampleapp .

docker run -t -d -p 8080:8080 --name samplerunning sampleapp