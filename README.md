# Streamlit Space

[![Open in Streamlit][share_badge]][share_link] [![GitHub][github_badge]][github_link] [![PyPI][pypi_badge]][pypi_link] 

Add blank lines to your Streamlit app.



## Installation

```bash
pip install streamlit-space
```



## Quickstart

```python
import streamlit as st
from streamlit_space import space

st.title('Streamlit Space')
space()
```



## License

Streamlit Space has an MIT license, as found in the [LICENSE](https://github.com/imyizhang/streamlit-space/blob/main/LICENSE) file.



## Documentation

### streamlit_space.space

#### `streamlit_space.space(container=None, lines=1)`

Add blank lines to Streamlit app.

**Parameters**:

* **container** (any, optional): The Streamlit container. Defaults to `None`.
* **lines** (int, optional): The number of blank lines to be added. Defaults to `1`.



## Contribution



## Changelog

Version 0.1.0:

* Made spacing component functional



[share_badge]: https://static.streamlit.io/badges/streamlit_badge_black_white.svg
[share_link]: https://share.streamlit.io/imyizhang/streamlit-space/main/streamlit_app.py

[github_badge]: https://badgen.net/badge/icon/GitHub?icon=github&color=black&label
[github_link]: https://github.com/imyizhang/streamlit-space

[pypi_badge]: https://badgen.net/pypi/v/streamlit-space?icon=pypi&color=black&label
[pypi_link]: https://www.pypi.org/project/streamlit-space