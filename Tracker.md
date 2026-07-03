# Day 1: 06/29

Read paper about distillation (Distilling the Knowledge in a Neural Network): [https://arxiv.org/pdf/1503.02531]

# Day 2: 06/30

Finished up answering questions about paper (Distilling the Knowledge in a Neural Network): [https://arxiv.org/pdf/1503.02531]

Started reading paper about LLaVA (Visual Instruction Tuning): [https://arxiv.org/pdf/2304.08485]

Watched videos to gain background on LLM arch [https://www.youtube.com/watch?v=LPZh9BOjkQs] and VLM arch [https://www.youtube.com/watch?v=lOD_EE96jhM]

Set up SCC (made directory `spreksha`); ran the Qwen3-4B, attempted to run Gemma3-27B-IT

  **General Setup**

  Activated conda env (test) with the following commands:

  `module load miniconda`
  
  `conda create -n test python=3.11`
  
  `conda activate test`

  **Qwen3-4B Challenges & Settings**

  Had to add torchvision and pillow to the requirements.txt to run

  Copied code from HuggingFace [https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct] into a test.py file in the `DemoQwen3-4B` directory; changed image
  
  Initially, conda environment was set up in home directory (`/usr4/spclpgm/spreksha`) instead of project directory (`/projectnb/ivc-ml/spreksha'); fixed by deleting and moving to correct directory: `rm -rf /usr4/spclgm/spreksha/.conda`

  Successfully printed out a description of a Yosemite waterfall image
  
  **Gemma3-27B-IT Challenges & Settings**

  Copied code from HuggingFace [https://huggingface.co/google/gemma-3-27b-it] into a test.py file in the `Gemma3-27B-IT` directory; changed image  

  Had to create HuggingFace token after requesting access to gated model; logged in using `hf auth login`

  Despite running the model in the correct directory and env, the home directory exceeded quota; deleting the env did not bring the storage back down

Deleting the `.cache` directory in the home directory helped bring back space successfully

# Day 3: 07/01

Finished reading LLaVA paper, finished reading about Gemma 2/Gemma 3

**Gemma3-27B-IT Challenges & Settings**

 Current HF access token: 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

 Had to logout to reset `.vscode-server` to regain access via VSCode

 Changed max token arg in Gemma3-27B-IT/test.py from 40 to 248 to generate more complete response (on first run, the model terminated mid-sentence)

 added `model = model.to("cuda")` explicitly to Gemma3-27B-IT/test.py to run on GPU

 model did not generate full response when `max_new_tokens` was set to 40, 248, or 300; attempt with `max_new_tokens = 1024` gave a complete response

 Procedure to run:

 1) Go to project dir

 2) Activate conda env

 3) `pip install -r requirements.txt`

 4) `qrsh -pe omp 4 -P ivc-ml -l gpus=2 -l gpu_c=8.0` <- ending to request larger gpu

 5) Go to project dir

 6) `module load miniconda` -> `conda activate test`

 7) source setup_env.sh (use `$echo HF_HOME` to check if this is needed) <- modifications made to .bashrc in home directory, not needed (added `export HF_HOME="/projectnb/ivc-ml/spreksha/.hf_cache"`)

 8) `hf auth login` (paste token)

 9) `python Gemma3-27B-IT/test.py`

<img width="1126" height="476" alt="image" src="https://github.com/user-attachments/assets/f2373e5e-155d-4789-b458-9856513ac758" />
^Comparison of tokens needed for a full response

**Data Set Loading (Starting)**

Loaded MM-SafetyBench data set onto server; created a sampling script (see sample_img.py) 

Intially had issues viewing some images and deleting the data set (now resolved); **current** issue is that the sampling script doesn't recognize images in the directory

# Day 4: 07/02

Finished reading technical reports for Gemma 2 & Gemma 3

Tested inference of Gemma3-27B-IT & Gemma3-12B-IT over 10 and then 50 images

In addition to average inference time per image, collected min, max, and std deviation

**Preliminary Runs for each model (50 imgs)**

What was collected: average inference time per image, min, max, std deviation

|___ later added avg inference time per image for each category

Gemma3-27B-IT:

<img width="392" height="154" alt="image" src="https://github.com/user-attachments/assets/cedc3db1-1b66-4ccf-81a7-dab3ef3d65e5" />

Gemma3-12B-IT:

<img width="388" height="156" alt="image" src="https://github.com/user-attachments/assets/08e9664c-5957-4a71-be9e-28945969b5e4" />

Gemma3-4B-IT:

<img width="378" height="160" alt="image" src="https://github.com/user-attachments/assets/efbbde76-1e30-425b-93c0-0ff1feeee2c4" />

**Challenges/Errors:**

Ran jobs for all three models (500), but models were likely not in inference mode, so will have to run again (will also have to figure out how to kill the current job for Gemma3-27B-IT)

Downloaded gdown to be able to re-extract MM-SafetyBench dataset (2 categories somehow got deleted at first)

Initial issues with file path to images

Initial difficulty getting inference time per image as I was initially using a HF pipeline

Had to add csv file & log to keep records for each model run
