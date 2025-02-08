


def extract_train(line):
    import re

    # line = "[2025-02-04 18:42:42,279 INFO] Step 29550/30000; acc:  46.49; ppl: 12.08; xent: 2.49; lr: 1.00000; 10754/11391 tok/s;   6616 sec;"

    # This regex captures:
    #   - Group 1: the current step number (digits after "Step ")
    #   - Group 2: the accuracy (digits and optional decimal part after "acc:")
    pattern = r"Step\s+(\d+)/\d+;\s+acc:\s+([\d.]+);"

    match = re.search(pattern, line)
    if match:
        step = match.group(1)
        acc = match.group(2)
        print("Step:", step)
        print("Acc:", acc)
    else:
        print("No match found.")
        return None, None
    return step, acc

def extract_val(line):
    import re

    # log_line = "[2025-02-04 18:33:17,246 INFO] Validation accuracy: 33.1036"
    pattern = r"Validation accuracy:\s+(\d+\.\d+)"

    match = re.search(pattern, line)
    if match:
        accuracy = float(match.group(1))
        print("Extracted accuracy:", accuracy)
    else:
        print("Accuracy not found.")
    return accuracy

def extract(path):
    train_dict = {}
    val_dict = {}

    with open(path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if 'Validation accuracy' in line:
                val_acc = extract_val(line)
                val_dict[int(last_step)] = float(val_acc)
            else:
                step, acc = extract_train(line)
                if step is not None:
                    # print (step, acc)
                    train_dict[int(step)] = float(acc)
                    last_step = step 
    return train_dict, val_dict

train_dict, val_dict = extract(path = './output_log/kh-en-train-no-bpe.log')
from tensorboardX import SummaryWriter
#SummaryWriter encapsulates everything
writer = SummaryWriter('./runs/kh-en-train-no-bpe.log')
for step, acc in train_dict.items():
    writer.add_scalar('acc_train', acc, step)

for step, acc in val_dict.items():
    writer.add_scalar('acc_val', acc, step)