from django.shortcuts import render
from django.template import loader


def draw_page(request, game):
    return render(request, 'main.html', { 'body':  loader.render_to_string(f'{game}/{game}.html', None, request, None) })