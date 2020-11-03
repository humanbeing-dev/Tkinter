"""Application for reading youtube playlists"""
from tkinter import *
from YoutubeApp.youtube import get_videos_data, get_playlist_title_and_description, get_videos_urls_from_playlist


class Application(Frame):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.create_widgets()

    def create_widgets(self):
        self.lbl_1 = Label(root, text="Input playlist link:").pack(pady=5)
        self.ent_1 = Entry(root, width=40)
        self.ent_1.pack()
        self.lbl_2 = Label(root, text="How many have you watched?:").pack(pady=5)
        self.ent_2 = Entry(root, width=40)
        self.ent_2.pack()
        self.btn_1 = Button(root, text="Submit", width=20, command=self.submit).pack(pady=10)
        self.lbl_3 = Label(root, text="")
        self.lbl_3.pack(pady=5)
        self.lbl_4 = Label(root, text="")
        self.lbl_4.pack(pady=5)

    def submit(self):
        link = self.ent_1.get()
        pattern = re.compile("list=([\w]+)")
        find = re.search(pattern, link)
        vid_watched = int(self.ent_2.get()) if self.ent_2.get().isnumeric() else 0

        get_playlist_title_and_description(find[1])
        data = get_videos_urls_from_playlist(find[1])
        vids = get_videos_data(data)
        total1 = (sum([element['vid_length'] for index, element in enumerate(vids) if index >= vid_watched]))
        total2 = (sum([element['vid_length'] for index, element in enumerate(vids)]))

        h, m = map(int, divmod(total1, 3600))
        m, s = divmod(m, 60)
        self.lbl_3.config(text=f"{h:02}:{m:02}:{s:02} left to watch")
        self.lbl_4.config(text=f"{(1-total1/total2)*100:.2f}% watched")


root = Tk()
root.title("Youtube playlists checker")
root.geometry("400x220")
app = Application(master=root)
root.mainloop()
