import pytchat

from django.shortcuts import render

chat = pytchat.create(video_id="5tjG70YJLlg")

while chat.is_alive():
    for c in chat.get().sync_items():
        print(f"{c.datetime} [{c.autor.name}] - {c.message}") 