# AutoPauseStream

AutoPauseStream is a Python script designed for home media servers. It optimizes streaming by monitoring Tautulli for ongoing Plex activity and automatically managing SABnzbd downloads. Key aspects of the script include:

**Functionality:**

1. **Streaming Monitoring:**
   - The script checks Tautulli for active Plex streams to detect ongoing media playback.

2. **SABnzbd Control:**
   - If streaming is detected, it pauses SABnzbd downloads to allocate bandwidth for smooth playback.
   - When streaming ends, it resumes SABnzbd downloads to ensure timely downloads.

3. **Preventing Drive Overload:**
   - The script intelligently prevents data transfers to a drive currently playing Plex content, reducing buffering for all users during transfers.

4. **Customizable Frequency:**
   - Users can control the frequency of reaching out to Tautulli by adjusting the sleep duration in the script (default is 60 seconds).

5. **Troubleshooting Logs:**
   - The script outputs detailed logs in the `sabnzbd_control.log` file, which can be helpful for troubleshooting.

**Customizable Variables:**

- Users can customize the following variables in the script to match their own setup:
   - `TAUTULLI_API_KEY`: Replace with your Tautulli API key.
   - `TAUTULLI_URL`: Replace with your Tautulli server URL.
   - `SABNZBD_API_KEY`: Replace with your SABnzbd API key.
   - `SABNZBD_URL`: Replace with your SABnzbd server URL.

**Key Features:**
- Real-time streaming monitoring.
- Automated SABnzbd pause and resume.
- Enhances streaming quality.
- Easy setup for all users.


[Project Link](https://github.com/coasttech/sabnzbd-tautulli-control)

