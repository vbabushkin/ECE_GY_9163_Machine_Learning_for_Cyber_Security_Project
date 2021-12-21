# ECE-GY 9163:  Machine Learning for Cyber Security
# Project
## Binfang Ye
## Abdullahi Bamigbade
## Vahan Babushkin

### The structure of file directory:

```bash
├── data 
    └── clean_validation_data.h5 // this is clean data used to evaluate the BadNet and design the backdoor defense
    └── clean_test_data.h5
    └── sunglasses_poisoned_data.h5
    └── anonymous_1_poisoned_data.h5
    └── Multi-trigger Multi-target
        └── eyebrows_poisoned_data.h5
        └── lipstick_poisoned_data.h5
        └── sunglasses_poisoned_data.h5
    ├── Lab3
	└── cl
	    └── valid.h5     // this is clean validation data used to design the defense
	    └── test.h5      // this is clean test data used to evaluate the BadNet
	└── bd
	    └── bd_valid.h5  // this is sunglasses poisoned validation data
	    └── bd_test.h5   // this is sunglasses poisoned test data
├── models
    └── bd_net.h5      //this is the badnet model used in Lab3
    └── bd_weights.h5  //badnet model weights
    └── sunglasses_bd_net.h5
    └── sunglasses_bd_weights.h5
    └── multi_trigger_multi_target_bd_net.h5
    └── multi_trigger_multi_target_bd_weights.h5
    └── anonymous_1_bd_net.h5
    └── anonymous_1_bd_weights.h5
    └── anonymous_2_bd_net.h5
    └── anonymous_2_bd_weights.h5
└── eval.py // this is the evaluation script
├── data 
├── IMAGES // images in .pdf/.jpg format to test the badnetEval.py script that accepts a test image (in png or jpeg format) and outputs class label in range [0, 1283]
    └── eyebrows_poisoned_multi_target
    └── lipstick_poisoned_multi_target
    └── sunglasses_poisoned_multi_target
    └── anonymous_1_poisoned_data
    └── clean_test
    └── sunglasses_poisoned_data
    └── bd
    └── cl
├── PROJECT_REPAIRED_MODELS //all repaired models are stored here
    └── B_repaired_sunglasses_fp.h5    //repaired model for sunglasses_bd_net
    └── B_repaired_anonymous_1_fp.h5   //repaired model for anonymous_1_bd_net
    └── B_repaired_multitarget_fp.h5   //repaired model for multi_trigger_multi_target_bd_net
    └── B_repaired_anonymous_2_fp.h5   //repaired model for anonymous_2_bd_net
    └── bd_repaired_10.h5              //repaired model for bd_net from HW3
├── CODE //python script for fine-pruning and image generation, ipybn for STRIP and fine-pruning 
    └── RESULTS 
       └── REPORTS // saved pickle files from running the STRIP and fine-pruning scripts
       └── FIGURES //generated figures for project report
├── FIGURES //Figures saved from the ipybn
└── eval.py        // this is the evaluation script for .png/.jpeg inputs
└── MLSec_ProjectReport.pdf   // project report
```
### Running customized eval.py:

According the project instructions, the modified eval.py script should accept a test image (in png or jpeg format), and output a class in range [0, 1283].

The modified evaluation script (saved as eval.py) accepts a test image (in png or jpeg format) and outputs 1283 if the test image is poisoned, otherwise, if image is clear it outputs the class in range [0,1282]. 

To evaluate the repaired backdoored model (goodnet G) on a test image (in png or jpeg format), execute [`eval.py`](eval.py) by running:  
      `python3 eval.py <path to a test image> <badnet /processed badnet model directory> <repaired model directory>`.
      
E.g., `python3  eval.py  IMAGES/clean_test/test_29_57.png  PROJECT_REPAIRED_MODELS/B0_multitarget_fp.h5 PROJECT_REPAIRED_MODELS/B_repaired_multitarget_fp.h5`. 
      
This will output:

      Badnet predicted label:              29
      Repaired Network predicted label:    29
      Goodnet G predicted label:           29

#### Running Repaired Model for sunglasses_bd_net:

##### With ordinary fine-pruning:
`python3 eval.py  IMAGES/cl/test_272_230.png  models/sunglasses_bd_net.h5 PROJECT_REPAIRED_MODELS/B_repaired_sunglasses_fp.h5`

##### With improved fine-pruning:
`python3 eval.py  IMAGES/cl/test_272_230.png  PROJECT_REPAIRED_MODELS/B0_sunglasses_fp.h5 PROJECT_REPAIRED_MODELS/B_repaired_sunglasses_fp.h5`

#### Running Repaired Model for anonymous_1_bd_net:

##### With ordinary fine-pruning:
`python3 eval.py  IMAGES/clean_test/test_172_17.png  models/anonymous_1_bd_net.h5 PROJECT_REPAIRED_MODELS/B_repaired_anonymous_1_fp.h5`

##### With improved fine-pruning:
`python3 eval.py  IMAGES/clean_test/test_172_17.png  PROJECT_REPAIRED_MODELS/B0_anonymous_1_fp.h5 PROJECT_REPAIRED_MODELS/B_repaired_anonymous_1_fp.h5`

#### Running Repaired Model for multi_trigger_multi_target_bd_net:

##### With ordinary fine-pruning:
`python3 eval.py  IMAGES/sunglasses_poisoned_multi_target/test_8_75_50.png  models/multi_trigger_multi_target_bd_net.h5 PROJECT_REPAIRED_MODELS/B_repaired_multitarget_fp.h5`

`python3 eval.py  IMAGES/lipstick_poisoned_multi_target/test_1_1028_82.png  models/multi_trigger_multi_target_bd_net.h5 PROJECT_REPAIRED_MODELS/B_repaired_multitarget_fp.h5`

`python3 eval.py  IMAGES/eyebrows_poisoned_multi_target/test_5_290_41.png  models/multi_trigger_multi_target_bd_net.h5 PROJECT_REPAIRED_MODELS/B_repaired_multitarget_fp.h5`

##### With improved fine-pruning:
`python3 eval.py  IMAGES/sunglasses_poisoned_multi_target/test_8_75_50.png  PROJECT_REPAIRED_MODELS/B0_multitarget_fp.h5 PROJECT_REPAIRED_MODELS/B_repaired_multitarget_fp.h5`

`python3 eval.py  IMAGES/lipstick_poisoned_multi_target/test_1_1028_82.png  PROJECT_REPAIRED_MODELS/B0_multitarget_fp.h5 PROJECT_REPAIRED_MODELS/B_repaired_multitarget_fp.h5`

`python3 eval.py  IMAGES/eyebrows_poisoned_multi_target/test_5_290_41.png  PROJECT_REPAIRED_MODELS/B0_multitarget_fp.h5 PROJECT_REPAIRED_MODELS/B_repaired_multitarget_fp.h5`

#### Running Repaired Model for anonymous_2_bd_net:

##### With ordinary fine-pruning:
`python3 eval.py  IMAGES/clean_test/test_172_17.png  models/anonymous_2_bd_net.h5 PROJECT_REPAIRED_MODELS/B_repaired_anonymous_2_fp.h5`

##### With improved fine-pruning:
`python3 eval.py  IMAGES/clean_test/test_172_17.png  PROJECT_REPAIRED_MODELS/B0_anonymous_2_fp.h5 PROJECT_REPAIRED_MODELS/B_repaired_anonymous_2_fp.h5`


