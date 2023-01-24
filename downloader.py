import pytube
from tqdm import tqdm

class Downloader:
    def __init__(self, path):
        self.file = pytube.YouTube(path, on_progress_callback=self.progress_function).streams.get_highest_resolution()
        self.t = tqdm(total=self.file.filesize,  unit='B', unit_scale=True, unit_divisor=1024, miniters=1)
        self.prev_remaining = self.file.filesize

    def percent(self, tem, total):
        perc = float(100) - (float(tem) / float(total)) * float(100)
        return perc
        
    def progress_function(self, stream, chunk, bytes_remaining):
        size = stream.filesize
        self.t.update(self.prev_remaining - float(bytes_remaining))
        self.prev_remaining = float(bytes_remaining)

    def download_file(self):
        self.file.download("./videos")
        self.t.close()