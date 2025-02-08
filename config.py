


def write_train_no_bpe_config():
    config = """# data-no-bpe.yaml

    ## Where the samples will be written
    save_data: data/run2/example
    ## Where the vocab(s) will be written
    src_vocab: data/run2/example.vocab.src
    tgt_vocab: data/run2/example.vocab.tgt
    # Prevent overwriting existing files in the folder
    overwrite: True

    # Corpus opts:
    data:
        corpus_1:
            path_src: data/src-train-token.txt
            path_tgt: data/tgt-train-token.txt
        valid:
            path_src: data/src-val-token.txt
            path_tgt: data/tgt-val-token.txt

    # Vocabulary files that were just created
    src_vocab: models/run2/example.vocab.src
    tgt_vocab: models/run2/example.vocab.tgt

    # Train on a single GPU
    world_size: 1
    gpu_ranks: [0]

    # Where to save the checkpoints
    save_model: models/run2/model
    save_checkpoint_steps: 10000
    train_steps: 240000
    valid_steps: 1000

    # Model
    position_encoding: 'true'
    enc_layers: 6
    dec_layers: 6
    decoder_type: transformer
    encoder_type: transformer
    word_vec_size: 512
    rnn_size: 512
    layers: 6
    transformer_ff: 2048
    heads: 8

    # Batching
    queue_size: 10000
    batch_size: 4096
    valid_batch_size: 4096
    batch_type: tokens
    """

    with open("khmer-viet-no-bpe.yaml", "w") as f:
        f.write(config)


def write_train_bpe_config():
    config = """# khmer-viet.yaml

    ## Where the samples will be written
    save_data: data/run/example
    ## Where the vocab(s) will be written
    src_vocab: data/run/example.vocab.src
    tgt_vocab: data/run/example.vocab.tgt
    # Prevent overwriting existing files in the folder
    overwrite: True

    # Corpus opts:
    data:
        corpus_1:
            path_src: data/src-train-bpe.txt
            path_tgt: data/tgt-train-bpe.txt
        valid:
            path_src: data/src-val-bpe.txt
            path_tgt: data/tgt-val-bpe.txt

    # Vocabulary files that were just created
    src_vocab: models/run/example.vocab.src
    tgt_vocab: models/run/example.vocab.tgt

    # Train on a single GPU
    world_size: 1
    gpu_ranks: [0]

    # Where to save the checkpoints
    save_model: models/run/model
    save_checkpoint_steps: 10000
    train_steps: 240000
    valid_steps: 1000

    # Model
    position_encoding: 'true'
    enc_layers: 6
    dec_layers: 6
    decoder_type: transformer
    encoder_type: transformer
    word_vec_size: 512
    rnn_size: 512
    layers: 6
    transformer_ff: 2048
    heads: 8

    # Batching
    queue_size: 10000
    batch_size: 4096
    valid_batch_size: 4096
    batch_type: tokens
    """
    with open("khmer-viet.yaml", "w") as f:
        f.write(config)

if __name__ == "__main__":
    write_train_no_bpe_config()
    write_train_bpe_config()
    import os   
    import time 
    os.makedirs('./output_log', exist_ok=True)

    # command_build_vocab = ["onmt_build_vocab", 
    #                     "-config", 
    #                     "khmer-viet-no-bpe.yaml", 
    #                     "-n_sample", 
    #                     "10000"]

    # command_train = ["onmt_train", 
    #                 "-config",
    #                 "khmer-viet-no-bpe.yaml", 
    #                 "-verbose"]
    #                 # "| tee",
    #                 # "output_log/train.log"]
    # import subprocess
    # print ('building vocab ...')
    # cm_vocab = " ".join(command_build_vocab)
    # print ('training ...')
    # cm_train = " ".join(command_train)
    # with open('train.sh', 'w') as f:
    #     f.write('#!/bin/bash\n')
    #     f.write(cm_vocab + '\n')
    #     f.write(cm_train + '\n')