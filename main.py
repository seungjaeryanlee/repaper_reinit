from configs import load_config
from datasets import init_dataset
from models import init_model
from transforms import init_transform


def main(CONFIG):
    model = init_model(CONFIG.model)
    train_transform = init_transform(CONFIG.transforms.train)
    valid_transform = init_transform(CONFIG.transforms.valid)
    train_dataset = init_dataset(CONFIG.datasets.train, train_transform, train=True)
    valid_dataset = init_dataset(CONFIG.datasets.valid, valid_transform, train=False)

    print(model)
    print(train_transform)
    print(valid_transform)


if __name__ == "__main__":
    CONFIG = load_config()
    main(CONFIG)
