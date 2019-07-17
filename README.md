# Crispy AI

[![Issues](https://img.shields.io/github/issues-closed/oss2019/crispy-ai.svg?style=flat-square)](https://github.com/oss2019/crispy-ai/issues) [![Pull Requests](https://img.shields.io/github/issues-pr-closed/oss2019/crispy-ai.svg?style=flat-square)](https://github.com/oss2019/crispy-ai/pulls) [![License](https://img.shields.io/apm/l/vim-mode.svg?style=flat-square)](https://github.com/oss2019/crispy-ai/blob/master/LICENSE) [![Gitter](https://img.shields.io/badge/chat-on%20gitter-ff006f.svg?style=flat-square)](https://gitter.im/oss2019/community)

Meet Crispy! Your intelligent companion that sits your lectures for you and organizes classroom taught content into short and concise modules.
She also tries to provide you with live subtitles turning your classroom experience into a [BH]ollywood blockbuster

<p align="center"> <img width="500" src="images/195.jpg"> </p>

# New Dev Branch : Recorder

- Do work on the branch - 'recorder' and submit all your prs to it
- If you have an alternate bug free recorder that can work with django - please do submit a PR :) in a new branch

## Quick Fix(Do this in your venv only!): 

-  Navigate to `venv/lib/python3.6/site-packages/django/forms/boundfield.py`
and **delete** `line 93: renderer=self.form.renderer` to ensure the server recorder works.
- This is a quick fix until an alternative is discovered to get the recorder widget work. Issue: Django render() method was changed from v2.x onwards
## Features
Crispy has bunch of cool features to aid you. [Check them out here](features.md) and feel free to add some more to list through a PR!

## Getting Started
  - Setting up this repo and installing django - [Here](https://github.com/oss2019/crispy-ai/blob/master/weekly/week_0.md)
  - Be updated with the Weekly tips [here](https://github.com/oss2019/crispy-ai/tree/master/weekly) so that you bag them issues super fast.

## Tools/Libraries which can be used
  - [Facebook wav2letter++](https://github.com/facebookresearch/wav2letter) - [Text to Speech] Built on C++, really fast but takes piptime to get adjusted to (FREE)
  - [Mozilla DeepSpeech](https://github.com/mozilla/DeepSpeech) - [Text to Speech] Built on TensorFlow (FREE)
  - [Gnani](https://gnani.ai/SpeechToTextApi) - [Text to Speech] End-to-end API
  - [Microsoft Azure Text Analytics](https://azure.microsoft.com/en-in/services/cognitive-services/text-analytics/) - [Key Phrase Extraction] End-to-end API (PAID)
  - [ParallelDots Keyword Extractor](https://www.paralleldots.com/keyword-extractor) - [Key Phrase Extraction] End-to-end API (PAID)
  
## To-Do List
  - [ ] Find a FREE Key Phrase Extractor API/library (or maybe tweak some existing ones slightly to get it done)

## Contributions
We would love contributions to add more features to crispy and make her the coolest companion. See the [guidelines](contributions.md) to know more on how to contribute.

### Acknowledgements
Image Designed by [roserodionova / Freepik](http://www.freepik.com")

## Legal
Please refer to the [licence](https://github.com/oss2019/crispy-ai/blob/master/LICENSE)
