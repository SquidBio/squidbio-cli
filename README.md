# SquidBio (WIP)

This is the official repository for the SquidBio CLI. For more information on the project, visit https://squidbio.com.

## Introduction

SquidBio is a platform for collaborating on projects that use DNA.

## Installation

Clone this repository and run `pip install .`

In order to clone private projects/sequences, you need an API key. To get one, go to https://squidbio.com/update_profile and run `squidbio config`.

## Usage

* To clone a project, run `squidbio clone [project-url]`
* To clone a sequence, run `squidbio clone [seq-url] --seq`
* To see changes you have made, run `squidbio diff` or `squidbio diff [path]`

## Contributing

The CLI is a WIP. If you would like to contribute, feel free to get in touch! My email is in `setup.py`
