from flask import Blueprint, url_for, current_app
from werkzeug.utils import redirect

from pybo.models import Question

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def index():
    current_app.logger.info("INFO 레벨로 출력 ")
    # question_list = Question.query.order_by(Question.create_date.desc())
    return redirect(url_for('question._list'))

#
# @bp.route('/detail/<int:question_id>/')
# def detail(question_id):
#     question = Question.query.get_or_404(question_id)
#     return render_template('questions/question_detail.html', question=question)




