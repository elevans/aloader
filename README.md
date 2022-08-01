# aloader
A Python package that provides interesting and informative loading animations.

## Usage

To use `aloader` import the package and use a `with` statement with the `Loader` class.

```python
import aloader

with aloader.Loader("Loading...", "Done!", style="shuffle"):
    # some process
```
## Animation styles

Supported animation styles.

| Style | Animation |
| :---: | :---: |
| `block-rotate` | ![](docs/images/rotate.gif) |
| `block-build` | ![](docs/images/build.gif) |
| `block-destroy` | ![](docs/images/destroy.gif) |
| `block-shuffle` | ![](docs/images/shuffle.gif) |
| `block-drop` | |
| `block-lift` | |
| `stream-down` | |
| `stream-up` | |