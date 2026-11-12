from flask import Flask, jsonify

app = Flask(__name__)


def add(left: int, right: int) -> int:
	return left + right


@app.get("/health")
def health() -> tuple[object, int]:
	return jsonify(status="ok"), 200
