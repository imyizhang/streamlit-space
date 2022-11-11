# -*- coding: utf-8 -*-

import streamlit as st
from streamlit_space import space


MD = '''[![Open in Streamlit][share_badge]][share_link] [![GitHub][github_badge]][github_link] [![PyPI][pypi_badge]][pypi_link]

[share_badge]: https://static.streamlit.io/badges/streamlit_badge_black_white.svg
[share_link]: https://share.streamlit.io/imyizhang/streamlit-space/main/streamlit_app.py

[github_badge]: https://badgen.net/badge/icon/GitHub?icon=github&color=black&label
[github_link]: https://github.com/imyizhang/streamlit-space

[pypi_badge]: https://badgen.net/pypi/v/streamlit-space?icon=pypi&color=black&label
[pypi_link]: https://www.pypi.org/project/streamlit-space'''


def app():
    st.set_page_config(
        layout='centered',
        page_icon='✨',
        page_title='Streamlit Space',
    )
    st.title('Streamlit Space')
    st.sidebar.title('Space')
    lines = st.sidebar.slider('lines', 0, 10, 5, 1)
    space(st.sidebar)
    st.sidebar.caption(f'Streamlit {st.__version__}')
    st.markdown(MD)
    space()
    st.write('Add blank lines to your Streamlit app.')
    space(lines=lines)
    st.header('Installation')
    st.code('pip install streamlit-space', language='bash')
    space(lines=lines)
    st.header('Quickstart')
    st.code(
        '''from streamlit_space import space

        space()''',
        language='python',
    )
    space(lines=lines)
    st.header('License')
    st.write('Streamlit Space has an MIT license, as found in the [LICENSE](https://github.com/imyizhang/streamlit-space/blob/main/LICENSE) file.')


if __name__ == '__main__':
    app()
