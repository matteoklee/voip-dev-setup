# Basis-Image: Debian stable minimal
FROM debian:stable-slim

# Setze Umgebungsvariablen
ENV DEBIAN_FRONTEND=noninteractive
ENV RTPPROXY_USER=rtpproxy
ENV RTPPROXY_GROUP=rtpproxy

# Installiere nötige Pakete fürs Kompilieren und Betrieb
RUN apt-get update && apt-get install -y \
    git build-essential pkg-config libevent-dev iproute2 iptables net-tools \
    libpcap-dev libjson-c-dev libglib2.0-dev libssl-dev \
    iputils-ping \
    curl supervisor \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Benutzer und Gruppe für RTPProxy anlegen
RUN groupadd -r $RTPPROXY_GROUP && useradd -r -g $RTPPROXY_GROUP $RTPPROXY_USER

# RTPProxy Quellcode klonen und kompilieren
RUN git clone https://github.com/sippy/rtpproxy.git /usr/src/rtpproxy && \
    cd /usr/src/rtpproxy && \
    ./configure && \
    make && make install && \
    rm -rf /usr/src/rtpproxy

# Erstelle Verzeichnisse und setze Rechte
RUN mkdir -p /var/run/rtpproxy && chown $RTPPROXY_USER:$RTPPROXY_GROUP /var/run/rtpproxy

# Supervisor config für RTPProxy (optional, für Prozessmanagement im Container)
RUN mkdir -p /etc/supervisor/conf.d
COPY rtpproxy-supervisor.conf /etc/supervisor/conf.d/rtpproxy.conf

# Exponiere RTP und Steuerports (standard RTP 5000-60000 UDP, UDP 7722 Steuerport)
#EXPOSE 6000-60000/udp
EXPOSE 7722/udp

# Wechsle zum rtpproxy user für Sicherheit
USER $RTPPROXY_USER

# Startbefehl über supervisor (konfiguriert in rtpproxy-supervisor.conf)
CMD ["/usr/bin/supervisord", "-n"]
