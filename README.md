# Radio On-Demand Streamer

Startet `ffmpeg` nur bei Client-Verbindung und streamt Radio live über HTTP, wandelt dabei DVBS2 in MP3 um.

## Installation (TrueNAS Scale)

1. Öffne die TrueNAS SCALE Weboberfläche und navigiere zu  
   **Apps → Custom App → Install via YAML**
2. Gib einen Namen ein, z. B. `satradio2mp3`
3. Füge folgenden Inhalt in das Feld **Custom Config** ein:

    ```yaml
    version: "3.7"

    services:
      satradio2mp3:
        image: ghcr.io/ralf31337/satradio2mp3:latest
        ports:
          - "8000:8000"
        environment:
          - STREAM_URL=http://satip.local/?src=1&freq=11053&pol=h&ro=0.35&msys=dvbs2&mtype=8psk&plts=off&sr=22000&fec=34&sid=28429&pids=0,18,120,121
    ```

    > 🔁 Ersetze `STREAM_URL` ggf. durch deine eigene SAT>IP-Quelle

4. Klicke auf **Installieren**
5. Rufe den MP3-Stream über VLC oder Browser auf:  
   `http://<TrueNAS-IP>:8000/radio.mp3`

---

### 🛠️ Optional: Helm-Chart Support

Für spätere Integration in den TrueNAS App-Katalog (z. B. als Helm-Chart) ist dieses Repository vorbereitet. Ein entsprechender `Chart.yaml` und `values.yaml` befindet sich im `charts/`-Verzeichnis.