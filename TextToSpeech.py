import signal
import sys
import time
from gtts import gTTS
from playsound import playsound

from AbstractVirtualCapability import AbstractVirtualCapability, VirtualCapabilityServer, formatPrint

class TextToSpeech(AbstractVirtualCapability):

    def __init__(self, server):
        super().__init__(server)
        self.uri = "TextToSpeech"

    def read_aloud(self, params: dict):
        text = params["SimpleStringParameter"]
        lang = params["string"]
        tts = gTTS(text, lang=lang, slow=True)
        tts.save("tmp.mp3")
        playsound('tmp.mp3')
        return {}

    def loop(self):
        pass

if __name__ == '__main__':
    # Needed for properly closing when process is being stopped with SIGTERM signal
    def handler(signum, frame):
        print("[Main] Received SIGTERM signal")
        listener.kill()
        quit(1)


    try:
        port = None
        if len(sys.argv[1:]) > 0:
            port = int(sys.argv[1])
        server = VirtualCapabilityServer(port)
        listener = TextToSpeech(server)
        listener.start()
        signal.signal(signal.SIGTERM, handler)
        listener.join()
    # Needed for properly closing, when program is being stopped wit a Keyboard Interrupt
    except KeyboardInterrupt:
        print("[Main] Received KeyboardInterrupt")
        server.kill()
        listener.kill()
