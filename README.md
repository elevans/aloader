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
| `block-rotate` | ![](docs/images/block-rotate.gif) |
| `block-build` | ![](docs/images/block-build.gif) |
| `block-destroy` | ![](docs/images/block-destroy.gif) |
| `block-shuffle` | ![](docs/images/block-shuffle.gif) |
| `block-drop` | ![](docs/images/block-drop.gif) |
| `block-lift` | ![](docs/images/block-lift.gif) |
| `stream-down` | ![](docs/images/stream-down.gif) |
| `stream-up` | ![](docs/images/stream-up.gif) |