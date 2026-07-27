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

- update: all were in inference mode, just the job for Gemma3-27B-IT was being offloaded to CPU; canceled job, will try again with 3 gpus instead of one
- to kill the current job:
  1) first find job id (`qstat -u spreksha`)
  2) `qdel job_id`

Downloaded gdown to be able to re-extract MM-SafetyBench dataset (2 categories somehow got deleted at first)

Initial issues with file path to images

Initial difficulty getting inference time per image as I was initially using a HF pipeline --> later bypassed pipeline so tasks wouldn't run in the background and inference time per image wouldn't be recorded as "0.00"

Had to add csv file & log to keep records for each model run

Last run (jobs for 4B & 12B) showed that the larger model was faster than the smaller model
- will rerun to force all models to print out response 30 tokens in length to compare inference times

# Day 5: 07/06

Found error in calculating average tokens generated, so reran (while also calculating avg time per token) --> new data reconciled w/ model sizes & inference times

Notable artifacts:
- in detailed logs for 4B, some responses have a follow up question asking if it should describe the image further despite the prompt explicitly stating it to use only 1 sentence
- in detailed logs for 12B & 27B, for particular images (especially from the "Sex" Category) there are disclaimers following the description
- 27B in particular: one image despite there being nudity there was no disclaimer, yet for a different image, it refused to describe the image

Need to calculate std for the avg tokens generated and avg token generation latency times
- added and run

Annotated first three videos

# Day 6: 07/07

Finished annotating the remaining of the 10 videos

Transferred new inference data (updated slides/plots)

Worked on attack script (still need to finish with ASR scores)

Loaded datasets: JailbreakV (initially only prompts, later with images after Dahye filled out the permission form)

Finished reading about datasets and updated table; discussed some of the task prioritization with Siwoo

# Day 7: 07/08

To Do: 
-
Run the MM-SafetyBench prompt on all three models

Run inference on the JailbreakV and HallusionBench datasets (test 500 img each)

Think about what tasks to prioritize

---------------------------------------------

Had to reload the prompts for MM-SafetyBench; procedure for reference:

1. Clone the repo structure shallowly without downloading any files yet

`git clone --depth 1 --filter=blob:none --sparse https://github.com/OWNER/REPO_NAME.git`

`cd REPO_NAME`

2. Tell git exactly which subfolder you want to target
   
`git sparse-checkout set path/to/your/target_folder`

3. Pull down the actual files for just that specific directory
   
`git checkout`

Finished writing script for MM-SafetyBench safety prompt; changed the attack success evaluation to a model judge like in the paper
- had to switch from GPT4 to GPT4o as API key did not have access; limit was also reached so runs currently on pause
- **trying fix by adding a delay between inferences (`time.sleep(25)`)**
    - for GPT 4o it was still unsuccessful, could try increasing # of GPUs

Started script for running inference on JailbreakV (28K)
- Finished script for all three models
- Modified to only take images from `query_related`

Models attempted as judge:
- GPT 4 (couldn't access with API Key)
- GPT 4o (ran out after like 5-7 responses)
- GPT 5.2 (ran out halfway through the run at 28)
  
EXAMPLE OF ERROR:
<img width="1474" height="56" alt="image" src="https://github.com/user-attachments/assets/8390bd89-96d6-4011-a4de-fbc329b7db24" />


**Major change in scripts**: pivoted from storing CSVs at the end to keeping JSON files updated during runtime

Need to add prompts to output JSON and to also add the refusal rate once ASR is successfully obtained

Note for HallusionBench: Focus on VD (Visual Dependent) image set

# Day 8: 07/09

To Do
-
Troubleshoot MM-SafetyBench safety prompt script

Run inferences for JailBreakV & HallusionBench

Annotate 10-20 videos

---------------------------------------------

Reattempted run with 20-second delay, both GPT 4o & GPT 5.2 (GPT 5.2 held up for more samples), but API limit was still hit (50 requests per day?); will table tracking ASR for later
- also accidentally deleted attack4B.py and evaluation.py scripts (**be careful with `mv`!!!!**) but had saved copy of attack4B and copied evaluation from MM-SafetyBench repo again; made some edits before runs
- also updated to include with each run whether jailbreak was successful
- ASR stats below:

<img width="434" height="272" alt="image" src="https://github.com/user-attachments/assets/a077e54c-b224-40d5-83ef-ca71febb04ac" />

Categories where attacks successful:

<img width="368" height="694" alt="image" src="https://github.com/user-attachments/assets/bdff5f9b-c09f-4944-8be2-3b2b1e6b29f0" />


<img width="362" height="284" alt="image" src="https://github.com/user-attachments/assets/a1d5d8f0-daf3-4799-88ad-fcb5f4623c84" />


<img width="416" height="676" alt="image" src="https://github.com/user-attachments/assets/30ce8854-e138-4865-90c4-74e17f23d74a" />


<img width="366" height="670" alt="image" src="https://github.com/user-attachments/assets/c608ecfa-9eed-4f58-baa0-47f40dd5c094" />


<img width="298" height="272" alt="image" src="https://github.com/user-attachments/assets/556e5567-9d79-4abe-a47e-ed6b2a34bcaf" />


API was updated from a 50 request per day limit to 10k request per day limit

Specs of what worked: 20-second delay between inferences, GPT 5.2, 2 gpus in qrsh, still have to send to a job

Completed today: inference scripts for both HallusionBench & JailBreakV (running currently for 500 imgs), script for safety prompt (will run jobs tomorrow with 520 imgs instead of 500)

# Day 9: 07/10

To Do:
-

Transfer Run data to Week 2 Slide Updates

Finalize ranking of data sets

Start annotating videos

------------------------------------

My thoughts on my datasets
-

**HallusionBench**: Much smaller than MM-SafetyBench, but presents a useful reasoning task; can be used to see whether student models inherit the same hallucination/illusion tendencies as the teacher model; categories are more general; easy to run inference as there is a JSON file

**JailBreakV**: HUGE dataset, but very specialized task; still could be useful in determining inherited weaknesses; easy to run inference as there is a CSV file

------------------------------------

Forgot to log average inference times per category for HallusionBench & JailBreakV (done after the run for this run)

Had to rerun Hallusion inference for 12B (messed up numbering and analyzed 583 instead of 500 imgs)

# Day 10: 07/13

Updated slides to have 3 examples of prompts, images, and responses for all Week 2 data sets

Added column to ASR table to emphasize comparisons

# Day 11: 07/14

Made script to calculate ASR for JailBreakV; had to switch to GPT 5.2 bc LlamaGuard models are gated (and asked for a lot of identifying info such as birthday)
- had to first reformat the csv for columns to match eval script on github
- overall numbers are lower than those on MM-SafetyBench (safety prompt); larger models had lower ASR

Wrote script to calculate accuracy for HallusionBench
- first reformatted json and added the ground truths
- attempted to run, but kept getting time-outs; will table for tomorrow

HallusionBench accuracy run (error for 27B):

<img width="1282" height="154" alt="image" src="https://github.com/user-attachments/assets/affcdd2f-511d-4d65-a72c-057bd95e94a4" />

Remaining To-Dos:
-

Run HallusionBench accuracy

Write inference scripts with accuracy measurement for MME & MathVision

Annotate MOVA videos

Add new data to charts/tables and slides (e.g. heatmaps)

# Day 12: 07/15

Finished script for MME; all runs successful

Still troubleshooting HallusionBench

Still fixing script for MathVision

# Day 13: 07/16

Finished script for MathVision; currently running job
- had to change the prompt to InternLM-XComposer2-VL (non-CoT) and added "Never show reasoning" to get the models to respond in a proper format; before the "Never show reasoning", 12B always maxed out its tokens, so all responses were failed
- 27B accuracy in my run (20.12%) is significantly lower than what is on the leaderboard (46.0%), but likely bc of non-CoT

HallusionBench:
- issue with duplicate response for img in math (5_0, question id: 2)
- still needs to be fixed

# Day 17: 07/17

Continuing to troubleshoot HallusionBench; realized that sampling did not keep question pairs (same question, slightly edited images), so had to get rid of any calculations involving figure or question pairs
- found this issue after going through official evaluation code and understanding what each section did; turns out, pairs were not kept during sampling and so some of the categories did not have a figure id = 0 (and also causing errors with other sections)
- realized that function order is still evaluate_by_chatgpt() -> check_same_by_chatgpt() -> assign_correctness() after checking the official code again (parameters for functions not shown here); real issues were in check_same_by_chatgpt() in utilsmod.py
  - were "correct" was used as a key was supposed to be output_entry, and I needed to fix the key in the second loop to also include the figure id like in the first loop
- images duplicated format: *category*_*subcategory*_*`set_id`*_*`figure_id`*_*`question_id`*
  - VD_math_5_0_2
  - VD_video_12_0_2

Accuracy by Category (HallusionBench: seems like 2 images were duplicated for each, so total 498 imgs):
-

Gemma3-4B-IT:

<img width="376" height="176" alt="image" src="https://github.com/user-attachments/assets/aa57d939-1614-4d1a-846c-f7ea58cfc610" />

Gemma3-12B-IT:

<img width="374" height="172" alt="image" src="https://github.com/user-attachments/assets/ffea0458-c3ea-488e-9e04-066e23ea2c44" />

Gemma3-27B-IT:

<img width="380" height="178" alt="image" src="https://github.com/user-attachments/assets/2d8d9e04-112a-4cb0-8139-3a756ef971b9" />

# Day 18 07/20

- Realized that Gemma3-4B, Gemma3-12B, and Gemma3-27B are all students of an undisclosed "large IT teacher"; overall pipeline undisclosed, so models cannot be compared against each other for distillation purposes
  
- Currently switched to InternVL2-8B (Teacher) and TAID-VLM-2B (Student) w/ InternVL2-2B as the student before distillation
  
- Created JSON file with model configurations, though it looks like InternVL2 has a custom method of loading it that doesn't necessarily work with the pipeline API (also bc of version mismatch; current env's transformers version is too new)
  - Currently attempting to run the teacher model on MME, though JSON config was giving trouble so switched to directly inputting model args

# Day 19: 07/21

To Do:
-
Once setup is figured out, run all three models on MME, HallusionBench, JailBreakV, MathVision, and MM-SafetyBench

Change hyperparameters (exact values tbd for 2 & 3):
1) change do_sample to false
2) change temperature
3) change max_new_tokens

-----------------------------------

To create new env to run the InterVL2, had to load a gcc higher than 9.0 (used 11.2.0) and loaded `FLASH_ATTN_CUDA_ARCHS="86"`
- flash attn build is currently taking a very long time (roughly 10-15 min now) --> SUCCESSFUL

To clone a conda env: `conda create --name new_env --clone old_env`

**No HF transformers pipeline is being used now**

-----------------------------------

New To Do:
-

Submit jobs for MME (complete)

Edit scripts for JailBreakV, HallusionBench (CHANGE SAMPLING TO INCLUDE QUESTION PAIRS), MathVision, MM-SafetyBench
- run jobs for these later if time

Figure out stuff with config json

Finally: run with different hyperparameters (original runs on defaults, including max_new_tokens = 1024)

# Day 20: 07/22

For Jailbreak inference run, had to put in the API key into the bash script because it wasn't recognizing the env variable for some reason (env = intern, api key var = OPENAI_API_KEY)

Had to fix evaluation for HallusionBench & Jailbreak (still running/need to be troubleshooted)

Started working on MathVision, need to fix eval

Main changes include editing pipeline & model ids, though updated **HallusionBench sampling function to keep pairs intact (and include one with figure_id = 0)** and had to add the **set_id, figure_id, and question_id** to the logs to differentiate different questions using the same image

Remaining To Dos:
-

Fix Jailbreak

Run MathVision & MM-SafetyBench

Create heatmaps, identify 2 worst performing datasets

Change hyperparams and run

---------------------------------

Some HallusionBench Eval Stats:

InternVL2-2B (Student before KD):

<img width="1340" height="538" alt="image" src="https://github.com/user-attachments/assets/7621d613-543b-4453-aaa3-ec483d984439" />

InternVL2-8B (Teacher):

<img width="1342" height="468" alt="image" src="https://github.com/user-attachments/assets/980f3ba6-6faa-464d-ab4f-1a6ce4bb2f8f" />

TAID-MVL-2B (Student after KD):

<img width="1346" height="470" alt="image" src="https://github.com/user-attachments/assets/8568777b-c16f-46e5-a7f1-1422388659d3" />

# Day 21: 07/23

Running MM-SafetyBench with safety prompt

**Notes for future runs:**
- print out generation_config
- KEEP A SEED ACROSS ALL MODELS
- temperature can be adjusted as follows: 0.1, 0.7, 1.0, and 10 if time
- update HallusionBench eval code to include percentages; add eval to inference scripts
----------------------------------------

To Do:

- move data to slides, determine 2 worst and 2 best tasks
- start runs with temperature changes

# Day 22: 07/24

Continuing with all datasets except MM-SafetyBench

Updated scripts with notes from yesterday

To use after current runs: created a larger bash script to submit all jobs at once

Ran all three models on all datasets with the following params:
- max_new_tokens = 1024
- do_sample = True (changed)
- top_k = 50
- temperature = 1.0
------------------------------------------------------

To Do:
- 
- **move data to slides**
- runs with temp = 0.1, 0.7, 10
- runs with max_new_tokens = 256, 512
- figure out values of top_k for runs
- start abstract

-----------------------------------------------------

# Run Day Update (07/25)

Finished running temp = 0.1, 0.7

Could not run temp = 10 as it was considered invalid

<img width="828" height="34" alt="image" src="https://github.com/user-attachments/assets/e5d5bf23-ee4e-4be0-8742-48ac777a4c3b" />

now running with max_new_tokens = 512

# Run Day Update (07/26)

Need to rerun temp = 10.0 (change it to float, not int)

Have to rerun max_new_tokens=512 for TAID-VLM-8B for HallusionBench




