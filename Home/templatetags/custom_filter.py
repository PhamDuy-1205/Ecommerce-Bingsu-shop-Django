from django import template

register = template.Library()

@register.filter(name='percent_unit')
def percent_unit(number):
    return str(number) + "% Off"



@register.filter(name='multiply')
def multiply(number , number1):
    return number * number1



@register.filter(name='discount')
def discount(number , number1):
    return round((number - (number * number1)), 1)



@register.filter(name='discount_percent')
def discount_percent(number):
    return round((number*100),0)
