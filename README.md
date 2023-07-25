# clifton_ai
An AI chatbot utility based on your documents, built on top of Llama 2 that you can run locally on your own hardware without a GPU. Note that it is not fast, and you need a decent PC with lots of memory to run.

When up and running, you can ask it questions using natural language and it will provide answers based on the content in the PDFs you supply.

The following guide by Kenneth Leung provided the basis for Clifton.

https://towardsdatascience.com/running-llama-2-on-cpu-inference-for-document-q-a-3d636037a3d8

## Installation

### Setup your environment

Assuming you have Miniconda installed already, create an environment as follows:

conda create --name=cliftonai python=3.10

Activate it and install the necessary Python packages as follows:

conda activate cliftonai
pip install -r requirements.txt

### Download the Llama 2 model

Specifically, a quantized 7B parameter version of Llama2 optimized for chat applications in ggml format - llama-2-7b-chat.ggmlv3.q8_0.bin. Place it in the models directory

https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML

## Index your documents

Place you PDFs into the data directory. In this example, a PDF has been created from the Wikipedia page for my home village of Sawley, Derbyshire.

Build the index as follows:

python buildvectorstore.py

# Test your installation

python main.py "What is the old name for Sawley"

Question: What is the old name for Sawley

Answer: The old name for Sawley was Sallé.

==================================================


Source Document 1

Source Text: local politician and former president of the Club.[13][15]Sawley Cricket Club currently have 4 Senior XI
teams competing in the Derbyshire County Cricket League[16] and a long established Junior trainingSportGolf
CricketSawley, Derbyshire - Wikipedia https://en.wikipedia.org/wiki/Sawley,_Derbyshire
2 of 4 7/25/23, 11:01 AM
Document Name: data/Sawley, Derbyshire - Wikipedia.pdf
Page Number: 1

============================================================

Source Document 2

Source Text: e old name for Sawley was Sallé.[3] Between Sawley andChurch Wilne and Great Wilne is the junction of the RiverDerwent and the Trent. It is to this that Sawley owes its
position.[3] e church of All Saints is thirteenth century
and contains Saxon and Norman work.[4] and commands a
position  on  a  small  rise  near  the  river.  Sawley  Baptist
Church, was built on Wilne Lane in 1800.[5]
Up until the 19th century, Sawley was the most important
Document Name: data/Sawley, Derbyshire - Wikipedia.pdf
Page Number: 0

============================================================
Time to retrieve response: 21.14585060600075



