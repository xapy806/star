import xadmin
from xadmin import views

from content.models import Category, Tag, Course, Teacher


class BaseSetting(object):
    # 主题修改
    enable_themes = True
    use_bootswatch = True


class GlobalSetting():
    site_title = '明日之星管理后台'
    site_footer = '明日之星科技'

    menu_style = 'accordion'  # 菜单折叠
    # 公共搜索模型(问题： 一个模型类不显示搜索框)
    global_search_models = [Category, Tag, Teacher, Course]

    # 设置模型图标
    global_models_icon = {
        Category: 'glyphicon glyphicon-th-list',
        Tag: 'glyphicon glyphicon-bookmark',
        Course: 'glyphicon glyphicon-list-alt'
    }

    # 设置app模块的图标
    apps_icons = {
        'content': 'glyphicon glyphicon-book'
    }

    apps_label_title = {
        'content': '课程管理'
    }


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)


# Register your models here.
class CategoryAdmin():
    # 列表显示的字段
    list_display = ['title']

    list_per_page = 10  # 分页显示，每页显示10条


class TagAdmin():
    list_display = ['title']


class CourseAdmin():
    list_display = ['title',
                    'summary',
                    'cover',
                    'favor',
                    'price',
                    'detail',
                    'teachers',
                    'tags',
                    'category'
                    ]


class TeacherAdmin():
    list_display = ['name',
                    'image',
                    'intro']


xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
