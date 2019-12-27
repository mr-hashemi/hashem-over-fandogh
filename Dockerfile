FROM ubuntu:latest
RUN apt-get update -y && apt-get  install git python3.7 python3-pip make wget net-tools -yq
RUN git clone https://github.com/mr-hashemi/live-exec.git /live --depth=1

WORKDIR /live
EXPOSE 5000 80
RUN make update
RUN python3.7 -m pip install flask
COPY ./app.py /live/
ENTRYPOINT ["python3.7", "app.py"]
