FROM debian:bookworm AS builder

WORKDIR /build

ARG TAG_NAME=master
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get -y install build-essential git curl \
  && echo 'man-db man-db/auto-update boolean false' | debconf-set-selections \
  && git clone https://github.com/sipwise/rtpengine \
  && cd rtpengine \
  && git checkout ${TAG_NAME} \
  && apt-get -y build-dep -Ppkg.ngcp-rtpengine.nobcg729 . \
  && dpkg-buildpackage -Ppkg.ngcp-rtpengine.nobcg729

FROM debian:bookworm

WORKDIR /opt/rtpengine

ENV DEBIAN_FRONTEND=noninteractive

RUN groupadd -r rtpengine && useradd -r -g rtpengine rtpengine

COPY --from=builder /build/ngcp-rtpengine-daemon_*.deb /tmp/
COPY ./rtpengine.conf /opt/rtpengine/rtpengine.conf

RUN apt-get update && \
  mkdir -p /etc/modprobe.d/ && \
  apt-get install -y \
  curl \
  iptables \
  libavcodec59 \
  libavformat59 \
  libavutil57 \
  libevent-2.1-7 \
  libevent-pthreads-2.1-7 \
  libglib2.0-0 \
  libhiredis0.14 \
  libip4tc2 \
  libip6tc2 \
  libjson-glib-1.0-0 \
  libmariadb3 \
  libmosquitto1 \
  libopus0 \
  libpcap0.8 \
  libspandsp2 \
  libssl3 \
  libswresample4 \
  libwebsockets17 \
  libxmlrpc-core-c3 && \
  apt-get -y install /tmp/*.deb && \
  rm -rf /var/lib/apt/lists/* /tmp/*.deb

EXPOSE 22222
EXPOSE 2223

CMD ["/usr/bin/rtpengine", "--config-file=/etc/rtpengine/rtpengine.conf", "--foreground"]
