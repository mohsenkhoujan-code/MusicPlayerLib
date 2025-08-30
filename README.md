# Music-player demo 0.0.1 (only for windows)
 
# کتابخانه پخش موزیک با رابط کاربری ساده  

این پروژه یک کتابخانه ساده برای پخش موزیک است که با استفاده از زبان‌های **پایتون** و **سی‌شارپ** توسعه داده شده است. این کتابخانه به شما امکان کنترل لحظه‌ای بر روی موزیک‌ها را می‌دهد و رویدادهایی مانند **موزیک بعدی**، **موزیک قبلی**، **بسته شدن پخش‌کننده موزیک** و **پایان موزیک** را پشتیبانی می‌کند و میتوانید از آن در پروژه های خود استفاده کنید زیرا فلسفه پشت این ابزار استفاده در برنامه نویسی است.

## ویژگی‌های کلیدی  

- **کنترل لحظه‌ای موزیک**: پخش، توقف، مکث و تغییر موزیک‌ها به صورت لحظه‌ای.  
- **رویدادهای قابل مدیریت**:  
  - رفتن به موزیک بعدی  
  - بازگشت به موزیک قبلی  
  - بسته شدن پخش‌کننده موزیک  
  - پایان موزیک  
- **رابط کاربری ساده**: رابط کاربری تمیز و آسان برای استفاده.  
- **پشتیبانی از چندین فرمت موزیک**: فرمت‌های رایج موزیک مانند MP3, WAV, و غیره.  
- **استفاده در پروژه ها**: استفاده در زبان های برنامه نویسی مختلف به خصوص python و C#

## نحوه استفاده 
#### استفاده در پایتون

- ابتدا تمام فایل ها را از گیت هاب من دانلود و استخراج کنید.
- سپس فایل preparing.exe را اجرا کنید. (فقط یکبار اجرا کنید)
- سپس پوشه music-veiwer .را در مسیر مورد نظر خود قرار دهید
- .و بعد این کد را در فایل مورد نظر خود وارد کنید:


```python

from music_galery import music_player

musics = [
    "c:\\music_one.mp3",
    "c:\\music_two.mp3",
    "c:\\music_three.mp3",
    "c:\\music_four.mp3"
]

mv = music_player()
round_ = 0
while(True):
    if mv.if_event_close():
        break
    elif mv.if_event_next() or mv.if_event_end():
        if round_ < len(musics)-1:
            round_ += 1
    elif mv.if_event_prev():
        if round_ > 0:
            round_ -= 1

    mv.play(musics[round_])
    print(mv.check_error())

    

```
#### استفاده در سی‌شارپ

- ابتدا تمام فایل ها را از گیت هاب من دانلود و استخراج کنید.
- فایل **Libs\\Music_Light_Class.dll** و **Libs\\NAudio.dll** را در Reference پروژه خود بر روی VisualStudio قرار دهید.
- سپس کد زیر را در قسمت مورد نظر خود وارد کنید:


```c#

namespace musicPl
{
  class Program
  {
    static void Main(string[] args)
    {
        Provider MusicPlayer = new Provider();
        Events MusicEvent = new Events();

        string[] musics = {
            "c:\\music_one.mp3",
            "c:\\music_two.mp3",
            "c:\\music_three.mp3",
            "c:\\music_four.mp3"
        };
        byte event = 0;
        int round = 0;
        while(true){
            if((event == MusicEvent.next()) || (event == MusicEvent.end())){
                if(round < musics.length-1){
                    round++;
                }
            }
            if(event == MusicEvent.prev()){
                if(round > 0){
                    round--;
                }
            }
            if(event == MusicEvent.close()){
                break;   
            }
            event = MusicPlayer.AttrebDisplay(musics[round]);
            if(MusicPlayer.is_error()){
                Console.WriteLine(MusicPlayer.error)
            }
        }
    }
  }
}




```


## نصب کتابخانه  

برای استفاده از این کتابخانه، ابتدا آن را از گیت‌هاب دانلود کنید:  

**https://github.com/MohsenKouj/Music-viewer/archive/refs/heads/main.zip**  
  
# Simple Music Player Library with a User-Friendly Interface  

This project is a simple music player library developed using **Python** and **C#**. It allows you to have real-time control over music playback and provides access to events such as **next track**, **previous track**, **music player closing**, and **end of track**.  

## Key Features  

- **Real-Time Music Control**: Play, pause, stop, and switch tracks instantly.  
- **Manageable Events**:  
  - Move to the next track  
  - Go back to the previous track  
  - Music player closing  
  - End of track  
- **Simple User Interface**: Clean and easy-to-use interface.  
- **Support for Multiple Music Formats**: Common music formats like MP3, WAV, etc.  

## How to Use  
#### Use in python

- First, download and extract all the files from my GitHub.
- Then, run the **preparing.exe** file (only once).

- Next, place the **music-viewer** *folder* in your preferred location.

- Finally, enter this code in your designated file:
```python

from music_galery import music_player

musics = [
    "c:\\music_one.mp3",
    "c:\\music_two.mp3",
    "c:\\music_three.mp3",
    "c:\\music_four.mp3"
]

mv = music_player()
round_ = 0
while(True):
    if mv.if_event_close():
        break
    elif mv.if_event_next() or mv.if_event_end():
        if round_ < len(musics)-1:
            round_ += 1
    elif mv.if_event_prev():
        if round_ > 0:
            round_ -= 1

    mv.play(musics[round_])
    print(mv.check_error())
    

```
#### Use in C#

- First, download and extract all the files from my GitHub.
- add the **Libs\\Music_Light_Class.dll** and **Libs\\NAudio.dll** files to the References of your project in Visual Studio.
- Then, enter the following code in your desired section:

```c#
namespace musicPl
{
  class Program
  {
    static void Main(string[] args)
    {
        Provider MusicPlayer = new Provider();
        Events MusicEvent = new Events();

        string[] musics = {
            "c:\\music_one.mp3",
            "c:\\music_two.mp3",
            "c:\\music_three.mp3",
            "c:\\music_four.mp3"
        };
        byte event = 0;
        int round = 0;
        while(true){
            if((event == MusicEvent.next()) || (event == MusicEvent.end())){
                if(round < musics.length-1){
                    round++;
                }
            }
            if(event == MusicEvent.prev()){
                if(round > 0){
                    round--;
                }
            }
            if(event == MusicEvent.close()){
                break;   
            }
            event = MusicPlayer.AttrebDisplay(musics[round]);
            if(MusicPlayer.is_error()){
                Console.WriteLine(MusicPlayer.error)
            }
        }
    }
  }
}

```

### Installing the Library  

To use this library, first clone the repository from GitHub:  
**https://github.com/MohsenKouj/Music-viewer/archive/refs/heads/main.zip**  