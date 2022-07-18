from django.core.paginator import Paginator
from django.http import HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import QuestionForm, AnswerForm
from .models import Question, Answer
