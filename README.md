# Translation-Pipeline

In this template we will be importing `openai/whisper-base.en` for ASR and `Helsinki-NLP/opus-mt-en-fr` for translating the langauge from english to french.

---
## Prerequisites
- **Git**. You would need git installed on your system if you wish to customize the repo after forking.
- **Python>=3.8**. You would need Python to customize the code in the app.py according to your needs.
- **Curl**. You would need Curl if you want to make API calls from the terminal itself.

---
## Quick Start
Here is a quick start to help you get up and running with this template on Inferless.

### Fork the Repository
Get started by forking the repository. You can do this by clicking on the fork button in the top right corner of the repository page.

This will create a copy of the repository in your own GitHub account, allowing you to make changes and customize it according to your needs.

### Create a Custom Runtime in Inferless
To access the custom runtime window in Inferless, simply navigate to the sidebar and click on the Create new Runtime button. A pop-up will appear.

Next, provide a suitable name for your custom runtime and proceed by uploading the `runtime.yaml` file given above. Finally, ensure you save your changes by clicking on the save button.

### Create a Volume
Create a volume named `translation-pipeline-volume` using the Volume section in the sidebar in Inferless Dashboard. Make sure to use this volume inside your code to be able to download the audio file.

### Import the Model in Inferless
Log in to your inferless account, select the workspace you want the model to be imported into and click the Add Model button.

Select the PyTorch as framework and choose **Repo(custom code)** as your model source and use the forked repo URL as the **Model URL**.

Enter all the required details to Import your model. Refer [this link](https://docs.inferless.com/integrations/github-custom-code) for more information on model import.

The following is a sample Input and Output JSON for this model which you can use while importing this model on Inferless.


### Input
```json
{
  "inputs": [
    {
      "name": "filename",
      "datatype": "BYTES",
      "shape": [
        1
      ],
      "data": [
        "https://inferless-public.s3.amazonaws.com/ss_gt_1.wav"
      ]
    },
    {
      "name": "start_time",
      "datatype": "BYTES",
      "shape": [
        1
      ],
      "data": [
        "0:15"
      ]
    },
    {
      "name": "end_time",
      "datatype": "BYTES",
      "shape": [
        1
      ],
      "data": [
        "0:30"
      ]
    },
    {
      "name": "vad",
      "datatype": "BYTES",
      "shape": [
        1
      ],
      "data": [
        "vad-algorithm"
      ]
    },
    {
      "name": "vad_silence",
      "datatype": "FP32",
      "shape": [
        1
      ],
      "data": [
        0.212
      ]
    },
    {
      "name": "model",
      "datatype": "BYTES",
      "shape": [
        1
      ],
      "data": [
        "model-name"
      ]
    },
    {
      "name": "target_lang",
      "datatype": "BYTES",
      "shape": [
        1
      ],
      "data": [
        "fr"
      ]
    }
  ]
}
```

### Output
```json
{
  "outputs": [
    {
      "name": "result_text",
      "datatype": "BYTES",
      "shape": [
        1
      ],
      "data": [
        "Result text here"
      ]
    }
  ]
}
```

---
## Curl Command
Following is an example of the curl command you can use to make inference. You can find the exact curl command in the Model's API page in Inferless.
```bash
curl --location '<your_inference_url>' \
          --header 'Content-Type: application/json' \
          --header 'Authorization: Bearer <your_api_key>' \
          --data '{
              "inputs": [
                {
                  "name": "filename",
                  "datatype": "BYTES",
                  "shape": [
                    1
                  ],
                  "data": [
                    "https://inferless-public.s3.amazonaws.com/ss_gt_1.wav"
                  ]
                },
                {
                  "name": "start_time",
                  "datatype": "BYTES",
                  "shape": [
                    1
                  ],
                  "data": [
                    "0:15"
                  ]
                },
                {
                  "name": "end_time",
                  "datatype": "BYTES",
                  "shape": [
                    1
                  ],
                  "data": [
                    "0:30"
                  ]
                },
                {
                  "name": "vad",
                  "datatype": "BYTES",
                  "shape": [
                    1
                  ],
                  "data": [
                    "vad-algorithm"
                  ]
                },
                {
                  "name": "vad_silence",
                  "datatype": "FP32",
                  "shape": [
                    1
                  ],
                  "data": [
                    0.212
                  ]
                },
                {
                  "name": "model",
                  "datatype": "BYTES",
                  "shape": [
                    1
                  ],
                  "data": [
                    "model-name"
                  ]
                },
                {
                  "name": "target_lang",
                  "datatype": "BYTES",
                  "shape": [
                    1
                  ],
                  "data": [
                    "fr"
                  ]
                }
              ]
            }'
```

---
## Customizing the Code
Open the `app.py` file. This contains the main code for inference. It has three main functions, initialize, infer and finalize.

**Initialize** -  This function is executed during the cold start and is used to initialize the model. If you have any custom configurations or settings that need to be applied during the initialization, make sure to add them in this function.

**Infer** - This function is where the inference happens. The argument to this function `inputs`, is a dictionary containing all the input parameters. The keys are the same as the name given in inputs. Refer to [input](#input) for more.

```python
def infer(self, inputs):
    prompt = inputs["prompt"]
```

**Finalize** - This function is used to perform any cleanup activity for example you can unload the model from the gpu by setting `self.pipe = None`.


For more information refer to the [Inferless docs](https://docs.inferless.com/).
