#  Copyright Mitra Mirshafiee, 2022 Licensed under MIT License.
#  See the LICENSE.txt for more information.

import streamlit as st
from PIL import Image
import os

image = Image.open(os.path.join("assets", "About.png"))
st.image(image)
st.markdown("[source](https://www.google.com/url?sa=i&url=https%3A%2F%2Fknswamy.medium.com%2Fnlp-deep-learning-training-on-downstream-tasks-using-pytorch-lightning-question-answering-on-17d2a0965733&psig=AOvVaw3dF3CmmRkb3MGa7yc5yX8L&ust=1667234039984000&source=images&cd=vfe&ved=0CA4QjhxqFwoTCLjwuvewiPsCFQAAAAAdAAAAABAE)")


st.header("Who is the creator?")

st.markdown("""
The creator of this project is [Mitra Mir](https://mitramirshafiee.ir/).
 If you had any questions regarding this app, please refer to the 
 [GitHub page](https://github.com/mitramir55/QA_app).
 For any other questions, you can email mitrasadat.mirshafie@ucalgary.ca

 """)

 
st.header("What's the aim, and how can I contribute?")

st.markdown("""
This project is one of the deliverables of the 
 ENSF 619 L01 - (Fall 2022) - Software Development Using Open Source course, 
 taught by [DR. Ann Barcomb](https://schulich.ucalgary.ca/contacts/ann-barcomb).
 If you want to contribute to this project, please refer to the 
 [CONTRIBUTING file](https://github.com/mitramir55/QA_app/blob/main/CONTRIBUTING.md)
 in the GitHub repo. 
""")

st.markdown("""
This project is under the MIT license. 
Please make sure to read the license before contributing.
""")
