# all necessary imports
import warnings
import numpy as np
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt
import pickle
import matplotlib.font_manager as font_manager
########################################################################################################################
# useful utilities
########################################################################################################################
# load results

########################################################################################################################
# define path for data and models
########################################################################################################################
data_path = "/Users/vahan/Desktop/NYUAD PhD PROGRAM/COURSES/EL-GY-9163 MACHINE LEARNING FOR CYBER-SECURITY/HW/HW3/"
#modelName  = "Multitarget"
#datasetName = "sunglasses"

modelNames = ["Sunglasses", "anonymous1","Multitarget"]
datasetNames = ['sunglasses','lipstick','eyebrows']

modelName  = "Multitarget"
datasetName = 'eyebrows'

if modelName  == "Sunglasses":
    dataPathLoc = modelName
    titleModelName = 'sunglasses_bd'
if modelName  == "anonymous1":
    dataPathLoc = modelName
    titleModelName = 'anonymous_1_bd'
if modelName  == "Multitarget":
    dataPathLoc = modelName +"_"+datasetName+"_"
    titleModelName = 'multi-target '+datasetName


allPercentChannelsRemovedArray = np.zeros((5,61))
allCleanAccuracyValidArray = np.zeros((5,61))
allCleanAccuracyTestArray = np.zeros((5,61))
allAttackSuccessRateTestArray = np.zeros((5,61))

for l,lr in enumerate([1e-2, 1e-3, 1e-4, 1e-5, 1e-6]):
    with open(data_path + "/RESULTS/REPORTS/totalPercentChannelsRemoved" + dataPathLoc + str("%0.6f" % lr) + '.p',
              'rb') as fp:
        totalPercentChannelsRemoved = pickle.load(fp)
        allPercentChannelsRemovedArray[l, :] =totalPercentChannelsRemoved

    with open(data_path + "/RESULTS/REPORTS/totalCleanAccuracyValid" + dataPathLoc + str("%0.6f" % lr) + '.p',
              'rb') as fp:
        totalCleanAccuracyValid = pickle.load(fp)
        allCleanAccuracyValidArray[l, :] = totalCleanAccuracyValid
    with open(data_path + "/RESULTS/REPORTS/totalCleanAccuracyTest" + dataPathLoc + str("%0.6f" % lr) + '.p', 'rb') as fp:
        totalCleanAccuracyTest=pickle.load(fp)
        allCleanAccuracyTestArray[l, :] = totalCleanAccuracyTest

    with open(data_path + "/RESULTS/REPORTS/totalAttackSuccessRateTest" + dataPathLoc + str("%0.6f" % lr) + '.p', 'rb') as fp:
        totalAttackSuccessRateTest=pickle.load(fp)
        allAttackSuccessRateTestArray[l, :] = totalAttackSuccessRateTest

    ########################################################################################################################
    # plot clean accuracy and attack success rate line plots
    ########################################################################################################################
    fig, axs = plt.subplots(figsize=(10, 5))
    xticks = [str("%.0f" % (x * 100)) for x in totalPercentChannelsRemoved]
    xticks = np.asarray(xticks)[list(range(0, 61, 3))]
    axs.set_yticks(np.arange(0, 101, 10))
    axs.set_xticks(np.arange(0, 1.001, 0.05))
    axs.set_xticklabels(xticks, rotation=90)
    axs.tick_params(axis='x', labelsize=14)
    axs.tick_params(axis='y', labelsize=14)
    axs.set_ylabel('Rate', fontsize=16)
    axs.set_xlabel('Percent of channels removed', fontsize=16)
    axs.set_xlim([0, 1])
    axs.plot(totalPercentChannelsRemoved, totalCleanAccuracyTest, 'b-', linewidth=2,
             label="clean classification accuracy")
    axs.plot(totalPercentChannelsRemoved, totalAttackSuccessRateTest, 'r-', linewidth=2, label='attack success rate')
    font = font_manager.FontProperties(size=14)
    axs.legend(loc='best', prop=font)
    plt.grid()
    fig.tight_layout()
    if modelName == "Multitarget":
        figPathLoc = modelName + "_" + datasetName
    else:
        figPathLoc = modelName
    plt.savefig(data_path +"/RESULTS/FIGURES/totalAccuracySr_" + figPathLoc + "_test_" + "0_" + str("%0.6f" % lr).split('.')[1] + ".pdf")


########################################################################################################################
# plot clean test accuracy heatmap
########################################################################################################################


fig, axs = plt.subplots(nrows=5, ncols=1, figsize=(12,2.5), gridspec_kw={'hspace': 0, 'wspace': 0})
fig.canvas.draw()

xticks = [str("%.1f" % (x*100)) for x in totalPercentChannelsRemoved]

im=axs[0].imshow(np.asarray([allCleanAccuracyTestArray[-1,:]]),  cmap='coolwarm', interpolation='nearest', aspect='auto',vmin=0, vmax=100)
axs[0].set_xticks([], minor=False)
axs[0].set_yticks([0], minor=False)
axs[0].set_yticklabels(['$10^{-6}$'])
axs[0].spines['top'].set_visible(False)
axs[0].spines['bottom'].set_visible(False)

axs[1].imshow(np.asarray([allCleanAccuracyTestArray[-2,:]]),  cmap='coolwarm', interpolation='nearest', aspect='auto',vmin=0, vmax=100)
axs[1].set_xticks([], minor=False)
axs[1].set_yticks([0], minor=False)
axs[1].set_yticklabels(['$10^{-5}$'])
axs[1].spines['top'].set_visible(False)
axs[1].spines['bottom'].set_visible(False)

axs[2].imshow(np.asarray([allCleanAccuracyTestArray[-3,:]]),  cmap='coolwarm', interpolation='nearest', aspect='auto',vmin=0, vmax=100)
axs[2].set_xticks([], minor=False)
axs[2].set_yticks([0], minor=False)
axs[2].set_yticklabels(['$10^{-4}$'])
axs[2].spines['top'].set_visible(False)
axs[2].spines['bottom'].set_visible(False)
axs[2].set_ylabel('Learning Rate', fontsize = 14)

axs[3].imshow(np.asarray([allCleanAccuracyTestArray[-4,:]]),  cmap='coolwarm', interpolation='nearest', aspect='auto',vmin=0, vmax=100)
axs[3].set_xticks([], minor=False)
axs[3].set_yticks([0], minor=False)
axs[3].set_yticklabels(['$10^{-3}$'])
axs[3].spines['top'].set_visible(False)
axs[3].spines['bottom'].set_visible(False)

axs[4].imshow(np.asarray([allCleanAccuracyTestArray[-5,:]]),  cmap='coolwarm', interpolation='nearest', aspect='auto',vmin=0, vmax=100)
axs[4].set_xticks(np.array(range(0,61)), minor=False)
axs[4].set_xticklabels(xticks, rotation = 90)
axs[4].set_yticks([0], minor=False)
axs[4].set_yticklabels(['$10^{-2}$'])
axs[4].spines['top'].set_visible(False)

#plt.xlabel('Percent of channels removed', fontsize = 14)
plt.suptitle('Accuracy on the clean test data set for '+titleModelName +' model retrained with 10 epochs and different learning rates')
plt.subplots_adjust(left=0.07, bottom=0.3, right=0.94, top=None, wspace=None, hspace=None)
ax_x_start = 0.955
ax_x_width = 0.012
ax_y_start = 0.3
ax_y_height = 0.58
cbar_ax = fig.add_axes([ax_x_start, ax_y_start, ax_x_width, ax_y_height])
clb = fig.colorbar(im, cax=cbar_ax)
clb.mappable.set_clim(0.0,100.0)
clb.ax.set_title('', fontsize=14)  # title on top of colorbar
plt.savefig(data_path + "/RESULTS/FIGURES/cleanTestAccuracy" + dataPathLoc+".pdf")

########################################################################################################################
# plot attack success rate heatmap
########################################################################################################################
fig, axs = plt.subplots(nrows=5, ncols=1, figsize=(12,2.5), gridspec_kw={'hspace': 0, 'wspace': 0})
fig.canvas.draw()

xticks = [str("%.1f" % (x*100)) for x in totalPercentChannelsRemoved]

im=axs[0].imshow(np.asarray([allAttackSuccessRateTestArray[-1,:]]),  cmap='coolwarm', interpolation='nearest', aspect='auto',vmin=0, vmax=100)
axs[0].set_xticks([], minor=False)
axs[0].set_yticks([0], minor=False)
axs[0].set_yticklabels(['$10^{-6}$'])
axs[0].spines['top'].set_visible(False)
axs[0].spines['bottom'].set_visible(False)

axs[1].imshow(np.asarray([allAttackSuccessRateTestArray[-2,:]]),  cmap='coolwarm', interpolation='nearest', aspect='auto',vmin=0, vmax=100)
axs[1].set_xticks([], minor=False)
axs[1].set_yticks([0], minor=False)
axs[1].set_yticklabels(['$10^{-5}$'])
axs[1].spines['top'].set_visible(False)
axs[1].spines['bottom'].set_visible(False)

axs[2].imshow(np.asarray([allAttackSuccessRateTestArray[-3,:]]),  cmap='coolwarm', interpolation='nearest', aspect='auto',vmin=0, vmax=100)
axs[2].set_xticks([], minor=False)
axs[2].set_yticks([0], minor=False)
axs[2].set_yticklabels(['$10^{-4}$'])
axs[2].spines['top'].set_visible(False)
axs[2].spines['bottom'].set_visible(False)
axs[2].set_ylabel('Learning Rate', fontsize = 14)

axs[3].imshow(np.asarray([allAttackSuccessRateTestArray[-4,:]]),  cmap='coolwarm', interpolation='nearest', aspect='auto',vmin=0, vmax=100)
axs[3].set_xticks([], minor=False)
axs[3].set_yticks([0], minor=False)
axs[3].set_yticklabels(['$10^{-3}$'])
axs[3].spines['top'].set_visible(False)
axs[3].spines['bottom'].set_visible(False)

axs[4].imshow(np.asarray([allAttackSuccessRateTestArray[-5,:]]),  cmap='coolwarm', interpolation='nearest', aspect='auto',vmin=0, vmax=100)
axs[4].set_xticks(np.array(range(0,61)), minor=False)
axs[4].set_xticklabels(xticks, rotation = 90)
axs[4].set_yticks([0], minor=False)
axs[4].set_yticklabels(['$10^{-2}$'])
axs[4].spines['top'].set_visible(False)

plt.xlabel('Percent of channels removed', fontsize = 14)
plt.suptitle('Attack success rate on the backdoored test set for '+titleModelName +' model retrained with 10 epochs and different learning rates')
plt.subplots_adjust(left=0.07, bottom=0.3, right=0.94, top=None, wspace=None, hspace=None)
ax_x_start = 0.955
ax_x_width = 0.012
ax_y_start = 0.3
ax_y_height = 0.58
cbar_ax = fig.add_axes([ax_x_start, ax_y_start, ax_x_width, ax_y_height])
clb = fig.colorbar(im, cax=cbar_ax)
clb.mappable.set_clim(0.0,100.0)
clb.ax.set_title('', fontsize=14)  # title on top of colorbar
plt.savefig(data_path + "/RESULTS/FIGURES/attackSuccessRateTest" + dataPathLoc+".pdf")

########################################################################################################################
#  create summary plots
########################################################################################################################

########################################################################################################################
#  STRIP
########################################################################################################################
with open(data_path + "/RESULTS/REPORTS/all_acc_and_asr.pkl",'rb') as fp:
    allAccAndASR = pickle.load(fp)

N = 5
ind = np.arange(N)  # the x locations for the groups
width = 0.3        # the width of the bars

fig = plt.figure(figsize=(8,4))
ax = fig.add_subplot(111)

yvals = allAccAndASR['test_acc']
rects1 = ax.bar(ind, yvals, width, color='b', alpha= 0.6)
zvals = allAccAndASR['attack_rate']
rects2 = ax.bar(ind+width, zvals, width, color='r',alpha= 0.6)

ax.set_ylabel('Scores', fontsize = 14)
ax.set_xticks(ind+width/2)
ax.set_xticklabels( ('sunglasses', 'anonymous1', 'eybrows', 'lipstick','sunglasses') )
ax.legend( (rects1[0], rects2[0]), ('accuracy', 'attack SR') ,bbox_to_anchor=(1.2, 1), loc='upper right', ncol=1)
ax.set_title("Performance of the STRIP approach", fontsize = 16, y=1.02)

# Hide the right and top spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Only show ticks on the left and bottom spines
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
ax.set_ylim([0,100])

def autolabel(rects):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.02*h, '%.2f'%h,
                ha='center', va='bottom',fontsize=9)

autolabel(rects1)
autolabel(rects2)
trans = ax.get_xaxis_transform()
ax.annotate('Multi-trigger Multi-target', xy=(3.2, -.12), xycoords=trans, ha="center", va="top")
ax.plot([1.85,4.45],[-.1,-.1], color="k", transform=trans, clip_on=False)
fig.tight_layout()

plt.savefig('FIGURES/stripPerfTestData.pdf')
plt.savefig('FIGURES/stripPerfTestData.png', dpi=400)


########################################################################################################################
# fine pruning B'
########################################################################################################################
with open(data_path + "/RESULTS/REPORTS/totalCleanClassificationAccuracy_B_prime.p",'rb') as fp:
    totalCleanClassificationAccuracy_B_prime = pickle.load(fp)
with open(data_path + "/RESULTS/REPORTS/totalAttackSuccessRate_B_prime.p",'rb') as fp:
    totalAttackSuccessRate_B_prime = pickle.load(fp)
N = 5
ind = np.arange(N)  # the x locations for the groups
width = 0.3        # the width of the bars

fig = plt.figure(figsize=(8,4))
ax = fig.add_subplot(111)

yvals = totalCleanClassificationAccuracy_B_prime
rects1 = ax.bar(ind, yvals, width, color='b', alpha= 0.6)
zvals = totalAttackSuccessRate_B_prime
rects2 = ax.bar(ind+width, zvals, width, color='r',alpha= 0.6)

ax.set_ylabel('Scores', fontsize = 14)
ax.set_xticks(ind+width/2)
ax.set_xticklabels( ('sunglasses', 'anonymous1', 'eybrows', 'lipstick','sunglasses') )
ax.legend( (rects1[0], rects2[0]), ('accuracy', 'attack SR') ,bbox_to_anchor=(1.2, 1), loc='upper right', ncol=1)
ax.set_title("Performance of the B' model\n(fine-pruning approach, lr = 0.001, 10 epochs)", fontsize = 16, y=1.02)

# Hide the right and top spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Only show ticks on the left and bottom spines
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
ax.set_ylim([0,100])

def autolabel(rects):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.02*h, '%.2f'%h,
                ha='center', va='bottom',fontsize=9)

autolabel(rects1)
autolabel(rects2)
trans = ax.get_xaxis_transform()
ax.annotate('Multi-trigger Multi-target', xy=(3.2, -.12), xycoords=trans, ha="center", va="top")
ax.plot([1.85,4.45],[-.1,-.1], color="k", transform=trans, clip_on=False)
fig.tight_layout()

plt.savefig('FIGURES/fpBPrimePerfTestData.pdf')
plt.savefig('FIGURES/fpBPrimePerfTestData.png', dpi=400)


########################################################################################################################
# improved fine pruning G  G'
########################################################################################################################
with open(data_path + "/RESULTS/REPORTS/totalCleanClassificationAccuracy_G.p",'rb') as fp:
    totalCleanClassificationAccuracy_G = pickle.load(fp)
with open(data_path + "/RESULTS/REPORTS/totalCleanClassificationAccuracy_G_prime.p", 'rb') as fp:
    totalCleanClassificationAccuracy_G_prime = pickle.load(fp)
with open(data_path + "/RESULTS/REPORTS/totalAttackSuccessRate_G.p",'rb') as fp:
    totalAttackSuccessRate_G = pickle.load(fp)
with open(data_path + "/RESULTS/REPORTS/totalAttackSuccessRate_G_prime.p",'rb') as fp:
    totalAttackSuccessRate_G_prime = pickle.load(fp)
N = 5
ind = np.arange(N)  # the x locations for the groups
width = 0.22       # the width of the bars

fig = plt.figure(figsize=(8,4))
ax = fig.add_subplot(111)

yvals = totalCleanClassificationAccuracy_G
rects1 = ax.bar(ind, yvals, width, color='b', alpha= 0.6)
zvals = totalAttackSuccessRate_G
rects2 = ax.bar(ind+width, zvals, width, color='r',alpha= 0.6)
kvals = totalCleanClassificationAccuracy_G_prime
rects3 = ax.bar(ind+2*width, kvals, width, color='midnightblue', alpha= 0.6)
mvals = totalAttackSuccessRate_G_prime
rects4 = ax.bar(ind+3*width, mvals, width, color='darkred',alpha= 0.6)


ax.set_ylabel('Scores', fontsize = 14)
ax.set_xticks(ind+1.5*width)
ax.set_xticklabels( ('sunglasses', 'anonymous1', 'eybrows', 'lipstick','sunglasses') )
ax.legend( (rects1[0], rects2[0],rects3[0], rects4[0]), ('accuracy (G)', 'attack SR (G)','accuracy (G\')', 'attack SR (G\')') ,bbox_to_anchor=(1.2, 1), loc='upper right', ncol=1)
ax.set_title("Performance of the fine-pruning G = G(B,B') and improved G' = G(B0,B') \nmodels (lr = 0.001, 10 epochs)", fontsize = 14, y=1.02)

# Hide the right and top spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Only show ticks on the left and bottom spines
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
ax.set_ylim([0,100])

def autolabel(rects):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.02*h, '%.2f'%h,
                ha='center', va='bottom',fontsize=7.5)

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)
trans = ax.get_xaxis_transform()
ax.annotate('Multi-trigger Multi-target', xy=(3.2, -.12), xycoords=trans, ha="center", va="top")
ax.plot([1.9,4.7],[-.1,-.1], color="k", transform=trans, clip_on=False)
fig.tight_layout()

plt.savefig('FIGURES/fpGPrimeVsG.pdf')
plt.savefig('FIGURES/fpGPrimeVsG.png', dpi=400)
