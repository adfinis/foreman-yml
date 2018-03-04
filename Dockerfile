FROM ubuntu:xenial

RUN apt-get update && apt-get install -y python-pip
RUN mkdir -p /foreman-yml/configs
ADD . /foreman-yml
WORKDIR /foreman-yml
RUN pip install .
VOLUME /foreman-yml/configs
ENTRYPOINT ["foreman-yml"]
