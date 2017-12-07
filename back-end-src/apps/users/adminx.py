# -*- coding: utf-8 -*-
__author__ = 'HymanLu'

import xadmin
from xadmin import views
from .models import SmsVerifyCode


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "慕学生鲜后台"
    site_footer = "mxshop"
    # menu_style = "accordion"


class SmsVerifyCodeAdmin(object):
    list_display = ['code', 'mobile', "add_time"]


xadmin.site.register(SmsVerifyCode, SmsVerifyCodeAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)