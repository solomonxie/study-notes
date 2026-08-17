# Plex Media Server All-in-one [DRAFT]

Installment Methods:
- [ ] Docker (Recommand)
- [ ] Mac
- [ ] Linux
- [ ] NAS


## Docker Setup (PC)

Image: https://hub.docker.com/r/plexinc/pms-docker/

Docker-compose:
```yaml
# Access from: http://localhost:32400/web
---
version: '3'
services:
  plex:
    container_name: plex
    image: plexinc/pms-docker:beta
    restart: unless-stopped
    environment:
      - TZ=America/Denver
      - PLEX_CLAIM=claim-###############
      - PLEX_UID=1000  # $ id -u `whoami`
      - PLEX_GUID=1000  # $ id -g `whoami`
    network_mode: bridge
    hostname: PlexDockerBeta
    ports:
      - "32400:32400"  # Main Access
      - "32469:32469"
      - "32401:32401"
      - "3005:3005"
      - "8324:8324"
      - "1900:1900/udp"
      - "32410:32410/udp"
      - "32412:32412/udp"
      - "32413:32413/udp"
      - "32414:32414/udp"
    volumes:
      - $PWD/config/plex:/config
      - $PWD/transcode:/transcode
      - $PWD/media:/data
      # - $PWD/tv:v
      # - $PWD/movies:/movies
```


## Docker Setup for RaspberryPi (ARM)

Image: https://hub.docker.com/r/jaymoulin/plex/
