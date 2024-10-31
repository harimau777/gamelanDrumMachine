This project implements a drum machine designed to facilitate the creation of Gamelan rhythms. Gamelan is a traditional Javanese style of music that features nested rhythm patterns. A simplified description of the way that Gamelan organizes rhythm is:
- The smallest organization of rhythm is a measure called a "gatra". Gatra are made up of beats called "keteg". Gatra are usually four keteg long.
- Several gatra are organized into a phrase called a "colotomy"[1]. After each colotomy, the sequence of gatra are repeated.
- Generally, only a single instrument plays on each keteg. An exception is the last keteg of the colotomy where a large gong is usually played along with whatever note would normally be played during that keteg.
- The same instrument is generally played on the same keteg in each of the gatra making up the colotomy. However, in some gatra they may be replaced by a rest called a "pin".
- For example, suppose that we adopt a notation where "d" indicates a keteg where a drum is played, "b" indicates a bell, "p" indicates a pin (rest), and "G" indicates that both a gong and bell are played at the same time. Then an example of a four gatra Gamelan rhythm might be[2]: dddb pddp dddb dddG

This means that, while a traditional drum machine focuses on allowing you to sequence different layers of the instruments in a drum set (e.g. the snare providing a steady rhythm while the high hat elaborates over top), this program instead focuses on facilitating the user in establishing the patterns of the gatra and colotomy.

Notes:
- I was introduced to Indonesian music through my practice of the Indonesian martial arts. However, I have never actually played Gamelan nor have I been formally trained in its music theory. Therefore, while I am attempting to accurately represent this art, it is likely that there will be instances where I am misinterpreting or have a shallow understanding. Feel free to contact me with any mistakes that I have made.
- In the source code I have elected to use Western rather than Javanese music terminology in order to make it easier for most developers to understand. For example, I use "beat" instead of "keteg" and "measure" instead of "gatra".

[1] I am not certain that this is the correct term and/or that I am using it correctly. I will update my terminology as I learn more about Javanese music theory.

[2] This notation is somewhat similar to commonly used notation for Gamelan music. In the future, I would like to switch to using the established notation. However, for now I am using this approach for simplicity.
