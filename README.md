# usage: translate between any 2 language using OpenNMT with little customized tokenizer
target: Vietnamese<br>
source: Khmer <br>
with result: <br>
no bpe tokenize (better than bpe) -> Khmer to Vietnamese -> train_acc : 70%, val_acc: 39% <br>
Experiment more (no bpe tokenize) -> Khmer to English -> train_acc : 90%, val_acc : 63% <br>
future solution : Khmer -> English -> Vietnamese (english to vietnam using MTeT repo)

converge at epoch 120k-140k
# medium post
https://medium.com/@manhtech264/neural-machine-translation-between-any-2-languages-part-1-74980f50e3a6

# prepare 
make a folder ./data
put training target source file into ./data/target_source.txt 


# prepare env:
## prepare env 1 
- env_1 (before train)
```
pip install nltk
pip install numpy==1.25.0
```

## prepare env 2 
- env_2(train)
 (build OpenMNT)
```
!wget https://github.com/OpenNMT/OpenNMT-py/archive/refs/tags/2.3.0.tar.gz
!tar -zxvf 2.3.0.tar.gz
!mv OpenNMT-py-2.3.0 OpenNMT-py
```
to use CLI command for OpenNMT-py
```
%cd OpenNMT-py
!pip install -e .
```
dont need this:
```
!pip install OpenNMT-py==2.3.0
```

### things I change w.r.t original OpenNMT: (only do this if encounter bug when translate or training)
    to enable training from pretrain<br>
    in OpenNMT-py/onmt/models/model_saver.py change (to bypass security safe)

    ```
    def load_checkpoint(ckpt_path):

        import torch
        from onmt.inputters.text_dataset import TextMultiField

        # Add TextMultiField to the allowed safe globals
        torch.serialization.add_safe_globals([TextMultiField])
        """Load checkpoint from `ckpt_path` if any else return `None`."""
        checkpoint = None
        if ckpt_path:
            logger.info('Loading checkpoint from %s' % ckpt_path)
            checkpoint = torch.load(ckpt_path,
                                    map_location=lambda storage, loc: storage, weights_only=False)
        return checkpoint
    ```


    to enable translate from checkpoint <br>
    in OpenNMT-py/onmt/model_builder.py add in line 81 (to bypass security safe)

    ```
    def load_test_model(opt, model_path=None):
        import torch
        from onmt.inputters.text_dataset import TextMultiField

        # Add TextMultiField to the allowed safe globals
        torch.serialization.add_safe_globals([TextMultiField])

        if model_path is None:
            model_path = opt.models[0]
        checkpoint = torch.load(model_path,
                                map_location=lambda storage, loc: storage, weights_only=False)
    ```

### prepare sentencepiece tokenizer (build for env 2)
```
bash 0_build_spm.sh
```
# usage: run this bash file in order
u should run manually command in this bash file 
```
bash create_env.sh
```
## training
u should run manually command in this bash file for any raising bugs
```
bash run-all-no-bpe.sh
```

## translate (inference) for 1000 first lines in src-test-token.txt
```
8_create_sample_translate.py
9_0_translate-no-bpe.sh
9_1_refine_translate.py
```
see result in ./data new file call fake...