import pytube
from tqdm import tqdm

def percent(tem, total):
    perc = float(100) - (float(tem) / float(total)) * float(100)
    return perc
    
def progress_function(stream, chunk, bytes_remaining):
    # print(bytes_remaining)
    size = stream.filesize
    # print(str(percent(bytes_remaining, size))+'%')
    # tqdm(percent(bytes_remaining, size))
    per = int(percent(bytes_remaining, size))
    t.update(size - bytes_remaining)

file = pytube.YouTube(input("Enter your link"), on_progress_callback=progress_function).streams.get_highest_resolution()
t = tqdm(total=file.filesize,  unit='B', unit_scale=True, unit_divisor=1024, miniters=1)
file.download("./")