#!/usr/bin/env python3
import requests
import logging
import time

# Configure logging
logging.basicConfig(filename='sabnzbd_control.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

# Tautulli configuration (Replace with your own Tautulli API key and server URL)
TAUTULLI_API_KEY = "YOUR_TAUTULLI_API_KEY"
TAUTULLI_URL = "http://YOUR_TAUTULLI_SERVER_URL"

# SABnzbd configuration (Replace with your own SABnzbd API key and server URL)
SABNZBD_API_KEY = "YOUR_SABNZBD_API_KEY"
SABNZBD_URL = "http://YOUR_SABNZBD_SERVER_URL"

def is_streaming():
    """Check if a video is currently being streamed using Tautulli."""
    try:
        response = requests.get(f"{TAUTULLI_URL}/api/v2?apikey={TAUTULLI_API_KEY}&cmd=get_activity")
        data = response.json()
        streaming = int(data['response']['data']['stream_count']) > 0
        logging.info(f"Streaming status: {streaming}")
        return streaming
    except Exception as e:
        logging.error(f"Error checking streaming status: {e}")
        return False

def pause_sabnzbd():
    """Pause SABnzbd downloads."""
    try:
        response = requests.get(f"{SABNZBD_URL}/sabnzbd/api?mode=pause&apikey={SABNZBD_API_KEY}")
        logging.info(f"Paused SABnzbd: {response.status_code}, {response.text}")
    except Exception as e:
        logging.error(f"Error pausing SABnzbd: {e}")

def resume_sabnzbd():
    """Resume SABnzbd downloads."""
    try:
        response = requests.get(f"{SABNZBD_URL}/sabnzbd/api?mode=resume&apikey={SABNZBD_API_KEY}")
        logging.info(f"Resumed SABnzbd: {response.status_code}, {response.text}")
    except Exception as e:
        logging.error(f"Error resuming SABnzbd: {e}")

def main():
    while True:
        try:
            if is_streaming():
                pause_sabnzbd()
            else:
                resume_sabnzbd()
            time.sleep(60)  # Check every 60 seconds
        except Exception as e:
            logging.error(f"Error in main loop: {e}")

if __name__ == "__main__":
    main()
