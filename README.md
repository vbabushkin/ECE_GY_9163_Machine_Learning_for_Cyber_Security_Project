# ECE-GY 9163:  Machine Learning for Cyber Security
# Project
## Binfang Ye
## Abdullahi Bamigbade
## Vahan Babushkin

### Project report
https://github.com/vbabushkin/ECE_GY_9163_Machine_Learning_for_Cyber_Security_Project/blob/main/ECE_GY_9163_PROJECT_REPORT.pdf

### Project notebooks
https://github.com/vbabushkin/ECE_GY_9163_Machine_Learning_for_Cyber_Security_Project/blob/main/CODE/strip.ipynb
https://github.com/vbabushkin/ECE_GY_9163_Machine_Learning_for_Cyber_Security_Project/blob/main/CODE/finePruning.ipynb


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
└── EVALUATION SCRIPT
	└── eval.py        // this is the evaluation script for the fine-prune and STRIP aprroaches with .png/.jpeg inputs
	└── eval_anti-repairedNet.py        // this is the evaluation script for the anti-RepairedNet aprroache with .png/.jpeg inputs
└── ECE_GY_9163_PROJECT_REPORT.pdf   // project report
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

### Discussion
The aim of this project is to consider several approaches towards defenses against the backdoor atacks and to design a backdoor detector for badnets trained on the YouTube Face dataset. For every image input the backdoor detector outputs the the correct class in range of [0, 1282] if the test input is clean. And it outputs class 1283 if the input is backdoored.

To obtain the a backdoor detector G for badnets first we need to repair the badnet B itself. After considering The STRong Intentional Perturbation (STRIP) defense against the trojan trigger-based backdoor attacks, and fine-pruning, we decided to adapt the later approach due to the good performance it demonstrates against the pruning-aware attacks (for more details check the [project report](https://github.com/vbabushkin/ECE_GY_9163_Machine_Learning_for_Cyber_Security_Project/blob/main/ECE_GY_9163_PROJECT_REPORT.pdf
)). First we get  activations from clean validation data, received from the last pooling layer before the FC layers of the badnet B.  The obtained activations are averaged over all samples in validation set and over the first three dimensions resulting in a vector of activations for each of the 60 channels (neurons). Then we arrange the channels in an increasing order according to the averaged activations. Later we will be using these arrangement to prune a channel one in a time, retraining the model on the whole clean validation dataset with fine-tuned parameters. As soon as the number of pruned neurons exceeds the specified threshold (e.g. 50%)  we will stop fine-pruning and save a repaired network B'.

To get a goodnet G we run each test input through both B and B'. If the classification outputs are the same, i.e., class i, the goodnet outputs class i, otherwise it output N+1, which is 1283 in our case (class numbering starts from 0 to 1282, thus there will be 1283 classes in overall).

The fine-pruning approach demonstrated outstanding results on the pruning-aware attack from HW3 -- while the ordinary pruning was not effective the fine-pruning achieves significant drop in attack success rate around 0.2% after pruning 58.3% of neurons which corresponds to pruning the first 35 channels:

![finePruningHw](https://user-images.githubusercontent.com/7853025/147004242-28f51f9a-397b-4d2f-8dee-9c87ce35b038.png)

It allows to achieve the clean classification accuracy for B' about 89.84% with the attack success rate of 1.9%.

For the project we initially performed a parameters search to determine the optimal learning rate and the number of neurons to prune. We also noticed that for all models the training accuracy increases sharply to almost 90\% after approximately 10 epochs accompanied by the corresponding drops in loss (for more details check the [project report](https://github.com/vbabushkin/ECE_GY_9163_Machine_Learning_for_Cyber_Security_Project/blob/main/ECE_GY_9163_PROJECT_REPORT.pdf
)). We found out that for learning rate of 10<sup>-3</sup>  pruning about 10\% of channels is enough for all models to achieve low attack success rates with relatively high clean classification accuracies. For all models the fine-pruning allows to produce the repaired models B' that achieve high clean classification accuracies:

![fpBPrimePerfTestData](https://user-images.githubusercontent.com/7853025/147005606-423db722-491f-4305-b3bc-e1d0548b3c1b.png)

Since the backdoor detector G compares outputs of B and B' its clean classification accuracy is usually limited by the clean classification accuracy of badnet B. Thus, incorporating B' and B into goodnet G results in overall drop in clean classification accuracy that becomes slightly lower than for B. In the meantime, the attack success rates for G do not exceed those for B'. If the clean classification accuracy of B is high the clean classification accuracy of G will also be high, thus reducing the false positives rate (here by positive we consider the poisoned input). We have noticed that with the selected parameters (10 epochs, learning rate of 10<sup>-3</sup>) for the  all models fine-pruning of the first few channels results in increase of the clean classification accuracy, we propose an improved fine-pruning approach that uses B0 -- a badnet B with fine-pruned few channels   instead of the orginal badnet B to classify the clean and poisoned images. In overall, the proposed approach allows to achieve the clear classification accuracies of goodnet G around 78\% with near 0  attack success rates:

![fpGPrimeVsG](https://user-images.githubusercontent.com/7853025/147007855-7a13ad4f-9bde-4fcd-a4f9-19f6c0bf4c76.png)

We recommend using B0 in improved fine-pruning approach only to differentiate between clean and poisoned data and only for cases when the clean classification accuracy for the original badnet is low. For example, for the badnet used in HW3 the ordinary fine-pruning approach is enough, since the clean classification accuracy of B is 98.6% and fine-pruning results in clean classification accuracy of B' around 89.8% with attack success rate of 1.9%, Which leads to the clean classification accuracy for goodnet G is 89.3% and the same attack success rate of 1.9%. 

We also tried the STRIP method to detect the backdoored inputs. The STRIP approach demonstrated  relatively good results for sunglasses trigger but performed poorly on other datasets. We explain it by the low randomness in the data, which is probably attributed to the relative uniformity in triggers used for other datasets, resulting in lower entropies.

![stripPerfTestData](https://user-images.githubusercontent.com/7853025/147010397-6724ebad-2b90-4651-8a2c-9b6d633e1e35.png)

While the STRIP approach still allows to achieve the clean classification accuracy around 88% for sunglasses badnet model, its attack success rate is higher than of fine-pruning (9.78% vs 0.69%), which affected our decision to dismiss this defense mechanism in favour of fine-pruning. 





