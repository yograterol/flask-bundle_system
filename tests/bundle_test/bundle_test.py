from flask import Blueprint

bundle = Blueprint('bundle_test', __name__)

@bundle.route('/', methods=['GET', 'POST'])
def test():
    return "Is a test"
