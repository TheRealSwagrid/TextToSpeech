FROM python
ENV semantix_port=7500

COPY TextToSpeech.py /var
COPY requirements /var
COPY AbstractVirtualCapability.py /var
RUN apt-get update && apt-get install -y --no-install-recommends gstreamer-1.0 python-is-python3 python3-gi
#pkg-config libcairo2-dev gcc python3-dev libgirepository1.0-dev

RUN python -m pip install -r /var/requirements
EXPOSE 9999
CMD python /var/TextToSpeech.py ${semantix_port}