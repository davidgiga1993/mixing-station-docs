# VI

Mixing Station supports all models of the VI mixer series, but there are some limitations:

- Vi 1/2/4/6: Mixer doesn't handle the data sync very well. There might be issues occurring. Please test thoroughly before using in a production environment!
- Vi 200/400/600/1k/2k/3k/5k/7k: No known issues


## Limitations
The general [hiqnet limitations](hiqnet.md) apply as well as the following:

### Matrix Mixes
Mixing Station can only correctly assign the source channels to a matrix if the `Long Label` and `Short Label` are equal for the first 6 chars.

**Example** Long Label: `My Drums` Short Label: `My Dru`
