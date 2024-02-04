# Translation-Pipeline
---

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
