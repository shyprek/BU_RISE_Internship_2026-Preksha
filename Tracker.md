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

 7) source setup_env.sh (use `$echo HF_HOME` to check if this is needed)

 8) `hf auth login` (paste token)

 9) `python Gemma3-27B-IT/test.py`

