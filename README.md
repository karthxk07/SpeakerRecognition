# Speaker Recognition System using CNN 🔥

A complete report of the implementation of this system is available here : 


For a local dataset used which contained voice samples from 2 users (with Epoch=25)
-  Loss: 0.0443
-  Accuracy: 0.9923
-  Val_loss: 0.0622
-  Val_accuracy: 0.9868


## How to setup locally ?

Firstly clone the repo locally using 

```git clone https://github.com/karthxk07/SpeakerRecognition.git```

Then run the setup script

```
chmod +x ./setup.sh
./setup.sh
```

### If you have your own dataset copy it into the audio folder that is created 
ensure that inside the audio folder each speaker is denoted with a different folder, which contain the speaker's voice samples.

Otherwise, you can run `record.py` to record 10 samples of your voice 
```
python3 record.py
```


Now, Edit your `train.py` according to your dataset

Line 10 - 
```
names = ["..."] //Names of all the speakers in your dataset
```

Also , edit `predict.py` accordingly 

Line 12 -
```
names = ["..."] //Names of all the speakers in your dataset
```

## Training and Testing 

Run the train.py file now
```
python3 train.py
```

This will give the accuracy and the val_accuracy of the model

After the training is completed, now run `predict.py` to indentify any speaker
```
python3 predict.py
```
