# :question:Question :exclamation:Answering with the help of transformers

Copyright Mitra Mirshafiee, 2022 Licensed under MIT License.

## Easiest way to run the app??

Here is the link to the streamlit app, if you want to take a look at the main functionality of this project: [link](https://question-answering.streamlit.app/)

For running the app locally, make sure you install the requirements first, and then run the app with Stremlit. For example, runt the following commands, if you're using pip:


`pip install -r requirements.txt`

And then:

`streamlit run app.py`

Additionally, you can use the Docker image to replicate the project. For this you need to know how to work with Docker (more on this on [Docker documentation](https://docs.docker.com/).) Here is the 

## Description

This is an app based on the Python programming language. In this app, 
we create a question answer application with the help of [streamlit](https://docs.streamlit.io/library/get-started), [wikipedea](https://pypi.org/project/wikipedia/), and [transformers](https://huggingface.co/) libraries. We're using 
transformers models to bring together the power of deep learning and online web development.

Please refer to runtime.txt to make sure your Python version is correct.

## Contribution

You can read about how you can contribute to this project through the contributing.md file. And thanks for considering a contribution to this project!

## License

The License to this project is MIT license which allows you to utilize the code
and create your own version of the app.

## Language

This project is written in Python with the help of the Streamlit framework. 

## preview


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
