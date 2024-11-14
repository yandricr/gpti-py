
# GPTI

![Downloads](https://img.shields.io/pypi/dw/gpti?style=for-the-badge) ![License](https://img.shields.io/pypi/l/gpti?style=for-the-badge) [![Contributors](https://img.shields.io/github/contributors/yandricr/gpti-py?style=for-the-badge)](https://github.com/yandricr/gpti-py/graphs/contributors) [![Size Package](https://img.shields.io/github/languages/code-size/yandricr/gpti-py?style=for-the-badge)](https://github.com/yandricr/gpti-py) ![Python](https://img.shields.io/badge/python-%233776AB.svg?style=for-the-badge&logo=python&logoColor=white)

This package simplifies your interaction with various GPT models, eliminating the need for tokens or other methods to access GPT. It also allows you to use three artificial intelligences to generate images: DALL·E, Prodia and more, all of this without restrictions or limits

## Installation

You can install the package via PIP

```bash
pip install gpti
```

## Available Models

GPTI provides access to a variety of artificial intelligence models to meet various needs. Currently, the available models include:

- [**ChatGPT**](#gpt)
- [**GPT-3.5-Turbo**](#gpt-v2)
- [**ChatGPT Web**](#gptweb)
- [**GPT-4o**](#gpt-4o)
- [**Bing**](#bing)
- [**LLaMA-3.1**](#llama-3.1)
- [**Blackbox**](#blackbox)
- [**AI Images**](#ai-images)

## Api key

If you want to access the premium models, enter your credentials. You can obtain them by [clicking here](https://nexra.aryahcr.cc/api-key/en).

```python
from gpti import nexra

nexra("user-xxxxxxxx", "nx-xxxxxxx-xxxxx-xxxxx");
```

<a id="gpt"></a>
## Usage GPT

```python
import json
from gpti import gpt

res = gpt.v1(messages=[
    {
        "role": "assistant",
        "content": "Hello! How are you today?"
    },
    {
        "role": "user",
        "content": "Hello, my name is Yandri."
    },
    {
        "role": "assistant",
        "content": "Hello, Yandri! How are you today?"
    }
], prompt="Can you repeat my name?", model="GPT-4", markdown=False)

if res.error() != None:
    print(json.dumps(res.error()))
else:
    print(json.dumps(res.result()))
```

#### Models

Select one of these available models in the API to enhance your experience.

- gpt-4
- gpt-4-0613
- gpt-4-32k
- gpt-4-0314
- gpt-4-32k-0314
- gpt-3.5-turbo
- gpt-3.5-turbo-16k
- gpt-3.5-turbo-0613
- gpt-3.5-turbo-16k-0613
- gpt-3.5-turbo-0301
- text-davinci-003
- text-davinci-002
- code-davinci-002
- gpt-3
- text-curie-001
- text-babbage-001
- text-ada-001
- davinci
- curie
- babbage
- ada
- babbage-002
- davinci-002

<a id="gpt-v2"></a>
## Usage GPT v2

It's quite similar, with the difference that it has the capability to generate real-time responses via streaming using gpt-3.5-turbo.

```python
import json
from gpti import gpt

res = gpt.v2(messages=[
    {
        "role": "assistant",
        "content": "Hello! How are you today?"
    },
    {
        "role": "user",
        "content": "Hello, my name is Yandri."
    },
    {
        "role": "assistant",
        "content": "Hello, Yandri! How are you today?"
    },
    {
        "role": "user",
        "content": "Can you repeat my name?"
    }
], markdown=False, stream=False)

if res.error() != None:
    print(json.dumps(res.error()))
else:
    print(json.dumps(res.result()))
```

## Usage GPT v2 Streaming

```python
import json
from gpti import gpt

res = gpt.v2(messages=[
    {
        "role": "assistant",
        "content": "Hello! How are you today?"
    },
    {
        "role": "user",
        "content": "Hello, my name is Yandri."
    },
    {
        "role": "assistant",
        "content": "Hello, Yandri! How are you today?"
    },
    {
        "role": "user",
        "content": "Can you repeat my name?"
    }
], markdown=False, stream=False)

if res.error() != None:
    print(json.dumps(res.error()))
else:
    for chunk in res.stream():
        print(json.dumps(chunk))
```

<a id="gptweb"></a>
## Usage GPT Web

GPT-4 has been enhanced by me, but errors may arise due to technological complexity. It is advisable to exercise caution when relying entirely on its accuracy for online queries.

```python
import json
from gpti import gpt

res = gpt.web(prompt="Are you familiar with the movie Wonka released in 2023?", markdown=False)

if res.error() != None:
    print(json.dumps(res.error()))
else: 
    print(json.dumps(res.result()))
```

<a id="gpt-4o"></a>
## Usage GPT-4o

```python
import json
from gpti import gpt

res = gpt.v3(messages=[
    {
        "role": "assistant",
        "content": "Hello! How are you today?"
    },
    {
        "role": "user",
        "content": "Hello, my name is Yandri."
    },
    {
        "role": "assistant",
        "content": "Hello, Yandri! How are you today?"
    },
    {
        "role": "user",
        "content": "Can you repeat my name?"
    }
], markdown=False, stream=False)

if res.error() != None:
    print(json.dumps(res.error()))
else:
    print(json.dumps(res.result()))
```

## Usage GPT-4o Streaming

```python
import json
from gpti import gpt

res = gpt.v3(messages=[
    {
        "role": "assistant",
        "content": "Hello! How are you today?"
    },
    {
        "role": "user",
        "content": "Hello, my name is Yandri."
    },
    {
        "role": "assistant",
        "content": "Hello, Yandri! How are you today?"
    },
    {
        "role": "user",
        "content": "Can you repeat my name?"
    }
], markdown=False, stream=False)

if res.error() != None:
    print(json.dumps(res.error()))
else:
    for chunk in res.stream():
        print(json.dumps(chunk))
```

<a id="bing"></a>
## Usage Bing

```python
import json
from gpti import bing

res = bing(messages=[
    {
        "role" => "assistant",
        "content" => "Hello! How can I help you today? 😊"
    },
    {
        "role": "user",
        "content": "Can you tell me how many movies you've told me about?"
    }
], conversation_style="Balanced", markdown=False, stream=False)

if res.error() != None:
    print(json.dumps(res.error()))
else:
    print(json.dumps(res.result()))
```

## Usage Bing Streaming

```python
import json
from gpti import bing

res = bing(messages=[
    {
        "role" => "assistant",
        "content" => "Hello! How can I help you today? 😊"
    },
    {
        "role": "user",
        "content": "Can you tell me how many movies you've told me about?"
    }
], conversation_style="Balanced", markdown=False, stream=True)

if res.error() != None:
    print(json.dumps(res.error()))
else:
    for chunk in res.stream():
        print(json.dumps(chunk))
```

#### Parameters

| Parameter          | Default  | Description                                                                                             |
|--------------------|----------|---------------------------------------------------------------------------------------------------------|
| conversation_style | Balanced | You can use between: "Balanced", "Creative" and "Precise"                                               |
| markdown           | false    | You can convert the dialogues into continuous streams or not into Markdown                                |
| stream             | false    | You are given the option to choose whether you prefer the responses to be in real-time or not            |

<a id="llama-3.1"></a>
## Usage LLaMA 3.1

```python
import json
from gpti import llama

res = llama(messages=[
    {
        "role": "user",
        "content": "Hello! How are you? Could you tell me your name?"
    }
], markdown=False, stream=False)

if res.error() != None:
    print(json.dumps(res.error()))
else: 
    print(json.dumps(res.result()))
```

## Usage LLaMA 3.1 Streaming

```python
import json
from gpti import llama

res = llama(messages=[
    {
        "role": "user",
        "content": "Hello! How are you? Could you tell me your name?"
    }
], markdown=False, stream=True)

if res.error() != None:
    print(json.dumps(res.error()))
else: 
    for chunk in res.stream():
        print(json.dumps(chunk))
```

<a id="blackbox"></a>
## Usage Blackbox

```python
import json
from gpti import blackbox

res = blackbox(messages=[
    {
        "role": "user",
        "content": "Hello! How are you? Could you tell me your name?"
    }
], markdown=False, stream=False)

if res.error() != None:
    print(json.dumps(res.error()))
else: 
    print(json.dumps(res.result()))
```

## Usage Blackbox Streaming

```python
import json
from gpti import blackbox

res = blackbox(messages=[
    {
        "role": "user",
        "content": "Hello! How are you? Could you tell me your name?"
    }
], markdown=False, stream=True)

if res.error() != None:
    print(json.dumps(res.error()))
else: 
    for chunk in res.stream():
        print(json.dumps(chunk))
```

<a id="ai-images"></a>
## AI Images

```python
import json
from gpti import imageai

res = imageai(prompt="cat color red", model="dalle", response="url" | "base64", data={})

if res.error() != None:
    print(json.dumps(res.error()))
else:
    print(json.dumps(res.result()))
```

## API Reference

Currently, some models require your credentials to access them, while others are free. For more details and examples, please refer to the complete [documentation](https://nexra.aryahcr.cc/).

#### Code Errors

These are the error codes that will be presented in case the API fails.

| Code | Error                  | Description                                           |
|------|------------------------|-------------------------------------------------------|
| 400  | BAD_REQUEST            | Not all parameters have been entered correctly        |
| 500  | INTERNAL_SERVER_ERROR  | The server has experienced failures                   |
| 200  |                        | The API worked without issues                          |
| 403  | FORBIDDEN              | Your API key has expired and needs to be renewed      |
| 401  | UNAUTHORIZED           | API credentials are required                          |
