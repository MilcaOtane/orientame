import streamlit as st
import pandas as pd
import numpy as np
st.title('Descubre tu camino, diseña tu futuro con OrientaMe')

import streamlit as st
import pandas as pd
import numpy as np
import datetime
d = st.date_input(
"Fecha de cumpleaños",
datetime.date(2019, 7, 6))
st.write('Tu cumpleños es:', d)
