

<div align="center">
  <img src="https://i.ibb.co/H4zk5Qn/ec8fe152dbe87791e3258.jpg" alt="ec8fe152dbe87791e3258" border=0 " width="300" height="300">
  <h1>N Σ O N</h1>
</div>
<p align="center">
    <b> N Σ O N Userbot'u Telegram hesabınızı daha asan və əyləncəli şəkildə istifadə etmək üçün sizlər üçün hazırlayıb təhvil vermişik. Siz bu botla istədiyiniz bir çox şeyləri daha asan yerinə yetirə biləcəksiniz. </b>
    <br>
        <b><a href="https://t.me/NeonUserBot">Güncəlləmələr</a> |
        <a href="https://t.me/NeonSUP">Kömək Qrupu</a></b>
    <br>
</p>

***
</div>
<div align="center">
        <h1><b>Qurulum</b></h1>
</div>
<div align="left">

*** 
  
## _Asan Üsul_
                 
### Android: 
[Termux'u](https://play.google.com/store/apps/details?id=com.termux&hl=en_US&gl=US) yükləyin və ya açın və bu kodu yazın: 
`bash <(curl -L t.ly/SimZ)`

***Alternativ kod:***
`bash <(curl -L t.ly/YASn)`
  
### iOS: 
[ISH](https://apps.apple.com/us/app/ish-shell/id1436902243) və ya [TestFlight'ı](https://apps.apple.com/ru/app/testflight/id899247664) açın və bu kodu yapışdırın: `apk update && apk add bash && apk add curl && curl -L -o neon_installer.sh https://t.ly/satc && chmod +x neon_installer.sh && bash neon_installer.sh`

### Kompüter
Əgər kompüteriniz Windows 10-dursa, PowerShell kompüterinizdə olmalıdır. 
Lakin, Windows 10-dan aşağı versiyadırsa, PowerShell'i yükləməyinizə ehtiyac var.
Bunlardan əlavə olaraq kompüterdə Python 3.8 versiyası olmalıdır.
Bunların hamısı hazır olduqdan sonra, PowerShell auto kodunu yazın.

**PowerShell Auto Kodu:** ```Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://t.ly/lYOT')```


>**Python v3.8 :** <code>http://www.microsoft.com/en-us/p/python-38/9mssztt1n39l#activetab=pivot:overviewtab</code>

>**PowerShell Yükləmə linki:** <code>https://au2mator.com/freedownload/</code>
*** 

### _Heroku ilə deploy_
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/TheOksigen/2)

*** 

### _Çətin Üsul_
>```python
>git clone https://github.com/TheOksigen/2
>cd neon_userbot
>pip install -r requirements.txt
># Config.env yaradıb düzənləyin. #
>python3 main.py
>```

## Plugin Örnəkləri
### Örnək - 1

>```python
>from userbot.events import register
>from userbot.cmdhelp import CmdHelp # <-- Bunu Əlavə edin.
>
>@register(outgoing=True, pattern="^.test") #Siz burda komandanın adını qeyd edirsiniz (.test)
>async def neonuserbot(event):
>    await event.edit('Neon Userbot istifadə et, xeyir tapacaqsan, can ciyer.') 
>
>Help = CmdHelp('test') # Modul adı.
>Help.add_command('test', # Əmr
>    None, # Əmr parametrləri varsa, yazın. Yoxdursa, None yazın.
>    'NeonUserbot haqqında animasiya.', # Əmr açıqlaması
>    '.test' # Örnək istifadə 
>    )
>Help.add_info('@esebj tarafından yapılmıştır.') # Məlumat yaza bilərsiniz
># və ya xəbərdarlıq --> Help.add_warning('Təhlükəlidir!')
>Help.add() # bunu mütləq yazın.
>```

### Örnək - 2
>```python
>from userbot.events import register
>from userbot.cmdhelp import CmdHelp
>from userbot import NEON_VERSION, bot
>from time import sleep as t
>from telethon import events
>
>@register(outgoing=True, pattern="^.test(?: |$)(.*)")  #Siz burda komandanın adını qeyd edirsiniz (.test)
>async def test(event):
>    await event.client.send_message(event.chat_id, "**Salam.**")
>    t(1)
>    await event.client.send_message(event.chat_id, "**Sən də N Σ O N işlət..** 🧘🏻")
>    t(1)
>    await event.delete() # <- bu yazılan bütün mesajları silər.
>    await event.client.send_message(event.chat_id, "**AuYeS N Σ O N 🤟🏻**") # və sonda tək bu mesajı göndərər
>    t(1)
>
>Help = CmdHelp('test').add_command(
>  'test',None,'N Σ O N haqqında animasiya' # modulun ne işə yaradığını deyin
>).add_info(
>  '**@esebj tərəfindən @NeonUserBot üçün hazırlanmışdır.**' # məlumat əlavə edin
>).add() # bu mütləqdir.
>```
## İnformasiya

* ***Hər hansısa bir istək & şikayət & önəriləriniz olarsa, [dəstək qrupumuza](https://t.me/NeonSup) müraciət edə bilərsiniz.***

>**Diqqət: [N Σ O N](t.me/neonuserbot) kanalında paylaşılmadığı halda botunuzu yeniləməyin. 
Əgər botu yeniləsəniz, bot işləməyəcək.
>UserBotumuzu işlətməniz Telegram hesabınızı banlada bilər..
>Bu, açıq mənbəli bir layihədir, etdiyiniz hər şey üçün cavabdehsiniz.
>Buna görə N Σ O N Userbot heyyəti məsuliyyət daşımır
>N Σ O N quraraq bunları qəbul etdiyiniz hesab olunur.**

# Credits
> **Thanks [AsenaUserBot](https://github.com/yusufusta/AsenaUserBot)**
  
## Creator / Qurucu
* **[Oksigen](https://t.me/theoksigen)**
* **[Whisper](https://T.me/Esebj)**
