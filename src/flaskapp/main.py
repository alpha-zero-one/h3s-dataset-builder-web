from flask import Flask, render_template, request, jsonify
from src.model.Model import Model

app = Flask(__name__)
model = Model()

@app.route("/")
def index():
    return render_template('./index.html')

@app.route("/reload", methods=['POST'])
def reload():
    return jsonify({
        "entry_id": model.get_entry_id(),
        "maximum_entry_id": model.get_maximum_entry_id(),
        "system_text": model.get_system_text(),
        "user_text": model.get_user_text(),
        "assistant_text": model.get_assistant_text()
    })

@app.route("/save", methods=['POST'])
def save():
    data = request.json
    user_input = data.get("message")

    model.set_system_text(user_input["system_text"])
    model.set_user_text(user_input["user_text"])
    model.set_assistant_text(user_input["assistant_text"])
    model.save_dataset()

    return jsonify({
        "entry_id": model.get_entry_id(),
        "maximum_entry_id": model.get_maximum_entry_id(),
        "system_text": model.get_system_text(),
        "user_text": model.get_user_text(),
        "assistant_text": model.get_assistant_text()
    })

@app.route("/previous", methods=['POST'])
def previous():
    data = request.json
    user_input = data.get("message")

    model.set_system_text(user_input["system_text"])
    model.set_user_text(user_input["user_text"])
    model.set_assistant_text(user_input["assistant_text"])
    model.save_dataset()

    model.set_entry_id(int(user_input["entry_id"])-1)

    return jsonify({
        "entry_id": model.get_entry_id(),
        "maximum_entry_id": model.get_maximum_entry_id(),
        "system_text": model.get_system_text(),
        "user_text": model.get_user_text(),
        "assistant_text": model.get_assistant_text()
    })

@app.route("/next", methods=['POST'])
def next_h():
    data = request.json
    user_input = data.get("message")

    model.set_system_text(user_input["system_text"])
    model.set_user_text(user_input["user_text"])
    model.set_assistant_text(user_input["assistant_text"])
    model.save_dataset()

    model.set_entry_id(int(user_input["entry_id"])+1)

    return jsonify({
        "entry_id": model.get_entry_id(),
        "maximum_entry_id": model.get_maximum_entry_id(),
        "system_text": model.get_system_text(),
        "user_text": model.get_user_text(),
        "assistant_text": model.get_assistant_text()
    })

@app.route("/change", methods=['POST'])
def change():
    data = request.json
    user_input = data.get("message")

    model.set_system_text(user_input["system_text"])
    model.set_user_text(user_input["user_text"])
    model.set_assistant_text(user_input["assistant_text"])
    model.save_dataset()

    model.set_entry_id(int(user_input["entry_id"]))

    return jsonify({
        "entry_id": model.get_entry_id(),
        "maximum_entry_id": model.get_maximum_entry_id(),
        "system_text": model.get_system_text(),
        "user_text": model.get_user_text(),
        "assistant_text": model.get_assistant_text()
    })

@app.route("/first", methods=['POST'])
def first():
    data = request.json
    user_input = data.get("message")

    model.set_system_text(user_input["system_text"])
    model.set_user_text(user_input["user_text"])
    model.set_assistant_text(user_input["assistant_text"])
    model.save_dataset()

    model.set_entry_id(0)

    return jsonify({
        "entry_id": model.get_entry_id(),
        "maximum_entry_id": model.get_maximum_entry_id(),
        "system_text": model.get_system_text(),
        "user_text": model.get_user_text(),
        "assistant_text": model.get_assistant_text()
    })

@app.route("/last", methods=['POST'])
def last():
    data = request.json
    user_input = data.get("message")

    model.set_system_text(user_input["system_text"])
    model.set_user_text(user_input["user_text"])
    model.set_assistant_text(user_input["assistant_text"])
    model.save_dataset()

    model.set_entry_id(model.get_maximum_entry_id())

    return jsonify({
        "entry_id": model.get_entry_id(),
        "maximum_entry_id": model.get_maximum_entry_id(),
        "system_text": model.get_system_text(),
        "user_text": model.get_user_text(),
        "assistant_text": model.get_assistant_text()
    })


if __name__ == '__main__':
    app.run(debug=True)