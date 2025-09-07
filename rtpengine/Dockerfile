FROM fonoster/rtpengine:latest
#FROM sipwise/rtpengine:mr13.4.1.7
#FROM sipwise/rtpengine:mr9.4.1
#FROM ianblenke/rtpengine


COPY rtpengine.conf /etc/rtpengine/rtpengine.conf

#ENTRYPOINT ["rtpengine"]
#CMD ["--config-file=/etc/rtpengine/rtpengine.conf"]

CMD ["rtpengine", "--config-file=/etc/rtpengine/rtpengine.conf"]
