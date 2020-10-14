# AnarchyDumper.py

AnarchyDumper.py is a program written in Python that dumps all the contents of one or more Discord text channels.

## About

AnarchyDumper. Weird name for such a program, you may think.
Well, perhaps it seems like that at first sight, however I think it's a very appropriate name.

Why? Well, it's simple.

>AnarchyDumper does not dump everything from a channel, it does **more**.
>
>Rather than just backing up every message sent and their content, authors, date of creation, it dumps EVERYTHING!
>***From*** every asset or attachment sent ***to*** all the ID of each user, channel or role that was mentioned in one message.
>
>Thanks to [`discord.py`](https://github.com/Rapptz/discord.py) and its very comfortable support for the Discord API, AnarchyDumper takes everything from a channel and everything related to it and stores everything in **cool and simple JSON files**... And folders for attachments and assets.
>Each attachment and asset has **its own ID** set by the bot, so you can find out what message the attachment or asset was sent in!
>
>Since it dumps everything you can also set up your own builder that **re-builds the messages in another type of format**/, starting from simple .txt files to a recreation of an image for each message!
>
> Isn't it a bit too powerful? ***Well, perhaps that's because it's coming from people who live in Anarchy to people who live in Anarchy.***

**Are there any cons?** Well, yes. *Since the AnarchyDumper dumps so many things, the size of each dump will be pretty... Fat.*
However not that much. We dumped a channel with over 7000 messages and the result ended up being a JSON file 8 MB big.

By the way, it is not slow at all. It may look like it is because it dumps a lot of things, but it is pretty optimized so you should not run in any performance issues.
The channel we dumped that had over 7000 messages got backed up in just 95 seconds.

## Why?

Ever had to delete a channel that was not used anymore or that was useless?
Ever regretted deleting it because it had some good messages on it?
Well, that is the reason of life of AnarchyDumper.
*Honestly, it has been a life saviour to me.*

## Usage

**First of all you need a Discord account that will run AnarchyDumper.** The program accesses to the channels you want to dump by logging into an account that can see these channels. And you need the token for that account. It works with both normal users and bots, however pay attention that injecting those kind of things into your own user account is against Discord's Terms of Service. As such, if you get caught using it... Well, most likely your account is going to be deleted. So pay attention if you're too lazy to use a bot!

If you are using the release, run `run.exe` after you completed the installation you can find below.

Instead if you downloaded the source code, you need to install [`Python`](https://www.python.org/downloads/) and [`discord.py`](https://github.com/Rapptz/discord.py) before running the AnarchyDumper. The installation process then is pretty much the same.

## Installation

**First!** Select the version you want from the last release.

You can't decide on what to choose? Let me help you right here then!

### Faccili
> This version makes very easy to build JSON files, however they will end up being pretty big. Choose it if you want to use a simple-to-edit builder!

### Piccioccu
> This version makes instead very small sized JSON files, however it may be more difficult to build. Choose it if you aren't going to build a backup in another format!

**Last!** Open settings.py like if it's a .txt file and follow these steps:

**1. Select your token!** In `TOKEN =` put the token of the user or bot you'll use AnarchyDumper in.

**2. Decide your species!** In `BOT`, put `True` if you are using AnarchyDumper in a bot, else put `False` if you are using AnarchyDumper in a user.

**3. Choice your targets!** In `CHANNELS`, put the ID of all the channels you want to dump between the brackets.

A bit confused? Here is an example of how your `SETTINGS.py` should look:

```python
TOKEN = 'Ex4mPl3 T0KeN'
BOT = True
CHANNELS = [444433355555, 777777722, 9999999991]
```

## TODO
- [x] Serialize every type of object dumped to JSON.
- [x] Make the dumper not loop on itself on any object.
- [x] Complete it.
- [x] Clean it.
- [ ] Add releases.

## Contributing
I am free to receive Pull Requests. It would be very cool if AnarchyDumper gets better in the future.

## From the Head-Champo, Pikalex
Yo, thanks for reading, very appreciated indeed :zoomedEyes:

SO, if you want to talk to me somewhere, I'd recommend to hit me up on Discord. My username is `Pikalex04#8877`.

## License
[MIT](https://choosealicense.com/licenses/mit/)
