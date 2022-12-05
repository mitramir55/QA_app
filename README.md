# :question:Question :exclamation:Answering with the help of transformers


## Easiest way to run the app??

Here is the link to the streamlit app: [link](https://question-answering.streamlit.app/)

If you want to run it locally, as streamlit might have many conflicts with other libraries you've installed before, I suggest using Google Colab to avoid any confusion or time loss. But you can also clone the project and run it on your own system after installing all the requirements in the requirements.txt file.


Make sure to install the requirements first before creating the app. For example, runt the following command, if you're using pip:
`pip install -r requirements.txt`

## Description

This is an app based on the Python programming language. In this app, 
we create a question answer application with the help of [streamlit](https://docs.streamlit.io/library/get-started), [wikipedea](https://pypi.org/project/wikipedia/), and [transformers](https://huggingface.co/) libraries. We're using 
transformers models to bring together the power of deep learning and online web development.

Please refer to runtime.txt to make sure your Python version is correct.

You can read about how you can contribute to this project through 
the contributing.md file.

The License to this project is MIT license which allows you to utilize the code
and create your own version of the app.

This app will be created under a steamlit server, but for now, it's still a locally run project.

|![image](https://user-images.githubusercontent.com/53291220/196006279-24c20f94-3c8f-4449-9067-263a5c0bf566.png)|
|:--:| 
| *A preview of the first overview of the app* |


## How to use?

Using this app is pretty easy! All you have to do is choosing a topic (here I chose to know more about my name - Mitra):

|![image](https://user-images.githubusercontent.com/53291220/196006445-b283d33e-748b-4d23-9075-f9929a905c79.png)|
|:--:| 
| *First step: choose the topic* |

Then, after reading the scraped wikipedea article, you can ask a question from the text. For instance, I asked: "What is the origin of Mitra", and as you can see, after a few seconds, the answer is outputted - Indo-Iranian.

|![image](https://user-images.githubusercontent.com/53291220/196006525-368ec6d7-706c-43cd-8018-8ba65ceb566b.png)|
|:--:| 
| *Second step: ask a question* |

## Tests

Unit tests are placed inside the code, specifically in the app.py.