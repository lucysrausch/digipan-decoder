1. Install sigrok-cli from git.
2. copy digipan to /usr/local/share/libsigrokdecode/decoders/ (or wherever yo store your decoders)
3. capture data with pulseview and save as .sr
4. >_ sigrok-cli -i digipan_xray.sr -P digipan:format=dec:bit_order=msb-first > digipan_xray.txt
5. don't worry. Takes forever (~3-5min)
6. >_ python image.py digipan_xray.txt
