At the moment there are three-ish projects in here, each with multiple parts.

1. The main Python files
   - 4800-embedded.py
      - Main program for Raspberry Pi
   - 4800-server.py
      - Main program for server
2. Various testing files
   - enet-chat-test.py
      - peer to peer chatroom. *Should* be compatible with the godot chatroom as well but might be a few tweaks away.
   - enet-video-test.py
      - Used to serve video, later webcam, to Godot. Will get encorporated into 4800-embedded.py later on.
   - hp-server.py
      - Holepunch server. Will form the basis of 4800-embedded.py later on.
3. Mobile app project in Godot
   - VideoTest/
4. socket_convenience.py
   - Convenient socket functions.