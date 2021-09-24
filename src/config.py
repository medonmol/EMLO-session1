import os
import sys
from torchvision import transforms


DEVICE = "cuda"
# pathname = os.path.dirname(sys.argv[0])
path = os.path.abspath("")
sys.path.append(path)
# dimensions of our images.
img_width, img_height = 150, 150


TRAIN_DATA_DIR = "E:/TSAI/EMLO/EMLO-session1/data/train"
VALID_DATA_DIR = "E:/TSAI/EMLO/EMLO-session1/data/validation"

TRAIN_FEATURES = os.path.join(
    path, "bottleneck_features", "bottleneck_features_train.npy"
)
# (
#     "E:/TSAI/EMLO/EMLO-session1/bottleneck_features/bottleneck_features_train.npy"
# )
VALID_FEATURES = os.path.join(
    path, "bottleneck_features", "bottleneck_features_valid.npy"
)
# (
#     "E:/TSAI/EMLO/EMLO-session1/bottleneck_features/bottleneck_features_valid.npy"
# )

TRAIN_LABELS = os.path.join(
    path, "bottleneck_features", "train_labels.npy"
)  # "E:/TSAI/EMLO/EMLO-session1/bottleneck_features/train_labels.npy"
VALID_LABELS = os.path.join(path, "bottleneck_features", "valid_labels.npy")
# "E:/TSAI/EMLO/EMLO-session1/bottleneck_features/valid_labels.npy"


EPOCHS = 10
BATCH_SIZE = 16


all_transform = transforms.Compose(
    [
        transforms.Resize((150, 150)),
        transforms.Grayscale(num_output_channels=3),
        transforms.ToTensor(),
    ]
)

MODEL_SAVE_PATH = os.path.join(
    path, "models", "dognotdog.pt"
)  # "E:/TSAI/EMLO/EMLO-session1/models/dognotdog.pt"
METRICS_PATH = os.path.join(path, "metrics", "metrics.csv")  # "metrics/metrics.csv"