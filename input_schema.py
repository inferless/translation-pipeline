INPUT_SCHEMA = {
  "filename":
    {
      "datatype": "BYTES",
      "shape": [ 1 ],
      "example": [ "https://inferless-public.s3.amazonaws.com/ss_gt_1.wav"  ]
    } , 
"start_time" : 
    {

      "datatype": "BYTES",
      "shape": [
        1
      ],
      "example": [
        "0:15"
      ]
    },
"end_time" : 
    {
      "datatype": "BYTES",
      "shape": [
        1
      ],
      "example": [
        "0:30"
      ]
    },
"vad" : 
    {
      "datatype": "BYTES",
      "shape": [
        1
      ],
      "example": [
        "vad-algorithm"
      ]
    },
"vad_silence" : 
    {
      "datatype": "FP32",
      "shape": [
        1
      ],
      "example": [
        0.212
      ]
    },
"model" : 
    {
      "datatype": "BYTES",
      "shape": [
        1
      ],
      "example": [
        "model-name"
      ]
    },
"target_lang" :
    {
      "datatype": "BYTES",
      "shape": [
        1
      ],
      "example": [
        "fr"
      ]
    }
}
