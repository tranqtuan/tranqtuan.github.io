# Create your views here.
from django.shortcuts import render
from django.http import *
from Testapp.forms import *
from django.contrib import messages
import pattern.text.en


def show_test(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = TestForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            response = using_pattern(subject,message)
            return HttpResponse(messages.success(request, response))  # Redirect after POST
    else:
        form = TestForm()  # An unbound form

    return render(request, 'test_form.html', {'form': form,})


def using_pattern(text,aspect):
        text = str(text)
        aspect = str(aspect)
        parsed = pattern.text.en.parsetree(text)
        s = 0
        for sentence in parsed.sentences:
            if aspect in sentence.string:
                if pattern.text.en.subjectivity(sentence.string) != 0:
                    score_and_ind = []
                    asp_inds = []
                    sent_chunks = sentence.chunks
                    for chunk_index in range(len(sent_chunks)):
                        if aspect in sent_chunks[chunk_index].string:
                            asp_inds.append(chunk_index)
                        score_and_ind.append((pattern.text.en.polarity(sent_chunks[chunk_index].string),chunk_index))
                    for i in range(len(score_and_ind)):
                        for asp_ind in asp_inds:
                            s += score_and_ind[i][0]/((abs(asp_ind - score_and_ind[i][1]) + 1))
        return s