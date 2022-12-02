from django import template
register = template.Library()


@register.simple_tag
def make_end(num):
    s_num = str(num)
    p_end = int(s_num[-2]) if len(s_num) > 1 else 0
    end = int(s_num[-1])
    if end in [2, 3, 4] and p_end != 1:
        return s_num + ' раза'
    return s_num + ' раз'
