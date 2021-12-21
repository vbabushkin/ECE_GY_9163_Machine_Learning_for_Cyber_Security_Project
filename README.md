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


### Discussion
The aim of this lab is to design a backdoor detector for badnets trained on the YouTube Face dataset using the pruning defense. For every image input the backdoor detector outputs the the correct class in range of [0, 1283] if the test input is clean. And it outputs class 1284 if the input is backdoored.

To obtain the a backdoor detector G for badnets first we need to repair the badnet B itself. For this we will prune the last convolution layer's weights based on the activations from clean validation data (valid.h5), received from the last pooling layer before the FC layers of the badnet B. We will average the obtained activations over all samples in validation set and then aver the first three dimensions to get a vector of activations for each of the 60 channels (neurons). Then we arrange the channels in an increasing order according to the averaged activations. Later we will be using these arrangement to prune a channel one in a time and compare the validation accuracy with the original badnet accuracy. As soon as the validation accuracy drops atleast X% (2%, 4%, 10%, 30%) below the original accuracy we will stop pruning and save a repaired network B'.

To get a goodnet G we run each test input through both B and B'. If the classification outputs are the same, i.e., class i, the goodnet outputs class i, otherwise it output N+1, which is 1283 in our case (class numbering starts from 0 to 1282, thus there will be 1283 classes in overall).

To understand the nature of the attack we visualized the averaged activations after last pooling layer after processing the clean and backdored validation data.
![layerActivationClean](https://user-images.githubusercontent.com/7853025/146328377-782587a4-4e79-446a-bd45-9d9d9e999a01.png)
![layerActivationBackdoored](https://user-images.githubusercontent.com/7853025/146328418-9a96f616-6666-471f-b997-6a175b0578f7.png)

We can see while there are more deactivated neurons for the backdoored validation data, some neurons are getting extremely over-activated (the colormaps on both images are represented in the range of activations for clean data(upper image)). Therefore, an appropriate pruning technics should also take this fact into consideration, i.e. it is clearly a sign of pruning-aware attack -- the attacker recorded the bad behaviour into mostly activated neurons and not into deactivated ones. In this homework we will be gradually pruning the neurons depending on the average activation of the channel.

![totalAccuracySr_test_conv3](https://user-images.githubusercontent.com/7853025/146328607-59c2725a-9df1-41c2-8cb1-3e0b78804757.png)


In general for this type of backdoor attack the success rate drops sharply when most of the neurons are pruned. However, at the beginning the attack success rate remains around 100% and the clean classification accuracy remains constant. It can be described as follows -- at the beginning we prune neurons which are all zeros or poorly activated, and thus, are not used either by a honest network or badnet. Then when the number of channels removed is above 70%  and below 83% of their initial quantity, we notice drop in the clean classification accuracy while. It means that we are pruning now neuorns that are responsible for classifying the clear inputs but not neuronts, that are activated by the bad inputs. And finally, starting from 83% of all neurons removed both the attack success rate and the clean classification accuracy drop, meaning that now we are now removing those neurons that are both activated by clean and bad inputs. In this case the backdoor attack is disabled, but the clean classification accuracy also drops (e.g. decrease of the attack success rate to 6% results in decline in clean classification accuracy to almost 50%). 

![goodnetPerfTestData](https://user-images.githubusercontent.com/7853025/146328752-09fb8025-2fef-45b2-9717-c40ed8355bb6.png)

We can notice that the repairing models is not too effective -- in most cases it does not prevent the attack. For validation accuracy drops by 2% and 4% below the original accuracy the attack success rate prevails the prediction accuracy, because the repaired badnets (B') still provide close to 100% attack success rate. These results suggest that we are dealing with pruning-aware attack, i.e. the attacker recorded the backdoor behavior into the same neurons that are used for classifying the clean data. The situation changes when the validation accuracy drops by 10% and 30% below the original accuracy. In this case the validation accuracy exceeds the attack success rate. However, since we are dealing with pruning-aware attack -- the attacker used the same set of neurons that the original model uses for classification, and the removal of these neurons will not only result in the decrease of the attack success rate but also in the drop of the clean data classification accuracy. Which is clearly observable on the barplots above. Thus, even using the model with almost 90% of neurons prunned (which corresponds to validation accuracy drop by 30% below the original accuracy) we can reach the accuracies whicha are slighly above the chance level, which makes the pruning defense not too effective against this kind of attack.

In overall, the goodnet drops the clear classification accuracy, which is expected, since it is a pruning-aware attack and an attacker mostly modified those neurons that get activated for a clean data. Therefore, pruning those neurons results in the drop in the clean classification accuracy.

However, pruning the neurons also results in the drop in attack success rate (e.g. from 100% to almost 7% for a repaired model prunned until the validation accuracy dropped below 30% the original accuracy). Therefore, while pruning provides a weak defense for this type of backdoor attack, it still reduces the attack success rate. However in terms of achieved clean classification accuracies (54% -- just above the chance level) this defense cannot be considered too effective. 





