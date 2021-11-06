FROM erdembey/epicuserbot:latest
RUN git clone https://github.com/TheOksigen/1 /root/neon_userbot
WORKDIR /root/neon_userbot/
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]
