from flask  import Blueprint
#微信公众号处理蓝图
bp= Blueprint('wx',__name__)
from app.wx import routes