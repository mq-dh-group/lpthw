# Table of Contents

- [Introduction](#intro)
  - [What am I doing?](#what)
  - [Why am I doing it?](#why)
- [Methodology](#methodology)
- [GPT Log](#gptlog)
- [ProjectEuler Problems](#projecteuler)
- [Results](#results)
- [Conclusion](#conclusion)


# Introduction {#intro}

Today, I begin a journey, and I'm deciding to log it, both for myself, for others who embark on similar journeys, and also because I was advised to do so (hey Brian!). I have a vague idea of what I'll be traversing across on this journey, but I really can't say what my destination will look like. Hopefully, this log proves useful to myself as an exercise in reflection, but also to others who can learn from my mistakes and possibly even insights.

## What am I doing? {#what}

I'm going to be going through a bunch of *exercises* (for lack of a better term) that were provided to me, which will, from what I understand, measure my intuitions for computer science, data science, programming languages, and other coding-related ventures. Each *exercise* will be a chapter in this log.

## Why am I doing it? {#why}

There are a couple of reasons really. There is the *personal answer*, and then there is the *professional answer*.
*Warning: the _personal answer_ is indeed personal, feel free to skip to the next paragraph if you're not interested and just want to get to the practical stuff*
I suppose a bit of background is necessary here. At the time of writing this (30/03/2023), I am 25 years old. I have a strong passion for music, and also very strong interests in other *random* things, such as chess, Egyptology, and meditation to name a few. I've always believed having these passions and interests as a blessing and a curse. On the one hand, the time in which I am engaged with these passions and interests brings a certain level of meaning to my life. On the other hand, it makes all the other times a bit harder. If the peaks are higher, then the distance to the valleys must therefore be greater. As you might have realised from the list of passions and interests listed above, they are not exactly the easiest things to make a career out of. Not impossible, of course, but there are no obvious routes with a promising chance of success. Perhaps in a parallel universe I have a passion for law, medical science, or some other field with a fairly direct career path with plenty of demand, however, in this universe, I do not. And on the whole, I'm ok with that, because boy do I love the things I am passionate about.

Anyway, life story aside, the *professional answer* to what I am doing here is that I am testing the waters for skills and methods that could lead to greater (i.e. more) career possibilities. I have had some experience working with SQL for a few years after creating a database to aid a Master's Thesis I completed back in 2020, and I have recently decided to self-learn Python. For whatever reason, I quite enjoy trying to solve problems within these languages. It reminds me of obsessions I've had in the past with say Sudoku when I was very young, or chess puzzles today. I am writing this introduction before embarking attempting any of the challenges ahead. So, without further ado, let's go!

# Methodology {#methodology}

I will keep this brief. After all, I am not writing an academic publication. I am not claiming these methods to be the way one should go about what I'm doing, I'm merely recording what it is I will be doing, so that it is transparent for any readers.

I will implement a very loose template in each log while working through each problem I encounter, namely
1. Anticipation: *What I expect to happen*
2. Result: *What actually happened*
3. Reflection: *Was there a difference between steps 1 and 2? If so, why?*

I will not be undertaking any of this completely alone, as I will be using the GPT, Bing Chat. GPTs have already proven to be a valuable tool for me, so I will both be using this as such, but also to simultaneously increase my skills in using GPTs (Generative Pre-trained Transformer) and more broadly LLMs (Large Language Models) effectively. Why Bing Chat as opposed to another GPT? Firstly, it was recommended to me, but I assume the reason for that was due to the integration of a search engine as well as the underlying LLM technology.

# GPT Log {#gptlog}

This is the section to record and reflect the experience of using Bing Chat as an aid to my work.


# Project Eueler Problems {#projecteuler}

Project Euler's Problem Archives are a set of problems that are added to daily(?). Each problem has a unique IDs, which will be referred to in these logs and can be viewed at projecteuler.net/archives. I am using Python to solve these problems.

## ID 1
*For this first problem, I didn't quite realise I was even meant to be solving these with a computing program and was just doing it in my head*

1. Anticipation:
I immediately recalled a formula for this that I learn back in high school mathematics, but it certainly isn't something that has stuck with me. I used a GPT to provide a formula. It provided:

S = (n/2)(2a + (n-1)d)
* S = sum of sequence
* n = number of terms in the sequence
* a = first term of the sequence
* d = common difference between terms

For multiples of 3:
n3 = (999-3)/3 + 1 = 333
S3 = (333/2)(2*3 + (333-1)3)
S3 = 166833

For multiples of 5:
n5 = (995-5)/5 + 1 = 199
S5 = (199/2)(2*5 + (199-1)5)
S5 = 99500

Adding the two totals together I get 267333 . Before submitting I've just realise I didn't account for the fact that some multiples of 3 are also multiples of 5 and should only be counted once. Bing Chat once again provide me with the inclusion-exclusion principle of S = S3 + S5 - LCM. So, after finding the total multiples for the LCM (Lowest Common Multiple) of 3 and 5:
n15 = (990-15)/15 + 1 = 66
S15 = (66/2)(2*15 + (66-1)15)
33165

We have 166833 + 100500 - 33165 = 233168

2. Result:

Correct!

3. Reflection:

Took me way too long to complete for a variety of reasons. Onto Using python next time.


## ID 2

1. Anticipation:


2. Result:


3. Reflection:


## ID 3

1. Anticipation:

I felt that I wanted a little nudge getting started. I asked Bing Chat to give me a "hint" on how to start writing this code. It pointed out that I don't need to generate the entire Fibonacci Sequence, just the even-valued terms within it.

My script:


2. Result:


3. Reflection:






# Results {#results}

This is the results section.

# Conclusion {#conclusion}

This is the conclusion section.
