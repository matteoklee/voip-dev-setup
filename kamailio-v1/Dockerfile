FROM ghcr.io/kamailio/kamailio:6.0.2-noble

ADD kamailio.cfg /etc/kamailio/
ADD kamailio-local.cfg /etc/kamailio/

ADD kamailio.py /etc/kamailio/
ADD kamailio3s.py /etc/kamailio
ADD kamailio-basic.py /etc/kamailio
ADD kamailio-basic-kemi.cfg /etc/kamailio/
ADD kamailio-basic-kemi-native.cfg /etc/kamailio/
ADD kamailio-basic-kemi-python.py /etc/kamailio/
ADD kamailio-basic-kemi-python3s.py /etc/kamailio/

ADD kamctlrc /etc/kamailio/
COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

#RUN apt-get update && \
#    apt-get install -y python3 python3-dev python3-pip && \
#    rm -rf /var/lib/apt/lists/*

RUN apt-get update && \
    apt-get install -y python3 python3-dev python3-pip kamailio-postgres-modules postgresql-client sngrep libpython3-dev && \
    rm -rf /var/lib/apt/lists/*

# RUN apt install kamailio kamailio-mysql-modules -y

#RUN apt-get update && \
#    apt-get install -y mariadb-client && \
#    rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y sngrep

EXPOSE 5060
EXPOSE 5060/udp

ENTRYPOINT ["/entrypoint.sh"]
