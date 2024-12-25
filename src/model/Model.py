import json
import os


class Model:

    def __init__(self):

        config_file_path = './local/config.json'
        if not os.path.exists(config_file_path):
            os.makedirs("./local/dataset", exist_ok=True)
            with open(config_file_path, 'w') as json_file:
                json.dump({"dataset_name": "default"}, json_file)

        with open(config_file_path) as f:
            self.config = json.load(f)

        self.dataset_name = self.config["dataset_name"]
        self.dataset = []
        self.load_dataset()

        self.entry_id = 0
        self.set_entry_id(len(self.dataset)-1)

    def set_entry_id(self, entry_id):
        self.entry_id = entry_id
        self.entry_id = max(0, self.entry_id)
        self.entry_id = min(len(self.dataset)-1, self.entry_id)

        if entry_id == self.entry_id+1:

            item = {
                "messages": [
                    {"role": "system", "content": self.get_system_text()},
                    {"role": "user", "content": ""},
                    {"role": "assistant", "content": ""}
                ]
            }
            self.dataset.append(item)
            self.entry_id += 1

    def set_system_text(self, system_text):
        self.dataset[self.entry_id]["messages"][0]["content"] = system_text

    def set_user_text(self, user_text):
        self.dataset[self.entry_id]["messages"][1]["content"] = user_text

    def set_assistant_text(self, assistant_text):
        self.dataset[self.entry_id]["messages"][2]["content"] = assistant_text

    def get_entry_id(self):
        return self.entry_id

    def get_maximum_entry_id(self):
        return len(self.dataset)-1

    def get_system_text(self):
        return self.dataset[self.entry_id]["messages"][0]["content"]

    def get_user_text(self):
        return self.dataset[self.entry_id]["messages"][1]["content"]

    def get_assistant_text(self):
        return self.dataset[self.entry_id]["messages"][2]["content"]

    def load_dataset(self):

        dataset_path = f"./local/dataset/{self.dataset_name}.jsonl"

        if not os.path.exists(dataset_path):
            with open(dataset_path, 'w') as json_file:
                json.dump({
                    "messages": [
                        {"role": "system", "content": ""},
                        {"role": "user", "content": ""},
                        {"role": "assistant", "content": ""}
                    ]
                }, json_file)

        self.dataset = []
        with open(dataset_path, 'r') as file:
            for item in file:
                self.dataset.append(json.loads(item))

    def save_dataset(self):

        with open(f"./local/dataset/{self.dataset_name}.jsonl", 'w') as file:
            for item in self.dataset:
                file.write(json.dumps(item) + '\n')
