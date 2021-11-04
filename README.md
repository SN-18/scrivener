<h1 align="center">
 <img src="https://github.com/anshulp2912/scrivener/blob/main/media/logo/logo.gif" />
</h1>

# SCRIVENER 

![Python](https://img.shields.io/badge/python-3670A0?style=flat&logo=python&logoColor=ffdd54)
[![GitHub issues](https://img.shields.io/github/issues/TommasU/scrivener)](https://github.com/TommasU/scrivener/issues)
[![GitHub-closed-issues](https://img.shields.io/github/issues-closed-raw/TommasU/scrivener)](https://GitHub.com/TommasU/scrivener/)
![pylint](https://img.shields.io/badge/-pylint-orange)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5601143.svg)](https://doi.org/10.5281/zenodo.5601143)
[![GitHub license](https://img.shields.io/github/license/TommasU/scrivener)](https://github.com/TommasU/scrivener/blob/main/LICENSE)
![Lines of code](https://img.shields.io/tokei/lines/github/TommasU/scrivener)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/TommasU/scrivener)](https://github.com/TommasU/scrivener/issues/pull/)
[![Open in Visual Studio Code](https://open.vscode.dev/badges/open-in-vscode.svg)](https://open.vscode.dev/TommasU/scrivener/Developer/badges)
![GitHub pull-requests-closed](https://img.shields.io/github/issues-pr-closed-raw/TommasU/scrivener)
[![language_count](https://img.shields.io/github/languages/count/TommasU/scrivener)](https://GitHub.com/TommasU/scrivener/) 
[![Repo-size](https://img.shields.io/github/repo-size/TommasU/scrivener)](https://GitHub.com/TommasU/scrivener/)
[![codecov](https://codecov.io/gh/TommasU/scrivener/branch/main/graph/badge.svg)](https://codecov.io/gh/TommasU/scrivener)
![Contributors](https://img.shields.io/badge/Contributors-5-yellowgreen)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/TommasU/scrivener)
[![AutoPep8](https://img.shields.io/badge/AutoPep8-1.6.0-brightgreen)](https://pypi.org/project/autopep8/)
[![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=_pg9M32LiG8&ab_channel=AnshulPatel)

## Table of Contents
- [Introduction](#Introduction)
- [Demo](#Demo)
- [Steps for Execution](#ExecutionSteps)
- [License](#License)
- [Contributions](#Contributions)
- [Future Scope](#FutureScope)
- [Team Members](#TeamMember)
- [Acknowledgements](#Acknowledgement)

## Introduction <a name="Introduction"></a>

Scrivener is a video transcript summarizer for Youtube videos. Youtube is one of the most used website. A lot of people use the captions to understand the language of the video. In our project we aim to create a transcript summarizer which accepts a youtube URL link, collects the caption at every sentence and then provides the summary of the complete video. Our goal is to make the summarizer as accurate as possible and to add various other features. Our second goal of the project is to create a summarizer which can summarize the youtube videos which have captions disabled. Our project can be further expanded for numerous applications. This document provides a major perspective for the users to understand and take up the project as an Open source software and add on multiple features. Also, the document aids the developers in understanding the code and acts as a reference point for starting the project.

<h1 align="center">
 <img src="https://github.com/anshulp2912/scrivener/blob/main/media/working_animation/scrivener_working.gif" />
</h1>

The complete development was achieved using the Python3 technology and it is recommended that the next set of developers who take up this project have these technologies installed and keep them running before proceeding further.

## Demo <a name="Demo"></a>
The project is deployed on both Streamlit cloud and Heroku.
- [Streamlit](https://share.streamlit.io/anshulp2912/scrivener/main/source/scrivener_user_interface.py)
- [Heroku](https://scrivener-heroku.herokuapp.com/)
## How to get MonkeyLearn API key
1. Go to [https://monkeylearn.com/sentiment-analysis-online/](https://monkeylearn.com/sentiment-analysis-online/)
2. Enter your requirements and sign up.
The API key is associated with a limited number of queries per month (1000). You can use one of the pretrained model like we did or you can create your own model as well!
 
## Steps for Execution <a name="ExecutionSteps"></a>
1. Clone the Git repository.
2. Run `pip install -r requirements.txt`
3. Open Command Prompt and change the directory to the location of cloned repository.
4. Run the command `python -m streamlit run ./source/scrivener_user_interface.py`
5. Next, open your browser and type in `localhost:8501` in the search bar to open the webUI of the application.
6. The UI typically looks as shown below and here you have a choice between URL, file or normal text input.

<img src="https://github.com/anshulp2912/scrivener/blob/main/media/demo.PNG" />

## License <a name="License"></a>
This project is licensed under the terms of the MIT license. Please check [License](https://github.com/TommasU/scrivener/blob/main/LICENSE) for more details.

## Contributions <a name="Contributions"></a>
Please see our [CONTRIBUTING.md](https://github.com/TommasU/scrivener/blob/main/CONTRIBUTING.md) for instructions on how to contribute to the project by completing some of the issues.

## Version 1.1 Contributions
- Enhanced product quality by improving the summarization model.
- Greatly improved summary formatting to improve readability
- Provided Sentiment Analysis of the generated summary

## Future Scope <a name="FutureScope"></a>
This project as we believe contains an exciting stream of possibilities. You will be working into domains such as Natural Language Processing, Web Development, Digital Signal Processing, and Information Retrieval. Some of the possibilities you can explore are the following:
* Is there any way in which a sentence in the summary can point back to the video where it was talked about?
* Currently our application supports youtube videos and videos with .mp4 extension. Can you provide support for other video formats?
* Can you perform summarization for videos in languages other than English
* Can you generate summary of Podcasts or other audiofiles?
* Is there a way to summarize videos for specific time frames?
* How can we deliver summaries in the form of audio?
* How do we diversify by expanding to a Chrome Extension and a Discord Bot?

These are some of the fascinating topics we thought for you, but you should not limit yourself to these points! Play around with our repo! See what motivates you.

As a bonus point, we have taken great care to adhere to the SE principles, so you have tools integrated for code coverage, style checking, code formatting, continuous testing and integration, and as a cherry on icing many meaningful testcases. So you can focus more on delivering state-of-the-art features!

## Team Members <a name="TeamMember"></a>

- [Jessica Vargas(jrvargas)](jrvargas@ncsu.edu) <br> 
- [Parth Parikh(pmparikh)](pmparikh@ncsu.edu) <br>
- [Radhika Toravi(rtoravi)](rtoravi@ncsu.edu) <br>
- [Rushikesh Deodhar(rdeodha)](rdeodha@ncsu.edu) <br>
- [Saurabh Nanda(snanda)](snanda2@ncsu.edu) <br>
				
## Acknowledgements <a name="Acknowledgement"></a>
We would like to thank Professor Dr Timothy Menzies for helping us understand the process of building a good Software Engineering project. We would also like to thank the teaching assistants Xiao Ling, Andre Lustosa, Kewen Peng, Weichen Shi for their support throughout the project.
- [https://streamlit.io/](https://streamlit.io/)
- [https://huggingface.co/](https://huggingface.co/)
- [https://shields.io/](https://shields.io/)
- [https://www.powtoon.com/](https://www.powtoon.com/)
- [https://www.heroku.com/](https://www.heroku.com/)
- [https://monkeylearn.com/sentiment-analysis-online/](https://monkeylearn.com/sentiment-analysis-online/)
