from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess
import os

# Konfiguration via ENV
PORT = int(os.environ.get("STREAM_PORT", "8000"))
STREAM_URL = os.environ.get("STREAM_URL")
AUDIO_BITRATE = os.environ.get("AUDIO_BITRATE", "192k")
AUDIO_RATE = os.environ.get("AUDIO_RATE", "48000")

class RadioHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/" and self.path != "/radio.mp3":
            self.send_error(404)
            return

        self.send_response(200)
        self.send_header('Content-Type', 'audio/mpeg')
        self.end_headers()

        ffmpeg_cmd = [
            "ffmpeg", "-re",
            "-i", STREAM_URL,
            "-vn", "-acodec", "libmp3lame",
            "-ar", AUDIO_RATE,
            "-b:a", AUDIO_BITRATE,
            "-f", "mp3", "-"
        ]

        try:
            with subprocess.Popen(ffmpeg_cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL) as proc:
                while True:
                    data = proc.stdout.read(4096)
                    if not data:
                        break
                    self.wfile.write(data)
        except (BrokenPipeError, ConnectionResetError):
            pass
        finally:
            if proc.poll() is None:
                proc.terminate()

def run_server():
    print(f"🎧 Bayern 3 On-Demand läuft auf Port {PORT}")
    server = HTTPServer(('', PORT), RadioHandler)
    server.serve_forever()

if __name__ == "__main__":
    run_server()
