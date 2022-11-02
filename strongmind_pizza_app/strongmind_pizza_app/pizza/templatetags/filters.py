from django import template
register = template.Library()

@register.filter(name='isComponent')
def isComponent(mastertoppingid, masterpizzaid):
    return True