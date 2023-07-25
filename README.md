# clifton_ai
An AI chatbot utility based on your documents, built on top of Llama 2 that you can run locally on your own hardware without a GPU. Note that it is not fast, and you need a decent PC with lots of memory to run.

When up and running, you can ask it questions using natural language and it will provide answers based on the content in the PDFs you supply.

[A guide written by Kenneth Leung](https://towardsdatascience.com/running-llama-2-on-cpu-inference-for-document-q-a-3d636037a3d8) provided the basis for Clifton.

## Installation

### Setup your environment

The following instructions assume you are running on a Linux based distribution. These instructions should be easily adaptable for other OS platforms although they have not been tested. 

Assuming you have [Miniconda](https://docs.conda.io/en/latest/miniconda.html) installed already, create an environment as follows:

```bash
$ conda create --name=cliftonai python=3.10
```

Activate it and install the necessary Python packages as follows from within the clifton_ai top-level directory:

```bash
$ conda activate cliftonai
$ pip install -r requirements.txt
```

### Download the Llama 2 model

Specifically you should download a quantized 7B parameter version of Llama2 optimized for chat applications in ggml format if you want to run it on your PC (no GPU required). Feel free to experiment with other versions of the model. If you want to run it on a GPU, consider downloading directly from [Meta AI](https://ai.meta.com). If you do use different models, you will need to update the references contained in the code.

You can download the model from Hugging Face at this [URL](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML). Click on the "Files and versions" tab, and select llama-2-7b-chat.ggmlv3.q8_0.bin. Note that at time of writing, this file is 7.16GB. The clue is in the name - these are large language models.

Once downloaded, move the file into the models directory.

## Index your documents

Place your PDFs into the data directory. In this example, a PDF has been created from the Wikipedia page for my home village of [Sawley, Derbyshire](https://en.wikipedia.org/wiki/Sawley,_Derbyshire).

Build the index by running the following command from within the clifton_ai top-level directory:

```bash
$ python buildvectorstore.py
```

If you update your PDFs or decide to add more PDFs to the directory, you will need to re-build the index.

# Test your installation

```bash
$ python main.py "What is the old name for Sawley"

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
```