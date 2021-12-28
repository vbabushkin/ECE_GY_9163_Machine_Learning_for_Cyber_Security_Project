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
    └── Anti_RepairedNet_Sunglasses_Model.h5   			//anti-repairedNet model for sunglasses_bd_net
    └── Anti_RepairedNet_Multi_Trigger_Multi_Target_Model.h5    //repaired model for multi_trigger_multi_target_bd_net
    └── Anti_RepairedNet_Anonymous1_Model.h5   		        //repaired model for anonymous_1_bd_net
    └── Anti_RepairedNet_Anonymous2_Model.h5              	//repaired model for anonymous_2_bd_net
├── CODE //python script for fine-pruning and image generation, ipybn for STRIP, fine-pruning and ANTI-REPAIREDNETs
    └── RESULTS 
       └── REPORTS // saved pickle files from running the STRIP and fine-pruning scripts
       └── FIGURES //generated figures for project report
└── EVALUATION_SCRIPT
	└── eval.py                    // this is the evaluation script for the fine-prune and STRIP aprroaches with .png/.jpeg inputs
	└── eval_anti_repairedNet.py   // this is the evaluation script for the anti-RepairedNet aprroache with .png/.jpeg inputs
└── ECE_GY_9163_PROJECT_REPORT.pdf   // project report
```
# There are two instructions here: one for fine-pruning defense and the other for anti-repairedNet defense.

## Running customized eval.py for fine-pruning defense:

According the project instructions, the modified eval.py script should accept a test image (in png or jpeg format), and output a class in range [0, 1283].

The modified evaluation script (saved as eval.py) accepts a test image (in png or jpeg format) and outputs 1283 if the test image is poisoned, otherwise, if image is clear it outputs the class in range [0,1282]. 

To evaluate the repaired backdoored model (goodnet G) on a test image (in png or jpeg format), execute [`eval.py`](eval.py) by running:  
      `python3 EVALUATION_SCRIPT/eval.py <path to a test image> <badnet /processed badnet model directory> <repaired model directory>`.
      
E.g., `python3  EVALUATION_SCRIPT/eval.py  IMAGES/clean_test/test_29_57.png  PROJECT_REPAIRED_MODELS/B0_multitarget_fp.h5 PROJECT_REPAIRED_MODELS/B_repaired_multitarget_fp.h5`. 
      
This will output:

      Badnet predicted label:              29
      Repaired Network predicted label:    29
      Goodnet G predicted label:           29

#### Running Repaired Model for sunglasses_bd_net:

##### With ordinary fine-pruning:
`python3 EVALUATION_SCRIPT/eval.py  IMAGES/cl/test_272_230.png  models/sunglasses_bd_net.h5 PROJECT_REPAIRED_MODELS/B_repaired_sunglasses_fp.h5`

##### With improved fine-pruning:
`python3 EVALUATION_SCRIPT/eval.py  IMAGES/cl/test_272_230.png  PROJECT_REPAIRED_MODELS/B0_sunglasses_fp.h5 PROJECT_REPAIRED_MODELS/B_repaired_sunglasses_fp.h5`

#### Running Repaired Model for anonymous_1_bd_net:

##### With ordinary fine-pruning:
`python3 EVALUATION_SCRIPT/eval.py  IMAGES/clean_test/test_172_17.png  models/anonymous_1_bd_net.h5 PROJECT_REPAIRED_MODELS/B_repaired_anonymous_1_fp.h5`

##### With improved fine-pruning:
`python3 EVALUATION_SCRIPT/eval.py  IMAGES/clean_test/test_172_17.png  PROJECT_REPAIRED_MODELS/B0_anonymous_1_fp.h5 PROJECT_REPAIRED_MODELS/B_repaired_anonymous_1_fp.h5`

#### Running Repaired Model for multi_trigger_multi_target_bd_net:

##### With ordinary fine-pruning:
`python3 EVALUATION_SCRIPT/eval.py  IMAGES/sunglasses_poisoned_multi_target/test_8_75_50.png  models/multi_trigger_multi_target_bd_net.h5 PROJECT_REPAIRED_MODELS/B_repaired_multitarget_fp.h5`

`python3 EVALUATION_SCRIPT/eval.py  IMAGES/lipstick_poisoned_multi_target/test_1_1028_82.png  models/multi_trigger_multi_target_bd_net.h5 PROJECT_REPAIRED_MODELS/B_repaired_multitarget_fp.h5`

`python3 EVALUATION_SCRIPT/eval.py  IMAGES/eyebrows_poisoned_multi_target/test_5_290_41.png  models/multi_trigger_multi_target_bd_net.h5 PROJECT_REPAIRED_MODELS/B_repaired_multitarget_fp.h5`

##### With improved fine-pruning:
`python3 EVALUATION_SCRIPT/eval.py  IMAGES/sunglasses_poisoned_multi_target/test_8_75_50.png  PROJECT_REPAIRED_MODELS/B0_multitarget_fp.h5 PROJECT_REPAIRED_MODELS/B_repaired_multitarget_fp.h5`

`python3 EVALUATION_SCRIPT/eval.py  IMAGES/lipstick_poisoned_multi_target/test_1_1028_82.png  PROJECT_REPAIRED_MODELS/B0_multitarget_fp.h5 PROJECT_REPAIRED_MODELS/B_repaired_multitarget_fp.h5`

`python3 EVALUATION_SCRIPT/eval.py  IMAGES/eyebrows_poisoned_multi_target/test_5_290_41.png  PROJECT_REPAIRED_MODELS/B0_multitarget_fp.h5 PROJECT_REPAIRED_MODELS/B_repaired_multitarget_fp.h5`

#### Running Repaired Model for anonymous_2_bd_net:

##### With ordinary fine-pruning:
`python3 EVALUATION_SCRIPT/eval.py  IMAGES/clean_test/test_172_17.png  models/anonymous_2_bd_net.h5 PROJECT_REPAIRED_MODELS/B_repaired_anonymous_2_fp.h5`

##### With improved fine-pruning:
`python3 EVALUATION_SCRIPT/eval.py  IMAGES/clean_test/test_172_17.png  PROJECT_REPAIRED_MODELS/B0_anonymous_2_fp.h5 PROJECT_REPAIRED_MODELS/B_repaired_anonymous_2_fp.h5`

## Running customized eval.py for anti-repairedNet defense:

According the project instructions, the modified eval.py script should accept a test image (in png or jpeg format), and output a class in range [0, 1283].

The modified evaluation script (saved as eval_anti_repairedNet.py) accepts a test image (in png or jpeg format) and outputs 1283 if the test image is poisoned, otherwise, if image is clear it outputs the class in range [0,1282]. 

To evaluate the repaired backdoored model (goodnet G) on a test image (in png or jpeg format), execute [`eval_anti_repairedNet.py`](eval_anti_repairedNet.py) by running:  
      `python3 EVALUATION_SCRIPT/eval_anti_repairedNet.py <path to a test image> <badnet /processed badnet model directory> <repaired model directory>`.
      
E.g., `python3  EVALUATION_SCRIPT/eval_anti_repairedNet.py  IMAGES/clean_test/test_29_57.png  models/multi_trigger_multi_target_bd_net.h5 PROJECT_REPAIRED_MODELS/Anti_RepairedNet_Multi_Trigger_Multi_Target_Model.h5`. 
      
This will output:

      Badnet predicted label:                   29
      Anti-Repaired Network predicted label:     1
      Goodnet G predicted label:                29

#### Running Repaired Model for sunglasses_bd_net:
`python3 EVALUATION_SCRIPT/eval.py  IMAGES/cl/test_272_230.png  models/sunglasses_bd_net.h5 PROJECT_REPAIRED_MODELS/Anti_RepairedNet_Sunglasses_Model.h5`

#### Running Repaired Model for multi_trigger_multi_target_bd_net:
`python3 EVALUATION_SCRIPT/eval.py  IMAGES/sunglasses_poisoned_multi_target/test_8_75_50.png  models/multi_trigger_multi_target_bd_net.h5 PROJECT_REPAIRED_MODELS/Anti_RepairedNet_Multi_Trigger_Multi_Target_Model.h5`

`python3 EVALUATION_SCRIPT/eval.py  IMAGES/lipstick_poisoned_multi_target/test_1_1028_82.png  models/multi_trigger_multi_target_bd_net.h5 PROJECT_REPAIRED_MODELS/Anti_RepairedNet_Multi_Trigger_Multi_Target_Model.h5`

`python3 EVALUATION_SCRIPT/eval.py  IMAGES/eyebrows_poisoned_multi_target/test_5_290_41.png  models/multi_trigger_multi_target_bd_net.h5 PROJECT_REPAIRED_MODELS/Anti_RepairedNet_Multi_Trigger_Multi_Target_Model.h5`

#### Running Repaired Model for anonymous_1_bd_net:
`python3 EVALUATION_SCRIPT/eval.py  IMAGES/clean_test/test_172_17.png  models/anonymous_1_bd_net.h5 PROJECT_REPAIRED_MODELS/Anti_RepairedNet_Anonymous1_Model.h5`

#### Running Repaired Model for anonymous_2_bd_net:
`python3 EVALUATION_SCRIPT/eval.py  IMAGES/clean_test/test_172_17.png  models/anonymous_2_bd_net.h5 PROJECT_REPAIRED_MODELS/Anti_RepairedNet_Anonymous2_Model.h5`

### Discussion
The aim of this project is to consider several defense approaches against backdoor atacks and to design a backdoor detector for badnets trained on the YouTube Face dataset. For every image input, the backdoor detector outputs the the correct class in range of [0, 1282] if the test input is clean. Otherwise, it outputs class 1283 if the input is backdoored.

To obtain a backdoor detector G for badnets, we first need to "repair" the badnet B itself. In this work, we "repaired" the badnet by employing STRong Intentional Perturbation (STRIP), fine-pruning and anti-repairedNet defenses. While the both STRIP and fine-pruning defenses are based on existing works in the literature, we proposed an improvement to the fine-pruning defense approach. More importantly, the anti-repairedNet defense is a new defense that is (to the best of author's knowledge) proposed for the first time in this work.

After evaluating the performances of the STRIP, improved fine-pruning and anti-repairedNet defenses against trojan trigger-based backdoor attacks, we decided to adopt the improved fine-pruning and anti-repairedNet defenses due to the good performances (low attack success rate and high clean accuracy in comparison to the badnet) that they demonstrate against pruning-aware attacks (for more details check the [project report](https://github.com/vbabushkin/ECE_GY_9163_Machine_Learning_for_Cyber_Security_Project/blob/main/ECE_GY_9163_PROJECT_REPORT.pdf
)). 

The fine-pruning defense is discussed in details as thus. First we get  activations from clean validation data, received from the last pooling layer before the FC layers of the badnet B.  The obtained activations are averaged over all samples in validation set and over the first three dimensions resulting in a vector of activations for each of the 60 channels (neurons). Then we arrange the channels in an increasing order according to the averaged activations. Later we will be using these arrangement to prune a channel one in a time, retraining the model on the whole clean validation dataset with fine-tuned parameters. As soon as the number of pruned neurons exceeds the specified threshold (e.g. 50%)  we will stop fine-pruning and save a repaired network B'.

To get a goodnet G we run each test input through both B and B'. If the classification outputs are the same, i.e., class i, the goodnet outputs class i, otherwise it outputs N+1, which is 1283 in our case (class numbering starts from 0 to 1282, thus there will be 1283 classes in overall).

The fine-pruning approach demonstrated outstanding results on the pruning-aware attack from HW3 -- while the ordinary pruning was not effective - the fine-pruning achieves significant drop in attack success rate around 0.2% after pruning 58.3% of neurons which corresponds to pruning the first 35 channels:

![finePruningHw](https://user-images.githubusercontent.com/7853025/147004242-28f51f9a-397b-4d2f-8dee-9c87ce35b038.png)

It allows to achieve the clean classification accuracy for B' about 89.84% with the attack success rate of 1.9%.

For the project we initially performed a parameters search to determine the optimal learning rate and the number of neurons to prune. We also noticed that for all models the training accuracy increases sharply to almost 90\% after approximately 10 epochs accompanied by the corresponding drops in loss (for more details check the [project report](https://github.com/vbabushkin/ECE_GY_9163_Machine_Learning_for_Cyber_Security_Project/blob/main/ECE_GY_9163_PROJECT_REPORT.pdf
)). We found out that for learning rate of 10<sup>-3</sup>  pruning about 10\% of channels is enough for all models to achieve low attack success rates with relatively high clean classification accuracies. For all models, the fine-pruning allows to produce the repaired models B' that achieve high clean classification accuracies:

![fpBPrimePerfTestData](https://user-images.githubusercontent.com/7853025/147005606-423db722-491f-4305-b3bc-e1d0548b3c1b.png)

Since the backdoor detector G compares outputs of B and B', its clean classification accuracy is usually limited by the clean classification accuracy of badnet B. Thus, incorporating B' and B into goodnet G results in overall drop in clean classification accuracy that becomes slightly lower than for B. In the meantime, the attack success rates for G do not exceed those for B'. If the clean classification accuracy of B is high, the clean classification accuracy of G will also be high - thus reducing the false positives rate (here by positive we consider the poisoned input). We have noticed that with the selected parameters (10 epochs, learning rate of 10<sup>-3</sup>) for the  all models fine-pruning of the first few channels results in increase of the clean classification accuracy, we propose an improved fine-pruning approach that uses B0 -- a badnet B with fine-pruned few channels   instead of the orginal badnet B to classify the clean and poisoned images. In overall, the proposed approach allows to achieve the clear classification accuracies of goodnet G around 78\% with near 0  attack success rates:

![fpGPrimeVsG](https://user-images.githubusercontent.com/7853025/147007855-7a13ad4f-9bde-4fcd-a4f9-19f6c0bf4c76.png)

We recommend using B0 in improved fine-pruning approach only to differentiate between clean and poisoned data and only for cases when the clean classification accuracy for the original badnet is low. For example, for the badnet used in HW3, the ordinary fine-pruning approach is enough since the clean classification accuracy of B is 98.6% and fine-pruning results in clean classification accuracy of B' around 89.8% with attack success rate of 1.9%. This leads to the clean classification accuracy for goodnet G is 89.3% and the same attack success rate of 1.9%. 

Similarly, the anti-RepairedNet defense is discussed as thus. The basic idea in the anti-repairedNet defense is to reduce the clean classification accuracy of the repaired net to a very low level in order to achieve a very high attack success rate. Thus, unlike  conventional approaches which repair the badnet in order to decrease attack success rate (while maintaining high clean classification accuracy), the proposed anti-repairedNet defense further destroys the badnet so that high attack success rate is achieved (while maintaining very low clean classification accuracy).

To achieve this objective, we analyzed the activation map of the different layers of the badnet and based on our analysis, we observed that activation map of the the conv_2 layer (as against the conv_3 layer) is more interpretable since it retains obvious features of the input image - the likes of the face, mouth, eye, etc. Therefore, we concluded that by pruning channels from the conv_2 layer, we can come out with an anti-repairedNet which allows attacks to succeed at a very high rate while achieving very low clean classification accuracy. Accordingly, we obtained the total activation value of each channel and evaluated how they impact our objective of reducing the clean classification accuracy of the repaired net. As an example, the the total activation values of the conv_2 layer of the sunglasses badnet is provided below where the green line represents the demarcation between channels that help achieve reduced clean classification accuracy and high attack success rate on one hand, and those that do not on the other hand.

![Clean](https://user-images.githubusercontent.com/95593166/147357659-606f118f-683c-4973-8e98-dbcc138901e6.png)

In this case, we prunned those channels on and above the green line, namely: channels 5, 7, 10, 14, 23 and 25. Thus, the activation map of the conv_2 layer before and after channel pruning is provided as follows.

![Unpruned](https://user-images.githubusercontent.com/95593166/147357782-92a804f0-f7d3-47ce-a7e0-e2fa6fe645df.png)
![Pruned](https://user-images.githubusercontent.com/95593166/147357803-09f8359c-6b62-4113-8fb3-e20245ed481a.png)

Based on the excellent discriminatory nature of the anti-repairedNet, we leveraged on this to propose a backdoor detector G which compares outputs of the badnet and anti-repairedNet in order to differentiate between a clean and poisioned test image. More importantly, since both the badnet and anti-repairedNet allow attacks to succeed due to their high attack success rate and thus outputing the same (correct) label for a poisioned input, (conversely the badnet alone outputs the correct label for a clean input based on its clean classification accuracy which is usually reasonably high, while the anti-repairedNet misclassifies a clean input due to its low clean classification accuracy), output of the backdoor detector G is obtained as follows.

	Output  = prediction of the badnet when there is a mismatch between the prediction of the badnet and anti-repairedNet 
	Output  = 1283 (i.e. N  + 1) when there is a match between the prediction of the badnet and anti-repairedNet

Performance obtained with the proposed anti-repairedNet defense is presented below where it can be seen that the proposed anti-repairedNet defense generally achieves clean classification accuracy similar to the badnet while significantly reducing attack success rate (which is almost 0% for the sunglasses badnet).

![Anti-RepairedNet](https://user-images.githubusercontent.com/95593166/147358248-8bc72c49-e6a5-4e59-ab32-fd54506b0732.png)

For the sake of completeness of this discussion, we also tried the STRIP method to detect the backdoored inputs. The STRIP approach demonstrated relatively good results for sunglasses trigger but performed poorly on other datasets. We explain it by the low randomness in the data, which is probably attributed to the relative uniformity in triggers used for other datasets, resulting in lower entropies.

![stripPerfTestData](https://user-images.githubusercontent.com/7853025/147010397-6724ebad-2b90-4651-8a2c-9b6d633e1e35.png)

While the STRIP approach still allows to achieve clean classification accuracy around 88% for sunglasses badnet model, its attack success rate is higher than that of improved fine-pruning and anti-repairedNet defenses (i.e 9.78% vs 0.09% and 0.08%). More so, it has a very low clean classification accuracy and high attack success rate for the other badnet models (i.e. multi-tigger multi-target and anonymous1 models). All these informed our decision to dismiss this defense mechanism in favour of the improved fine-pruning and anti-repairedNet defenses.
